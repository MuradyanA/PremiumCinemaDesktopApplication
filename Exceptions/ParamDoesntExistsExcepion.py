class ParamDoesntExistsException(Exception):
    def __init__(self, param_name):
        self.message = f"{param_name} isn't set"
        super().__init__(self.message)