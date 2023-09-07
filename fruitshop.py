fruit = {'apple' : 150,
              'orange' : 300,
               'durian' : 450}

while True:
        product = input("Please choose the product: apple, durian, orange: ")
        quatity = float(input("how many kilo :  "))
        print(quatity * fruit[product] )
        print("--------------")
