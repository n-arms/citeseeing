#!/usr/bin/env python3
import json
from tkinter import *

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
        self.entries = [(Label(self, text=i, font="arial 15"), Entry(self, text='', font="arial 15")) for i in self.pretty_name]
        for i in range(len(self.entries)):
            self.entries[i][0].grid(row=i, column=0)
            self.entries[i][1].grid(row=i, column=1)
        self.citation_box = Text(self, wrap='word', height=3)
        self.citation_box.insert('end', "Enter some data for a citation!")
        self.citation_box['state'] = 'disabled'
        self.citation_box.grid(row=len(self.entries), column=0, columnspan=2)
        self.citation_box.tag_config("normal", font="arial 15")
        self.citation_box.tag_add("normal", "1.0", "end")


        self.cite_button = Button(self, text="cite", command=self.generate_citation, font="arial 15")
        self.cite_button.grid(row=len(self.entries)+1, column=0)

    def generate_citation(self):
        data = {}
        for i in self.entries:
            if i[1].get() != '':
                data[self.pretty_name[i[0]["text"]]] = i[1].get()
        self.citation_box['state'] = "normal"
        self.citation_box.delete('1.0', 'end')
        self.citation_box.insert("end", cite(data, "APA") or "please enter more data")
        self.citation_box.tag_add("normal", "1.0", "end")
        self.citation_box['state'] = 'disabled'


root = Tk()
f = GUIFrame(root)
root.mainloop()
