# -*- coding: utf-8 -*-
import numpy as np

# Header information for the GJF file
gjf_header = """%nprocshared=12
%mem=45GB
%NoSave
%chk=DNA_C0_min.chk
# b3lyp/6-31g(d,p) scrf=(solvent=generic,water) Int=SuperFineGrid SCF=Big

Title

-12 1
"""

# Extracting coordinates from the PDB file
pdb_filename = 'DNA.pdb'  # Change this filename for each new file
temp_filename = 'temp.txt'
output_gjf_filename = 'DNA.gjf'  # Change this if needed

with open(pdb_filename) as pdb_file, open(temp_filename, 'w') as temp_file:
    for line in pdb_file:
        if line.startswith(('ATOM', 'HETATM')):  
            atom_name = line[12:14].strip()
            if atom_name in {'H2', 'H5', 'HO'}:
                atom_name = 'H'
            coordinates = line[26:54]
            temp_file.write(f"{atom_name:<2} {coordinates}\n")  # Left-align atom name in 2-character space



print('Coordinates extracted successfully.')

# Merging header and extracted coordinates
with open(temp_filename) as temp_file, open(output_gjf_filename, 'w') as gjf_file:
    gjf_file.write(gjf_header + '\n' + temp_file.read())

print('GJF file created successfully :)')
