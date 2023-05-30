// Rational Agent without sensors Code in c++

#include <iostream>
#include <vector>
#include <tuple>

class SimpleRationalAgent
{
public:
    SimpleRationalAgent() : performance_measure(0) {}

    void clean()
    {
        performance_measure += 1;
    }

    std::string act(std::tuple<std::pair<int, int>, std::string> percept)
    {
        auto location = std::get<0>(percept);
        auto status = std::get<1>(percept);
        if (status == "dirty")
        {
            clean();
            return "clean";
        }
        else
        {
            return "noop";
        }
    }

    int get_performance_measure() const
    {
        return performance_measure;
    }

private:
    int performance_measure;
};

int main()
{
    SimpleRationalAgent agent;

    // Assuming the environment provides percepts
    std::vector<std::tuple<std::pair<int, int>, std::string>> percepts = {
        std::make_tuple(std::make_pair(0, 0), "dirty"),
        std::make_tuple(std::make_pair(0, 1), "clean"),
        std::make_tuple(std::make_pair(1, 0), "dirty"),
        std::make_tuple(std::make_pair(1, 0), "clean")};

    for (const auto &percept : percepts)
    {
        std::string action = agent.act(percept);
        std::cout << "Agent's action: " << action << std::endl;
        std::cout << "Performance measure: " << agent.get_performance_measure() << std::endl;
        std::cout << std::endl;
    }

    return 0;
}