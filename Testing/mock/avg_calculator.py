class AvgCalculator:
    """The class is used to calculate the average of a file."""
    def __init__(self, filename):
        self.filename = filename

    def _get_content(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            return [line.split(',') for line in lines]

    def _ensure_casted_data(self):
        data = self._get_content()
        new_data = []
        for x in data:
            new_data.append([int(n) for n in x])

        return new_data

    def calculate(self):
        numbers = self._ensure_casted_data()
        return [sum(x) / len(x) for x in numbers]

    def get_data(self):
        """returns the raw data"""
        return self._get_content()


# The problem is that the class reads from the file. Now, if we want to write tests, we have to create these files?
