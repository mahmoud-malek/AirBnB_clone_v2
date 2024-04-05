#!/usr/bin/python3
""" a Fabric script (based on the file 2-do_deploy_web_static.py)
 that creates and distributes an archive to your web servers,
  using the function deploy:"""

from fabric.api import env, local, run, put, runs_once
from datetime import datetime
import os
env.hosts = ['18.234.145.174', '34.202.158.120']


@runs_once
def do_pack():
    """ A function to pack all files in web_static
    folder
    """
    date_now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = 'versions/web_static_{}.tgz'.format(date_now)
    local('mkdir -p versions')

    status = local(
     'tar -cvzf {} web_static'.format(archive_path))

    if status.failed:
        return None
    else:
        return archive_path


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


def deploy():
    """this is a function to fully deploy the website"""

    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
