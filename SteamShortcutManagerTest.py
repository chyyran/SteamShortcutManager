#!/usr/bin/env python
# encoding: utf-8
"""
SteamShortcutManagerTest.py

Created by Scott on 2012-12-20.
Copyright (c) 2012 Scott Rice. All rights reserved.
"""

import sys, os, inspect
import unittest

from SteamShortcutManager import *

# Just need an empty class, so I am going to put some random stuff here
class TestSteamShortcutManager(unittest.TestCase):
    def setUp(self):
        self.folder = "vdfs"

def create_test(file):
    def test_file_equality(self):
        file_name = os.path.basename(file)
        file_contents = open(file,"r").read()
        manager = SteamShortcutManager(file)
        self.assertEqual(file_contents,manager.to_shortcuts_string())
    return test_file_equality

# Taken from a StackOverflow answer, which you can find here:
# http://stackoverflow.com/questions/279237/python-import-a-module-from-a-folder
current_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
vdfs_folder = os.path.join(current_folder,"vdfs")

for file in os.listdir(vdfs_folder):
    if not os.path.isdir(file):
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".vdf":
            test_method = create_test(os.path.join(vdfs_folder,file))
            test_method.__name__ = 'test_%s' % filename
            setattr (TestSteamShortcutManager, test_method.__name__, test_method)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSteamShortcutManager)
    unittest.TextTestRunner(verbosity=2).run(suite)