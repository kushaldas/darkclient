#!/usr/bin/env python
"""darkclient command line tool"""
from distutils.core import setup


setup(name='darkclient',
      version='0.1',
      description="Command line tool for darkserver",
      long_description = "Command line tool for darkserver",
      platforms = ["Linux"],
      author="Kushal Das",
      author_email="kdas@redhat.com",
      url="https://github.com/kushaldas/darkclient",
      license = "http://www.gnu.org/copyleft/gpl.html",
      data_files=[("/usr/bin",['darkclient']),
          ('/usr/share/darkclient', ['README']),
          ('/etc/',['darkclient.conf'])]
      )
