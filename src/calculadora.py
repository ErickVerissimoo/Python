print ("\n\tCalculadora \n\t1 - Soma \n\t2 - Subtração \n\t3 - Multiplicação \n\t4 - Divisão ")
escolha = int (input("\n\tEntre com a escolha: "))
if escolha ==1:
    numero1 = float (input("\n\tEntre com o numero um: "))
    numero2 = float (input("\n\tEntre com o numero dois: "))
    print("\n\t", numero1 + numero2)
elif escolha ==2:
    numero1 = float (input("\n\tEntre com o numero um: "))
    numero2 = float (input("\n\tEntre com o numero dois: "))
    print("\n\t", numero1 - numero2)
elif escolha ==3:
            numero1 = float (input("\n\tEntre com o numero um: "))
            numero2 = float (input("\n\tEntre com o numero dois: "))
            print("\n\t", numero1 * numero2)
elif escolha ==4:
            numero1 = float (input("\n\tEntre com o numero um: "))
            numero2 = float (input("\n\tEntre com o numero dois: "))
            print("\n\t", numero1 / numero2)
else:
        print("errado")