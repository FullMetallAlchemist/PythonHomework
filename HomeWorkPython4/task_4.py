# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 
# k = 6
# ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
# a, b, c, d, e, h - рандом

from random import randint, choice

def generate_polynomial(powers_dict: dict):
    result = []

    for power, coef in sorted(powers_dict.items(), reverse=True):
        if power == 0:
            if coef == 0:
                continue

            result.append(str(coef))
            continue

        if coef == 0:
            continue

        elif coef == 1:
            if power == 1:
                result.append(f'x')

            else:
                result.append(f'x^{power}')

        else:
            if power == 1:
                result.append(f'{coef}*x')

            else:
                result.append(f'{coef}*x^{power}')

    return result

def get_polynom(power: int, max_coef: int = 100) -> str:
    lst_coefs = [randint(0, max_coef) for _ in range(power + 1)]
    # Разделил специально, чтобы в 5 задании меньше писать)
    dct_pows = {power - i: lst_coefs[i] for i in range(power + 1)}

    result = generate_polynomial(dct_pows)

    return ' + '.join(result)

max_power = int(input('Enter the maximal power of the polynom: '))
print(f'The final polynom of power {max_power}:', get_polynom(max_power))