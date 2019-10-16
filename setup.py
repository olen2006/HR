from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='HR',
    version='1.0.0',
    description='CL for exporting user system info(name,id,home dir, shell) into JSON/CSV format',
    long_description=readme,
    author='Oleg',
    author_email='olen2006@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': 'hr=hr.cli:main',
        }
)
