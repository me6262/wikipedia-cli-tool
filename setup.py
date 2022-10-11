from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().readlines()
    
setup(
    name='wikipedia-cli-tool',
    version='0.1.0',
    author='Hayden Mitchell',
    author_email='hayd6262@gmail.com',
    description='A command line tool for searching Wikipedia and other things that the wikipedia module can do.',
    
)