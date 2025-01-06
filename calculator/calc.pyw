from tkinter import *
window=Tk()
window.title("Calculator Beta")
window.configure(bg="#07569b")
input_field = Entry(font=('Aptos', 15) , bg="#b9bbba")
input_field.grid(row=1,column=1,columnspan=4,padx=25,pady=25)
def input(number):
    current=str(input_field.get())
    input_field.delete(0,END)
    input_field.insert(0, str(current) + str(number))
def clear():
    input_field.delete(0, END)
def calculation():
    inpt = input_field.get()
    invalid_characters = [" "]
    operators = ["^", "X", 'x', '*', '/', '-', '+']
    parentheses = []
    parentheses_indexes = []
    parentheses_pairs = []
    inpt = inpt.replace(" ", "")

    def parse(string):
        parsed_inp = []
        num = ''
        for index in range(len(string)):
            if string[index].isdigit() or string[index] == "." or (
                    string[index] == "-" and (string[index - 1] in operators[0:operators.index('-')]) or (
                    (string[index] == "-") and index == 0)):
                num += string[index]
            else:
                if num:
                    parsed_inp.append(num)
                parsed_inp.append(string[index])
                num = ""
        if num:
            parsed_inp.append(num)
        return parsed_inp

    inpt = parse(list(inpt))

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
            if str[index] == "(" or str[index] == ")":
                parentheses.append(str[index])
                parentheses_indexes.append(index)
        # print(parentheses,parentheses_indexes)

    parenthesis_handler(inpt)

    # inpt = inpt.replace("(", "")
    # inpt = inpt.replace(")", "")
    i = 0
    print(inpt)
    while inpt.count("(") != 0 and inpt.count(")") != 0:
        if parentheses[i] == "(" and parentheses[i + 1] == ")":
            print(i, "t")
            o = inpt[parentheses_indexes[i] + 1:parentheses_indexes[i + 1]]
            inpt[parentheses_indexes[i]:parentheses_indexes[i + 1] + 1] = [procedure(parse(o))]
            print(inpt)
            i = 0
            parentheses_indexes = []
            parentheses = []
            parenthesis_handler(inpt)
        else:
            i += 1
    input_field.delete(0, END)
    input_field.insert(0,procedure(inpt))

#________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________

b1 = Button(window,text="1", padx=25, pady=25, command=lambda:input("1"), bg="white").grid(row=4,column=1)
b2 = Button(window,text="2", padx=25, pady=25, command=lambda:input("2"), bg="white").grid(row=4,column=2)
b3 = Button(window,text="3", padx=25, pady=25, command= lambda:input("3"), bg="white").grid(row=4,column=3)
b4 = Button(window,text="4", padx=25, pady=25, command=lambda: input("4"), bg="white").grid(row=3,column=1)
b5 = Button(window,text="5", padx=25, pady=25, command=lambda: input("5"), bg="white").grid(row=3,column=2)
b6 = Button(window,text="6", padx=25, pady=25, command=lambda: input("6"), bg="white").grid(row=3,column=3)
b7 = Button(window,text="7", padx=25, pady=25, command=lambda: input("7"),bg="white").grid(row=2,column=1)
b8 = Button(window,text="8", padx=25, pady=25, command= lambda:input("8"), bg="white").grid(row=2,column=2)
b9 = Button(window,text="9", padx=25, pady=25, command= lambda:input("9"),bg="white").grid(row=2,column=3)
b0 = Button(window,text="0", padx=25, pady=25, command= lambda:input("0"), bg="white").grid(row=5,column=2)
bdot = Button(window,text=".", padx=25, pady=25, command= lambda:input(".")).grid(row=5,column=3)
bclear = Button(window,text="C", padx=25, pady=25,command=lambda:clear()).grid(row=5,column=1)
badd = Button(window,text="+", padx=25, pady=25,command=lambda:input("+")).grid(row=2,column=4)
bsubtract = Button(window,text="-", padx=25, pady=25,command=lambda:input("-")).grid(row=3,column=4)
bmultiply = Button(window,text="*", padx=25, pady=25,command=lambda:input("*")).grid(row=4,column=4)
bmdivide = Button(window,text="/", padx=25, pady=25,command=lambda:input("/")).grid(row=5,column=4)
bequals = Button(window,text="=", padx=25,pady=25,command=lambda:calculation()).grid(row=6,column=4,)
bpower = Button(window,text="^", padx=25,pady=25,command=lambda:input("^")).grid(row=6,column=3,)
bparopen = Button(window,text="(", padx=25,pady=25,command=lambda:input("(")).grid(row=6,column=1,)
bparclose = Button(window,text=")", padx=25,pady=25,command=lambda:input(")")).grid(row=6,column=2,)
window.mainloop()

