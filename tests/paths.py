import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
ROOT = os.path.dirname(CURRENT_DIRECTORY)
RESOURCE_DIR = os.path.join(ROOT, 'resource')
TEMP_DIR = os.path.join(ROOT, 'temp')
ZIP_FILE = os.path.join(RESOURCE_DIR, 'files.zip')