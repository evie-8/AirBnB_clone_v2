#!/usr/bin/python3
"""delpoy based on task 2"""


from fabric.api import *
from datetime import datetime
from os.path import exists
import os


env.hosts = ['52.91.136.4', '34.229.184.55']


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


def do_deploy(archive_path):
    """deploying using fab"""
    if exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")

        # creating new filename
        archive_name = os.path.basename(archive_path)

        new_dir = "/data/web_static/releases/" + archive_name.split(".")[0]
        run("mkdir -p {}".format(new_dir))

        # uncompress
        run(f"tar -xzf /tmp/{archive_name} -C {new_dir}/")

        # delete the archive
        run(f"rm /tmp/{archive_name}")

        run(f"mv {new_dir}/web_static/* {new_dir}")

        run(f"rm -rf {new_dir}/web_static")

        # remove symbolic link
        run("rm -rf /data/web_static/current")

        run(f"ln -s {new_dir} /data/web_static/current")
        return True
    except Exception:
        return False


def deploy():
    """combining all the tasks into one"""
    file = do_pack()
    if file is None:
        return False

    r = do_deploy(file)

    return r
