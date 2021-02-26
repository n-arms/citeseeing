import json

def cite(data, style):
    with open("cite-logic.json") as config_file:
        template = json.load(config_file)[style]
    print("loaded template", template)
    for key in data:
        print("processing key", key, "with template", template)
        template = template.replace(key, data[key])
    return template

print(cite_file({"author": "john smith"}, "APA"))
