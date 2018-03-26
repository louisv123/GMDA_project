

## Code description

The code file is composed with :
-`Distance.py`
This script takes as input the aladip_implicit.txt file and return `output`, the distance matrix with conformation key at the beginning of the line:
``` 54, 0.2545, 0.3121, 0.0123, .... , 0.14534
...
4758, 0.1445, 0.454, 0.1511, ... , 0.2154```

This script takes two arguments :
- `m` the number of conformation which we will focus on.
- `k` the number of conformation we keep to compute RMSD distance.
Example:
Computing RMSD with 10 000 conformations in dimension 5 000 would be : 
```python Distance.py 10000 5000`

-`dataprocessing.py`
This script takes as input the `output` from `Distance.py` and return `rsmd.txt`, the distance matrix without conformation key.
``` 0.2545, 0.3121, 0.0123, .... , 0.14534
...
 0.1445, 0.454, 0.1511, ... , 0.2154```

-`Vizualizing.py`
This script takes as input the `output` from `Distance.py`, `clusters.txt` from ToMATo, and `dihedral.txt` file, the 2D projection.
This script plots the 2D projection with clusters. 

## Method

-Indicate path of aladip_implicit.txt file in `Distance.py`
-Run `Distance.py` with `m` and `k` arguments.
-Indicate path of output file from `Distance.py` in `dataprocessing.py`
-Run `dataprocessing.py`
-Run main_w_density.cpp from ToMATo on `rmsd.txt`, the output file from `dataprocessing.py`
-Indicate path of output file, clusters.txt file and dihedral.txt in `vizualizing.py`.
-Run `vizualizing.py`




