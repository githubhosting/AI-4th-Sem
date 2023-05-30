class VacuumCleanerAgent:
    def __init__(self):
        self.location = 'A'
        self.status = {'A': 'dirty', 'B': 'dirty'}

    def perceive(self):
        return self.location, self.status[self.location]

    def clean(self):
        self.status[self.location] = 'clean'

    def move(self):
        if self.location == 'A':
            self.location = 'B'
        else:
            self.location = 'A'

    def simple_reflex_agent(self):
        location, status = self.perceive()
        if status == 'dirty':
            self.clean()
            return f"Location {location}: Cleaned"
        else:
            self.move()
            return f"Location {location}: Moved"


# Test the agent
agent = VacuumCleanerAgent()

# Scenario 1: Both locations are dirty
print(agent.simple_reflex_agent())  # Clean A
print(agent.simple_reflex_agent())  # Clean B

# Scenario 2: Only location B is dirty
agent.status = {'A': 'clean', 'B': 'dirty'}
print(agent.simple_reflex_agent())  # Move to B
print(agent.simple_reflex_agent())  # Clean B

# Scenario 3: Only location A is dirty
agent.status = {'A': 'dirty', 'B': 'clean'}
print(agent.simple_reflex_agent())  # Clean A
print(agent.simple_reflex_agent())  # Move to B
