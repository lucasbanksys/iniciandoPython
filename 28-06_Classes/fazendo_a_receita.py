from receita import Receita
from time import sleep

bolo_chocolate = Receita(5, 1, 5, 1)

print(bolo_chocolate.misturar())
sleep(2)
bolo_chocolate.assar()