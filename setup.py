#!/usr/bin/env python
from setuptools import setup

with open('README.md') as f:
    DESCRIPTION = f.read()


setup(
    name='Quaternion Convolutional Neural Networks for automatic speech recognition',
    version='1',
    license='MIT',
    long_description=DESCRIPTION,
    packages=['complexnn'],
    scripts=['scripts/run.py', 'scripts/training.py'],
    install_requires=[
        "numpy", "scipy", "sklearn", "Theano", "keras", "kerosene", "tensorflow-gpu"]
        
)
