from os.path import dirname, abspath, join


PATH = {
    "root": dirname(dirname(abspath(__file__))),
    "assets": join(dirname(dirname(abspath(__file__))), "assets"),
}

REDIS = {
    "host": 'localhost',
    "port": 6379,
    "db": 0,
    "password": ""
}

if __name__ == "__main__":
    print(PATH["assets"])
