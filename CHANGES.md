\# Modifications to Original PLIP



This is a modified version of PLIP (Protein-Ligand Interaction Profiler)



\## Original Software

\- Original Authors: Sebastian Salentin, Joachim Haupt, Melissa F. Adasme, et al.

\- Original Repository: https://github.com/pharmai/plip

\- License: GNU General Public License v2



\## Modifications

\- Date: 2026

\- Modified by: Pedro Tenório T. F. Leite



### Changes Made:

#### 1. Added COFACTOR Configuration Variable
- **File**: `plip/basic/config.py`
- **Line Added**: `COFACTOR = []`
- **Purpose**: Global configuration to store list of cofactor residue names

#### 2. Added `--cofactor` Command-Line Argument
- **File**: `plipcmd.py`
- **Lines Added**: 
```python
  parser.add_argument("--cofactor", dest="cofactor", default=[],
                      help="Allows to define one or multiple residue names to be treated as part of the protein structure",
                      nargs="+")
```
- **Configuration Assignment**: `config.COFACTOR = arguments.cofactor`
- **Purpose**: Allow users to specify cofactor molecules via command line

#### 3. Modified Ligand Filtering
- **File**: `plip/structure/preparation.py`
- **Method**: `filter_for_ligands()`
- **Lines Added**:
```python
  if config.COFACTOR:  # If cofactors are specified to be part of the protein
      candidates1 = [res for res in candidates1 if res.GetName() not in config.COFACTOR]
```
- **Purpose**: Exclude specified cofactors from ligand candidate list

#### 4. Modified Protein Residue Definition
- **File**: `plip/structure/preparation.py`
- **Method**: `load_pdb()` in `PDBComplex` class
- **Lines Added**:
```python
  if config.COFACTOR:
      self.resis = [obres for obres in pybel.ob.OBResidueIter(
          self.protcomplex.OBMol) if obres.GetName() in config.COFACTOR
      ] + [obres for obres in pybel.ob.OBResidueIter(
          self.protcomplex.OBMol) if obres.GetResidueProperty(0)]
```
- **Purpose**: Include specified cofactors in protein residue list for interaction detection




\## Purpose

These modifications allow cofactors (e.g., NADH, NAD, FAD, FMN) to be treated as part of the protein structure rather than as ligands, enabling detection of interactions between cofactors and actual ligands.



\## Usage Example

```bash

plip -f structure.pdb --cofactor NAD NADH -x -t

```

