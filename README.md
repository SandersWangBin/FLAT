# FLAT
FLAT (Flat LAnguage Tool) is the python tool to convert the specified rules to specified data structure.

For example:

```
FLAT:

j'{int:{range:"0, 2, 4-6"}}'.FLAT({format:list, out:all})

Output:

[0, 2, 4, 5, 6]
```
