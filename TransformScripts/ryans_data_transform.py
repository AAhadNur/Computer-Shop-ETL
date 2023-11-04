import pandas as pd
from number_extraction import extract_number, extract_currency


def ryans_data_transform(columns, df):

    result_df = pd.DataFrame(columns=columns)

    for i in range(len(df)):
        brand = df.iloc[i]['brand']
        model = df.iloc[i]['model']
        regular_price = df.iloc[i]['regular_price']
        special_price = df.iloc[i]['special_price']
        discount = 0
        processor_brand = df.iloc[i]['processor_brand']
        processor_model = df.iloc[i]['processor_model']
        processor_base_frequency = df.iloc[i]['processor_base_frequency']
        ram = df.iloc[i]['ram']
        ram_type = df.iloc[i]['ram_type']
        storage = df.iloc[i]['storage']
        display_size = df.iloc[i]['display_size']
        display_type = df.iloc[i]['display_type']
        graphics_chipset = df.iloc[i]['graphics_chipset']
        battery = df.iloc[i]['battery']
        battery_capacity = df.iloc[i]['battery_capacity']
        battery_type = df.iloc[i]['battery_type']
        reviews = df.iloc[i]['reviews']

        regular_price, special_price, discount = extract_currency(
            regular_price, special_price)

        processor_base_frequency = extract_number(processor_base_frequency)

        ram = extract_number(ram)

        display_size = extract_number(display_size)

        if battery is not None and battery != '':
            if battery_type is not None and battery_type != '':
                battery_type = battery + ' ' + battery_type
            else:
                battery_type = ''
        else:
            battery_type = ''

        reviews = extract_number(reviews)

        if reviews == None:
            reviews = 0

        battery_capacity = extract_number(battery_capacity)

        info = [
            model,
            brand,
            regular_price,
            special_price,
            discount,
            processor_brand,
            processor_model,
            processor_base_frequency,
            ram,
            ram_type,
            storage,
            display_size,
            display_type,
            graphics_chipset,
            battery_type,
            battery_capacity,
            reviews,
        ]
        result_df.loc[len(result_df)] = info

    return result_df
