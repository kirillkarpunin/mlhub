"""
Структура для хранения информации о датасете.
"""

from typing import List

from app.models.VisualisationDataCSV import VisualisationDataCSV


class DatasetInfo:
    """
    Структура для хранения информации о датасете.
    """

    def __init__(
            self,
            dataset_id: str,
            dataset_name: str,
            dataset_description: str,
            dataset_type: str,
            dataset_size: str,
            dataset_columns: str,
            dataset_rows: str,
            visualisation_data: List[VisualisationDataCSV]
    ):
        self.dataset_id: str = dataset_id
        self.dataset_name: str = dataset_name
        self.dataset_description: str = dataset_description
        self.dataset_type: str = dataset_type
        self.dataset_size: str = dataset_size
        self.dataset_columns: str = dataset_columns
        self.dataset_rows: str = dataset_rows
        self.visualisation_data: List[VisualisationDataCSV] = visualisation_data
