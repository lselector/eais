### packaging and uploading a python module

```
I want to create module "eais" to use as:
     pip install eais
     import eais.mybag
     import eais.myutils
     import eais.util_jupyter

I have created repo "eais" with the following structure:

eais/
├── setup.py
├── README.md
├── LICENSE
├── eais/
│   ├── __init__.py
│   ├── mybag/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── myutils/
│   |   ├── __init__.py
│   |   └── main.py
│   ├── util_jupyter/
│   |   ├── __init__.py
│   |   └── main.py
└── tests/
    ├── test_mybag.py
    ├── test_myutils.py
    └── test_util_jupyter.py
```

setup.py:

``` python
from setuptools import setup, find_packages

setup(
    name='eais',
    version='0.1',
    packages=find_packages(exclude=['tests*'. 'doc*']),
    author='Lev Selector',
    author_email='lev.selector@gmail.com',
    description='A package containing modules mybag and myutils ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/eais',
    install_requires=[
        os, sys, re, pandas, numpy, pickle, json, 
        time, datetime, unidecode, glob, gc, IPython
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
```

eais/__init.py:

``` python
from . import mybag
from . import myutils
from . import util_jupyter
```

create empty __init__.py for individual modules:

```
   touch mybag/__init__.py
   touch myutils/__init__.py
   touch util_jupyter/__init__.py

   touch mybag/main.py
   touch myutils/main.py
   touch util_jupyter/main.py
```

 - copy code into main.py files
 - Create a `README.md` file
 - Create a `LICENSE` file
 - Install required tools:
   ```
   pip install setuptools wheel twine
   ```
 - Build your package:
   ```
   python setup.py sdist bdist_wheel
   ```
   This will create a `dist/` directory with your package files.
 - Create a PyPI Account - register on https://pypi.org 
   (email, username, password)
 - Upload Your Package using twine (use username/password)
   ```
   twine upload dist/*
   ```
 - Install and Test Your Package
   ```
   pip install eais

   import eais
   ```

### Additional Tips

- Use virtual environments to keep your development environment clean.
- Consider using `setup.cfg` for configuration and `pyproject.toml` for build system requirements.
- For subsequent releases, update the version number in `setup.py`
- You can use TestPyPI for testing before uploading to the main PyPI repository.
