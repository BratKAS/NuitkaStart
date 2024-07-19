import importlib.util
import sys
from pathlib import Path

module_name = 'main_with_my_module' # Название модуля без изменений
file_path = Path('./pyinstaller --onefile --add-binary "main.cp312-win_amd64.pyd;."') # А вот имя файла изменено

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)