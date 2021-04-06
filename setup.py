#!/usr/bin/env python

from distutils.core import setup

setup(name='celestial-client',
      version='0.1',
      description='Python client for www.celestial-automl.com',
      author='Lars Hertel',
      author_email='lars.h.hertel@gmail.com',
      url='https://github.com/LarsHH/celestial-client',
      project_urls={
        "Website": "https://www.celestial-automl.com",
        "Bug Tracker": "https://github.com/LarsHH/celestial-client/issues",
      },
      packages=['celestial'],
      install_requires=['requests'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
     )
