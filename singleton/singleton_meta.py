class Singleton(type):
    _instances = {}  # dict([cls, instance])

    def __call__(cls, *args, **kwargs):
        # Check if class exists in a dictionary
        if cls not in cls._instances:
            # If not new Singleton class is created first and only time
            instance = super().__call__(*args, **kwargs)
            # Adds class to the dictionary
            cls._instances[cls] = instance
        return cls._instances[cls]
