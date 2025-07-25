# -*- coding: utf-8 -*-

# Este script es un test de limpieza de datos JSON.
# Utiliza la API de Coderbyte para obtener datos JSON y limpiarlos de valores problemáticos.
# Los valores problemáticos incluyen "N/A", "-", "", "null" y None.
# La función `clean_json_element` recorre el JSON y elimina estos valores, devolviendo un JSON limpio que se imprime al final.

import requests
import json


def clean_json_element(element):
    problematic_values = ["N/A", "-", "", "null", None]
    if isinstance(element, dict):
        cleaned_dict = {}
        for key, value in element.items():
            cleaned_value = clean_json_element(value)
            if value not in problematic_values:
                cleaned_dict[key] = cleaned_value
        return cleaned_dict
    elif isinstance(element, list):
        cleaned_list = []
        for item in element:
            cleaned_item = clean_json_element(item)
            if cleaned_item not in problematic_values:
                cleaned_list.append(cleaned_item)
        return cleaned_list
    else:
        if isinstance(element, str) and element in problematic_values:
            return None
        return element


def clean_data():
    r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
    original_data = r.json()
    cleaned_data = clean_json_element(original_data)
    return json.dumps(cleaned_data, separators=(',', ':'))

print(clean_data())
