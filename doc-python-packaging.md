### packaging and uploading a python module

```
I want to create module "levutils" to use as:
     pip install levutils
     import levutils.mybag
     import levutils.myutils
     import levutils.util_jupyter

I have created repo "eais" with with directory levutils:

eais/
├── setup.py
├── README.md
├── LICENSE
├── levutils/
│   ├── __init__.py
│   ├── mybag.py
│   ├── myutils.py
│   ├── util_jupyter.py
```

setup.py:

``` python
from setuptools import setup, find_packages

setup(
    name='levutils',
    version='0.2',
    packages=find_packages(exclude=['tests*', 'doc*']),
    author='Lev Selector',
    author_email='lev.selector@gmail.com',
    description='A package containing modules mybag and myutils ',
    long_description=open('README.md').read(),
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
```

levutils/__init.py:

``` python
from . import mybag
from . import myutils
from . import util_jupyter
```

 - Create a `README.md` file
 - Create a `LICENSE` file
 - Install required tools:
   ```
   pip install setuptools wheel twine
   ```
 - Build your package:
   ```
   rm -rf build dist levutils.egg-info
   python setup.py sdist bdist_wheel
   ```
   This will create a `dist/` directory with your package files.
 - Create a PyPI Account - register on https://pypi.org 
   (email, username, password), generate API token
 - Upload Your Package using twine (use API token)
   ```
   twine upload dist/*
   ```
 - Install and Test Your Package
   ```
   pip install levutils

   import levutils
   ```

### Additional Tips

- Use virtual environments to keep your development environment clean.
- Consider using `setup.cfg` for configuration and `pyproject.toml` for build system requirements.
- For subsequent releases, update the version number in `setup.py`
- You can use TestPyPI for testing before uploading to the main PyPI repository.
