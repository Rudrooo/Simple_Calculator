from art import logo



def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    print(logo)
    num1=float(input("What's the first number?: "))
    for i in operation:
        print(i)
    cal_on=True

    while cal_on:
        sign=input("Pick an operation:")
        num2=float(input("What's the second number?: "))
        fun=operation[sign]
        ans=round(fun(num1,num2),2)
        print(f"{num1} {sign} {num2} = {ans}")
        again=input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calcultor")
        if again=="n":
            cal_on=False
            calculator()
        num1=ans
calculator()