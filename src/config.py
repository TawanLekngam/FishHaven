import os.path as path

ASSET_DIR = path.join(path.dirname(__file__), "assets")
POND_NAME = "Doo-Pond"
WINDOW_SIZE = (1600, 900)


# redis
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DB = 0


# other pond
OTHER_POND = {
    "matrix-pond": {
        "host": "localhost",
        "port": 6379,
        "password": None,
        "db": 0
    },
}

# debug
DEBUG_MODE = True
