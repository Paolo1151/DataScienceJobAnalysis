import os

'''
Resource PATHS
'''
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
CONTENT_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'content')

'''
Singleton Instances
'''
from utils.render import Renderer

RENDERER = Renderer()

