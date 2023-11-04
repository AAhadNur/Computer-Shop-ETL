
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
