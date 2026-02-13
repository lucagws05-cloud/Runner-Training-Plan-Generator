TRAINING PROGRAM

class TrainingProgram:
    def run(self):
        runner = self.create_runner()
        goal = self.choose_goal()
        generator = self.select_generator(runner)
        plan = generator.generate_plan(runner, goal)
        self.display_plan(plan)
