import os


class Config:
    DEBUG = False
    TESTING = False
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", 5))
    RESTCOUNTRIES_URL = os.getenv(
        "RESTCOUNTRIES_URL",
        "https://restcountries.com/v3.1/name"
    )


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
