import os
import re
from Parser import parser, buckets, valid_name, isLegalName

# folder tests
directory = 'test2_1'

ocaml = re.compile("^.*(.ml)$")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is an OCaml file
    if re.search(ocaml, filename):
        # open file location
        file = open('test2_1/' + filename, 'r')
        # new file location
        new_file = open('test4/' + filename, 'w') 
        for line in file:
            if line:
                line = parser(line)
            new_file.writelines(line)
            new_file.writelines("\n")
    file.close()
    new_file.close()