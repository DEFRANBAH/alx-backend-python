#!/usr/bin/env python3

# module to handle at test files in the FAP project
from fabric.api import local, settings, abort, run, cd, env, sudo
from fabric.contrib.console import confirm

def test():
    local('ls -l /etc/nginx/sites-available')   # list the files in the directory   
    local('ls -l /etc/nginx/sites-enabled')     # list the files in the directory
    local('ls -l /etc/nginx/sites-enabled/default')  # list the files in the directory
    local('cat /etc/nginx/sites-available"/default')  # list the files in the directory
