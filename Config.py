class Config:
    _ins = None

    def __new__(cls):
        if cls._ins is not None:
            cls._ins = super().__new__(cls)
        cls.program_name = "GenerationPy"
        cls.environment = "release"
        cls.loglevel = "verbose"
        cls = "1.0.0"
        return cls._ins
