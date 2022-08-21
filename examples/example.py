import json
from src.procx import procx

args = [
    "-driver",
    "redis-list",
    "-redis-host",
    "localhost",
    "-redis-port",
    "6379",
    "-redis-key",
    "test-redis-list",
]

out, err = procx.procx(args)
print(out)