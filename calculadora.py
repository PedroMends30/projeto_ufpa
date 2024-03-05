op = 0

inicio = '''
----------------- BEM VINDO -----------------'''

fim = '''
------------------ Até logo ------------------
'''

menu = '''           Calculadora Monstra
    1 . Somar
    2 . Subtrair
    3 . Multiplicar
    4 . Dividir
    5 . Nª Potência
    6 . Raiz Nª
    7 . Fatorial
    8 . Sair'''

operacoes = [1,2,3,4,5,6,7,8]

def soma(a,b): return a+b
def subtracao(a,b): return a-b
def multiplicacao(a,b): return a*b
def divisao(a,b): return a/b
def exp(a,b): return a**b
def nrt(a,b): return a**(1/b)

def fatorial(a):
    fat = 1
    for i in range(a):
        fat *= i+1
    return fat

print(inicio)
while op != 8:
    print(menu)
    
    op = int(input(""))
    
    if op == 8:
        break
    
    operando = int(input("Digite o valor do operando: "))
    
    if op != 7:
        operador = int(input("Digite o numero do operador: "))
            
    if op not in operacoes:
        print("Numero Invalido\n")
    else:
        match op:
            case 1:
                print(f"\n{operando} + {operador} = {soma(operando,operador)}\n")
            case 2:
                print(f"\n{operando} - {operador} = {subtracao(operando,operador)}\n")
            case 3:
                print(f"\n{operando} * {operador} = {multiplicacao(operando,operador)}\n")
            case 4:
                if operador == 0:
                    print("indefinido")
                else:
                    print(f"\n{operando} / {operador} = {divisao(operando,operador)}\n")
            case 5:
                print(f"\n{operando} ^ {operador} = {exp(operando,operador)}\n")
            case 6:
                print(f"\nRaiz {operador}ª de {operando} = {nrt(operando,operador)}\n")
            case 7:
                print(f"\n{operando}! = {fatorial(operando)}\n")

print(fim)