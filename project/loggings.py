import logging


# Создаем или получаем новый логгер
logger_api = logging.getLogger("logger_api")
# logging.basicConfig(filename='api.log', encoding='utf-8', level=logging.WARNING)
# Cоздаем ему обработчик
api_logger_handler = logging.FileHandler(filename="../api.log", encoding="utf-8")

# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# Применяем форматирование к обработчику
api_logger_handler.setFormatter(formatter_one)
# Добавлякем обработчик к журналу
logger_api.addHandler(api_logger_handler)
