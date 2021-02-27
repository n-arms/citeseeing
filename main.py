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
        self.pretty_name = {"Lastname": "Last Name", "rMonth": "Retrieved (Month)", "rYear": "Retrieved (Year)", "rDate": "Retrieved (Date)", "Initials": "Initials", "Month": "Published (Month)", "Year": "Published (Year)", "Date": "Published (Date)", "Title": "Title", "Group": "Group Name", "URL": "URL"}
        print(self.pretty_name)
        self.entries = [(Label(self, text=self.pretty_name[i]), Entry(self, text='')) for i in self.pretty_name]
        for i in range(len(self.entries)):
            self.entries[i][0].grid(row=i, column=0)
            self.entries[i][1].grid(row=i, column=1)

root = Tk()
f = GUIFrame(root)
root.mainloop()
