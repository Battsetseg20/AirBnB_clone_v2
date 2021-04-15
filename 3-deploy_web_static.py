#!/usr/bin/python3
"""
Creates and distributes an archive to web servers
"""

from os.path import exists, isdir
from fabric.api import local, put, run, env
from datetime import datetime


env.hosts = ['35.196.60.120', '35.237.139.171']


def do_pack():
    """Generates .tgz archive"""
    try:
        if isdir('versions') is False:
            local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archiveName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archiveName))
        return archiveName
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to web server"""
    if exists(archive_path) is False:
        return False
    try:
        file_path = archive_path.split("/")[-1]
        fileName = file_path.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, fileName))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_path, path, fileName))
        run('rm /tmp/{}'.format(file_path))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, fileName))
        run('rm -rf {}{}/web_static'.format(path, fileName))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, fileName))
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
