class DevConfig:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@localhost:5432/lavacar_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True