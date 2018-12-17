from setuptools import setup, find_packages, tests_require, packages

with open("README", 'r') as f:
    long_description = f.read()

setup = (
    name='Embedded Link Previews',
    version='1.0',
    description='Generates embedded link previews on all pages of an existing site.',
    long_description=long_description,
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    url="https://github.com/toddbirchard/embedded-link-previews",
    packages=['application'],
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
    install_requires=[
        "bs4",
        "flask",
        "configparser",
        "pandas",
        "flask_sqlalchemy"
    ]
)
