from setuptools import setup
import os

d = {}
exec(open("cariboo/version.py").read(), None, d)
version = d['version']

install_requires = [
                    'numpy',
                    ]
                    
long_description = ""

setup(
    name = "cariboo",
    version = version,
    packages = ['cariboo'],
    install_requires=install_requires,
    author = "Cariboo team from Lyon",
    author_email = "",
    description = "Un viewer qui defonce",
    long_description = long_description,
    license = "MIT",
    url='https://github.com/tridesclous/trisdesclous',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering']
)
