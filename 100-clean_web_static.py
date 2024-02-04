#!/usr/bin/python3
# Fabfile to delete outdated archives
import os
from fabric.api import *


env.hosts = ["52.91.123.243", "34.227.101.27"]


def do_clean(number=0):
    """
    Cleaning outdated archives from both the servers and local storage
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
