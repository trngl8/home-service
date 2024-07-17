class Validator:
    
    def __init__(self, data):
        self.data = data
        self.errors = []


    def is_not_empty(self, field):
        if not self.data.get(field):
            self.errors.append(f"The field {field} can not be empty")
            return False
        return True


    def is_integer(self, field):
        value = self.data.get(field)
        if value is not None and not value.isdigit():
            self.errors.append(f"The field '{field}' must be an integer.")
            return False
        return True


    def is_in_range(self, field, min_possible, max_possible):
        value = self.data.get(field)
        if value is not None and value.isdigit():
            if not (min_possible <= int(value) <= max_possible):
                self.errors.append(f"The filed {field} muts be between {min_possible} and {max_possible}")
                return False
        return True
    
    def validate(self):
        if len(self.errors) == 0:
            return True
        return False
