from app.models.DatasetCSV import DatasetCSV
from app.models.DatasetFormValues import DatasetFormValues
from app.repository.dataset_repository import DatasetRepository


class DatasetService:
    @staticmethod
    def get_all_datasets_brief() -> list:  # Any он может еще none вернуть
        return DatasetRepository.get_all_datasets_brief()

    @staticmethod
    def get_dataset(dataset_id) -> dict:  # Any мб none
        return DatasetRepository.get_dataset(dataset_id)

    @staticmethod
    def add_csv_dataset(form_values: DatasetFormValues) -> None:
        dataset_csv: DatasetCSV = DatasetCSV(form_values)
        DatasetRepository.add_dataset(dataset_csv)
