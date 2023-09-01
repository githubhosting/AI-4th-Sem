class KnowledgeBasedAgent:
    def __init__(self):
        self.knowledge_base = set()

    def add_statement(self, statement):
        self.knowledge_base.add(statement)

    def query(self, statement):
        return statement in self.knowledge_base

    def display_knowledge_base(self):
        print("Knowledge Base:")
        for statement in self.knowledge_base:
            print("-", statement)


# Creating an instance of the KnowledgeBasedAgent
agent = KnowledgeBasedAgent()

# Adding statements to the knowledge base
agent.add_statement("The sky is blue.")
agent.add_statement("Water boils at 100 degrees Celsius.")
agent.add_statement("Cats are mammals.")

# Querying the knowledge base
print("Query Results:")
print("The sky is blue.", agent.query("The sky is blue."))  # Output: True
print("Water is pink.", agent.query("Water is pink."))    # Output: False
print("Cats are mammals.", agent.query("Cats are mammals."))  # Output: True

# Displaying the entire knowledge base
agent.display_knowledge_base()
