"""
Структура для хранения данных датасета.
"""

from abc import abstractmethod, ABC

from app.models.DatasetFormValues import DatasetFormValues


class Dataset(ABC):
    """
    Класс для хранения данных датасета.
    Наследуется от ABC для того, чтобы можно было сделать @abstractmethod.
    """

    def __init__(self, form_values: DatasetFormValues):
        self.dataset_name: str = form_values.dataset_name
        self.dataset_description: str = form_values.dataset_description
        self.dataset_type: str = form_values.dataset_type

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Метод для представления объекта класса в виде словаря.
        """
        pass
