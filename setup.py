from setuptools import setup, find_packages, tests_require, packages

with open("README", 'r') as f:
    long_description = f.read()

setup = (
    name='Hackers and Slackers API',
    version='0.0.1',
    description='Standalone API to handle account creation, auto-publish to medium, and site-wide link embeds.',
    long_description=long_description,
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    url="https://github.com/toddbirchard/hackersandslackers-api",
    packages=['application'],
    install_requires=[
        "bs4",
        "flask",
        "flask-redis",
        "sendgrid",
        "pandas",
        "flask_sqlalchemy",
        "sqlalchemy",
        "requests"
    ]
)
