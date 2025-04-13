from application.db.people import get_people
from salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    get_people()
    calculate_salary()