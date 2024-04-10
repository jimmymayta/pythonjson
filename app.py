import os
import sys
import json


class Database:
    def __init__(self):
        self.filename = 'data.json'
        self.datafile()

    def datafile(self):
        if not os.path.exists(self.filename):
            file = open(self.filename, 'w', encoding='utf-8')
            file.write(json.dumps({'tasks': []}))

    def dataread(self):
        file = open(self.filename, 'r', encoding='utf-8')
        return json.loads(file.read())

    def datawrite(self, data):
        file = open(self.filename, 'w', encoding='utf-8')
        file.write(json.dumps(data))


if __name__ == "__main__":
    db = Database()

    args = sys.argv[1]

    if args == "tareas":
        data = db.dataread()
        for t in data['tasks']:
            if t['state']:
                print(f"{t['id']}: {t['task']}")
    elif args == "nuevo":
        task = sys.argv[2]
        data = db.dataread()
        data['tasks'].append({
            'id': len(data['tasks'])+1,
            'task': task,
            'state': True
        })
        db.datawrite(data)
    elif args == "eliminar":
        number = int(sys.argv[2])
        data = db.dataread()

        for t in data['tasks']:
            if t['id'] == number:
                t['state'] = False

        db.datawrite(data)
