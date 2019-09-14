import argparse
import json
import os
import tempfile
import os.path



parser = argparse.ArgumentParser()
parser.add_argument("--key",default='False', nargs='?')
parser.add_argument("--val",default='False', nargs='?')
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')





def load():
	if make_data()==None:
		with open(storage_path, "r") as f:
			data_from_json = json.load(f)
		data=json.loads(data_from_json)
		if (args.key) in data:
			data[(args.key)].append(args.val)
			data_to_json=json.dumps(data)
		else:
			data[args.key]=[args.val,]
			data_to_json=json.dumps(data)
	else:
		data_to_json={}
		data_to_json[args.key]=[args.val,]
		data_to_json=json.dumps(data_to_json)
	with open(storage_path, 'w') as f:
		json.dump(data_to_json,f)



def make_data():
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	if not os.path.isfile(storage_path):
		with open(storage_path, 'w') as f:
			pass
		return True

def get(key):
	if os.path.isfile(storage_path):
		with open(storage_path, "r") as f:
			data_from_json = json.load(f)
			data=json.loads(data_from_json)
			l=(data[key])
			print(', '.join(str(x) for x in l))
	else:
		print('None')

if args.val!='False':
	load()

else:
	get(args.key)