import json

def cite(data, style):
    with open("cite-logic.json") as config_file:
        format = json.load(config_file)[style]
    template = format["text"]
    for regex in format["regexes"]:
        if regex in data:
            template = template.replace(regex, data[regex])
        else:
            template = template.replace(regex, "")
    return template

print(cite({"Name": "Smith J.", "Year": "0000", "Month": "0", "Date": "0", "Title": "A treatise on the evolution of yaks", "Site": "yaks global", "URL": "yaks-global.com"}, "APA"))
