import os
import pytest
import shutil
import zipfile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
ROOT = os.path.dirname(CURRENT_DIRECTORY)
RESOURCE_DIR = os.path.join(ROOT, 'resource')
TEMP_DIR = os.path.join(ROOT, 'temp')
ZIP_FILE = os.path.join(RESOURCE_DIR, 'files.zip')


@pytest.fixture(scope="session", autouse=True)
def create_zip_and_add_files():
    # Создаём папку resource, если она еще не существует
    if not os.path.exists(RESOURCE_DIR):
        os.makedirs(RESOURCE_DIR)

    # Создаём архив files.zip в папке resource и добавляем туда файлы из temp
    with zipfile.ZipFile(os.path.join(RESOURCE_DIR, 'files.zip'), 'w') as zf:
        for file in os.listdir(TEMP_DIR):
            add_file = os.path.join(TEMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield

    # После завершения тестов удаляем созданную директорию
    shutil.rmtree(RESOURCE_DIR)
