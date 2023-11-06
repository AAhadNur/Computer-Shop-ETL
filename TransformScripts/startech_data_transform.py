"""
Data Transformation Functions for Startech Laptops

This Python script contains data transformation functions for Startech laptops' data. It takes a DataFrame with
raw data and transforms it into a DataFrame with clean and structured information, suitable for analysis.

Functions:
- startech_data_transform(columns, df): Transforms the raw data from the input DataFrame and returns a new DataFrame
  with structured columns. The transformation includes extracting and converting numeric values, cleaning
  and reformatting columns, and calculating discounts.

Args:
- columns (list): A list of column names for the output DataFrame.
- df (pandas.DataFrame): The input DataFrame containing raw data.

Returns:
- result_df (pandas.DataFrame): The transformed DataFrame with structured data.

Usage:
You can use the 'startech_data_transform' function to process raw data from Startech laptops and obtain a clean
DataFrame for further analysis.

Author: [Abdul Ahad]
"""

import pandas as pd
from number_extraction import extract_number, extract_currency


def startech_data_transform(columns, df):

    print("Transforming and Cleaning Startech data .............")

    result_df = pd.DataFrame(columns=columns)

    for i in range(len(df)):
        brand = df.iloc[i]['brand']
        model = df.iloc[i]['model']
        regular_price = df.iloc[i]['regular_price']
        special_price = df.iloc[i]['special_price']
        discount = 0
        processor_brand = df.iloc[i]['processor_brand']
        processor_model = df.iloc[i]['processor_model']
        processor_base_frequency = df.iloc[i]['processor_frequency']
        ram = df.iloc[i]['ram']
        ram_type = df.iloc[i]['ram_type']
        storage_type = df.iloc[i]['storage_type']
        storage_capacity = df.iloc[i]['storage_capacity']
        graphics_chipset = df.iloc[i]['graphics_model']
        display_size = df.iloc[i]['display_size']
        display_type = df.iloc[i]['display_type']
        battery_type = df.iloc[i]['battery_type']
        battery_capacity = df.iloc[i]['battery_capacity']
        reviews = df.iloc[i]['reviews']

        model = model.split(':')[-1]

        regular_price, special_price, discount = extract_currency(
            regular_price, special_price)

        processor_base_frequency = extract_number(processor_base_frequency)

        ram = extract_number(ram)

        display_size = extract_number(display_size)

        storage = storage_capacity + ' ' + storage_type

        reviews = extract_number(reviews)

        if reviews == None:
            print(".")
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
