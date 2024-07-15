import configparser
from configparser import ConfigParser
def get_config(category,key):
    config=ConfigParser()

    config.read("D:\\Branch_kiruthika\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\Configurations\\config.ini")
    print("Available sections:", config.sections())  # Debugging output
    if not config.has_section(category):
        raise configparser.NoSectionError(category)
    print(f"Options in '{category}':", config.options(category))  # Debugging output
    if not config.has_option(category, key):
        raise configparser.NoOptionError(key, category)
    return config.get(category,key)
    
 


