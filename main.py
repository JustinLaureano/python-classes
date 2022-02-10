from models.Order import Order
from models.Shipment import Shipment
from helpers.Faker import Faker
from helpers.FileHelper import FileHelper
import uuid
import random

# Start with no orders and shipments for testing purposes
FileHelper.truncate_file(Order().data_file)
FileHelper.truncate_file(Shipment().data_file)

# Make some random orders
for i in range(0, 10):
    order = Order()
    order.fill({
        'id': uuid.uuid4(),
        'item': random.choice(Faker.items),
        'amount': random.choice(Faker.amounts),
        'account_number': uuid.uuid1()
    })
    order.calculate_tax()
    order.save()

# Get all the orders
orders = Order().get()

# Print order records
for order in orders:
    print(f"Order Id: {order.id}, Item: {order.item}, Amount: {order.amount}, Tax {order.tax}, Account Number: {order.account_number}")

    # Create a shipment for each order
    shipment = Shipment()
    shipment.fill({
        'id': uuid.uuid4(),
        'order_id': order.id,
        'status': random.choice(Faker.statuses)
    })
    shipment.save()

# Get all the shipments
shipments = Shipment().get()

# Print shipment records
for shipment in shipments:
    print(f"Shipment ID: {shipment.id}, Order ID: {shipment.order_id}, Status: {shipment.status}")
    shipment.send_status_notification()
