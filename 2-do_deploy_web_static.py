#!/usr/bin/python3
""" script to deploy the static webserers """

import os
from fabric.api import run, put, env

env.hosts = ['34.202.158.120', '18.234.145.174']


def do_deploy(archive_path):
    """ this is  a function to deploy the server """

    if not os.path.isfile(archive_path):
        return False

    archive_name = archive_path.split('/')[1].split('.')[0]

    status = put(archive_path, '/tmp')
    if status.failed:
        return False

    status = run('mkdir -p /data/web_static/releases/{}'.format(archive_name))
    if status.failed:
        return False

    status = run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.format(
        archive_name, archive_name))
    if status.failed:
        return False

    status = run('rm /tmp/{}.tgz'.format(archive_name))
    if status.failed:
        return False

    status = run('mv /data/web_static/releases/{}/web_static/* \
    /data/web_static/releases/{}'.format(archive_name, archive_name))
    if status.failed:
        return False

    status = run(
        'rm -rf /data/web_static/releases/{}/web_static'.format(archive_name))
    if status.failed:
        return False

    status = run('rm -rf /data/web_static/current')
    if status.failed:
        return False

    status = run('ln -s /data/web_static/releases/{} \
        /data/web_static/current'.format(archive_name))
    if status.failed:
        return False

    return True
