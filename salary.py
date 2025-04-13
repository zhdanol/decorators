import os
import datetime
from functools import wraps

def logger(old_function):
    inform = 'Выводим информацию о зарплате'
    
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('result.log', 'a', encoding='utf-8') as f:
            f.write(f'{datetime.datetime.now()} - {inform},{old_function.__name__}({args}, {kwargs})= {result}\n')
        return result
    return new_function

@logger
def calc_salary(base_salary, bonus):
    return base_salary + bonus

if __name__ == '__main__':
    calc_salary(20000, 2000)