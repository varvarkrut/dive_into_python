import argparse
import json
import os
import tempfile
import os.path
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
'''
To input value write request  according form:
python3 storage.py --key [key] --value [value]
to get value write request:
python3 storage.py --key [key]
example:
python3 storage.py --key 1 --value 1
python3 storage.py --key 1
'''

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", default='False', nargs='?')
    parser.add_argument("--val", default='False', nargs='?')
    args = parser.parse_args()
    return args


def load(args):
    if make_data() == None:
        with open(storage_path, "r") as f:
            data_from_json = json.load(f)
        data = json.loads(data_from_json)
        if (args.key) in data:
            data[(args.key)].append(args.val)
            data_to_json = json.dumps(data)
        else:
            data[args.key] = [args.val, ]
            data_to_json = json.dumps(data)
    else:
        data_to_json = {}
        data_to_json[args.key] = [args.val, ]
        data_to_json = json.dumps(data_to_json)
    with open(storage_path, 'w') as f:
        json.dump(data_to_json, f)


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
            data = json.loads(data_from_json)
            l = (data[key])
            print(', '.join(str(x) for x in l))
    else:
        print('None')


if __name__ == "__main__":
    args = argparser()
    if args.val != 'False':
        load(args)

    else:
        get(args.key)

