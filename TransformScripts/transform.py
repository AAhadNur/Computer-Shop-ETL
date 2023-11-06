"""
Data Transformation and Aggregation for Laptop Data

This Python script reads and transforms data from two different sources (Ryans and Startech laptops) and
aggregates the information into a single structured dataset. The transformed data is then saved as a CSV file.

Functions:
- transform(): The main transformation function that reads, processes, and aggregates data from both sources.

Usage:
1. Place the Ryans and Startech laptop data JSON files in the appropriate paths.
2. Run this script to transform and aggregate the data.
3. The resulting CSV file contains the structured laptop data.

Author: [Abdul Ahad]
"""

import pandas as pd
from ryans_data_transform import ryans_data_transform
from startech_data_transform import startech_data_transform


def transform():

    df1 = pd.read_json('../ExtractingLaptopData/RyansData.json')
    df2 = pd.read_json('../ExtractingLaptopData/StartechData.json')

    columns = [
        'Model',
        'Brand',
        'Regular Price (BDT)',
        'Special Price (BDT)',
        'Discount (BDT)',
        'Processor Brand',
        'Processor Model',
        'Processor Frequency (GHz)',
        'RAM (GB)',
        'RAM Type',
        'Storage',
        'Display Size (inch)',
        'Display Type',
        'Graphics Model',
        'Battery Type',
        'Battery Capacity (WHr)',
        'Number of Reviews',
    ]

    rdf = ryans_data_transform(columns=columns, df=df1)
    sdf = startech_data_transform(columns=columns, df=df2)

    df = pd.concat([rdf, sdf]).reset_index(drop=True)

    df = df.drop_duplicates(subset=['Model'], keep='first')

    # df.to_json('data.json', orient='records')

    df.to_csv('data.csv', index=False)


if __name__ == "__main__":
    transform()
