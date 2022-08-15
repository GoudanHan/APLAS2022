import os
import re
from cleaner import keyword_ls, cleaner

directory = 'test1'

ocaml = re.compile("^.*(.ml)$")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is an OCaml file
    if re.search(ocaml, filename):
        file = open('test1/' + filename, 'r')
        new_file = open('test2_1/' + filename, 'w')
        try:
            content = file.read()
            new_file.writelines(cleaner(content))
        except:
            None
        file.close()
        new_file.close()
