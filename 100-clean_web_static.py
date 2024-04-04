#!/usr/bin/python3
""" a fabric script that deletes out-of-date archives,
 using the function do_clean"""

import os
from fabric.api import local, env, run

env.hosts = ['18.234.145.174', '34.202.158.120']


def do_clean(number=0):
    """ a function that deletes out-of-date archives"""
    number = int(number)
    if number < 2:
        number = 2
    local('ls -dt versions/* | tail -n +{} | xargs rm -rf'.format(number))
    run('ls -dt /data/web_static/releases/* |\
         tail -n +{} | xargs rm -rf'.format(number))
