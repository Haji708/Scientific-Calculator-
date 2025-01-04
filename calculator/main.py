inpt="3 * (2 + (4 - 1))"
print(list(inpt))
invalid_characters=[" "]
parentheses=[]
parentheses_indexes=[]
inpt = inpt.replace(" ","")
for index in range(len(inpt)):
    if inpt[index] =="(" or inpt[index] ==")":
        parentheses.append(inpt[index])
        parentheses_indexes.append(index)
inpt = inpt.replace("(", "")
inpt = inpt.replace(")", "")
operators=["^","X",'x','*','/','-','+']
print(parentheses_indexes)
def parse(string):
    parsed_inp=[]
    num=''
    for index in range(len(inpt)):
        if inpt[index].isdigit() or inpt[index] == "." or (inpt[index]=="-" and (inpt[index-1] in operators[0:operators.index('-')] or inpt[0]=="-")):
            num += inpt[index]
        else:
            parsed_inp.append(float(num))
            parsed_inp.append(inpt[index])
            num=""
    print(num)
    parsed_inp.append(float(num))
    return parsed_inp
inp=parse(list(inpt))
print(inp)
def parenthesis_handler(str):
    return


#functions = {"*": inp[inp.index("*") - 1] * inp[inp.index("*") + 1],
#             "/": inp[inp.index("/") - 1] / inp[inp.index("/") + 1],
 #            "+": inp[inp.index("+") - 1] + inp[inp.index("+") + 1],
  #           "-": inp[inp.index("-") - 1] - inp[inp.index("-") + 1]}
def procedure(inp):
    for operator in operators:
        while inp.count(operator) != 0:
            if operator == "^":
                p = inp[inp.index(operator) - 1] ** inp[inp.index(operator) + 1]
            if operator in operators[operators.index("X"):operators.index("/")]:
                p = inp[inp.index(operator) - 1] * inp[inp.index(operator) + 1]
            if operator == "/":
                p = inp[inp.index(operator) - 1] / inp[inp.index(operator) + 1]
            if operator == "+":
                p = inp[inp.index(operator) - 1] + inp[inp.index(operator) + 1]
            if operator == "-":
                p = inp[inp.index(operator) - 1] - inp[inp.index(operator) + 1]
            del inp[inp.index(operator) - 1]
            del inp[inp.index(operator) + 1]
            inp[inp.index(operator)] = p
procedure(inp)
print(inp[0])

