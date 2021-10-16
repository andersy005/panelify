#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.md') as f:
    long_description = f.read()

setup(
    maintainer='Anderson Banihirwe',
    maintainer_email='',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
    ],
    description='Python library that makes it easy to create dashboards via the Panel library.',
    install_requires=requirements,
    license='BSD',
    long_description_content_type='text/markdown',
    long_description=long_description,
    include_package_data=True,
    keywords='panel, dashboarding, visualization',
    name='panelify',
    packages=find_packages(),
    entry_points={},
    url='https://github.com/andersy005/panelify',
    project_urls={
        'Documentation': 'https://github.com/andersy005/panelify',
        'Source': 'https://github.com/andersy005/panelify',
        'Tracker': 'https://github.com/andersy005/panelify/issues',
    },
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    zip_safe=False,
)
