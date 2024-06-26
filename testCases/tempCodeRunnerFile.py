import json

def compare_jsons(json1, json2):
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)
    
    for key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                print(f"Difference found at key '{key}': '{dict1[key]}' vs '{dict2[key]}'")
        else:
            print(f"Key '{key}' not found in second JSON")
    
    # Check for keys in dict2 not in dict1
    for key in dict2:
        if key not in dict1:
            print(f"Key '{key}' not found in first JSON")

# Example JSON strings
json1 = '{"name": "John", "age": 30, "city": "New York"}'
json2 = '{"name": "John", "age": 30, "city": "Los Angeles"}'

# Call the function to compare
compare_jsons(json1, json2)
