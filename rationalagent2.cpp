#include <iostream>

// Function representing the agent's decision-making process
int rationalAgent(int environmentState)
{
    // Agent's logic for making decisions based on the environment state
    if (environmentState == 0)
    {
        return 1; // Take action 1
    }
    else
    {
        return 0; // Take action 0
    }
}

int main()
{
    // Assume the environment state is represented by an integer
    int environmentState = 0;

    // Call the rational agent function to make a decision
    int action = rationalAgent(environmentState);

    // Print the action chosen by the agent
    std::cout << "Agent chose action: " << action << std::endl;

    return 0;
}
