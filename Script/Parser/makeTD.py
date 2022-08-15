import os
import re
from Parser import parser, buckets, valid_name, isLegalName

ocaml = re.compile("^.*(.ml)$")
directs = [ "Data/Data/", "Data/Data2/", "Data/Data3/", "summerProj/" , "summerProj/summerProj/" , "test4/" ]

output_file = open( "trainingData.txt" , 'w')

counter = 0

for direct in directs:
    for filename in os.listdir(direct):
        f = os.path.join(direct, filename)
        # checking if it is an OCaml file
        if re.search(ocaml, filename):
            # open file location
            file = open(direct + filename, 'r')
            try:
                for line in file:
                    if line or line != "\n":
                        line = parser(line)
                        counter +=1

                        output_file.writelines(line)
                        output_file.writelines("\n")
            except:
                None
                
    print( "finishing collecting data from directory : {}".format( direct ) )

print( "{} of OCaml expressions have been collected. Have fun with training the NL model:3".format(counter) )
