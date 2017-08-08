# FLAT
FLAT (Flat LAnguage Tool) is the python tool to convert the specified rules to specified data structure.

For example:

## EXAMPLE 1:

```
FLAT:
j'{"type":"int", "rule":{"range":"0,2,4-6"}}'.FLAT({"out":"list", "format":"value if matched else None"})
Output:
[0, 2, 4, 5, 6]
```

## EXAPLE 2:
```
FLAT:
j'{"type":"str", "rule":{"regex":"[a-zA-Z0-9_]", "length":"1-255"}}'.FLAT({"out":"list", "format":"(value,'POS' if matched else 'NEG')"})
Output:
[('atoz', 'POS'), ('AtoZ', 'POS'), ('öäå', 'NEG')]
```
