# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

long_description = open("README.md").read()

setup(
    name="pyzehndercloud",
    version="0.2",
    license="MIT",
    url="https://github.com/frankBS81/pyzehndercloud",
    author="Michaël Arnauts",
    description="Python interface for the Zehnder Cloud API.",
    long_description=long_description,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=list(val.strip() for val in open("requirements.txt")),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
