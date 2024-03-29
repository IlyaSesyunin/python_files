import os
import pytest
import shutil
import zipfile

from tests.paths import RESOURCE_DIR
from tests.paths import TEMP_DIR

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
