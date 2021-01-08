def error_checking(data):
    """"
    check if the data is dictionary or not and check whether is success if fail or not
    """
    if not isinstance(data, dict):
        raise("The data should be a dictionary")
    if data["success"] == False:
        raise("The data is catch unsuccessful")