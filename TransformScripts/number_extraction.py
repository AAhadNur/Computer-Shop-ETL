"""
Utility Functions for Extracting and Manipulating Prices

This Python file contains utility functions for extracting and manipulating price-related information.
The functions can be used to extract numerical values from strings, convert currency formats, and calculate
discounts between regular and special prices.

Functions:
- extract_number(value): Extracts numerical values from a given string and returns an integer.
- extract_currency(regular_price, special_price): Extracts and converts regular and special prices from string
  format to integers. Calculates the discount amount if both prices are available.

Usage:
You can import and use these functions in your Python scripts to work with price-related data and convert
currency formats to numeric values.

Author: [Abdul Ahad]
"""

import re


def extract_number(value):
    if value is not None and value != '':
        match = re.search(r'\d+', value)
        if match:
            value = int(match.group())
        else:
            value = None
    else:
        value = None
    return value


def extract_currency(regular_price, special_price):
    discount = 0

    if regular_price is not None and regular_price != '':
        match = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', regular_price)
        if match:
            regular_price = int(match.group().replace(',', ''))
        else:
            regular_price = 0

    if special_price is not None and special_price != '':
        match = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', special_price)
        if match:
            special_price = int(match.group().replace(',', ''))
        else:
            special_price = 0

    if regular_price is None or regular_price == '':
        if special_price is not None and special_price != '':
            regular_price = special_price
        else:
            regular_price = None

    if special_price is None or special_price == '':
        if regular_price is not None and regular_price != '':
            special_price = regular_price
        else:
            special_price = None

    if regular_price is not None and special_price is not None:
        if regular_price != '' and special_price != '':
            if regular_price > special_price:
                discount = regular_price - special_price

    return regular_price, special_price, discount
