# Simple Reflex Agent:
# A simple reflex agent makes decisions based solely on the current percept (input) without considering the history or future consequences.

class SimpleReflexAgent:
    def __init__(self):
        self.rules = {
            'dirty': self.clean,
            'clean': self.no_op
        }

    def decide(self, percept):
        state = percept['current_state']
        action = self.rules[state]()
        return action

    def clean(self):
        return 'Suck'

    def no_op(self):
        return 'NoOp'


percept = {'current_state': 'dirty'}
agent = SimpleReflexAgent()
action = agent.decide(percept)
print(action)

# Model-Based Agent:
# A model-based agent maintains an internal model of the world and uses it to make decisions based on a sequence of percepts.


class ModelBasedAgent:
    def __init__(self):
        self.model = {'A': 'dirty', 'B': 'dirty'}

    def decide(self, percept):
        self.update_model(percept)
        action = self.choose_action()
        return action

    def update_model(self, percept):
        location = percept['location']
        state = percept['current_state']
        self.model[location] = state

    def choose_action(self):
        if 'dirty' in self.model.values():
            return 'Suck'
        else:
            return 'NoOp'


percept = {'location': 'A', 'current_state': 'dirty'}
agent = ModelBasedAgent()
action = agent.decide(percept)
print(action)

# Goal-Based Agent:
# A goal-based agent maintains a set of goals and strives to achieve them by selecting actions that move it closer to the desired state.


class GoalBasedAgent:
    def __init__(self, goals):
        self.goals = goals

    def decide(self, percept):
        self.update_state(percept)
        action = self.select_action()
        return action

    def update_state(self, percept):
        pass  # Update the agent's internal state based on percept

    def select_action(self):
        if self.goals_achieved():
            return 'NoOp'
        else:
            return self.choose_next_action()

    def goals_achieved(self):
        return all(goal in self.state for goal in self.goals)

    def choose_next_action(self):
        pass  # Choose an action to work towards achieving the goals


goals = ['clean_A', 'clean_B']
percept = {'state': ['clean_A']}
agent = GoalBasedAgent(goals)
action = agent.decide(percept)
print(action)

# Utility-Based Agent:
# A utility-based agent makes decisions based on the expected utility of different actions, considering both the current state and potential future outcomes.


class UtilityBasedAgent:
    def __init__(self, utility_function):
        self.utility_function = utility_function

    def decide(self, percept):
        action = self.choose_best_action(percept)
        return action

    def choose_best_action(self, percept):
        actions = self.get_possible_actions(percept)
        best_action = max(
            actions, key=lambda a: self.expected_utility(a, percept))
        return best_action

    def get_possible_actions(self, percept):
        pass  # Return a list of possible actions based on the percept

    def expected_utility(self, action, percept):
        pass  # Calculate the expected utility of an action based on the utility function and potential outcomes


def utility_function(action, percept):
    pass  # Define a utility function based on the action and percept


percept = {'state': 'clean'}
agent = UtilityBasedAgent(utility_function)
action = agent.decide(percept)
print(action)
