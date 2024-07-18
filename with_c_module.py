import ctypes
import random

random_array = [random.randint(1, 100) for _ in range(1000)]

# Загрузка модуля на C
mymodule = ctypes.CDLL('./example.so')

mymodule.run_module()
