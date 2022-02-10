from models.BaseModel import BaseModel
from helpers.Faker import Faker
import random

class Order(BaseModel):
    data_file = 'orders.csv'
    storable = ['id', 'item', 'amount', 'tax', 'account_number']

    def calculate_tax(self):
        self.fill({
            'tax': random.choice(Faker.taxes)
        })