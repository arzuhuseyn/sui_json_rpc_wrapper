class Method:
    METHOD_NAME: str
    REQUIRED_PARAMS: list[str]

    def __init__(self):
        if not getattr(self, "METHOD_NAME", None):
            raise ValueError(f"Method name for `{self.__class__.__name__}` not set.")
