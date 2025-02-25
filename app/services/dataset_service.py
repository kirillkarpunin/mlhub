"""
Содержит сервисы приложения. Сервис представляет бизнес-логику приложения.
"""

from typing import List, Optional

from app.models.DatasetBrief import DatasetBrief
from app.models.DatasetCSV import DatasetCSV
from app.models.DatasetFormValues import DatasetFormValues
from app.models.DatasetInfo import DatasetInfo
from app.repository.dataset_repository import DatasetRepository


class DatasetService:
    """
    Класс-сервис для логики, связанной с датасетами.
    """

    @staticmethod
    def get_all_datasets_brief() -> List[DatasetBrief]:
        """
        Обращается к методу репозитория для получения списка Brief'ов всех датасетов в БД.
        """
        return DatasetRepository.get_all_datasets_brief()

    @staticmethod
    def get_dataset_brief(dataset_id: str) -> Optional[DatasetBrief]:
        """
        Обращается к методу репозитория для получения объекта Brief для датасета с индексом dataset_id.
        """
        return DatasetRepository.get_dataset_brief(dataset_id)

    @staticmethod
    def get_dataset(dataset_id: str) -> Optional[DatasetInfo]:
        """
        Обращается к методу репозитория для получения объекта Info для датасета с индексом dataset_id.
        """
        return DatasetRepository.get_dataset(dataset_id)

    @staticmethod
    def add_csv_dataset(form_values: DatasetFormValues) -> None:
        """
        Создает объект DatasetCSV на основе form_values.
        Обращается к методу репозитория для добавления датасета в БД.
        """
        dataset_csv: DatasetCSV = DatasetCSV(form_values)
        DatasetRepository.add_dataset(dataset_csv)
