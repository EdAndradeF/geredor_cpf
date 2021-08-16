from random import randint, randrange
from time import time

from models import cpfdig, verifycpf, cpfformat



inicio = time()
verificado = False
while not verificado:

    cpf_num = str(randint(100000000, 999999999))

    dig1 = cpfdig(cpf_num)
    dig2 = cpfdig(cpf_num+dig1)

    cpfnovo = cpf_num + dig1 + dig2

    verificado = verifycpf(cpfnovo)

cpf_ofc = cpfformat(cpfnovo)
print(cpf_ofc)
