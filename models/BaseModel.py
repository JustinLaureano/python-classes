from helpers.FileHelper import FileHelper
from copy import copy
import csv

class BaseModel:
    # The file that will store the model records
    data_file = None

    # the fields that will be stored
    storable = []


    def fill(self, data):
        """
            Fill the models properties with the provided data
        """
        for key, value in data.items():
            setattr(self, key, value)


    def save(self):
        """
            Save a new record based on the storable fields
        """

        if self.data_file is None:
            raise Exception('No data file specified.')

        if not self.storable:
            raise Exception('No attributes are provided to be saved.')

        data = []

        for attr in self.storable:
            data.append( str(getattr(self, attr)) )

        FileHelper.append_to_file(self.data_file, data)


    def get(self):
        """
            Get the records and return as model instances
        """

        # Start a list of records to be returned
        records = []

        # Read the model records file
        with open(FileHelper.get_file(self.data_file)) as file_obj:
            reader_obj = csv.reader(file_obj)

            # Make an instance of each record in the file
            for row in reader_obj:
                records.append( self.__singleton(row) )

        return records


    def __singleton(self, data):
        """
            Create a single instance from given data
        """
        # Create a new object instance of the model
        obj = copy(self)

        # Loop through all the record values
        for index, value in enumerate(data):
            # find the corresponding class property for this value
            obj_property = self.storable[index]

            # Assign the value to the property it belongs too
            setattr(obj, obj_property, value)

        return obj