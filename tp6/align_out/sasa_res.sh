#!/bin/bash
for file in ./*.pdb
do
  freesasa $file --format=rsa > "$file"_sasa_res.out
done
