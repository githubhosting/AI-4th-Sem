#include <iostream>
#include <string>
#include <vector>

class Environment; // Forward declaration

class Sensor
{
public:
    Sensor(Environment *environment) : environment(environment) {}

    std::vector<std::string> getPercept();

private:
    Environment *environment;
};

class Actuator
{
public:
    Actuator(Environment *environment) : environment(environment) {}

    void performAction(std::pair<std::string, std::string> action);

private:
    Environment *environment;
};

class Environment
{
public:
    Environment()
    {
        locationA = "Dirty";
        locationB = "Dirty";
    }

    std::vector<std::string> getPercept()
    {
        return {locationA, locationB};
    }

    void cleanLocation(std::string location)
    {
        if (location == "A")
        {
            locationA = "Clean";
        }
        else if (location == "B")
        {
            locationB = "Clean";
        }
    }

private:
    std::string locationA;
    std::string locationB;
};

std::vector<std::string> Sensor::getPercept()
{
    return environment->getPercept();
}

void Actuator::performAction(std::pair<std::string, std::string> action)
{
    std::string location = action.first;
    std::string actionType = action.second;

    if (actionType == "Suck")
    {
        environment->cleanLocation(location);
    }
}

class Agent
{
public:
    Agent(Environment *environment) : sensor(environment), actuator(environment) {}

    std::vector<std::string> perceive()
    {
        return sensor.getPercept();
    }

    void act()
    {
        std::vector<std::string> percept = perceive();
        std::string locationA = percept[0];
        std::string locationB = percept[1];

        std::pair<std::string, std::string> action;

        if (locationA == "Dirty")
        {
            action = std::make_pair("A", "Suck");
        }
        else if (locationB == "Dirty")
        {
            action = std::make_pair("B", "Suck");
        }
        else
        {
            action = (locationA == "Clean") ? std::make_pair("A", "Move") : std::make_pair("B", "Move");
        }

        actuator.performAction(action);
    }

private:
    Sensor sensor;
    Actuator actuator;
};

int main()
{
    // Create an environment
    Environment environment;

    // Create a vacuum cleaner agent with the environment
    Agent vacuumAgent(&environment);

    // Agent performs an action
    vacuumAgent.act();

    // Agent perceives the updated state
    std::vector<std::string> percept = vacuumAgent.perceive();
    std::cout << "Percept: " << percept[0] << ", " << percept[1] << std::endl;

    return 0;
}