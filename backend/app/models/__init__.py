import importlib
import inspect
from pathlib import Path

from core.base import Base

# Получаем путь к текущей папке и имя пакета
current_dir = Path(__file__).parent
package_name = __name__

# Ищем все файлы *.py, кроме __init__.py
module_files = [
    f.stem for f in current_dir.glob("*.py")
    if f.name != "__init__.py"
]

# Динамически импортируем и добавляем классы в глобальное пространство
for module_name in module_files:
    module = importlib.import_module(f".{module_name}", package=package_name)
    for name, obj in vars(module).items():
        if (
            inspect.isclass(obj)
            and issubclass(obj, Base)
            and obj is not Base
        ):
            globals()[name] = obj
