#!/usr/bin/python3
"""
Distributes an archive to web servers
- Upload the archive to the /tmp/ directory of the web server
- Uncompress the archive to the folder:
    /data/web_static/releases/<archive filename without extension>
    on the web server
- Delete the archive from the web server
- Delete the symbolic link /data/web_static/current from the web server
- Create a new the symbolic link /data/web_static/current on the web server,
    linked to the new version of your code
    (/data/web_static/releases/<archive filename without extension>)
"""

from os.path import exists
from fabric.api import put, run, env

env.hosts = ['35.196.60.120', '35.237.139.171']


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
