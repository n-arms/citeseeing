# citeseeing
Can't remember how APA works? Never fear! Citeseeing gives you time to focus on the important parts of your project (like sightseeing!)

## Modular Customization
The interesting part of this project is that it is very easy to add new syntaxes for different styles of citations (ie MLA, Boston, IEEE).

#### cite-logic.json
This file contains all of the data that is needed to parse citations. The syntax for the new styles is the following:
```
"STYLENAME": [
  RULE1,
  RULE2,
  RULE3,
  etc
]
```
And the syntax for a rule:
```
{
  "text": "CITATION SYNTAX"
  "requirements": "CITATION REQUIREMENTS"
}
```

Where a citation syntax is just a string that contains a series of "keys" to be replaced with other values, and requirements is the list of keys that needs to be present for the rule to apply.
