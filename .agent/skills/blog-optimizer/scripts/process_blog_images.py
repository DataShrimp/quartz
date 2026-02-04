#!/usr/bin/env python3
import os
import sys
import re
import json
import base64
import urllib.request
import urllib.error

# Configuration (Mirrors media-matrix setup)
API_BASE = "http://127.0.0.1:8045/v1/chat/completions"
API_KEY = "sk-51fdaee58ffd40b3b402eb12fce36e65"
MODEL = "gemini-3-pro-image"

def generate_image_api(prompt, output_path):
    """Generates an image using the local API."""
    
    # Context enhancement
    if "english" not in prompt.lower() and "text" not in prompt.lower():
         prompt += ", text in Simplified Chinese if any"
    
    print(f"🎨 Generating: {prompt[:60]}...")
    
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
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'wb') as f:
                f.write(base64.b64decode(base64_data))
            print(f"✅ Saved to: {os.path.basename(output_path)}")
            return True
        else:
            print(f"⚠️ Failed to extract image data.")
            return False
            
    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return False

def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"📂 Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Directory context
    base_dir = os.path.dirname(os.path.abspath(file_path))
    attachments_dir = os.path.join(base_dir, "attachments")
    
    # Regex for <!-- IMAGE_GEN: {...} -->
    # Using a function for replacement to handle logic
    def replace_image(match):
        raw_json = match.group(1)
        try:
            config = json.loads(raw_json)
            prompt = config.get('prompt')
            filename = config.get('filename')
            alt = config.get('alt', 'Image')
            
            if not prompt or not filename:
                print(f"⚠️ Invalid config: {raw_json}")
                return match.group(0) # Keep original
            
            # Target path
            full_image_path = os.path.join(attachments_dir, filename)
            
            # Check if exists
            if os.path.exists(full_image_path):
                print(f"⏩ Image exists: {filename}")
                return f"![{alt}](attachments/{filename})"
            
            # Generate
            success = generate_image_api(prompt, full_image_path)
            if success:
                return f"![{alt}](attachments/{filename})"
            else:
                return match.group(0) # Keep original if failed
                
        except json.JSONDecodeError:
            print(f"⚠️ JSON Error in: {raw_json}")
            return match.group(0)

    # Perform substitution
    new_content = re.sub(r'<!--\s*IMAGE_GEN:\s*(\{.*?\})\s*-->', replace_image, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("💾 Updated markdown file.")
    else:
        print("✨ No changes made.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 process_blog_images.py <markdown_file>")
        sys.exit(1)
        
    process_file(sys.argv[1])
