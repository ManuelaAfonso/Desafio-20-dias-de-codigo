'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

cod1, qnt1, valor1 = input().split()
cod1 = int(cod1)
qnt1 = int(qnt1)
valor1 = float(valor1)

cod2, qnt2, valor2 = input().split()
cod2 = int(cod2)
qnt2 = int(qnt2)
valor2 = float(valor2)

total = qnt1 * valor1 + qnt2 * valor2

print(f"VALOR A PAGAR: R$ {total:.2f}")
