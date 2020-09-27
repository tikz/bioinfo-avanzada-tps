#!/bin/bash
for file in ./*.pdb
do
  freesasa $file --format=json > "$file"_sasa.json
done
