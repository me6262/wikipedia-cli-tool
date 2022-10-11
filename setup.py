from importlib_metadata import entry_points
from setuptools import setup, find_packages


setup(
    name='wikipedia-cli-tool',
    version='0.1.0',
    author='Hayden Mitchell',
    author_email='hayd6262@gmail.com',
    description='A command line tool for searching Wikipedia and other things that the wikipedia module can do.',
    url="https://github.com/me6262/wikipedia-cli-tool",
    packages=find_packages(),
    license='MIT',
    entry_points={
        'console_scripts': [
            'wiki = wiki.cli:main']
    },
    classifiers=(
        'Programming Language :: Python :: 3',
        'license :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    )
    keywords='wikipedia cli tool',
    install_requires= [ 'click', 'wikipedia' ]
)
