"""Setup for learctatxblock XBlock."""

import os
from setuptools import setup

def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                totalPath = os.path.relpath(os.path.join(dirname, fname), pkg)
                data.append(totalPath)

    return {pkg: data}


setup(
    name='learctatxblock-xblock',
    version='0.75',
    description='CTAT Tutor Package',
    packages=[
        'learctatxblock',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'learctatxblock = learctatxblock:LEARCTATXBLOCKCLASS',
        ]
    },
    package_data=package_data("learctatxblock", ["static", "public"]),
)
