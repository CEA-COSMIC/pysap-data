#! /usr/bin/env python
##########################################################################
# XXX - Copyright (C) XXX, 2018
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# System import
from __future__ import print_function
import os
from setuptools import setup, find_packages


# Global parameters
PKGDATA = {
    "pysap-data": [
        os.path.join("*.nii"),
        os.path.join("*.nii.gz"),
        os.path.join("*.fits"),
        os.path.join("*.tif"),
        os.path.join("*.npy")]
}
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Environment :: Console",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering"]
AUTHOR = """
Antoine Grigis <antoine.grigis@cea.fr>
Samuel Farrens <samuel.farrens@gmail.com>
Jean-Luc Starck <jl.stark@cea.fr>
Philippe Ciuciu <philippe.ciuciu@cea.fr>
Zineb Saghi <zineb.saghi@cea.fr>
"""

# Write setup
setup(
    name="python-pySAP-data",
    description="Python Sparse data Analysis Package toy datasets.",
    long_description="Python Sparse data Analysis Package toy datasets.",
    license="CeCILL-B",
    classifiers="CLASSIFIERS",
    author=AUTHOR,
    author_email="XXX",
    version="0.0.1",
    url="https://github.com/CEA-COSMIC/pysap-data",
    packages=find_packages(),
    platforms="OS Independent",
    package_data=PKGDATA
)
