#!/usr/bin/python3
"""
Fabric script that creates a compressed version
of the web_static folder of the AirBnB Clone
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    local("mkdir -p versions")
    now = dateime.now
    archive_path = f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"
    if local(f"tar -czvf versions/{archive_path} web_static").succeeded:
        return archive_path
    else:
        return None
