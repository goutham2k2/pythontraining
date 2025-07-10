#fileutils.py

def write_to_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def read_from_file(path):
    with open(path, 'r') as f:
        return f.read()
