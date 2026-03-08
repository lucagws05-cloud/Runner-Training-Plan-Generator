from typing import List
from RUNNER import Runner
from training_goal_race import TrainingGoal
from WEEK import Week
from WORKOUT import Workout


class TrainingPlan:
    def __init__(self, runner: Runner, goal: TrainingGoal):
        self._runner = runner
        self._goal = goal
        self._weeks: List[Week] = []

    @property
    def runner(self) -> Runner:
        return self._runner

    @property
    def goal(self) -> TrainingGoal:
        return self._goal

    @property
    def weeks(self) -> List[Week]:
        return self._weeks

    def generate(self) -> None:
        self.weeks.clear()
        start_mileage = self._starting_mileage()

        for wk in range(1, self.goal.duration_weeks + 1):
            mileage = start_mileage * (1 + 0.05 * (wk - 1))

            if wk >= self.goal.duration_weeks - 1:
                mileage *= 0.7

            week = Week(wk, round(mileage, 1))
            self._build_week(week)
            self.weeks.append(week)

    def _starting_mileage(self) -> float:
        if self.runner.weekly_mileage > 0:
            return self.runner.weekly_mileage

        return {
            "beginner": 15.0,
            "intermediate": 30.0,
            "expert": 50.0,
        }[self.runner.experience_level]

    def _pace_defaults(self):
        if self.runner.experience_level == "beginner":
            return {"easy": 7.0, "long": 7.2, "tempo": 6.2, "interval": 5.8}
        if self.runner.experience_level == "intermediate":
            return {"easy": 6.0, "long": 6.2, "tempo": 5.2, "interval": 4.8}
        return {"easy": 5.3, "long": 5.5, "tempo": 4.6, "interval": 4.2}

    def _build_week(self, week: Week) -> None:
        paces = self._pace_defaults()
        mileage = week.target_mileage_km

        quality_type = "tempo"

        long_km = round(mileage * 0.35, 1)
        quality_km = round(mileage * 0.20, 1)
        easy_km_total = round(mileage - long_km - quality_km, 1)

        easy1 = round(easy_km_total / 2, 1)
        easy2 = round(easy_km_total - easy1, 1)

        week.add_workout(Workout("easy", easy1, paces["easy"], "low"))
        week.add_workout(Workout(quality_type, quality_km, paces[quality_type], "high"))
        week.add_workout(Workout("rest"))
        week.add_workout(Workout("easy", easy2, paces["easy"], "low"))
        week.add_workout(Workout("rest"))
        week.add_workout(Workout("long", long_km, paces["long"], "moderate"))
        week.add_workout(Workout("rest"))

    def pretty_print(self) -> str:
        output = []

        output.append(self.runner.get_info())
        output.append(
            f"Goal race: {self.goal.race_type} ({self.goal.distance_km} km), "
            f"{self.goal.duration_weeks} weeks"
        )
        output.append(f"Realistic? {'Yes' if self.goal.is_realistic() else 'Maybe not'}")
        output.append("")

        for week in self.weeks:
            output.append(
                f"Week {week.week_number} "
                f"(Target mileage: {week.target_mileage_km} km)"
            )
            for i, w in enumerate(week.workouts, start=1):
                output.append(f"  Day {i}: {w}")
            output.append("-" * 40)

        return "\n".join(output)