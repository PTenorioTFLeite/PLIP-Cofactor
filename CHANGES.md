\# Modifications to Original PLIP



This is a modified version of PLIP (Protein-Ligand Interaction Profiler)



\## Original Software

\- Original Authors: Sebastian Salentin, Joachim Haupt, Melissa F. Adasme, et al.

\- Original Repository: https://github.com/pharmai/plip

\- License: GNU General Public License v2



\## Modifications

\- Date: March 2026

\- Modified by: Pedro Tenório T. F. Leite



\### Changes Made:



\#### 1. Added `--cofactor` Command-Line Option

\- \*\*File\*\*: `plipcmd.py`

\- \*\*Change\*\*: Added argument parser option for specifying cofactors

\- \*\*Code\*\*: Added `parser.add\_argument("--cofactor", ...)`



\#### 2. Added COFACTOR Configuration Variable

\- \*\*File\*\*: `plip/basic/config.py`

\- \*\*Change\*\*: Added `COFACTOR = \[]` configuration variable



\#### 3. Modified Ligand Filtering Logic

\- \*\*File\*\*: `plip/structure/preparation.py`

\- \*\*Method\*\*: `filter\_for\_ligands()`

\- \*\*Change\*\*: Exclude cofactors from ligand candidates

\- \*\*Code\*\*: Added `if config.COFACTOR:` filtering condition



\#### 4. Modified Protein Residue Definition

\- \*\*File\*\*: `plip/structure/preparation.py`

\- \*\*Method\*\*: `load\_pdb()` in `PDBComplex` class

\- \*\*Change\*\*: Include cofactors in protein residue list (self.resis)



\## Purpose

These modifications allow cofactors (e.g., NADH, NAD, FAD, FMN) to be treated as part of the protein structure rather than as ligands, enabling detection of interactions between cofactors and actual ligands.



\## Usage Example

```bash

plip -f structure.pdb --cofactor NAD NADH -x -t

```

