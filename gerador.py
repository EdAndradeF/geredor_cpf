from random import randint, randrange
from models import cpfdig, verifycpf, cpfformat

n = False
while not n:
    cpf_num = ''
    for _ in range(9):
        c = str(randint(0, 9))
        cpf_num += c

    dig1 = cpfdig(cpf_num)
    dig2 = cpfdig(cpf_num+dig1)

    cpfnovo = cpf_num + dig1 + dig2

    n = verifycpf(cpfnovo)

    cpf_ofc = cpfformat(cpfnovo)

print(cpf_ofc)
