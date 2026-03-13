class Runner:
   """
   Base class representing a generic runner.


   Attributes:
       _name (str): The runner's name.
       _weekly_mileage (int/float): Current weekly running distance in km.
   """


   def __init__(self, name, weekly_mileage=0):
       """
       Initialize a Runner object.


       Args:
           name (str): Name of the runner.
           weekly_mileage (int/float): Current weekly mileage (default is 0).
       """
       self._name = name
       self._weekly_mileage = weekly_mileage


   @property
   def name(self):
       """Return the runner's name."""
       return self._name


   @property
   def weekly_mileage(self):
       """Return the runner's current weekly mileage."""
       return self._weekly_mileage


   @weekly_mileage.setter
   def weekly_mileage(self, mileage):
       """
       Set the weekly mileage.


       Raises:
           ValueError: If mileage is negative.
       """
       # Ensure mileage is not negative
       if mileage < 0:
           raise ValueError("Weekly mileage cannot be negative")
       self._weekly_mileage = mileage


   def suggest_plan(self):
       """
       Suggest a training plan.


       This method must be implemented by subclasses.
       """
       raise NotImplementedError("Subclasses must implement suggest_plan()")


   def get_info(self):
       """
       Return a formatted string containing runner information.
       """
       return f"Name: {self.name}, Experience level: {self.experience_level}, Current weekly mileage: {self.weekly_mileage} km"




# Subclasses for different experience levels
class BeginnerRunner(Runner):
   """
   Runner subclass representing a beginner runner.
   """
   _experience_level = "beginner"


   @property
   def experience_level(self):
       """Return the experience level of the runner."""
       return self._experience_level


   def suggest_plan(self):
       """
       Suggest a beginner training plan.
       """
       return "Run 3-4 times per week, 10-20km total"




class IntermediateRunner(Runner):
   """
   Runner subclass representing an intermediate runner.
   """
   _experience_level = "intermediate"


   @property
   def experience_level(self):
       """Return the experience level of the runner."""
       return self._experience_level


   def suggest_plan(self):
       """
       Suggest an intermediate training plan.
       """
       return "Run 4-5 times per week, 20-40km total"




class ExpertRunner(Runner):
   """
   Runner subclass representing an expert runner.
   """
   _experience_level = "expert"


   @property
   def experience_level(self):
       """Return the experience level of the runner."""
       return self._experience_level


   def suggest_plan(self):
       """
       Suggest an expert training plan.
       """
       return "Run 5-6 times per week, 40-60km total"