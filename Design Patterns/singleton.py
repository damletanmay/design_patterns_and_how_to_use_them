class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("Initializing the Singleton instance")

# Test the Singleton
if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()

    print(obj1 == obj2)  # True, both variables point to the same instance
