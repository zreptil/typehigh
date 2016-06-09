#!/usr/bin/env python

""" from a ttf file create a folder that contains an svg for each character in that font """

import fontforge
from sys import argv
import os

### argument handling
#print(argv)
fontname = argv[1].partition('.')[0]
if len(argv) > 2:
    out_path = argv[2]
else: out_path = '.'
save_path = out_path + '/' + fontname

### fontforge magic begins
f=fontforge.open(argv[1])       
fontforge.logWarning( "font name: " + f.fullname )
fontforge.logWarning( "saving..." )

try:
    os.mkdir(save_path)
except OSError: 
    pass

for g in f.glyphs():
    g.export(save_path+"/"+fontname+"_"+g.glyphname+".svg")


