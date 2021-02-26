import json

def match_format(data, format):
    for i in format:
        if i not in data:
            return False
    return True

def cite(data, style):
    with open("cite-logic.json") as config_file:
        format = json.load(config_file)[style]

    for i in format:
        if match_format(data, i["requirements"]):
            output = i["text"]
            for key in data:
                output = output.replace(key, data[key])
            return output

print(cite({"Lastname": "Smith",
"Initials": "J. Q.",
"Year": "2000",
"Month": "January",
"Date": "10",
"Title": "A treatise on the evolution of yaks",
"Site": "yaks global", "URL": "yaks-global.com"},
"APA"))
