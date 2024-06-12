from configparser import ConfigParser
def get_config(category,key):
    config=ConfigParser()
<<<<<<< HEAD
    config.read("D:\\Dinesh_branch_pytest_demo_smart_hospital\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\Configurations\\config.ini")
=======
    config.read("C:\\Pytest_Mainproject\\pilot_project_Demo_smart_hospital_Pytest\\Demo_smart_hospital\\Configurations\\config.ini")
>>>>>>> 6b7959b5c0961377f98844fecd08ec00e028720d
    return config.get(category,key)

