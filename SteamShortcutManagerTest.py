#!/usr/bin/env python
# encoding: utf-8
"""
SteamShortcutManagerTest.py

Created by Scott on 2012-12-20.
Copyright (c) 2012 Scott Rice. All rights reserved.
"""

import sys
import os

from SteamShortcutManager import *

def test(description,file,manager):
    file_contents = open(file,"r").read()
    generated_contents = manager.to_shortcuts_string()
    result = (file_contents == generated_contents)
    print "%s: %s" % (description,"Pass" if result else "Fail")    
    # If the contents did not match, write the contents to a file so I can
    # see where I went wrong
    generated_filename = file+".generated"
    if not result:
        open(generated_filename,"w").write(generated_contents)
    # If the test did pass, get rid of the generated files I made
    else:
        if os.path.exists(generated_filename):
            os.remove(generated_filename)
                
        

manager = SteamShortcutManager()

test("No Shortcuts","vdfs/empty-shortcuts.vdf",manager)

manager.add_game("iLoL Open Beta 1.1","\"/Applications/iLoL Open Beta 1.1.app\"","\"/Applications/\"")

test("One Shortcut","vdfs/onlyilol-shortcuts.vdf",manager)

windows_manager = SteamShortcutManager()
windows_manager.add_game(   "Paper Mario",
                            "\"C:\Program Files (x86)\Project64\Project64.exe\" \"C:\Users\Scott.Scott-PC\ROMs\N64\PaperMario.n64\"",
                            "\"C:\Program Files (x86)\Project64\\\"")
windows_manager.add_game(   "Final Fantasy X",
                            "\"C:\Program Files (x86)\Emulator Copies\Final Fantasy X\pcsx2-r5350.exe\"  \"C:\Users\Scott.Scott-PC\ROMs\PS2\Final Fantasy X.iso\"",
                            "\"C:\Program Files (x86)\Emulator Copies\Final Fantasy X\\\"")
windows_manager.add_game(   "Kingdom Hearts",
                            "\"C:\Program Files (x86)\Emulator Copies\Kingdom Hearts\pcsx2-r5350.exe\" \"C:\Users\Scott.Scott-PC\ROMs\PS2\Kingdom Hearts.iso\"",
                            "\"C:\Program Files (x86)\Emulator Copies\Kingdom Hearts\\\"")

test("Three Complex Shortcuts","vdfs/windows-shortcuts.vdf",windows_manager)                  

icon_manager = SteamShortcutManager()

icon_manager.add_game(  "Minecraft",
                        "\"/Users/scottrice/Applications/Minecraft.app\"",
                        "\"/Users/scottrice/Applications/\"",
                        "/Users/scottrice/Downloads/glyphish-icons/PNG icons/06-magnify.png")

test("One Shortcut, Custom Icon","vdfs/iconchange-shortcuts.vdf",icon_manager)

tag_manager = SteamShortcutManager()

tag_manager.add_game(   "Minecraft",
                        "\"/Users/scottrice/Applications/Minecraft.app\"",
                        "\"/Users/scottrice/Applications/\"",
                        "/Users/scottrice/Downloads/glyphish-icons/PNG icons/06-magnify.png",
                        "Dirty Casual")

test("One Shortcut, Custom Icon and Tag","vdfs/tag-shortcuts.vdf",tag_manager)

