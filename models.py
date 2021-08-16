from random import randint


def cpfdig(l_num):
    # l_num = l_num

    cpf_test1 = []

    for mult, _num in enumerate(l_num[::-1], 2):
        x = mult * int(_num)
        cpf_test1 += [x]
    dig = 11 - (sum(cpf_test1) % 11)
    if dig > 9:
        dig = 0

    return str(dig)


def sepcpf(cpf):
    if '-' in cpf:
        num, dig = cpf.split('-')
    else:
        dig, num = cpf[-2:], cpf[:-2]
    num = num.replace('.', '')
    return num, dig


def verifycpf(cpf):
    if cpf.count(cpf[0]) == 11:
        return False
    num, dig = sepcpf(cpf)
    d1 = cpfdig(num)
    d2 = cpfdig(num+d1)
    if d1+d2 == dig:
        rs = (num+dig).replace('', ' ').strip().split(' ')
        rs = sum(map(int, rs))
        return True if rs % 11 == 0 else False
    else:
        return False


def cpfformat(cpf):
    cpflista = cpf.replace('', ' ').strip().split(' ')
    cpflista.insert(9, '-')
    for ind in range(3, 9, 4):
        cpflista.insert(ind, '.')

    return ''.join(cpflista)


if __name__ == '__main__':
    f = False
    while not f:
        cpf = str(randint(100000000, 999999999))
        dig = cpfdig(cpf)
        f = verifycpf(cpf)
    print(f, cpf)
