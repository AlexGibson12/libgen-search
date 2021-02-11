#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='libgensearch',
     version='0.1',
     url = 'https://github.com/AlexGibson12/libgen-search',
     download_url =''
     scripts=['./libgensearch/libgensearch'] ,
     author="Alex Gibson",
     author_email="afg9000@gmail.com",
     description="Automatically downloads libgen titles",
     long_description=long_description,
     url="https://github.com/AlexGibson12/libgen-search",
     packages=setuptools.find_packages(),
     py_modules = ['libgensearch.search','libgensearch.downloadbar','libgensearch.textsimilarity'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
