#!/usr/bin/env python
from distutils.core import setup

setup(name         = 'robotframework-rammbock',
      version      = '0.1.0',
      description  = 'Protocol testing library for Robot Framework',
      author       = 'Robot Framework Developers',
      author_email = 'robotframework-users@googlegroups.com',
      url          = 'http://github.com/robotframework/Rammbock/',
      package_dir  = {'' : 'src'},
      packages     = ['Rammbock']
      )