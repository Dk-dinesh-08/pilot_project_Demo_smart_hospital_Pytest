from configparser import ConfigParser
def get_config(category,key):
    config=ConfigParser()
    config.read("D:\\Dinesh_branch_pytest_demo_smart_hospital\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\Configurations\\config.ini")
    return config.get(category,key)

