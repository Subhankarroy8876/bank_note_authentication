# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 22:59:36 2022

@author: 91863
"""

from setuptools import find_packages, setup

setup(
  name='flaskr',
  version='1.0.0',
  packages=find_packages(),
  include_package_data=True,
  zip_safe=False,
  install_requires=[
    'flask',
  ],
)