import json

# Python dict (nested)
data = {
    "user": "lonelydemon",
    "tasks": [
        {"title": "Finish Flask API", "done": False},
        {"title": "Read JSON docs", "done": True}
    ],
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}

# Convert to JSON string (pretty)
json_str = json.dumps(data, indent=2)
print("🔹 JSON String:\n", json_str)

# Save JSON to file
with open("tasks.json", "w") as f:
    json.dump(data, f, indent=2)

# Load JSON from file
with open("tasks.json", "r") as f:
    loaded = json.load(f)

# Access nested data
first_title = loaded["tasks"][0]["title"]
print("\n🔹 First Task Title:", first_title)
