class Sensor:
    def __init__(self, environment):
        self.environment = environment

    def get_percept(self):
        # Get the current percept from the environment
        return self.environment.get_percept()


class Environment:
    def __init__(self):
        self.location_a = "Dirty"
        self.location_b = "Dirty"

    def get_percept(self):
        # Return the current percept, indicating whether the current location is dirty or not
        return self.location_a, self.location_b

    def clean_location(self, location):
        # Clean the specified location
        if location == "A":
            self.location_a = "Clean"
        elif location == "B":
            self.location_b = "Clean"


class Actuator:
    def __init__(self, environment):
        self.environment = environment

    def perform_action(self, action):
        # Perform the given action on the environment
        location, action_type = action
        if action_type == "Suck":
            self.environment.clean_location(location)


class Agent:
    def __init__(self, environment):
        self.sensor = Sensor(environment)
        self.actuator = Actuator(environment)

    def perceive(self):
        # Get the current percept from the sensor
        return self.sensor.get_percept()

    def act(self):
        # Decide and perform an action based on the percept
        location_a, location_b = self.perceive()

        if location_a == "Dirty":
            action = ("A", "Suck")
        elif location_b == "Dirty":
            action = ("B", "Suck")
        else:
            # If both locations are clean, move randomly to another location
            action = ("A" if location_a == "Clean" else "B", "Move")

        self.actuator.perform_action(action)


if __name__ == '__main__':
    # Create an environment
    environment = Environment()

    # Create a vacuum cleaner agent with the environment
    vacuum_agent = Agent(environment)

    # Agent performs an action
    vacuum_agent.act()

    # Agent perceives the updated state
    percept = vacuum_agent.perceive()
    print("Percept:", percept)
