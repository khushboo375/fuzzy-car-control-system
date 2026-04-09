import csv
import os
from datetime import datetime

class DataLogger:
    def __init__(self):
        os.makedirs("data", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = f"data/log_{timestamp}.csv"

        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["time", "distance", "road", "light", "speed"])

        self.time = 0

    def log(self, distance, road, light, speed):
        self.time += 1

        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.time, distance, road, light, speed])