from models.BaseModel import BaseModel

class Shipment(BaseModel):
    data_file = 'shipments.csv'
    storable = ['id', 'order_id', 'status']

    def send_status_notification(self):
        """
            Send a status notification for the shipment
        """

        print(f"The status of shipment ID {self.id} is {self.status}")