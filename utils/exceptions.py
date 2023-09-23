class NotOwnerException(Exception):
    def __init__(self):
        self.context = {
            "status":401,
        }
        super().__init__("You don't have permission to acces this data")    

class InvalidIdException(Exception):
    def __init__(self):
        self.context = {
            "status":401,
        }
        super().__init__("The given id is not valid")   

class NotPermissionException(Exception):
    def __init__(self):
        self.context = {
            "status":401,
        }
        super().__init__("You don't have permission to do this operation")   

class NotStaffException(Exception):
    def __init__(self):
        self.context = {
            "status":401,
        }
        super().__init__("You must be a staff member to do this operation")  

class NotAuthenticatedException(Exception):
    def __init__(self):
        self.context = {
            "status":401,
        }
        super().__init__("You must be authenticated to do this operation")                                