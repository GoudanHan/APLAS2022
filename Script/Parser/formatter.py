import os


output_file = open( "trainingData(1).txt" , 'wb')

with open("trainingData.txt", 'r') as file:
    data = file.read().split("\n")
    for line in data:
        if line:
            output_file.write(bytes(line, "utf-8") )
            output_file.write(bytes("\n", "utf-8") )

print("done")