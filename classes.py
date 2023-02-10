class Operation:

    def __init__(self, id: int, state: str, data: str, operation_amount: dict, description: str, from_whom: str,
                 to_who: str):
        self.id = id
        self.state = state
        self.data = data
        self.operational_amount = operation_amount
        self.description = description
        self.from_whom = from_whom
        self.to_who = to_who


    def get_state(self):
        return self.state

    def get_date(self):
        return self.data

    def get_direction(self):
        return self.from_whom, self.to_who

    def get_operationamount(self):
        return self.operational_amount





