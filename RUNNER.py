class Runner:
    def __init__(self, name, weekly_mileage=0):
        self._name = name
        self._weekly_mileage = weekly_mileage

    @property
    def name(self):
        return self._name

    @property
    def weekly_mileage(self):
        return self._weekly_mileage

    @weekly_mileage.setter
    def weekly_mileage(self, mileage):
        if mileage < 0:
            raise ValueError("Weekly mileage cannot be negative")
        self._weekly_mileage = mileage

    def suggest_plan(self):
        raise NotImplementedError("Subclasses must implement suggest_plan()")

    def get_info(self):
        return f"Name: {self.name}, Experience level: {self.experience_level}, Current weekly mileage: {self.weekly_mileage} km"


# Subclasses for different experience levels
class BeginnerRunner(Runner):
    _experience_level = "beginner"

    @property
    def experience_level(self):
        return self._experience_level

    def suggest_plan(self):
        return "Run 3-4 times per week, 10-20km total"


class IntermediateRunner(Runner):
    _experience_level = "intermediate"

    @property
    def experience_level(self):
        return self._experience_level

    def suggest_plan(self):
        return "Run 4-5 times per week, 20-40km total"


class ExpertRunner(Runner):
    _experience_level = "expert"

    @property
    def experience_level(self):
        return self._experience_level

    def suggest_plan(self):
        return "Run 5-6 times per week, 40-60km total"