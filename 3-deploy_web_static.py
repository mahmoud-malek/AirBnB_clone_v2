#!/usr/bin/python3
""" a Fabric script (based on the file 2-do_deploy_web_static.py)
 that creates and distributes an archive to your web servers,
  using the function deploy:"""

import os
from fabric.api import run, put, env, local
from datetime import datetime

env.hosts = ['34.202.158.120', '18.234.145.174']


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

    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(
            name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(
            name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """this is a function to fully deploy the website"""

    archive_path = do_pack()
    if archive_path is None:
        return None

    return do_deploy(archive_path)
