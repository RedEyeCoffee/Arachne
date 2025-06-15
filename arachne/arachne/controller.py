from typing import Any


class SpiderController:

    def get_spider(self, spider_name: str) -> Any:
        """Заглушка фабрики пауков"""
        print(f"[DEBUG] Запрошен паук: {spider_name}")
        return None

    def run_spider(self, spider_name: str, **kwargs) -> None:
        """Заглушка запуска паука"""
        print(f"[DEBUG] Запуск паука {spider_name} с аргументами: {kwargs}")
