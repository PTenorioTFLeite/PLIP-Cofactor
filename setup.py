from setuptools import setup, find_packages
import os

# Read the README file for long description
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='plip-cofactor',
    version='2.3.0.post1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'plip=plip.plipcmd:main',
        ],
    },
    install_requires=[
        # openbabel should be installed via conda: conda install -c conda-forge openbabel
        # pymol should be installed via conda: conda install -c schrodinger pymol
    ],
    python_requires='>=3.6',
    author='Your Name (based on original PLIP by Salentin et al.)',
    author_email='your.email@example.com',
    description='PLIP with cofactor support - treats cofactors as protein components',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/YOUR_USERNAME/plip-cofactor',
    license='GPLv2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
    ],
    keywords='bioinformatics protein-ligand interactions structural-biology cofactor',
)
