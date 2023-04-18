class MonoState(object):
    """
    Monostate contains a dictionary containing the single state for all instances
    """
    _state = {}

    def __new__(cls, *args, **kwargs):
        self = super().__new__()
        # Instance's dict object where an instance's state is stored in redirected to the
        # single state dictionary maintaned at the class level
        # No matter how many new instances you crate - they all share the same state
        self.__dict__ = cls._state
        return self