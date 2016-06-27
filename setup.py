# AL3X V3GAS KeyGen
# AL3X V3GAS 2016 (C)
# The AVX Project 2016 (C)

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='keygen',


    version='2016.3',

    description='key generator',
    long_description=long_description,


    url='https://gitlab.com/al3xv3gas/keygen',


    author='al3xv3gas',
    author_email='alexvegasdesign@gmail.com',


    license='MIT',


    classifiers=[

        'Development Status :: 5 - Production/Stable',


        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',


        'License :: OSI Approved :: MIT License',


        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],


    keywords='development',


    packages=find_packages(),



    install_requires=['pip'],


    package_data={
        'asl': ['package_data.dat'],
    },


    data_files=[('my_data', ['data/data_file'])],


    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
