#!/usr/bin/env python3
import json
import os
import sys

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    profile_path = os.path.join(base_dir, 'assets', 'style_profile.json')

    if not os.path.exists(profile_path):
        print(f"No profile found at {profile_path}")
        return

    try:
        with open(profile_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
            print("-" * 30)
            print(f"Analyzed Sources: {len(data.get('analyzed_sources', []))}")
            for source in data.get('analyzed_sources', []):
                print(f" - {source}")
                
    except Exception as e:
        print(f"Error reading profile: {e}")

if __name__ == "__main__":
    main()
