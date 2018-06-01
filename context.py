dependencies = {}

def set_dependency(name, dependency):
    dependencies[name] = dependency

def get_dependency(name):
    return dependencies.get(name)
