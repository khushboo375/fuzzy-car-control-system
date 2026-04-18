class FuelSystem:
    def __init__(self):
        self.max_fuel = 100.0
        self.fuel = 100.0
        self.history = []

    def update(self, speed):
        #  Simple consumption model
        consumption = 0.01 + (speed / 120) * 0.05

        self.fuel -= consumption
        self.fuel = max(0, self.fuel)

        # Store history for graph
        self.history.append(self.fuel)

        # Limit history size
        if len(self.history) > 200:
            self.history.pop(0)

    def get_fuel(self):
        return self.fuel