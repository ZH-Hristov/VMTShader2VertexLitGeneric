import os
import re

directory = os.listdir(os.getcwd())

for file in directory:
    if not file.endswith(".vmt"):
        continue
    open_file = open(file, "r")
    read_file = open_file.read()
    num_subs = 0

    replacers = ['lightmappedGeneric', 'LightMappedGeneric', 'LightmappedGeneric', 'UnLitGeneric', 'UnlitGeneric', 'unlitgeneric', 'WorldVertexTransition']

    read_file = re.subn('LightmappedGeneric', 'VertexLitGeneric', read_file)
    num_subs += read_file[1]

    for replacer in replacers:
        read_file = re.subn(replacer, 'VertexLitGeneric', read_file[0])
        num_subs += read_file[1]

    modified = read_file[0]

    if num_subs == 0:
        print(f"Nothing to change in {file}")
        continue

    write_file = open(file, "w")
    write_file.write(modified)

    print(f'Converted {num_subs} shader names to VertexLitGeneric in {file}.')
