inpt="(1/4)^(4/2)"
invalid_characters=[" "]
operators=["^","X",'x','*','/','-','+']
parentheses=[]
parentheses_indexes=[]
parentheses_pairs=[]
inpt = inpt.replace(" ","")
def parse(string):
    parsed_inp=[]
    num=''
    for index in range(len(string)):
        if string[index].isdigit() or string[index] == "." or (string[index]=="-" and (string[index-1] in operators[0:operators.index('-')] )or ((string[index]=="-") and index == 0)):
            num += string[index]
        else:
            if num:
                parsed_inp.append(num)
            parsed_inp.append(string[index])
            num = ""
    if num:
        parsed_inp.append(num)
    return parsed_inp
inpt=parse(list(inpt))
def procedure(inp):
    for operator in operators:
        while inp.count(operator) != 0:
            if operator == "^":
                p = float(inp[inp.index(operator) - 1]) ** float(inp[inp.index(operator) + 1])
            if operator in operators[operators.index("X"):operators.index("/")]:
                p = float(inp[inp.index(operator) - 1]) * float(inp[inp.index(operator) + 1])
            if operator == "/":
                p = float(inp[inp.index(operator) - 1]) / float(inp[inp.index(operator) + 1])
            if operator == "+":
                p = float(inp[inp.index(operator) - 1]) + float(inp[inp.index(operator) + 1])
            if operator == "-":
                p = float(inp[inp.index(operator) - 1]) - float(inp[inp.index(operator) + 1])
            del inp[inp.index(operator) - 1]
            del inp[inp.index(operator) + 1]
            inp[inp.index(operator)] = str(p)
    return inp[0]
def parenthesis_handler(str):
    for index in range(len(str)):
        if str[index] =="(" or str[index] ==")":
            parentheses.append(str[index])
            parentheses_indexes.append(index)
    #print(parentheses,parentheses_indexes)
parenthesis_handler(inpt)

#inpt = inpt.replace("(", "")
#inpt = inpt.replace(")", "")
i=0
print(inpt)
while inpt.count("(") != 0 and inpt.count(")") != 0:
    if parentheses[i]=="(" and parentheses[i+1]==")":
        print(i,"t")
        o = inpt[parentheses_indexes[i]+1:parentheses_indexes[i+1]]
        inpt[parentheses_indexes[i]:parentheses_indexes[i+1]+1] =[procedure(parse(o))]
        print(inpt)
        i=0
        parentheses_indexes = []
        parentheses = []
        parenthesis_handler(inpt)
    else:
        i+=1

print(procedure(inpt))