from application.db.people import *
from application.salary import *
from datetime import date

if __name__ == '__main__':
    print(date.today())
    print(get_employees())
    print(calculate_salary())
