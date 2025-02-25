"""
Структура для хранения краткой информации о датасете.
"""


class DatasetBrief:
    """
    Класс для хранения краткой информации о датасете.
    """

    def __init__(
            self,
            dataset_id: str,
            dataset_name: str,
            dataset_description: str,
            dataset_type: str,
            dataset_size: str
    ):
        self.dataset_id: str = dataset_id
        self.dataset_name: str = dataset_name
        self.dataset_description: str = dataset_description
        self.dataset_type: str = dataset_type
        self.dataset_size: str = dataset_size
