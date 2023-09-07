#!/usr/bin/python3
"""distribute archive to webservers"""


from fabric.api import *
from datetime import datetime
from os.path import exists
import os

env.hosts = ['52.91.136.4', '34.229.184.55']


def do_deploy(archive_path):
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
