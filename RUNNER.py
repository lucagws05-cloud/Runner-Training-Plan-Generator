
class Runner:
    def __init__(self, name, experience_level, weekly_mileage=0):
        self._name = name
        self._experience_level = experience_level # beginner/intermediate/expert
        self._weekly_mileage = weekly_mileage   # distance they run now per week

    @property
    def name(self):
        return self._name

    @property
    def experience_level(self):
        return self._experience_level

    @experience_level.setter
    def experience_level(self, level):
        valid_levels = ["beginner", "intermediate", "expert"]
        if level not in valid_levels:
            raise ValueError("Experience level must be beginner, intermediate, or expert")
        self._experience_level = level

    @property
    def weekly_mileage(self):
        return self._weekly_mileage

    @weekly_mileage.setter
    def weekly_mileage(self, mileage):
        if mileage < 0:
            raise ValueError("Weekly mileage cannot be negative")
        self._weekly_mileage = mileage

    def suggest_plan(self):
        if self.experience_level == "beginner":
            return "Run 3-4 times per week, 10-20km total"
        elif self.experience_level == "intermediate":
            return "Run 4-5 times per week, 20-40km total"
        else:
            return "Run 5-6 times per week, 40-60km total"

    def get_info(self):
        return f"Name: {self.name}, Experience level: {self.experience_level}, Current weekly mileage: {self.weekly_mileage} km"