#PROJETO NÚMERO PENSANTE
from random import choice
from time import sleep
print('''Carregando...
Aguarde 8 segundos...''')
PC = choice(range(1,101))
sleep(1)
C1 = choice(range(1,PC+1))
sleep(1)
F1 = choice(range(PC,101))
sleep(1)
C2 = choice(range(C1,PC))
sleep(1)
F2 = choice(range(PC,F1))
sleep(1)
C3 = choice(range(C2,PC))
sleep(1)
F3 = choice(range(PC,F2))
sleep(1)
C4 = choice(range(C3,PC))
sleep(1)
F4 = choice(range(PC,F3))
COR = '\033[33m'
LIMPA = '\033[m'   
TENT = 0
NUM = 0
print(f'{'-=-'*16}\nTENTE ACERTAR O NÚMERO QUE EU ESTOU PENSANDO...\n{' '*16}(de 1 a 100)\n{'-=-'*16}')
while NUM != PC:
    NUM = int(input('Chute um número\n---> '))
    if NUM != PC:
        print(f'\033[31m(ERRADO){LIMPA}')
    elif NUM == PC:
        print(f'\033[1;36mACERTOU{LIMPA}')
    TENT += 1
    if TENT == 2:
        print(f'{COR}*DICA 1:\nESTÁ ENTRE {C1} E {F1}*{LIMPA}')
    elif TENT == 4:
        print(f'{COR}*DICA 2:\nESTÁ ENTRE {C2} E {F2}*{LIMPA}')
    elif TENT == 6:
        print(f'{COR}*DICA 3:\nESTÁ ENTRE {C3} E {F3}*{LIMPA}')
    elif TENT == 8:
        print(f'{COR}*DICA FINAL:\nESTÁ ENTRE {C4} E {F4}!!!!!{LIMPA}')
    elif TENT == 9:
        print(f'{'\033[1;31m'}=> TENTATIVA FINAL <={LIMPA}')
    elif TENT == 10:
        break
if PC == NUM:
    print(f'{'\033[36m'}O QUE!?!?!?!?!?!')
    sleep(1)
    print('COMO VOCÊ ACERTOU??????')
    sleep(2)
    print('>:(')
    sleep(2)
    print(f'NA PRÓXIMA VEZ, VOCÊ NÃO VAI ACERTAR{LIMPA}')
    sleep(2)
else:
    print(f'{'\033[31m'}HAHAHHAHAHAHHAHA')
    sleep(2)
    print('EU GANHEI!!!!!!')
    sleep(2)
    print('VOCÊ É HORRÍVEL NO CHUTE')
    sleep(1)
    print('TENTE ACERTAR NA PRÓXIMA')
    sleep(2)
    print('SÓ TENTAR MESMO HAHHAHAHAHAH')
    sleep(1)
    print(f'>:D{LIMPA}')
    sleep(2)
print(f'{'='*15}\n{'\033[1;30m'}TOTAL DE CHUTES\n===>{LIMPA} {TENT} de 10\n{'\033[1;32m'}O NÚMERO ERA\n===>{LIMPA} {PC}\n{'='*15}')
