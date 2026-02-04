#!/usr/bin/env python3
import os
import argparse
from datetime import datetime

def setup_content_dirs(topic, platforms=None):
    if platforms is None:
        platforms = ['redbook', 'twitter', 'wechat', 'zhihu']
    
    date_str = datetime.now().strftime('%Y%m%d')
    topic_sanitized = topic.replace(' ', '_').lower()
    base_dir = f"platform/{date_str}_{topic_sanitized}"
    
    created_dirs = []
    
    for platform in platforms:
        platform_dir = os.path.join(base_dir, platform)
        images_dir = os.path.join(platform_dir, "images")
        
        os.makedirs(images_dir, exist_ok=True)
        created_dirs.append(platform_dir)
        
        # Create a placeholder content file
        content_file = "content.md"
        if platform == "twitter":
            content_file = "thread.md"
        # Standardize strictly to content.md for unified processing where possible, 
        # but keep thread.md for Twitter to distinguish format.
        # Wechat/Zhihu/Redbook -> content.md
            
        with open(os.path.join(platform_dir, content_file), 'w') as f:
            f.write(f"# Content for {platform}\n\nTopic: {topic}\nDate: {date_str}\n")

    print(f"✅ Created content directories for topic '{topic}' in:\n{base_dir}")
    return base_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Setup content directories for media matrix.')
    parser.add_argument('topic', help='The topic of the content (e.g., "ai_agents")')
    parser.add_argument('--platforms', nargs='+', choices=['redbook', 'twitter', 'wechat', 'zhihu'], 
                        help='Specific platforms to generate for (default: all)')
    
    args = parser.parse_args()
    setup_content_dirs(args.topic, args.platforms)
