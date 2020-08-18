#!/usr/bin/python3
""" distributes an archive to web servers
"""
from fabric.operations import local, run, put, env
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['34.75.116.54', '35.243.144.246']


def do_pack():
    """Crates a .tgz"""
    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -zcvf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None


def do_deploy(archive_path):
    """distribute an archive"""
    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    file_name = archive_path[9:]
    dir_name = "/data/web_static/releases" + file_name[:-4]
    file_name = "/tmp/" + file_name
    if not run('mkdir -p {}'.format(dir_name)).succeeded:
        return False
    if not run('tar -zxf {} -c {}'.format(file_name, dir_name)).succeeded:
        return False
    if not run('rm {}'.format(file_name)).succeeded:
        return False
    if not run('mv {}/web_static/* {}'.format(dir_name, dir_name)).succeeded:
        return False
    if not run('rm -rf {}/web_static/'.format(dir_name)).succeeded:
        return False
    if not run('rm -rf /data/web_static/current').succeeded:
        return False
    return run('ln -s {} /data/web_static/current'.format(dir_name)).succeeded

if __name__ == "__main__":
    do_pack()
