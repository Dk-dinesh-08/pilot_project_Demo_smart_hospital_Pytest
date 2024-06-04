from configparser import ConfigParser
def get_config(category,key):
    config=ConfigParser()
    config.read("C:\\PilotProject_DemoWebShop_Pytest\\Demo_smart_hospital\\Configurations\\config.ini")
    return config.get(category,key)