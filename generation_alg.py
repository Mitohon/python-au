#Преобразование случайной строки в строку, введенную с консоли пользователем

import random
import string

letters = string.ascii_letters + "ąčęėįšųūqwertyuioplkjhgfdsazxcvbnmČĄĘĖĮĮŠŲŪQWERTYUIOPLKJHGFDSAZXCVBNMйцукенгшщзхъэждлорпавыфячсмитьбюёЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ' .,-!123456789"

def random_string(length):
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Рандомная строка из", length, "знаков:", rand_string)
    return rand_string


def reproduce(offsprings):
    new_off = []
    middle = int(len(offsprings[0]) / 2)
    i = 0
    for i in range(0, len(offsprings), 2):
        member1 = list(offsprings[i])
        member2 = list(offsprings[i+1])
        for j in range(middle, len(member1)):
            a = member2[j]
            member2[j] = member1[j]
            member1[j] = a
        new_off.append(member1)
        new_off.append(member2)
    return new_off

def match(member, str):
    i = len(str)-1
    differences = 0
    for i in range (len(str)-1, -1, -1):
        if str[i] != member[i]:
            differences += 1
    return differences

def select(offsprings, str):
    survival_value = map(lambda x: (match(x, str), x), offsprings)
    selection = list(map(lambda xy: xy[1], sorted(survival_value)[:len(offsprings)]))
    return selection

def mutation(offspring):
    mut_count = random.randint(0, len(offspring)-1)
    temp = list(offspring)
    temp[mut_count] = random.choice(letters)
    offspring = "".join(temp)
    return offspring

def mutations(offsprings):
    new_generation = []
    for member in offsprings:
        new_generation.append(mutation(member))
    return new_generation

def survival(offsprings, str):
    off = select(offsprings, str)
    if len(off) > 8:
        return off[:int(len(off)/4)]
    return off

def the_evolution_of_a_string():
    str = input()
    if len(str) == 0:
        return 'пустая строка'
    first_gen1 = random_string(len(str))
    offsprings = []
    offsprings.append(first_gen1)
    offsprings.append(mutation(first_gen1))
    i = 0

    while True:
        new_gen = reproduce(offsprings)
        offsprings += mutations(new_gen)
        offsprings = survival(offsprings, str)
        if offsprings[0] == str:
            print()
            print('эволюция: строка', offsprings[0], 'нашлась на ', i, 'итерации')
            break
        if i > 100000:
            print('Сегодня без эволюции')
            print('Попробуйте другую строку с другими символами (добавлен литовский язык, испанский пока что в разработке)')
            break
        i += 1

if __name__ == "__main__":
    the_evolution_of_a_string()
