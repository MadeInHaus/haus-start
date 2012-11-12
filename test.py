#!/usr/bin/env python
# NOTE: This file is a draft for a test suite that runs everything
# haus-start is supposed to do, so whenever you change haus-start
# you can run ./test.py and see if no errors are raised.
#
# TODO: Still needs a series of 'assert' to check that, apart from errors
# haus-start does what it is supposed to do
#
from shutil import rmtree
from os import chdir, system
from sys import exit as sys_exit

PROJECT_FOLDER = 'test-project'

rmtree(PROJECT_FOLDER, ignore_errors=True)
system('bin/haus-start --no-prompt %s' % PROJECT_FOLDER)
system('sh test-project/scripts/setup.sh test' )
system('test-project/env/bin/python test-project/project/manage.py test')
rmtree(PROJECT_FOLDER)
