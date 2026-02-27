class TrainingGoal:
   RACE_DISTANCES_KM = {    # Race lengths that we support
       "5k": 5.0,
       "10k": 10.0,
       "half": 21.1,
       "full": 42.2,
   }


   MIN_WEEKS = {           # Minimum weeks needed to train for each race
       "5k": 6,
       "10k": 8,
       "half": 12,
       "full": 16,}


   def __init__(self, race_type: str, duration_weeks: int):   #generally ensuring they put valid input (Idea for this section came from ChatGPT)
       race_type = race_type.lower().strip()                  #preventing typos through capitalization and spaces       
       if race_type not in self.RACE_DISTANCES_KM:
           raise ValueError(f"race_type must be one of {list(self.RACE_DISTANCES_KM.keys())}")
       if duration_weeks <= 0:
           raise ValueError("duration_weeks must be positive")


       self.distance_km = self.RACE_DISTANCES_KM[race_type]
       self.duration_weeks = int(duration_weeks)


   def is_realistic(self) -> bool:         #checks if the training duration is long enough for their goal
       return self.duration_weeks >= self.MIN_WEEKS[self.race_type]