#!/usr/bin/env python3
import os
import sys
import re
import base64
import json
import urllib.request
import urllib.error

# Configuration
API_BASE = "http://127.0.0.1:8045/v1/chat/completions"
API_KEY = "sk-51fdaee58ffd40b3b402eb12fce36e65"
MODEL = "gemini-3-pro-image"

def generate_image_api(prompt, output_path):
    """Generates an image using urllib to avoid dependencies."""
    
    # Ensure Chinese text constraint
    if "english" not in prompt.lower() and "text" not in prompt.lower():
        prompt += ", text in Simplified Chinese if any"
    elif "chinese" not in prompt.lower():
        prompt += ", ensure any text is Simplified Chinese"

    print(f"🎨 Generating: {prompt[:50]}... -> {os.path.basename(output_path)}")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "model": MODEL,
        "extra_body": { "size": "1024x1024" },
        "messages": [{
            "role": "user",
            "content": prompt
        }]
    }
    
    try:
        req = urllib.request.Request(API_BASE, data=json.dumps(payload).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            
        content = result['choices'][0]['message']['content']
        
        # Extract Base64
        match = re.search(r'data:image/([a-zA-Z]+);base64,([a-zA-Z0-9+/=]+)', content)
        if match:
            base64_data = match.group(2)
            with open(output_path, 'wb') as f:
                f.write(base64.b64decode(base64_data))
            print(f"✅ Saved to: {output_path}")
            return True
        else:
            print(f"⚠️ Failed to extract image data. Response: {content[:100]}...")
            return False
            
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code} - {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def parse_prompts(prompts_file):
    """Parses prompts.md."""
    with open(prompts_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'## \d+\..*?\((.*?)\).*?\*\*Prompt\*\*: "(.*?)"'
    matches = re.findall(pattern, content, re.DOTALL)
    
    results = []
    for filename_key, prompt in matches:
        filename = re.sub(r'[^\w\-_]', '_', filename_key.strip()).lower() + ".png"
        prompt = prompt.replace('\n', ' ').strip()
        results.append((filename, prompt))
    
    return results

def update_content_file(content_file, image_filename):
    """Injects or appends Obsidian style image reference."""
    if not os.path.exists(content_file):
        return

    ref_str = f"![[{image_filename}]]"
    
    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if ref_str in content:
        return

    is_cover = "cover" in image_filename.lower()
    
    if is_cover:
        parts = content.split('---')
        if len(parts) >= 3:
            new_content = '---'.join(parts[:2]) + '---\n\n' + ref_str + '\n' + '---'.join(parts[2:])
        else:
            new_content = ref_str + '\n\n' + content
    else:
        new_content = content + f"\n\n{ref_str}\n"

    with open(content_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"📝 Updated content with ref {ref_str}")

def process_platform_dir(platform_dir):
    prompts_file = os.path.join(platform_dir, "images", "prompts.md")
    if not os.path.exists(prompts_file):
        return

    print(f"\n📂 Processing {os.path.basename(platform_dir)}...")
    prompts = parse_prompts(prompts_file)
    
    # Determine content file
    content_file = None
    for f in os.listdir(platform_dir):
        if f.endswith(".md"):
            content_file = os.path.join(platform_dir, f)
            break
    
    for filename, prompt in prompts:
        output_path = os.path.join(platform_dir, "images", filename)
        if not os.path.exists(output_path):
            success = generate_image_api(prompt, output_path)
            if success and content_file:
                update_content_file(content_file, filename)
        else:
            print(f"⏩ Skipping existing: {filename}")
            if content_file:
                update_content_file(content_file, filename)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_matrix_images.py <content_root_dir>")
        sys.exit(1)
        
    root_dir = sys.argv[1]
    platforms = ['redbook', 'twitter', 'wechat', 'zhihu']
    for p in platforms:
        p_dir = os.path.join(root_dir, p)
        if os.path.isdir(p_dir):
            process_platform_dir(p_dir)

if __name__ == "__main__":
    main()
