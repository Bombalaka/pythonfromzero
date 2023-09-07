fruit = {'apple' : 150,
              'orange' : 300,
               'durian' : 450}

menucheck = {'a' : 'apple', 'b': 'durian', 'c' : 'orange' }

print("Welcome to program")
print("--------")
mainmenu = """
Welcome to program
[1]-products
[2]- a product
[3]- finish program
"""
print(mainmenu)

while True:
        print(mainmenu)
        menu = input("Please chosse menu [1]-[3] : ")

        text1 = '''
        ----------------------
        Please choose the prodect
        ----------------------
        '''
        allproduct = []
        productcheck = []
        submenu1 = 'a'

        

        if menu  == '1' :
                print(text1)
                while submenu1.lower() != 'q':
                        print("Please chose\n [A] - apple  [B]-orange  [C]-durian or [Q] quite from program  [T]- Total ")
                        submenu1 = input('menu :  ')
                        if submenu1.lower() != 'q' and submenu1.lower() != 't' :
                            product = menucheck[submenu1.lower() ] 
                            price = fruit[product]
                            quantity = float(input("quantity  (kg) : "))
                            d = [product,quantity]
                            if product not in productcheck:
                                    productcheck.append(product)
                                    allproduct.append(d)
                            else:
                                    pindex = productcheck.index(product)
                                    allproduct[pindex] [1] = allproduct[pindex] [1] + quantity
                                
                        elif submenu1.lower() == 'q' :
                            print("Quiting menu.......")
                            break
                        elif submenu1.lower()== 't' :
                            totaly = 0
                            for name,q in allproduct:
                                  cal = fruit[name] * q
                                  print("-{}  total: {}  kg  (total  {}  bath )" .format(name,q,cal))
                                  totaly += cal
                            print("Total : {} bath".format(totaly))                     
                            break
                        print("----------------------------------")

        elif menu == '2' :
                        product = input("Please choose the product: apple, durian, orange: ")
                        quatity = float(input("how many kilo :  "))
                        print(quatity * fruit[product] )
                        print("--------------")
        elif menu == '3' :
              break

print("Close program")


        
        
        


