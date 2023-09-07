#!/usr/bin/python3
"""fabric script
Generate a.tgz archive
"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """A fabric script that generates a .tgz archive"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"versions/web_static_{date}.tgz"
    r = local("sudo tar -cvzf {} web_static".format(file_name))

    if r.succeeded:
        return file_name
    else:
        return None
