import sys
import os
import re
import shutil
from distutils.dir_util import copy_tree
import stat
import fnmatch
from random import choice
from haus_start.template import parse_template_file

VERSION = ('0', '1', '1')
__version__ = '.'.join(VERSION)


def clean_copy(dirname):
    # remove un-needed files
    matches = []
    for root, _dirnames, filenames in os.walk(dirname):
        for filename in fnmatch.filter(filenames, '*.pyc') + \
                        fnmatch.filter(filenames, '.git'):
            matches.append(os.path.join(root, filename))

    for m in matches:
        if os.path.exists(m):
            os.remove(m)


def start_project(copy_to=None, copy_from=None, no_prompt=False, no_git=False):
    if not copy_from:
        basedir = os.path.join(os.path.dirname(__file__), 'templates/project')
        default_template = os.path.join(basedir, 'template.json')
        templates = [file_ for file_ in os.listdir(basedir) if file_.endswith('.json')]
        default = {
            file_: index for index, file_ in enumerate(templates)
        }[os.path.split(default_template)[1]] + 1
        prompt = '\nAvailable templates:\n{}\n Choose an option [{}]: '.format('\n'.join(
            '{}. {}'.format(index + 1, filename)
            for index, filename
            in enumerate(templates)
        ), default)

        template = raw_input(prompt)

        if template:
            copy_from = os.path.join(basedir, templates[int(template) - 1])
        else:
            copy_from = default_template

    if not copy_to:
        copy_to = os.getcwd()
    else:
        if os.path.exists(copy_to):
            print "%s already exists" % copy_to
            return

    libs = parse_template_file(copy_from, copy_to)

    for lib in libs:
        lib.fetch()

    clean_copy(copy_to)

    # 2. If template has a settings file, run its after_copy method
    settings_path = os.path.join(copy_to, 'haus_start_settings.py')
    if os.path.exists(settings_path):
        sys.path.append(copy_to)
        import haus_start_settings
        if callable(getattr(haus_start_settings, 'after_copy', None)):
            # First change current directory to copy_to
            os.chdir(copy_to)
            haus_start_settings.after_copy(no_prompt=no_prompt, no_git=no_git)
        sys.path.remove(copy_to)

        # remove post copy settings file
        os.remove('haus_start_settings.py')
        os.remove('haus_start_settings.pyc')

