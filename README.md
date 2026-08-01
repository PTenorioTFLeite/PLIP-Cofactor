\# PLIP with Cofactor Support



Modified version of PLIP (Protein-Ligand Interaction Profiler) that adds the ability to treat cofactors as part of the protein structure.



\## What's New



This fork adds a `--cofactor` option that allows you to specify molecules (like NADH, FAD, etc.) to be treated as part of the protein receptor rather than as ligands. This enables detection of interactions between cofactors and actual ligands.



\## Installation



\### From GitHub

```bash

pip install git+https://github.com/PTenorioTFLeite/PLIP-Cofactor.git

```



\### From Source

```bash

git clone https://github.com/PTenorioTFLeite/PLIP-Cofactor.git

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

\- Citation: 
If you are using PLIP with cofactor support in your work, please cite:

**For the cofactor modification:**
- Leite, P. et al. "Underexplored Ligand-Binding Features of FabI From Staphylococcus aureus and Escherichia coli: A Comparative Pharmacophoric Modeling and Surface Mapping Approach." ChemMedChem 2026. doi: [10.1002/cmdc.70410](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cmdc.70410)
- Leite, P. et al. "Reading between the Chains: Surface Mapping and Druggable Pockets on the Biological Assemblies of DENV-2's Protein E." *ACS Omega* 2026. doi: [10.1021/acsomega.5c08709](https://pubs.acs.org/doi/10.1021/acsomega.5c08709)

**For the original PLIP:**
- Adasme, M. et al. "PLIP 2021: expanding the scope of the protein-ligand interaction profiler to DNA and RNA." *Nucleic Acids Research* (05 May 2021), gkab294. doi: [10.1093/nar/gkab294](https://doi.org/10.1093/nar/gkab294)

or

- Salentin, S. et al. "PLIP: fully automated protein-ligand interaction profiler." *Nucleic Acids Research* (1 July 2015) 43 (W1): W443-W447. doi: [10.1093/nar/gkv315](https://doi.org/10.1093/nar/gkv315)






\## License



GNU General Public License v2 - see \[LICENSE](LICENSE) file for details.



This software is a derivative work of PLIP and maintains the same GPL v2 license.

