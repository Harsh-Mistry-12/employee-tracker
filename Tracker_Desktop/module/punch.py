from datetime import datetime

class TimeClock:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def punch_in(self):
        self.start_time = datetime.now()
        print("Punched in at:", self.start_time)

    def punch_out(self):
        if self.start_time is None:
            print("Error: Please punch in first.")
            return
        self.end_time = datetime.now()
        print("Punched out at:", self.end_time)
        self.calculate_work_hours()

    def calculate_work_hours(self):
        if self.start_time is None or self.end_time is None:
            print("Error: Work hours can't be calculated without punch in and out.")
            return
        work_hours = self.end_time - self.start_time
        print("Total work hours:", work_hours)

# Example usage
time_clock = TimeClock()
time_clock.punch_in()

# Simulating some work...
# For demonstration purposes, let's just wait for user input
input("Press Enter when you're done working...")

time_clock.punch_out()
