#standard file, used to create installable packages

from setuptools import find_packages, setup

#with open('README.rst', 'r') as f:
with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()


setup(
    name='HR',
    version='1.0',
    description='CLI exports user information',
    author='Oleg Fortochnik',
    author_email='user@email.com',
    url='https://random.url',
    long_description = readme,
    long_description_content_type = 'text/markdown',#do I need it ?
    packages = find_packages('src'),
    package_dir = {'':'src'},#package itself will be found here(from 'root':'src')
    install_requires = []
     )

