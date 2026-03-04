\# PLIP with Cofactor Support



Modified version of PLIP (Protein-Ligand Interaction Profiler) that adds the ability to treat cofactors as part of the protein structure.



\## What's New



This fork adds a `--cofactor` option that allows you to specify molecules (like NADH, FAD, etc.) to be treated as part of the protein receptor rather than as ligands. This enables detection of interactions between cofactors and actual ligands.



\## Installation



\### From GitHub

```bash

pip install git+https://github.com/YOUR\_USERNAME/plip-cofactor.git

```



\### From Source

```bash

git clone https://github.com/YOUR\_USERNAME/plip-cofactor.git

cd plip-cofactor

pip install -e .

```



\## Usage

```bash

\# Analyze with NAD as part of the protein

plip -f your\_structure.pdb --cofactor NAD -x -t



\# Multiple cofactors

plip -f your\_structure.pdb --cofactor NAD NADH FAD -x -t



\# From PDB ID

plip -i 1ABC --cofactor NAD -x -t

```



\## Changes from Original PLIP



See \[CHANGES.md](CHANGES.md) for detailed documentation of all modifications.



\## Original PLIP



This is based on PLIP. For the original software:

\- Repository: https://github.com/pharmai/plip

\- Citation: Adasme,M. et al. PLIP 2021: expanding the scope of the protein-ligand interaction profiler to DNA and RNA. Nucl. Acids Res. (05 May 2021)



\## License



GNU General Public License v2 - see \[LICENSE](LICENSE) file for details.



This software is a derivative work of PLIP and maintains the same GPL v2 license.

