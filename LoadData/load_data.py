"""
Insert Data from JSON into PostgreSQL Database

This Python script reads data from a JSON file and inserts it into a PostgreSQL database. It uses the SQLAlchemy model
'Laptop' to represent the data and provides the necessary database operations. If data for a laptop model already exists
in the database, it updates the existing record; otherwise, it inserts a new record.

Attributes:
- json_filename (str): Path to the JSON file containing laptop data to be inserted into the database.

Usage:
1. Ensure that the PostgreSQL database connection settings are correctly configured.
2. Create a JSON file with laptop data following the expected format.
3. Run this script to insert the updated data into the database.
4. It will update or insert records based on the presence of data in the database.

Author: [Abdul Ahad]
"""


from models import Laptop, Session
import json


def insert_data_from_json(json_filename):
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)

    session = Session()

    try:
        for item in data:

            existing_data = session.query(Laptop).filter_by(
                model=item['Model']).first()

            if existing_data:
                existing_data.model = item['Model'],
                existing_data.brand = item['Brand'],
                existing_data.regular_price = item['Regular Price (BDT)'],
                existing_data.special_price = item['Special Price (BDT)'],
                existing_data.discount = item['Discount (BDT)'],
                existing_data.processor_brand = item['Processor Brand'],
                existing_data.processor_model = item['Processor Model'],
                existing_data.processor_frequency = item['Processor Frequency (GHz)'],
                existing_data.ram = item['RAM (GB)'],
                existing_data.ram_type = item['RAM Type'],
                existing_data.storage = item['Storage'],
                existing_data.display_size = item['Display Size (inch)'],
                existing_data.display_type = item['Display Type'],
                existing_data.graphics_model = item['Graphics Model'],
                existing_data.battery_type = item['Battery Type'],
                existing_data.battery_capacity = item['Battery Capacity (WHr)'],
                existing_data.reviews = item['Number of Reviews'],

            else:
                laptop = Laptop(
                    model=item['Model'],
                    brand=item['Brand'],
                    regular_price=item['Regular Price (BDT)'],
                    special_price=item['Special Price (BDT)'],
                    discount=item['Discount (BDT)'],
                    processor_brand=item['Processor Brand'],
                    processor_model=item['Processor Model'],
                    processor_frequency=item['Processor Frequency (GHz)'],
                    ram=item['RAM (GB)'],
                    ram_type=item['RAM Type'],
                    storage=item['Storage'],
                    display_size=item['Display Size (inch)'],
                    display_type=item['Display Type'],
                    graphics_model=item['Graphics Model'],
                    battery_type=item['Battery Type'],
                    battery_capacity=item['Battery Capacity (WHr)'],
                    reviews=item['Number of Reviews'],
                )
                session.add(laptop)

        session.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    json_file_path = '../TransformScripts/data.json'
    insert_data_from_json(json_file_path)
