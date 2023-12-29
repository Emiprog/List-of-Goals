# Create global variable.
last_id = 0


class Goal:
    """Represent an objective with deadline, status and numeration."""

    def __init__(self, objective: str, deadline: str, status: str = 'active'):
        """Initialize objective, deadline, status and id."""
        self.objective = objective
        self.deadline = deadline
        self.status = status
        global last_id
        last_id += 1
        self.id = last_id

    # def __str__(self):
    #     if self.deadline:
    #         return f"Objective: {self.objective}. Time left: {self.deadline}."


class GoalsList:
    """
    Represent a list of goals with adding, deleting and modifying the goals.
    """
    def __init__(self):
        """Initialize a list of goals."""
        self.objectives = []

    def add_goal(self, objective: str, deadline: str, status: str):
        """Add goal to the list of goals."""
        self.objectives.append(Goal(objective, deadline, status))

    def remove_goal(self, goal_id):
        """Remove the goal from the list of goals."""
        goal = self._find_goal(goal_id)
        if goal:
            self.objectives.remove(goal)
            self._update_id()
            return
        print("The goal not found to be deleted.")

    def _update_id(self):
        """Update the IDs of goals to ensure a contiguous sequence."""
        for index, goal in enumerate(self.objectives, start=1):
            goal.id = index

    def _find_goal(self, goal_id: str):
        """Check if the goal is in list by its index."""
        try:
            goal = self.objectives[int(goal_id) - 1]
            return goal
        except IndexError:
            return None

    def modify_objective(self, goal_id: str, objective: str):
        """Modify the objective of the goal."""
        goal = self._find_goal(goal_id)
        if goal:
            goal.objective = objective
            return True
        return False

    def modify_deadline(self, goal_id: str, deadline: str):
        """Modify the deadline of the goal."""
        goal = self._find_goal(goal_id)
        if goal:
            goal.deadline = deadline
            return True
        return False

    def modify_status(self, goal_id: str, status: str):
        """Modify the status of the goal."""
        goal = self._find_goal(goal_id)
        if goal:
            goal.status = status
            return True
        return False


