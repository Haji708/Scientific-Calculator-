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
    invalid_characters = [" ", "(", ")"]
    for char in inpt:
        if char in invalid_characters:
            inpt = inpt.replace(char, "")
    operators = ["^", "X", 'x', '*', '/', '-', '+']

    def parse(string):
        parsed_inp = []
        num = ''
        for index in range(len(inpt)):
            if inpt[index].isdigit() or inpt[index] == "." or (
                    inpt[index] == "-" and (inpt[index - 1] in operators[0:operators.index('-')] or inpt[0] == "-")):
                num += inpt[index]
            else:
                parsed_inp.append(float(num))
                parsed_inp.append(inpt[index])
                num = ""
        parsed_inp.append(float(num))
        return parsed_inp

    inp = parse(inpt)
    # functions = {"*": inp[inp.index("*") - 1] * inp[inp.index("*") + 1],
    #             "/": inp[inp.index("/") - 1] / inp[inp.index("/") + 1],
    #            "+": inp[inp.index("+") - 1] + inp[inp.index("+") + 1],
    #           "-": inp[inp.index("-") - 1] - inp[inp.index("-") + 1]}
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
    input_field.delete(0, END)
    input_field.insert(0,inp[0])

#________________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________________

b1 = Button(window,text="1", padx=25, pady=25, command=lambda:input("1"), bg="red",fg="white").grid(row=4,column=1)
b2 = Button(window,text="2", padx=25, pady=25, command=lambda:input("2"), bg="red",fg="white").grid(row=4,column=2)
b3 = Button(window,text="3", padx=25, pady=25, command= lambda:input("3"), bg="red",fg="white").grid(row=4,column=3)
b4 = Button(window,text="4", padx=25, pady=25, command=lambda: input("4"), bg="red",fg="white").grid(row=3,column=1)
b5 = Button(window,text="5", padx=25, pady=25, command=lambda: input("5"), bg="red",fg="white").grid(row=3,column=2)
b6 = Button(window,text="6", padx=25, pady=25, command=lambda: input("6"), bg="red",fg="white").grid(row=3,column=3)
b7 = Button(window,text="7", padx=25, pady=25, command=lambda: input("7"), bg="red",fg="white").grid(row=2,column=1)
b8 = Button(window,text="8", padx=25, pady=25, command= lambda:input("8"), bg="red",fg="white").grid(row=2,column=2)
b9 = Button(window,text="9", padx=25, pady=25, command= lambda:input("9"), bg="red",fg="white").grid(row=2,column=3)
b0 = Button(window,text="0", padx=25, pady=25, command= lambda:input("0"), bg="red",fg="white").grid(row=5,column=2)
bdot = Button(window,text=".", padx=25, pady=25, command= lambda:input(".")).grid(row=5,column=3)
bclear = Button(window,text="Clear", padx=15, pady=25,command=lambda:clear()).grid(row=5,column=1)
badd = Button(window,text="+", padx=25, pady=25,command=lambda:input("+")).grid(row=2,column=4)
bsubtract = Button(window,text="-", padx=25, pady=25,command=lambda:input("-")).grid(row=3,column=4)
bmultiply = Button(window,text="*", padx=25, pady=25,command=lambda:input("*")).grid(row=4,column=4)
bmdivide = Button(window,text="/", padx=25, pady=25,command=lambda:input("/")).grid(row=5,column=4)
bequals = Button(window,text="=", padx=100,pady=25,command=lambda:calculation()).grid(row=6,column=1, columnspan=4)
window.mainloop()

