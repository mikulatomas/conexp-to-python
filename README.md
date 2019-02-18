# conexp-to-python


The **Concept Explorer (conexp)** is tool for calculating and exploring FCA lattice. This library is simple tool for extracting formal context and concepts from ``.cex`` file, which is created by conexp.

## Example output
Output for ``sample2.cex`` from ``sample-data`` directory:
```
{
    'context': {
        'objects': ['Obj 1', 'Obj 2', 'Obj 3'],
        'attributes': ['Attr 1', 'Attr 2', 'Attr 3'],
        'table': [
            [True, False, False],
            [False, True, False],
            [False, True, True]
            ]},
    'concepts': [
            [True, False, False],
            [False, True, True],
            [False, True, False],
            [True, True, True],
            [False, False, False]
            ]
}
```

## What is Formal Concept Analysis?

**Formal concept analysis (FCA)** is a principled way of deriving a concept hierarchy or formal ontology from a collection of objects and their properties. Each concept in the hierarchy represents the objects sharing some set of properties; and each sub-concept in the hierarchy represents a subset of the objects (as well as a superset of the properties) in the concepts above it. The term was introduced by **Rudolf Wille** in 1980, and builds on the mathematical theory of lattices and ordered sets that was developed by Garrett Birkhoff and others in the 1930s.

https://en.wikipedia.org/wiki/Formal_concept_analysis

## Links

- Basic info about FCA: https://phoenix.inf.upol.cz/esf/ucebni/formal.pdf
- Conexp: http://conexp.sourceforge.net

## Dependencies

conexp-to-python requires:

- Python (>= 3.4)
- xmltodict

Created 2018 by Tomáš Mikula

