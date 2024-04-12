# coding=utf-8

"""Build/test/install tf_agents"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import codecs
import datetime
import fnmatch
import io
import os 
import subprocess
import sys
import unittest

from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test as TestCommandBase
from setuptools.dist import Distribution


