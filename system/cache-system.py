import time
from random import randint
from functools import wraps

# cache = {
#     "city1": {
#         "data": **weather**,
#         "time": 12312312
#     },
#     "city2": {},
#     "city3": {},
# }

cache = {}

# - introduce some cache/memory
# - before invocation, check cache

def cache_decorator(func):
  @wraps(func)
  def wrapper(city):

    if city in cache and time.time() - cache[city]['time'] < 10:
      print(f"Returning cached result for {city}...")
      return cache[city]['data']

    result = func(city)
    cache[city] = {
        "data": result,
        "time": time.time()
    }
    return result
  return wrapper


@cache_decorator
def get_weather(city):
  print(f"Fetching weather data for {city}...")
  time.sleep(1)

  weather_data = {
      'temperature': randint(0, 39),
      'humidity': randint(0, 100)
  }
  print(weather_data)

get_weather("Manila")