def getPredictions(top_values, top_indices, d):
    '''
        input <- top_values  : a 2D list that contains
                               the probabilities of the spans being the error location
                 top_indices : a 2D matching list that with top_values contains
                               the indices of the spans
                 d           : a data type that stores the information of the xxxx.csv
                               in the op directory
        effect <- filter out the spans where the probabilities are less than 0.5
        return : a list of span
    '''
    iList = []
    for i in range(len(top_values)):
        if top_values[1][i] >= 0.5:
            index = top_indices[1][i]
            iList.append(d["SourceSpan"][index])
    