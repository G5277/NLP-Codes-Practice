import json

# Path to your input .txt file
txt_path = "abc.txt"

# Path where you want to save the output .ipynb file
ipynb_path = "NLP-3.ipynb"

# Read the content from the .txt file
with open(txt_path, "r", encoding="utf-8") as txt_file:
    notebook_json = txt_file.read()

# Try to parse and save as .ipynb
try:
    notebook_dict = json.loads(notebook_json)
    with open(ipynb_path, "w", encoding="utf-8") as ipynb_file:
        json.dump(notebook_dict, ipynb_file, indent=2)
    print(f"✅ Successfully converted to {ipynb_path}")
except json.JSONDecodeError as e:
    print("❌ Failed to parse JSON. Error:", e)
