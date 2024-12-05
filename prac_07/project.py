import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percent = int(completion_percent)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percent}%"

    def is_completed(self):
        return self.completion_percent == 100

    @staticmethod
    def from_string(data_string):
        """Creates a Project object from a tab-delimited string."""
        name, start_date, priority, cost_estimate, completion_percent = data_string.split("\t")
        return Project(name, start_date, priority, cost_estimate, completion_percent)

    def to_string(self):
        """Converts a Project object into a tab-delimited string."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percent}"

    def __lt__(self, other):
        """Less than operator for sorting by priority."""
        return self.priority < other.priority
