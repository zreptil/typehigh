#!/bin/bash
OPENSCAD_PATH=/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD
INFILE=all_emojis.png

echo "Converting png to scad"
../type2scad -f 1 "$INFILE"

if [ -e "$OPENSCAD_PATH" ]; then
  echo "Converting scad to stl"
  $OPENSCAD_PATH -o ${INFILE/png/stl} ${INFILE/png/scad}
fi
