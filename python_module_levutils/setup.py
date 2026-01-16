"""Setup script for levutils package."""

from setuptools import setup, find_packages

# --------------------------------------------------------------
def read_readme():
    """Read README.md file for long description."""
    return open('README.md').read()

# --------------------------------------------------------------
setup(
    name='levutils',
    version='0.2',
    packages=find_packages(exclude=['tests*', 'doc*']),
    author='Lev Selector',
    author_email='lev.selector@gmail.com',
    description='A package containing modules mybag and myutils',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/eais',
    install_requires=[
        "pandas", "numpy", "unidecode", "ipython"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)