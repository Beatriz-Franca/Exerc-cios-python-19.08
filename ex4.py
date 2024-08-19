from random import*

pessoa = int(input(" 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 - par ou ímpar  n/Escolha um número: "))
computer = randrange (0,9)
print("O número escolhido é:")

if pessoa == (1, 3, 5, 7, 9):
   print("ímpar",computer)
elif pessoa == (0, 2, 4, 6, 8):
    print("par",computer)
     