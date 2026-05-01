import json

def load_json(path, env):
    with open(path, 'r+') as file:
        data = json.load(file)
        default = data.get("defaults", {})
        prod = data.get(env, {})
        print(prod)
        for k,v in prod.items():
                default[k] = v
        print(default)
        # file.seek(0)
        # file.truncate()
        # json.dump(data, file, indent=4)
        print(default)

load_json("data.json", "production" )