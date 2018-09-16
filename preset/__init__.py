import os

if 'PRESET_PATH' not in os.environ:
    PRESET_PATH = os.path.dirname(__file__)
else:
    PRESET_PATH = os.environ['PRESET_PATH']

def bucketData():
    return os.path.join(PRESET_PATH, "bucketData.json").replace('\\', '/')

def launchDependency():
    return os.path.join(PRESET_PATH, "launchDependency.json").replace('\\', '/')

def showDefault():
    return os.path.join(PRESET_PATH, "showDefault.json").replace('\\', '/')

def showInput():
    return os.path.join(PRESET_PATH, "showInput.json").replace('\\', '/')
