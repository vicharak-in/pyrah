from setuptools import find_packages, setup

setup(
    name = "pyrah",
    packages = find_packages(),
    version = "0.0.3",
    install_requires = ['numpy'],
    description = "Vaaman Read - Write functions for FPGA",
    author = "djkabutar <d.kabutarwala@yahoo.com>",
)
