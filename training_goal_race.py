class TrainingGoal:
    RACE_DISTANCES_KM = {      # Race lengths that we support
        "5k": 5.0,
        "10k": 10.0,
        "half": 21.1,
        "full": 42.2,
    }

    MIN_WEEKS = {              # Minimum weeks needed to train for each race
        "5k": 6,
        "10k": 8,
        "half": 12,
        "full": 16,
    }

    def __init__(self, race_type: str, duration_weeks: int):
        self.race_type = race_type        # uses property setter
        self.duration_weeks = duration_weeks

    @property
    def race_type(self) -> str:
        return self._race_type

    @race_type.setter
    def race_type(self, value: str):
        value = value.lower().strip()
        if value not in self.RACE_DISTANCES_KM:
            raise ValueError(f"race_type must be one of {list(self.RACE_DISTANCES_KM.keys())}")
        self._race_type = value
        self._distance_km = self.RACE_DISTANCES_KM[value]

    @property
    def distance_km(self) -> float:
        return self._distance_km

    @property
    def duration_weeks(self) -> int:
        return self._duration_weeks

    @duration_weeks.setter
    def duration_weeks(self, value: int):
        if value <= 0:
            raise ValueError("duration_weeks must be positive")
        self._duration_weeks = int(value)

    def is_realistic(self) -> bool:   # checks if the training duration is long enough
        return self.duration_weeks >= self.MIN_WEEKS[self.race_type]