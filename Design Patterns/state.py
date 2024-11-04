# State Interface
class State:
    def handle(self, context):
        pass

# Concrete States
class StateA(State):
    def handle(self, context):
        print("StateA: Switching to StateB")
        context.state = StateB()

class StateB(State):
    def handle(self, context):
        print("StateB: Switching to StateA")
        context.state = StateA()

# Context Class
class Context:
    def __init__(self):
        self.state = StateA()  # Initial state

    def request(self):
        self.state.handle(self)

# Test the State Pattern
if __name__ == "__main__":
    context = Context()

    context.request()  # StateA: Switching to StateB
    context.request()  # StateB: Switching to StateA
    context.request()  # StateA: Switching to StateB
