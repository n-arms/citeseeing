#!/usr/bin/env python3
import json
from tkinter import *

def match_format(data, format):
    print("matching")
    for i in format:
        if i not in data:
            print("failed on", i)
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

class GUIFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.pretty_name = {
        "Last Name": "Lastname",
        "Retrieved (Month)": "rMonth",
        "Retrieved (Year)": "rYear",
        "Retrieved (Date)": "rDate",
        "Initials": "Initials",
        "Published (Month)": "Month",
        "Published (Year)": "Year",
        "Published (Date)": "Date",
        "Title": "Title",
        "Group Name": "Group",
        "Site Name": "Site",
        "URL": "URL"}
        self.entries = [(Label(self, text=i), Entry(self, text='')) for i in self.pretty_name]
        for i in range(len(self.entries)):
            self.entries[i][0].grid(row=i, column=0)
            self.entries[i][1].grid(row=i, column=1)
        self.citation_box = Label(self, text="Enter some data for a citation!")
        self.citation_box.grid()
        self.cite_button = Button(self, text="cite", command=self.generate_citation)
        self.cite_button.grid()

    def generate_citation(self):
        data = {}
        for i in self.entries:
            data[self.pretty_name[i[0]["text"]]] = i[1].get()
        self.citation_box['text'] = cite(data, "APA") or (self.citation_box['text']+"'")


root = Tk()
f = GUIFrame(root)
root.mainloop()
