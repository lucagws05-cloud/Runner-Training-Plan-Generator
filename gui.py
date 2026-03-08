import tkinter as tk
from unittest import runner
from RUNNER import BeginnerRunner, IntermediateRunner, ExpertRunner
from training_goal_race import TrainingGoal
from training_plan import TrainingPlan
from visualization import plot_weekly_mileage


def generate_plan():
    name = name_entry.get()
    mileage = float(mileage_entry.get())
    weeks = int(weeks_entry.get())
    goal_time = int(goal_time_entry.get())

    exp = experience_var.get()
    race = race_var.get()

    if exp == "beginner":
        runner = BeginnerRunner(name, mileage)
    elif exp == "intermediate":
        runner = IntermediateRunner(name, mileage)
    else:
        runner = ExpertRunner(name, mileage)

    goal = TrainingGoal(race, weeks, goal_time)

    plan = TrainingPlan(runner, goal)
    plan.generate()
    plan.pretty_print()

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, plan.pretty_print())

    plot_weekly_mileage(plan)

root = tk.Tk()
root.title("Runner Training Plan Generator")

tk.Label(root, text="Runner name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weekly mileage (km)").pack()
mileage_entry = tk.Entry(root)
mileage_entry.pack()

tk.Label(root, text="Number of Weeks Until Race").pack()
weeks_entry = tk.Entry(root)
weeks_entry.pack()

race_var = tk.StringVar(value="Race Distance")
tk.OptionMenu(root, race_var, "5k", "10k", "Half", "Full").pack()

experience_var = tk.StringVar(value="Experience Level")
tk.OptionMenu(root, experience_var, "Beginner", "Intermediate", "Expert").pack()

tk.Label(root, text="Goal time (minutes)").pack()
goal_time_entry = tk.Entry(root)
goal_time_entry.pack()


tk.Button(root, text="Generate Plan", command=generate_plan).pack()

output_box = tk.Text(root, height=20, width=60)
output_box.pack()

root.mainloop()

