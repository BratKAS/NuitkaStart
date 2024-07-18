import importlib.util
import sys
from pathlib import Path

module_name = 'main' # Название модуля без изменений
file_path = Path('./main.cpython-312-darwin.so') # А вот имя файла изменено

spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)