# Futuro modulo para validar cpf
class cpfSizeError(Exception):
    def __init__(self):
        self.msg = "Por Favor insira um cpf de 11 digitos."
        super().__init__(self.msg)

class invalidCpfError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)


def cpfFomator(cpf: str):
    cpf = cpf.replace('.', '')
    try:
        numbers, digits = cpf.split('-')

    except:
        numbers = cpf[:-2]
        digits = cpf[-2:]

    numbers = [int(numero) for numero in list(numbers)]
    digits = [int(numero) for numero in list(digits)]
        

    return numbers, digits


def cpfValidation(cpf):
    numbers, digits = cpfFomator(cpf)
    cpf_size = 11

    if len(numbers) + len(digits) != cpf_size:
        return cpfSizeError()

    weight = list(range(10, 1, -1))

    if not firstDigitValidation(digits=digits, numbers=numbers, numbers_size=9, weight=weight):
        return invalidCpfError('1° digito não confere')
    
    numbers.append(digits[0])
    weight.insert(0, cpf_size)

    if not secondDigitValidation(digits=digits, numbers=numbers, numbers_size=10, weight=weight):
        return invalidCpfError('2° digito não confere')

    return cpf



def firstDigitValidation(digits: list[int], numbers: list[int], numbers_size: int,  weight: list[int]):
    return digits[0] == 11 - sum([numbers[i]*weight[i] for i in range(numbers_size)])%11


def secondDigitValidation(digits: list[int], numbers: list[int], numbers_size: int,  weight: list[int]):
    second_digit = 11 - sum([numbers[i]*weight[i] for i in range(numbers_size)])%11
    return digits[1] == second_digit or digits[1] == 0 and second_digit > 9
    
if __name__ == '__main__':
    cpf = '023.482.392-55'

    
    try:
        if cpfValidation(cpf):
            print('cpf valido')
    
    except Exception as e:
        print(e)
    
    

    

