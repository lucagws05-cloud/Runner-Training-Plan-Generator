RUNNER

class Runner: 
    def __init__(self, name, experience_level, weekly_mileage=0):
        self.name = name
        self.experience_level = experience_level  # beginner/intermediate/expert
        self.weekly_mileage = weekly_mileage    # distance they run now per week

    def suggest_plan(self):
        if self.experience_level == "beginner":
            return "Run 3-4 times per week, 10-20km total"
        elif self.experience_level == "intermediate":
            return "Run 4-5 times per week, 20-40m total"
        else:
            return "Run 5-6 times per week, 40-60km total"

    def get_info(self):
        return f"Name: {self.name}, Experience level: {self.experience_level}, Current weekly mileage: {self.weekly_mileage} km"

