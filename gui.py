import tkinter as tk  # GUI library for creating the application window and widgets
from RUNNER import BeginnerRunner, IntermediateRunner, ExpertRunner
from training_goal_race import TrainingGoal
from training_plan import TrainingPlan
from visualization import plot_weekly_mileage


def generate_plan():
    """
    This method generates a week-by-week training plan based on the user's input
    from the GUI, including the runner's experience level, current weekly mileage,
    number of weeks until the race, and the goal race time.

    The generated plan includes weekly mileage progression and different types of
    running workouts such as easy runs, long runs, tempo runs, and rest days.

    The generated training plan is displayed in the output text box and the
    weekly mileage progression is plotted using the plot_weekly_mileage function.
    """

    # Retrieve input values
    name = name_entry.get()
    mileage = float(mileage_entry.get())
    weeks = int(weeks_entry.get())
    goal_time = int(goal_time_entry.get())

    exp = experience_var.get().lower()
    race = race_var.get().lower()

    # Create the appropriate runner class
    if exp == "beginner":
        runner = BeginnerRunner(name, mileage)
    elif exp == "intermediate":
        runner = IntermediateRunner(name, mileage)
    else:
        runner = ExpertRunner(name, mileage)

    # Create training goal
    goal = TrainingGoal(race, weeks, goal_time)

    # Generate training plan
    plan = TrainingPlan(runner, goal)
    plan.generate()

    # Display plan in GUI
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, plan.pretty_print())

    # Plot weekly mileage
    plot_weekly_mileage(plan)


# Create main window
root = tk.Tk()
root.title("Runner Training Plan Generator")

# Runner name
tk.Label(root, text="Runner name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Weekly mileage
tk.Label(root, text="Weekly mileage (km)").pack()
mileage_entry = tk.Entry(root)
mileage_entry.pack()

# Weeks until race
tk.Label(root, text="Number of Weeks Until Race").pack()
weeks_entry = tk.Entry(root)
weeks_entry.pack()

# Race selection
race_var = tk.StringVar(value="5k")
tk.OptionMenu(root, race_var, "5k", "10k", "half", "full").pack()

# Experience level
experience_var = tk.StringVar(value="beginner")
tk.OptionMenu(root, experience_var, "beginner", "intermediate", "expert").pack()

# Goal time
tk.Label(root, text="Goal time (minutes)").pack()
goal_time_entry = tk.Entry(root)
goal_time_entry.pack()

# Generate button
tk.Button(root, text="Generate Plan", command=generate_plan).pack()

# Output text box
output_box = tk.Text(root, height=20, width=60)
output_box.pack()

# Start GUI
root.mainloop()