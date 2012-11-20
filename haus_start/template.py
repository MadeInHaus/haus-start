""" Parses template.json and applies the fetch attribute 

Based in part on Kyle Phillip's library.js and sketchplate.js from his Sketchplate project: https://github.com/hapticdata/Sketchplate/blob/master/lib
"""


from os import path
import sys
from json import load

from fetch import fetch



class Library():
    def __init__(self, params):
        self.__dict__.update(params) 
    
    def exists(self):
        if isinstance(self.target, basestring):
            return path.exists(self.target)
        else:
            for prop in self.target:
                if not path.exists(self.target[prop]):
                    return False
            return True
    
    def fetch(self, **kwargs):
        fetch(self.__dict__, **kwargs)
    
    def __unicode__(self):
        return self.__dict__
        

def build_library(root, settings, key):
    libs = []
    for resource_id in settings[key]:
        lib_info = Library({ prop:  settings[key][resource_id][prop] for prop in settings[key][resource_id] })
        lib_info.id = resource_id
        if isinstance(lib_info.target, basestring):
            lib_info.target = path.join(root, lib_info.target)
        else:
            for prop in lib_info.target:
                lib_info.target[prop] = path.join(root, lib_info.target[prop])
        libs.append(lib_info)
    return libs

def parse_template_file(file_name, copy_to='default_dir'):
    libs = None
    try:
        json = load(open(file_name))
        libs = build_library(copy_to, json, 'fetch')
    except:
        print sys.exc_info()
        raise
    return libs