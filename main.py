import sys
import datetime
from goal import GoalsList



class Main:
    """Display a functionality and respond to choices when run."""

    def __init__(self):
        self.goal_list = GoalsList()
        self.choices = {
            '1': self.show_goals,
            '2': self.add_goal,
            '3': self.remove_goal,
            '4': self.modify_objective,
            '5': self.modify_deadline,
            '6': self.modify_status,
            '7': self.quit
        }

    def display(self):
        print(
            """
             List of Goals options:

            1. Show all goals
            2. Add goal
            3. Remove goal
            4. Modify objective
            5. Modify deadline
            6. Modify status
            7. Quit
            """
        )

    def run(self):
        while True:
            self.display()
            choice = input("Choose the option: ")
            if choice in self.choices:
                self.choices.get(choice)
            else:
                print("Choose a valid option.")

    def show_goals(self):
        for goal in self.goal_list.objectives:
            return "Number: {} | Objective: {} | Deadline: {}".format(goal.id, goal.objective, goal.status)

    def add_goal(self):
        objective = input("Enter your objective: ")
        deadline = input("Enter the deadline date (YYYY-MM-DD HH:MM:SS): ")
        try:
            ends = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
            time_now = datetime.datetime.now()
            time_difference = ends - time_now
            self.goal_list.objectives.append((objective, time_difference))
            print(f"Your new objective: {objective} with time to left: {time_difference}")
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.")

    def remove_goal(self):
        goal_id = input("Enter goal id: ")
        self.goal_list.remove_goal(goal_id)
        print(f"Removed goal nr {goal_id}")

    def modify_objective(self):
        goal_id = input("Enter the goal id you want to change the objective: ")
        new_objective = input("Enter new objective: ")
        self.goal_list.modify_objective(goal_id, new_objective)
        print(f"Modified goal nr {goal_id} with new objective: {new_objective}.")

    def modify_deadline(self):
        goal_id = input("Enter the goal id you want to change the objective: ")
        new_deadline = input("Enter new deadline: ")
        try:
            ends = datetime.datetime.strptime(new_deadline, '%Y-%m-%d %H:%M:%S')
            time_now = datetime.datetime.now()
            time_difference = ends - time_now
            self.goal_list.modify_deadline(time_difference)
            print(f"Modified goal nr {goal_id} with new deadline: {time_difference}.")
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM:SS.")

    def modify_status(self):
        goal_id = input("Enter the goal id you want to change the objective: ")
        new_status = input("Change the status of the goal: active/ inactive ")
        if new_status == "active":
            self.goal_list.modify_status(goal_id, 'active')
        else:
            self.goal_list.modify_status(goal_id, 'inactive')
        print(f"Modified goal nr {goal_id} with new status: {new_status}.")

    def quit(self):
        print("Thanks for using this app.")
        sys.exit()


if __name__ == "__main__":
    Main().run()
