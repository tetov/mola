#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
from os import path

from setuptools import find_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))


def _read(*names, **kwargs):
    return io.open(
        path.join(here, *names), encoding=kwargs.get("encoding", "utf8")
    ).read()


long_description = _read("README.md")

extras_require = {
    "dev": [
        "black ~= 19.10b0",
        "doc8",
        "flake8",
        "isort",
        "pydocstyle",
        "setuptools_scm[toml]",
    ],
    "blender": ["bpy"]
}

setup(
    name="mola",
    description="fork of dbt-ethz/mola as a buildable package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tetov/mola",
    author="Anton T Johansson",
    author_email="anton@tetov.se",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython",
    ],
    keywords=["architecture", "engineering", "fabrication", "construction"],
    project_urls={
        "Repository": "https://github.com/tetov/mola",
        "Issues": "https://github.com/tetov/mola/issues",
    },
    packages=find_packages(where="."),
    package_dir={"": "."},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    extras_require=extras_require,
    entry_points={"console_scripts": []},
)
