class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "yellow_leaves": {
                "questions": ["Are the leaves turning yellow?", "Are there brown spots on the leaves?"],
                "result": "Your plant might have a fungal infection."
            },
            "wilting": {
                "questions": ["Are the leaves drooping?", "Is the soil too dry?"],
                "result": "Your plant is likely experiencing dehydration."
            },
        }

    def ask_question(self, question):
        response = input(question + " (yes/no): ").strip().lower()
        return response == "yes"

    def run(self):
        print("Welcome to the Plant Disease Expert System!")
        print("Answer the following questions to diagnose your plant.")
        print("----------------------------------------------")

        for symptom, data in self.knowledge_base.items():
            print("\nSymptom:", symptom)
            for question in data["questions"]:
                if self.ask_question(question):
                    continue
                else:
                    break
            else:
                print("Diagnosis:", data["result"])
                return

        print("\nSorry, we couldn't diagnose the issue based on your answers.")


if __name__ == "__main__":
    expert_system = ExpertSystem()
    expert_system.run()
