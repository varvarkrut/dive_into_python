import json
import functools
def to_json(func):
	@functools.wraps(func)
	def wrapped(*args,**kwargs):
		data=func(*args,**kwargs)
		data_to_json=json.dumps(data)
		return data_to_json
	return wrapped


@to_json
def get_data():
  return {
    'data': 42
    }
get_data()  # вернёт '{"data": 42}'
