inpt="3 * (2 + (4 - 1))"
invalid_characters=[" "]
parentheses=[]
parentheses_indexes=[]
parentheses_pairs=[]
inpt = inpt.replace(" ","")
def parenthesis_handler(str):
    for index in range(len(inpt)):
        if inpt[index] =="(" or inpt[index] ==")":
            parentheses.append(inpt[index])
            parentheses_indexes.append(index)
#inpt = inpt.replace("(", "")
#inpt = inpt.replace(")", "")
for par,index in zip(range(len(parentheses)),parentheses_indexes):
    if parentheses[par] == "(" and parentheses[par+1] == ")":
        parentheses_pairs.append(index)
        parentheses_pairs.append(parentheses_indexes[par+1])
        del pa
print(parentheses_pairs)


