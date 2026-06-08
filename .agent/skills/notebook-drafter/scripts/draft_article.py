#!/usr/bin/env python3
import argparse
import subprocess
import json
import sys
import shutil

PROMPT_TEMPLATE = """请基于已上传的资料，围绕我的个人观点撰写一篇约2000-3000字的文章初稿。

**我的个人观点是：** {opinion}

**写作要求：**
1. **结构：** 包含引人入胜的标题、引言、3-4 个核心论证段落，以及总结展望。逻辑清晰，引人入胜，让读者有收获感。
2. **融合：** 请将我的个人观点作为文章的核心灵魂，并从资料中寻找支持该观点的具体案例、数据或理论框架。
3. **批判性：** 如果资料中存在与我观点冲突的内容，请进行辩证分析，并说明为什么我的观点在特定背景下更具说服力。
4. **风格**：专业严谨但不晦涩，用工程师的思维剖析技术本质，用清晰的表达传递洞察。”
5. **文献：** 文末给出文章引用的参考文献，遵循标准学术引用规范和格式。"""

def run_cmd(cmd_list, check=True):
    """Run a command (list of args) and return stdout."""
    try:
        # shell=False is safer and handles arguments correctly
        result = subprocess.run(cmd_list, capture_output=True, text=True)
        if check and result.returncode != 0:
            print(f"Command failed: {' '.join(cmd_list)}")
            print(f"Stderr: {result.stderr}")
            sys.exit(1)
        return result
    except FileNotFoundError:
        print(f"Command not found: {cmd_list[0]}")
        sys.exit(1)

def check_dependencies():
    if not shutil.which("notebooklm"):
        import glob
        import os
        possible_paths = [
            os.path.expanduser("~/.local/share/uv/python/cpython-*/bin"),
            os.path.expanduser("~/Library/Python/*/bin"),
            os.path.expanduser("~/.local/bin"),
        ]
        found = False
        for p_pattern in possible_paths:
            paths = glob.glob(p_pattern)
            paths.sort(reverse=True)
            for p in paths:
                if os.path.exists(os.path.join(p, "notebooklm")):
                    os.environ["PATH"] = p + os.path.pathsep + os.environ.get("PATH", "")
                    found = True
                    break
            if found:
                break

    if not shutil.which("notebooklm"):
        print("错误: 未找到 'notebooklm' 命令。请先安装: pip3 install notebooklm-py")
        sys.exit(1)
    
    # Check auth
    print("正在检查 NotebookLM 认证状态...")
    res = run_cmd(["notebooklm", "auth", "check", "--json"], check=False)
    if res.returncode != 0:
        print("认证检查失败，请先运行 'notebooklm login'。")
        sys.exit(1)
        
    try:
        auth_data = json.loads(res.stdout)
        # Relaxed check: just ensure we have some cookie domains or storage exists
        # detailed token_fetch is skipped by default unless --test is used
    except json.JSONDecodeError:
        print("无法解析认证状态，将尝试继续...")

def select_notebook():
    print("正在获取笔记本列表...")
    res = run_cmd(["notebooklm", "list", "--json"])
    try:
        data = json.loads(res.stdout)
        notebooks = data.get("notebooks", [])
    except json.JSONDecodeError:
        print("解析笔记本列表失败。")
        sys.exit(1)

    if not notebooks:
        print("未找到笔记本，请先创建一个: notebooklm create 'My Notebook'")
        sys.exit(1)

    print("\n可用笔记本:")
    for i, nb in enumerate(notebooks):
        print(f"{i+1}. {nb.get('title', 'Untitled')} ({nb.get('id')})")

    while True:
        try:
            choice = input("\n请选择笔记本 (输入序号或ID): ").strip()
        except EOFError:
            sys.exit(1)
            
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(notebooks):
                return notebooks[idx]['id']
            else:
                print("序号无效。")
        else:
            # Check if it looks like a valid ID
            found = False
            for nb in notebooks:
                if nb['id'] == choice:
                    found = True
                    break
            if found or len(choice) > 10: # Allow ID paste even if not in cached list?
                return choice
            print("无效的选择。")

def main():
    parser = argparse.ArgumentParser(description="Generate article draft using NotebookLM")
    parser.add_argument("--notebook", help="Notebook ID")
    parser.add_argument("--opinion", help="Personal opinion/viewpoint")
    parser.add_argument("--output", default="notebook_draft.md", help="Output filename")
    args = parser.parse_args()

    check_dependencies()

    notebook_id = args.notebook
    if not notebook_id:
        notebook_id = select_notebook()

    opinion = args.opinion
    if not opinion:
        print("\n请输入您的个人观点 (My Personal Opinion):")
        try:
            opinion = input("> ").strip()
        except EOFError:
            sys.exit(1)
    
    if not opinion:
        print("错误: 必须提供个人观点。")
        sys.exit(1)

    prompt = PROMPT_TEMPLATE.format(opinion=opinion)
    
    print(f"\n正在笔记本 ({notebook_id}) 中生成初稿...")
    print("这可能需要几分钟，请耐心等待...")

    # Construct command list
    cmd = [
        "notebooklm", "generate", "report",
        prompt,
        "--notebook", notebook_id,
        "--format", "custom",
        "--wait",
        "--json"
    ]
    
    res = run_cmd(cmd, check=False)
    
    if res.returncode != 0:
        print("生成失败:")
        print(res.stderr)
        sys.exit(1)
        
    output_json = res.stdout
    artifact_id = None
    
    try:
        data = json.loads(output_json)
        # Attempt to find ID in response
        if "id" in data:
             artifact_id = data["id"]
        elif "artifact_id" in data:
             artifact_id = data["artifact_id"]
        # Some versions might return just the artifact object
        elif "title" in data and "type" in data: # It's an artifact object
             artifact_id = data.get("id")
    except json.JSONDecodeError:
        pass

    if not artifact_id:
        print("无法直接获取 Artifact ID，尝试查找最新生成的报告...")
        list_cmd = ["notebooklm", "artifact", "list", "--notebook", notebook_id, "--json"]
        list_res = run_cmd(list_cmd, check=False)
        if list_res.returncode == 0:
            try:
                list_data = json.loads(list_res.stdout)
                artifacts = list_data.get("artifacts", [])
                # Filter for Report artifacts if possible, or just take the first one
                # Assuming the API returns the newest first (which is typical for such APIs)
                if artifacts:
                    artifact_id = artifacts[0]['id']
                    print(f"使用了最新的 Artifact: {artifacts[0].get('title')} ({artifact_id})")
            except:
                pass
    
    if not artifact_id:
        print("错误: 无法确定生成的 Artifact ID。请手动运行 'notebooklm artifact list' 查看。")
        sys.exit(1)
        
    print(f"正在下载 Artifact {artifact_id} 到 {args.output}...")
    
    dl_cmd = [
        "notebooklm", "download", "report",
        args.output,
        "--artifact", artifact_id,
        "--notebook", notebook_id
    ]
    dl_res = run_cmd(dl_cmd, check=False)
    
    if dl_res.returncode != 0:
        print("下载失败:")
        print(dl_res.stderr)
        sys.exit(1)
        
    print(f"\n成功！文章初稿已保存至: {args.output}")

if __name__ == "__main__":
    main()
