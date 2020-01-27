# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages
from os.path import join, abspath, dirname, normpath

with open(join(dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(join(dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = []
with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name='meta-metadata-rules',
    version=VERSION,
    author='Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/meta-trial/meta-metadata-rules',
    license='GPL license, see LICENSE',
    description='Metadata rules for meta/edc project',
    long_description=README,
    zip_safe=False,
    keywords='django edc clinicedc meta',
    install_requires=[
        #         'meta-ae',
        #         'meta-labs',
        #         'meta-lists',
        #         'meta-prn',
        #         'meta-rando',
        #         'meta-sites',
        #         'meta-screening',
        #         'meta-subject',
        #         'meta-reference',
        #         'meta_form_validators',
        #         'meta-visit-schedule',
        'edc-action-item',
        'edc-metadata',
        'edc-metadata-rules',
        'edc-offstudy',
        'edc_constants',
        'edc-reportable',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)
