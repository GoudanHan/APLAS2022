import sys

keyword_ls = ["module", "let", "sig", "type"] #, "try", "match", "map"]

def cleaner(text):
    '''
        input <- text content to be modified
        effect <- clean out comments and extra lines
        return -> clean text 
    '''

    # clean comments
    while "(*" in text:
        start_index = text.find("(*")
        end_index = text.find("*)", start_index)
        text = text[:start_index] + text[end_index+2:]
    
    # tokenize
    ls = text.split("\n")
    pre = ''
    result = []

    for line in ls:
        #skip all empty lines
        if line == "":
            continue
        
        #check the place of the first word
        if " " in line:
            first_word = line[:line.index(" ")]
        else:
            first_word = ""

        #clean data
        if first_word in keyword_ls:
            if pre != None and len(pre.split()) > 4:
                pre += "\n"
                result.append(pre)
                pre = ''
            pre = line
            continue
        elif first_word == "":
            pre += " " + line.strip()
        else:
            continue
    
    #append the last block
    if pre != None and len(pre.split()) > 4:
        result.append(pre)
        
    return "\n".join(result)

# print("`````````````Text 1 ```````````\n")
# text1 = "(* --- this is a  comment\n ----*)\n\nlet x = 5 + 9;;\nlet y a = a > 2;;"
# print(cleaner(text1))
# 
# with open("OASISMessage.ml") as f:
#    text2 = f.read()
# print("`````````````Text 2 ```````````\n")
# open("new_file.txt", "w").write(cleaner(text2))

    