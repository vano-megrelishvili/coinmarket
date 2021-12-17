import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('example.log')
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee {first} - {last}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Geno', 'Tylashadze')
emp_2 = Employee('Vaja', 'Buchukuri')

