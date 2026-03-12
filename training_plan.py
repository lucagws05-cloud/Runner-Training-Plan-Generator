from ast import If
from typing import List
from RUNNER import Runner
from training_goal_race import TrainingGoal
from WEEK import Week
from WORKOUT import Workout




class TrainingPlan:
   """
   Represents a full training plan for a runner.


   The plan is generated based on:
   - The runner's experience and current weekly mileage
   - The training goal (race type, distance, and duration)


   The plan consists of several Week objects, each containing workouts.
   """
   
   def __init__(self, runner: Runner, goal: TrainingGoal):
       """
       Initialize the training plan.


       Parameters
       ----------
       runner : Runner
           The runner for whom the training plan is created.
       goal : TrainingGoal
           The goal race and duration of the training plan.
       """      
       self._runner = runner           # stores the runner information
       self._goal = goal           # stores the training goal information
       self._weeks: List[Week] = []            # initializes an empty list to hold the weekly training plans  


   @property           # defines a property to access the runner information
   def runner(self) -> Runner:
       """
       Returns the runner associated with the training plan.
       """
       return self._runner


   @property           # defines a property to access the training goal information
   def goal(self) -> TrainingGoal:
       """
       Returns the training goal associated with the training plan.
       """
       return self._goal


   @property           # defines a property to access the list of weekly training plans
   def weeks(self) -> List[Week]:
       """
       Returns the list of weekly training plans.
       """
       return self._weeks




   def generate(self) -> None:   
       """
       Generate the full training plan.


       The plan is built week by week. Each week increases mileage
       by approximately 5% to ensure progressive overload.
       The last two weeks are tapered (reduced mileage) to allow
       recovery before the race.
       """                       
       self.weeks.clear()      # clears any existing weeks in the training plan


       start_mileage = self._starting_mileage()            # calculates the starting mileage based on the runner's current weekly mileage or experience level            


       for wk in range(1, self.goal.duration_weeks + 1):           # create each week of the training plan
           mileage = start_mileage * (1 + 0.05 * (wk - 1))         # +5% in mileage per week


           if wk >= self.goal.duration_weeks - 1:          # taper mileage over the last 2 weeks
               mileage *= 0.7


           week = Week(wk, round(mileage, 1))                      # creates the Week object with the week number and target mileage
           self._build_week(week)          # builds the workouts for the week based on the target mileage and default paces       
           self.weeks.append(week)     # adds the week to the training plan's list of weeks


   def _starting_mileage(self) -> float:             
       """
       Determine the starting weekly mileage.


       If the runner already has a specified weekly mileage,
       that value is used. Otherwise, a default value based
       on experience level is returned.


       Returns
       -------
       float
           The starting weekly mileage in kilometers.
       """             
       if self.runner.weekly_mileage > 0:          # use runner's current mileage if available          
           return self.runner.weekly_mileage


       return {            # otherwise determine mileage from experience level                 
           "beginner": 15.0,
           "intermediate": 30.0,
           "expert": 50.0,
       }[self.runner.experience_level]


   def _pace_defaults(self):    
       """
       Return default running paces depending on the runner's experience.


       Paces are expressed in minutes per kilometer and include:
       - easy pace
       - long run pace
       - tempo pace
       - interval pace


       More experienced runners have faster paces.
       """
       if self.runner.experience_level == "beginner":
           return {"easy": 7.0, "long": 7.2, "tempo": 6.2, "interval": 5.8}
       if self.runner.experience_level == "intermediate":
           return {"easy": 6.0, "long": 6.2, "tempo": 5.2, "interval": 4.8}
       return {"easy": 5.3, "long": 5.5, "tempo": 4.6, "interval": 4.2}            # expert runner default paces




   def _build_week(self, week: Week) -> None:    
       """
       Build the workouts for a given week.


       The weekly mileage is divided into:
       - long run (~35%)
       - quality session (~20%) such as tempo or intervals
       - easy runs (remaining distance)


       Rest days are included to allow recovery.
       """
       paces = self._pace_defaults()           # get default paces for the runner
       mileage = week.target_mileage_km            # target mileage for this week


       quality_type = "tempo"          # currently the quality session is always tempo


       # calculate distances for different workout types
       long_km = round(mileage * 0.35, 1)
       quality_km = round(mileage * 0.20, 1)
       easy_km_total = round(mileage - long_km - quality_km, 1)            # remaining mileage is assigned to easy runs


       easy1 = round(easy_km_total, 1)


       # build the weekly schedule with workouts and rest days
       week.add_workout(Workout("easy", easy1, paces["easy"], "low"))
       week.add_workout(Workout(quality_type, quality_km, paces[quality_type], "high"))
       week.add_workout(Workout("rest"))
       week.add_workout(Workout("easy", easy1, paces["easy"], "low"))
       week.add_workout(Workout("rest"))
       week.add_workout(Workout("long", long_km, paces["long"], "moderate"))
       week.add_workout(Workout("rest"))
  
   def pretty_print(self) -> None:
       """
       Print the training plan in a readable format.


       Displays:
       - runner information
       - goal race details
       - whether the goal is realistic
       - each week with its workouts
       """
       # print runner information
       print(self.runner.get_info())          
       # print goal race details
       print(
           f"Goal race: {self.goal.race_type} ({self.goal.distance_km} km),"
           f" {self.goal.duration_weeks} weeks"
       )          
      # print goal realism
       print(f"Realistic? {'Yes' if self.goal.is_realistic() else 'Maybe not'}")          
       print()


       # print weekly breakdown
       for week in self.weeks:
           print(
               f"Week {week.week_number} "
               f"(Target mileage: {week.target_mileage_km} km)"
           )          
           # print workouts for the week
           for i, w in enumerate(week.workouts, start=1):
               print(f"  Day {i}: {w}")
           print("-" * 40)         # separator between weeks

