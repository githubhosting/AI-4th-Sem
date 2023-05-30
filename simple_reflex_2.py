class VacuumCleanerAgent:
    def __init__(self):
        self.location = "A"  # Initial location of the vacuum cleaner

    def interpret_input(self, percept):
        location, status = percept
        if status == "dirty":
            return "clean"
        elif status == "clean":
            return "move"
        return None

    def rule_match(self, state, rules):
        for rule in rules:
            if rule["state"] == state:
                return rule["action"]
        return None

    def action(self):
        rule_set = [
            {"state": "A_dirty", "action": "suck"},
            {"state": "B_dirty", "action": "suck"},
            {"state": "A_clean", "action": "move"},
            {"state": "B_clean", "action": "move"},
        ]
        current_state = self.location + "_" + \
            self.get_status(self.location)  # type: ignore
        return self.rule_match(current_state, rule_set)

    def run(self):
        iterations = 0
        while not self.is_environment_clean() and iterations < 20:
            iterations += 1
            percept = self.get_percept()
            action = self.interpret_input(percept)
            self.perform_action(action)

    def get_percept(self):
        # Get the current percept from the environment
        location = self.location
        status = self.get_status(location)
        return location, status

    def get_status(self, location):
        # Get the status (dirty or clean) of the current location
        # You can implement the logic to check the status in your environment
        if location == "A":
            return "dirty" if self.is_location_a_dirty() else "clean"
        elif location == "B":
            return "dirty" if self.is_location_b_dirty() else "clean"

    def is_location_a_dirty(self):
        # Check if location A is dirty
        # Implement the logic to check the dirtiness status in your environment
        # For example:
        # Assume the vacuum cleaner is in location A and it is dirty
        return self.location == "A" and self.location == "dirty"

    def is_location_b_dirty(self):
        # Check if location B is dirty
        # Implement the logic to check the dirtiness status in your environment
        # For example:
        # Assume the vacuum cleaner is in location B and it is dirty
        return self.location == "B" and self.location == "dirty"

    def perform_action(self, action):
        # Perform the specified action
        if action == "clean":
            self.clean()
        elif action == "move":
            self.move()
        elif action == "suck":
            self.suck()

    def clean(self):
        # Clean the current location
        print("Cleaning the current location:", self.location)

    def move(self):
        # Move the vacuum cleaner to the other location
        if self.location == "A":
            self.location = "B"
        elif self.location == "B":
            self.location = "A"
        print("Moving to location:", self.location)

    def suck(self):
        # Suck up the dirt at the current location
        print("Sucking up dirt at location:", self.location)

    def is_environment_clean(self):
        # Check if both locations are clean
        return self.is_location_a_clean() and self.is_location_b_clean()

    def is_location_a_clean(self):
        # Check if location A is clean
        # Implement the logic to check the cleanliness status in your environment
        # For example:
        # Assume the vacuum cleaner is in location A and it is clean
        return self.location == "A" and self.location == "clean"

    def is_location_b_clean(self):
        # Check if location B is clean
        # Implement the logic to check the cleanliness status in your environment
        # For example:
        # Assume the vacuum cleaner is in location B and it is clean
        return self.location == "B" and self.location == "clean"


# Usage
agent = VacuumCleanerAgent()
agent.run()
