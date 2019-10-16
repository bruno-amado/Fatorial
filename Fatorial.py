#Make a function called "fatorial"
def fatorial(number): 
    #pok will be a inicializer because we cant change the number or that will affect theloop
    if number >= 0:
        pok = 1
        #For every number before number = i
        for i in range(number):
            #pok will be equal to (pok = 1 at starts) * (number - i ++ ) 
            #Like this we have sure that i keep adding +1 until number - (number-1) 
            pok = pok * (number-i)
        print(pok)
    else: 
        print("Fora do domínio")
#calling the function
fatorial(int(input("Enter a number: ")))
