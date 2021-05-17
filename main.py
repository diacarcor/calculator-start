from art import logo

print(logo)

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    if n2 == 0:
        return "Error"
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():

    n1 = float(input("What's the first number?: "))

    for symbol in operations:
        print (symbol)

    should_continue = True

    while should_continue:
    
        #Ask for the operation
        symbol = input("Pick and operation: ")

        n2 = float(input("What's the next number?: "))

        calc_function = operations [symbol]
        result = calc_function(n1,n2)
       
        print(f"{n1} {symbol} {n2} = {result}")

        carry_on = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new one: ").lower()

        if carry_on == "n":
            should_continue = False
            calculator()
        else:
            n1 = result

calculator()         

       

    
   



