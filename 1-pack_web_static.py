#!/usr/bin/python3

""" This is a fabric script to archive all web_static files
into one file """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ A function to pack all files in web_static
    folder
    """
    date_now = datetime.now().strftime("%Y%m%d%H%M%S")

    local('mkdir -p versions')
    status = local(
        'tar -cvf versions/web_static_{}.tgz web_static'.format(date_now))

    if status.failed:
        return None
    else:
        return 'versions/web_static_{}.tgz'.format(date_now)
