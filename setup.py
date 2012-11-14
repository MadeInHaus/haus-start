#!/usr/bin/env python
from distutils.core import setup
import glob
import os
import subprocess

subprocess.call(["git", 'submodule', 'init'])
subprocess.call(["git", 'submodule', 'update'])

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haus_start'))

data_files = []
for dirpath, dirnames, filenames in os.walk(os.path.join(base_path, 'templates')):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]

    files = [os.path.join(dirpath, f)[len(base_path)+1:] \
                            for f in filenames if not f.endswith('.pyc')]
    data_files.extend(files)

setup(
    name='haus-start',
    version=__import__('haus_start').__version__,
    description='Create a Django project based on HAUS best practices.',
    author='HAUS',
    author_email='cms-admin@madeinhaus.com',
    url='http://github.com/madeinhaus/haus-start/',
    packages=[
        'haus_start',
    ],
    package_data={ 'haus_start' : data_files },
    scripts=['bin/haus-start'],
    install_requires=['Fabric'],
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities'
    ],
)
