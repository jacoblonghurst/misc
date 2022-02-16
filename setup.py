from pathlib import Path
from setuptools import setup, find_packages


here = Path('.')

readme = here / 'README.rst'
long_desc = ''
if readme.exists():
    with readme.open('r', encoding='utf-8') as f:
        long_desc = f.read()


reqs = here / 'requirements.txt'
required = [] 
if reqs.exists():
    with reqs.open('r', encoding='utf-8') as f:
        required = f.read().splitlines()


setup_requires = list(required)

setup(
    name='misc',
    version='0.0.1',
    description='Miscellaneous tools and functions',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    url="https://github.com/jacoblonghurst/misc",
    setup_requires=setup_requires,
    install_requires=required,
    author='Jacob Longhurst',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False
)

