# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from setuptools import setup

import os
import sys

NAME = 'statementicatordb'
AUTHOR_EMAIL = 'mjt@fadconsulting.com'
URL = 'https://github.com/mjtorn/statementicatordb'

def get_egg_version():
    dirname = os.path.dirname(__file__)
    dir = os.path.split(dirname)[1]

    egg_dir = '%s.egg-info' % dir
    egg_path = os.path.join(dirname, egg_dir)

    #pkg_info = os.path.join(egg_path, 'PKG-INFO')
    pkg_info = 'PKG-INFO'

    #with open(pkg_info, 'r') as pkg_info_f:
    pkg_info_f = open(pkg_info, 'r')
    if True:
        for line in pkg_info_f.readlines():
            split_line = line.split(': ')
            if split_line[0] == 'Version':
                return split_line[1].strip()

    raise ValueError('No version found')

def get_version():
    stdin_f, stdout_f, stderr_f = os.popen3('git ls-remote .')

    stderr = stderr_f.read()
    if stderr:
        #print stderr
        try:
            return get_egg_version()
        except Exception, e:
            print e
            sys.exit(1)

    stdout = stdout_f.readlines()

    head = None
    tag = None
    for line in stdout:
        hash, name = line.split()
        if name == 'HEAD':
            head = hash

        if head and hash == head and 'tag' in name:
            tag = name.rsplit('/', 1)[-1]
            tag = '.'.join(tag.split('.')[:-1])

    if tag is None:
        print 'tag not found'
        sys.exit(1)

    return tag

packages = []

def get_packages(arg, dir, fnames):
    global packages

    if '__init__.py' in fnames:
        packages.append(dir.replace('/', '.'))

os.path.walk(NAME, get_packages, None)

setup(
    name = NAME,
    version = get_version(),
    author = 'Markus Törnqvist',
    author_email = AUTHOR_EMAIL,
    url = URL,
    packages = packages,
#    package_data = package_data, # MANIFEST.in where available
    include_package_data = True,
    long_description = '%s.' % NAME,
#    install_requires = ('django==1.3.1',),
)

# EOF

