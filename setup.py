from setuptools import setup

with open('requirements.txt') as f:
    reqs = f.read()

setup(
    name='datatools',
    version='0.1',
    description='Helper functions for processing raw data',
    url='https://github.com/mnguyenngo/datatools',
    author='Nguyen Ngo',
    author_email='mnguyenngo@gmail.com',
    license='MIT',
    packages=['datatools'],
    install_requires=[reqs.strip().split('\n')]
)
