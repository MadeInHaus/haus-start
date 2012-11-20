""" Fetch

Provides methods for downloading and copying resources into your project.

1. file download
2. git clone
3. zip

Based on Kyle Phillip's fetch.js from his Sketchplate project: https://github.com/hapticdata/Sketchplate/blob/master/lib/fetch.js

"""

import os
import errno
from os import path
import tempfile
from shutil import copy2, Error, copystat, WindowsError, rmtree
from urllib import urlretrieve
from urllib2 import urlopen
from zipfile import ZipFile

def fetch(resource, options=None, callback=None):
    if options is None:
        options = {}
    
    if isinstance(resource, dict):
        # a single resource is specified with a dict
        if resource.has_key('file'):
            _from_file(resource, options)
        elif resource.has_key('clone'):
            _from_git(resource, options)
        elif resource.has_key('zip'):
            _from_zip(resource, options)
        else:
            print "Unhandled resource type for resource: {}".format(resource) 
            exit(-1)
    else:
        # if not a string it should be a list
        for res in resource:
            fetch(res, options, callback)


def _processTargets(contents_folder, resource, callback):
    targets = []
    if resource.has_key('target') and isinstance(resource['target'], basestring):
        targets.append({'source': '', 'destination': resource['target']})
    else:
        for prop in resource['target']:
            targets.append({'source': prop, 'destination': resource['target'][prop]})
    for target in targets:
        print "processing target: {}".format(target)
        _copy(contents_folder, target)
        
    
def _mkdir_p(path):
    """ modeled on Unix's mkdir -p 
    
    create directory and its parents if they do not already exist
    from http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
    """
    
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def _copytree(src, dst, symlinks=False, ignore=None):
    """ based on shutil.copytree but utilizing _mkdir_p so that destination directory may already exist """
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    _mkdir_p(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                _copytree(srcname, dstname, symlinks, ignore)
            else:
                copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)


def _copy(contents_folder, target):
    target_dir = path.dirname(target['destination'])
    print "copying from: {} to: {}".format(contents_folder, target_dir)
    _mkdir_p(target_dir)
    _copytree(path.join(contents_folder, target['source']), target['destination'])


def _from_file(resource, options=None, callback=None):
    target_dir = path.dirname(resource['target'])
    _mkdir_p(target_dir)
    (_fname, _headers) = urlretrieve(resource['file'], resource['target'])

def _from_git(resource, options=None, callback=None):
    tmp_dir = tempfile.mkdtemp()
    os.system("git clone {} {}".format(resource['clone'], tmp_dir))
    _processTargets(tmp_dir, resource, callback)
    print "cloned in: {}".format(tmp_dir)
    rmtree(tmp_dir)
    print "{} removed".format(tmp_dir)
    

def _get_root_folder(zip_file):
    unique_folders = []
    for name in zip_file.namelist():
        if name[-1] == path.sep and name not in unique_folders:
            is_inner_folder = False
            for folder in unique_folders:
                if folder in name:
                    is_inner_folder = True
            if not is_inner_folder:
                unique_folders.append(name)
    nested_in_folder = True
    if len(unique_folders) == 1:
        folder_name = unique_folders[0]
        for name in zip_file.namelist():
            if not folder_name in name:
                nested_in_folder = False
    else:
        nested_in_folder = False
    folder_name = unique_folders[0] if nested_in_folder else ""
    print "root_folder: {}".format(folder_name)
    return folder_name
            
             

def _from_zip(resource, options=None, callback=None):
    (fname, _headers) = urlretrieve(resource['zip'])
    zip_file = ZipFile(fname)
    tmp_dir = tempfile.mkdtemp()
    zip_file.extractall(tmp_dir)
    _processTargets(path.join(tmp_dir, _get_root_folder(zip_file)), resource, callback)
    rmtree(tmp_dir)
    