import models

while True:
    cpf = input('CPF: ')

    verificado = models.verifycpf(cpf)
    print('Válido' if verificado else 'Inválido')