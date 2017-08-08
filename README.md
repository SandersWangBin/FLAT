# FLAT
FLAT (Flat LAnguage Tool) is the python tool to convert the specified rules to specified data structure.

For example:

```
FLAT:
j'{"type":"int", "rule":{"range":"0,2,4-6"}}'.FLAT({"out":"list", "format":"value"})

Output:
[0, 2, 4, 5, 6]
```
