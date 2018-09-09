import sys
import os


FILE_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(
    1, os.path.abspath(os.path.join(FILE_PATH, '..')))