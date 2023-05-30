# The VacuumCleanerAgent class represents an agent that can clean dirty locations in a vacuum cleaning scenario. 
# Let's go through each method in detail:


class VacuumCleanerAgent:

    def __init__(self):
        self.location = 'A'
        self.status = {'A': 'dirty', 'B': 'dirty'}


# The __init__ method initializes the agent's initial state.
# It sets the agent's current location to 'A' and initializes the status dictionary, which represents the cleanliness status of each location.
# In this case, both locations 'A' and 'B' are initially marked as 'dirty'.

    def perceive(self):
        return self.location, self.status[self.location]


# The perceive method allows the agent to perceive its current location and the cleanliness status of that location.
# It returns a tuple containing the current location and the cleanliness status of that location.


    def clean(self):
        self.status[self.location] = 'clean'


# The clean method updates the cleanliness status of the current location to 'clean'.


    def move(self):
        if self.location == 'A':
            self.location = 'B'
        else:
            self.location = 'A'


# The move method changes the agent's current location. If the agent is at location 'A', it moves to location 'B', and vice versa.


    def simple_reflex_agent(self):
        location, status = self.perceive()
        if status == 'dirty':
            self.clean()
            return f"Location {location}:Cleaned"
        else:
            self.move()
            return f"Location {location}:Moved"


# The simple_reflex_agent method represents a simple reflex agent that decides its actions based on the current perception.
# It first perceives its current location and the cleanliness status.
# If the status is 'dirty', it cleans the location, updates the status, and returns a message indicating that the location has been cleaned.
# If the status is already 'clean', it moves to the other location and returns a message indicating that it has moved.


# Now let's test the agent with different scenarios:


agent = VacuumCleanerAgent()


# Scenario 1: Both locations are dirty


print(agent.simple_reflex_agent())  # Clean A
print(agent.simple_reflex_agent())  # Clean B


# In this scenario, both locations 'A' and 'B' are initially dirty. 
# The agent starts at location 'A' and cleans it. 
# The output of the first call to simple_reflex_agent will be "Location A: Cleaned". 
# The agent then moves to location 'B' and cleans it. The output of the second call to simple_reflex_agent will be "Location B: Cleaned".


# Scenario 2: Only location B is dirty

agent.status = {'A': 'clean', 'B': 'dirty'}


print(agent.simple_reflex_agent())  # Move to B
print(agent.simple_reflex_agent())  # Clean B


# In this scenario, only location 'B' is dirty, while location 'A' is already clean. 
# The agent starts at location 'A' and perceives that location 'A' is clean. It then moves to location 'B'. 
# The output of the first call to simple_reflex_agent will be "Location A: Moved". 
# At location 'B', the agent perceives that it is dirty and proceeds to clean it. The output of the second call to simple_reflex_agent will be "Location B: Cleaned".


# Scenario 3: Only location A is dirty


agent.status = {'A': 'dirty', 'B': 'clean'}

print(agent.simple_reflex_agent())  # Clean A
print(agent.simple_reflex_agent())  # Move to B


# In this scenario, only location 'A' is dirty, while location 'B' is already clean.
# The agent starts at location 'A' and cleans it. The output of the first call to simple_reflex_agent will be "Location A: Cleaned".
# Since location 'B' is already clean, the agent moves to location 'B'.
# The output of the second call to simple_reflex_agent will be "Location B: Moved".
