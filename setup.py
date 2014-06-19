# -*- coding: utf-8 -*-
import repy

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name=repy.__pkgname__,
    version=repy.__version__,
    description="Python Regex cli tool",
    author_name=repy.__author_name__,
    author_email=repy.__author_email__,
    packages=["repy"],
    scripts=['bin/repy-cli'],
    data_files=[],
    include_package_data=True,
    install_requires=['docopt>=0.6.1'],
    classifiers=(
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        #'Development Status :: 6 - Mature',
        #'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Console',
        'Operating System :: POSIX',
        # 'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development',
        'Topic :: cli',
        'Topic :: Regex')
)
