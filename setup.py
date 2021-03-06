import sys
import os

from distutils.core import setup

if 'sdist' in sys.argv:
    os.system('./admin/makedoc')

import openid
version = openid.__version__

setup(
    name='python3-openid',
    version=version,
    description='OpenID support for servers and consumers.',
    long_description='''This is a set of Python packages to support use of
the OpenID decentralized identity system in your application.  Want to enable
single sign-on for your web site?  Use the openid.consumer package.  Want to
run your own OpenID server? Check out openid.server.  Includes example code
and support for a variety of storage back-ends.''',
    url='http://github.com/necaris/python3-openid',
    packages=[
        'openid',
        'openid.consumer',
        'openid.server',
        'openid.store',
        'openid.yadis',
        'openid.extensions',
        'openid.extensions.draft',
    ],
    # license specified by classifier
    author='Rami Chowdhury',
    author_email='rami.chowdhury@gmail.com',
    download_url=('http://github.com/necaris/python3-openid/tarball'
                  '/v{}'.format(version)),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        ("Topic :: Internet :: WWW/HTTP :: Dynamic Content :: "
         "CGI Tools/Libraries"),
        "Topic :: Software Development :: Libraries :: Python Modules",
        ("Topic :: System :: Systems Administration :: "
         "Authentication/Directory"),
    ]
)
