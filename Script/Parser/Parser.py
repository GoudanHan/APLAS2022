import re

texts = [
    "t'"
    ]
buckets = ["[", "]", "(", ")" , "{", "}" , '"', "'", ".", "`", ",", ";"]
valid_name = re.compile("^([a-z]|[A-Z])+([a-z]|[_]|[A-Z]|[0-9])*$")

def parser(text):
    '''
        input <- An OCaml expression (let-expr, function, type, module...)
        effect: Parse the given text into a string that's made of OCaml tokens separated by a blank space
        return -> parsed string
    '''
    
    tokens = text.split()
    result = []

    for i in range(len(tokens)):
        token = tokens[i]
        if isLegalName(token):
            result.append(token)
        else:
            tmp = ""
            tmp_s = ""
            for l in token:
                if l.isalnum() or l == "_":
                    tmp += l
                    if tmp_s:
                        result.append(tmp_s)
                        tmp_s = ""
                elif l in buckets:
                    if tmp:
                        result.append(tmp)
                        tmp = ""
                    result.append(l)
                else:
                    if tmp:
                        result.append(tmp)
                        tmp = ""
                    tmp_s += l
            result.append(tmp)
            result.append(tmp_s)
                    
    return " ".join(result)

def isLegalName(token):
    if re.search(valid_name, token):
        return True
    return False
# 
# for text in texts:
#     x = parser(text)
#     print(x)