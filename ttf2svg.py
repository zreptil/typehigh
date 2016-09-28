#!/usr/bin/env python

""" from a ttf file create a folder that contains an svg for each character in that font .  requires fontforge.  also works on dfont and, therefore possibly ttc out of the box for free"""

import sys
from sys import argv
import os
from localsettings import fontforgepath
sys.path.append(fontforgepath)
#sys.path.append("../fontforge")
import fontforge
import xml.etree.ElementTree as ET

### helper functions
def writeEditedSvgXml(anOutFilename, anInFilename):
    """ this changes the viewbox of the svg by changing the second elemtn (presumably a y element) to zero
    """
    ### http://stackoverflow.com/questions/23417466/cant-seem-to-remove-ns0-namespace-declaration
    ns = ET.register_namespace("", "http://www.w3.org/2000/svg") 
    treeOuter = ET.ElementTree()
    treeOuter.parse(anOutFilename)
    tree = treeOuter.getroot()
    sViewBox = tree.get('viewBox')
    aViewBox = sViewBox.split(" ")
    aViewBox[1] = 0
    sViewBox = " ".join(map(str, aViewBox))
    tree.set('viewBox', sViewBox)
    treeOuter.write(anInFilename, default_namespace=ns)
    return( ET.tostring(tree) )

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
    glyphFileName = save_path+"/"+fontname+"_"+g.glyphname
    g.export(glyphFileName+".svg")
    ### this also works for bitmaps!
    #g.export(glyphFileName+".bmp", 256)
    ### fix viewBox problem, that all of the svg's are rendered outside of their viewboxes
    writeEditedSvgXml(glyphFileName+".svg", glyphFileName+".svg")



