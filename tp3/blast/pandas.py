#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:30:35 2020

@author: roderick
"""

import pandas as pd
blast=pd.read_csv("/home/roderick/Documentos/Materia/Advance_Bioinformatics/TP3/blast/O14BLAsetA.csv", sep='\t', 
                  names=["qseqid", "qlen", "bitscore", "score", "length", "pident", "mismatch", "evalue"])
blast['significativo']=blast['evalue']<1e-05