class Singleton(object):
    """
    Singleton base class keeps track of all singleton instances in a dictionary where keys are class references and values are instance references.
    In this way, Singleton class can be created many times.
    Insteasd
    """
    _instances = {} # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        #Check if class exists in a dictionary
        if cls not in cls._instances:
            # If not new Singleton class is created first and only time
            instance = super().__new__(cls)
            # Adds class to the dictionary
            cls._instances[cls] = instance
        return cls._instances[cls]
