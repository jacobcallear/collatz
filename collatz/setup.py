from setuptools import setup, find_packages

setup(
    name='collatz',
    version='0.1.0',
    url='https://github.com/jacobcallear/collatz',
    author='Jacob Callear',
    author_email='jacob18@callear.net',
    description='Create, plot, and investigate Collatz sequences.',
    packages=find_packages(),
    install_requires=['matplotlib>=3.3.2']
)
