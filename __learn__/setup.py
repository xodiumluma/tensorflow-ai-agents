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

# add version.py to sys.path to make it possible to import it directly
version_path = os.path.join(os.path.dirname(__file__), 'tf_agents')
sys.path.append(version_path)
import version as tf_agents_version # pylint: disable=g-import-not-at-top

# what we set as default versions for packages
# they can be overridden for testing/RCs (and they are often overridden - with flags)
TFP_VERSION = 'tensorflow-probability'
TFP_NIGHTLY = 'tfp-nightly'
TENSORFLOW_VERSION = 'tensorflow'
TENSORFLOW_NIGHTLY = 'tf-nightly'
REVERB_VERSION = 'dm-reverb'
REVERB_NIGHTLY = 'dm-reverb-nightly'
RLDS_VERSION = 'rlds'
TF_KERAS_VERSION = 'tf-keras'
# @TODO(b/224850217): there aren't any rlds nightly builds
RLDS_NIGHTLY = 'rlds'

class StderrWrapper(io.IOBase):

  def write(self, *args, **kwargs):
    return sys.stderr.write(*args, **kwargs)

  def writeln(self, *args, **kwargs):
    if args or kwargs:
      sys.stderr.write(*args, **kwargs)
    sys.stderr.write('\n')