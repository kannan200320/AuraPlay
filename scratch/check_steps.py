import json

with open(r'C:\Users\KANNAN\.gemini\antigravity\brain\eb3d6109-6ab7-4408-bf23-62466738bcae\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT' and obj.get('step_index') in [630, 670]:
            print(f"=== Step {obj.get('step_index')} ===")
            print(obj.get('content'))
            print("Media:", [m.get('uri').split('/')[-1] for m in obj.get('media', [])])
