def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if "not enough values to unpack" in str(e): 
                return "Give me name and phone please."
            else:
                return str(e)     
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
            
    return inner