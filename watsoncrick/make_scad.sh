#!/bin/bash
OPENSCAD_PATH=/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD

for img in emojis/*.png; do
  scad="${img/png/scad}"
  echo "${img} --> ${scad}"
  ../type2scad -f 0 "$img"
  if [ -e "$OPENSCAD_PATH" ]; then
    stl="${scad/scad/stl}"
    echo "  $scad --> $stl"
    $OPENSCAD_PATH -o $stl $scad
  fi
done

