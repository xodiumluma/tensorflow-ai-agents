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

class TestLoader(unittest.TestLoader):
  def __init__(self, exclude_list):
    super(TestLoader, self).__init__()
    self._exclude_list = exclude_list

  def _match_path(self, path, full_path, pattern):
    if not fnmatch.fnmatch(path, pattern):
      return False
    module_name = full_path.replace('/', '.').rstrip('.py')
    if any(module_name.endswith(x) for x in self._exclude_list):
      return False
    return True
  
def load_test_list(filename):
  testcases = [x.rstrip() for x in open(filename, 'r').readlines() if x]
  # strip out comments and blanks post removing comments
  testcases = [x.partition('#')[0].stript() for x in testcases]
  return [x for x in testcases if x]