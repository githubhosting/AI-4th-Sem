import unittest
from simple_agent import Environment, Agent


class TestSimpleAgent(unittest.TestCase):
    def test_environment(self):
        # Test if the environment is initialized correctly
        env = Environment()
        self.assertEqual(env.get_percept(), ("Dirty", "Dirty"))

        # Test if cleaning a location works correctly
        env.clean_location("A")
        self.assertEqual(env.get_percept(), ("Clean", "Dirty"))

    def test_agent(self):
        # Test if the agent can clean a dirty location
        env = Environment()
        agent = Agent(env)
        self.assertEqual(env.get_percept(), ("Dirty", "Dirty"))
        agent.act()
        self.assertEqual(env.get_percept(), ("Clean", "Dirty"))

        # Test if the agent can move to a different location
        env.clean_location("B")
        self.assertEqual(env.get_percept(), ("Clean", "Clean"))
        agent.act()
        self.assertIn(env.get_percept(), [("Clean", "Dirty"), ("Dirty", "Clean")])