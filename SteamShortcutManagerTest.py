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

parse_results = []
generate_results = []

def test(description,file,manager):
    test_generate(description,file,manager)
    test_parse(description,file,manager)
            
def test_generate(description,file,manager):
    file_contents = open(file,"r").read()
    generated_contents = manager.to_shortcuts_string()
    result = (file_contents == generated_contents)
    # Add to the generate_results
    generate_results.append("%s: %s" % (description,"Pass" if result else "Fail"))    
    # If the contents did not match, write the contents to a file so I can
    # see where I went wrong
    generated_filename = file+".generated"
    if not result:
        open(generated_filename,"w").write(generated_contents)
    # If the test did pass, get rid of the generated files I made
    else:
        if os.path.exists(generated_filename):
            os.remove(generated_filename)

def test_parse(description,file,manager):
    generated_manager = SteamShortcutManager(file)
    result = (manager == generated_manager)
    parse_results.append("%s: %s" % (description,"Pass" if result else "Fail"))
    # generated_filename = file+".parsed"
    
        

manager = SteamShortcutManager()

# =============================================================================

single_manager = SteamShortcutManager()
single_manager.add_shortcut("iLoL Open Beta 1.1","\"/Applications/iLoL Open Beta 1.1.app\"","\"/Applications/\"")

# =============================================================================

windows_manager = SteamShortcutManager()
windows_manager.add_shortcut(   "Paper Mario",
                                "\"C:\Program Files (x86)\Project64\Project64.exe\" \"C:\Users\Scott.Scott-PC\ROMs\N64\PaperMario.n64\"",
                                "\"C:\Program Files (x86)\Project64\\\"")
windows_manager.add_shortcut(   "Final Fantasy X",
                                "\"C:\Program Files (x86)\Emulator Copies\Final Fantasy X\pcsx2-r5350.exe\"  \"C:\Users\Scott.Scott-PC\ROMs\PS2\Final Fantasy X.iso\"",
                                "\"C:\Program Files (x86)\Emulator Copies\Final Fantasy X\\\"")
windows_manager.add_shortcut(   "Kingdom Hearts",
                                "\"C:\Program Files (x86)\Emulator Copies\Kingdom Hearts\pcsx2-r5350.exe\" \"C:\Users\Scott.Scott-PC\ROMs\PS2\Kingdom Hearts.iso\"",
                                "\"C:\Program Files (x86)\Emulator Copies\Kingdom Hearts\\\"")

# =============================================================================

icon_manager = SteamShortcutManager()

icon_manager.add_shortcut(  "Minecraft",
                            "\"/Users/scottrice/Applications/Minecraft.app\"",
                            "\"/Users/scottrice/Applications/\"",
                            "/Users/scottrice/Downloads/glyphish-icons/PNG icons/06-magnify.png")

# =============================================================================

tag_manager = SteamShortcutManager()

tag_manager.add_shortcut(   "Minecraft",
                            "\"/Users/scottrice/Applications/Minecraft.app\"",
                            "\"/Users/scottrice/Applications/\"",
                            "/Users/scottrice/Downloads/glyphish-icons/PNG icons/06-magnify.png",
                            "Dirty Casual")

# =============================================================================

dave_manager = SteamShortcutManager()

dave_manager.add_shortcut(  "Portable Counter-Strike Source",
                            "\"G:\Program Files\Portable Counter-Strike Source\Counter-Strike Source.exe\"",
                            "\"G:\Program Files\Portable Counter-Strike Source\\\"")
dave_manager.add_shortcut(  "Halo",
                            "\"G:\Program Files\Halo\halo.exe\"",
                            "\"G:\Program Files\Halo\\\"")
dave_manager.add_shortcut(  "Halo 2",
                            "\"G:\Program Files\Halo 2\halo2.exe\"",
                            "\"G:\Program Files\Halo 2\\\"",
                            "\"G:\Program Files\Halo 2\halo2.exe\"")
dave_manager.add_shortcut(  "Dungeon Siege III",
                            "\"G:\Program Files\Dungeon Siege III\Dungeon Siege III.exe\"",
                            "\"G:\Program Files\Dungeon Siege III\\\"")                            

# =============================================================================

crlf_manager = SteamShortcutManager()
crlf_manager.add_shortcut(  "Paper Mario",
                            "\"C:\Program Files (x86)\Project64\Project64.exe\" \"C:\Users\Scott.Scott-PC\ROMs\N64\PaperMario.n64\"",
                            "\"C:\Program Files (x86)\Project64\\\"",
                            "",
                            "Nintendo 64")
crlf_manager.add_shortcut(  "Final Fantasy X",
                            "\"C:\Program Files (x86)\Emulator Copies\Final Fantasy X\pcsx2-r5350.exe\"  \"C:\Users\Scott.Scott-PC\ROMs\PS2\Final Fantasy X.iso\"",
                            "\"C:\Program Files (x86)\Emulator Copies\Final Fantasy X\\\"",
                            "",
                            "Playstation 2")
crlf_manager.add_shortcut(  "Kingdom Hearts",
                            "\"C:\Program Files (x86)\Emulator Copies\Kingdom Hearts\pcsx2-r5350.exe\" \"C:\Users\Scott.Scott-PC\ROMs\PS2\Kingdom Hearts.iso\"",
                            "\"C:\Program Files (x86)\Emulator Copies\Kingdom Hearts\\\"",
                            "",
                            "Playstation 2")

test("No Shortcuts","vdfs/empty-shortcuts.vdf",manager)
test("One Shortcut","vdfs/onlyilol-shortcuts.vdf",single_manager)
test("Three Complex Shortcuts","vdfs/windows-shortcuts.vdf",windows_manager)
test("One Shortcut, Custom Icon","vdfs/iconchange-shortcuts.vdf",icon_manager)
test("One Shortcut, Custom Icon and Tag","vdfs/tag-shortcuts.vdf",tag_manager)
test("Complex Shortcuts (Dave)","vdfs/dave-shortcuts.vdf",dave_manager)
test("Carraige Return and Line Feed","vdfs/wtfis0x0d-shortcuts.vdf",windows_manager)

print "===========Generated==========="
for result in generate_results:
    print result
print "============Parsed============="
for result in parse_results:
    print result