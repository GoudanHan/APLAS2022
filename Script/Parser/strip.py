import os

left = [ "{", "(", , "[" ]
right = [ "}", ")", "]" ]

output_file = open( "trainingData(2).txt" , 'wb')

with open("trainingData(1).txt", 'rb') as file:
    data = file.read().split(bytes("\n", "utf-8"))
    for line in data:
        if line:
            # get rid of unnecessary blank spaces
            line = line.decode("utf-8")
            line = line.split()
            line = " ".join(line)
            # to be implemented : "fruit . apple" -> "fruit.apple"
            #                     " / . " ->
            output_file.write(bytes(line, "utf-8") )
            output_file.write(bytes("\n", "utf-8") )

print("done")