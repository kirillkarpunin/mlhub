import json
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.json'))
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        db = json.load(file)  # Any
except FileNotFoundError:
    db = None


class DatasetRepository:
    @staticmethod
    def get_all_datasets_brief() -> list:  # Any он еще none может вернуть
        briefs: list = []
        for dataset in db:
            brief: dict = {
                'dataset_id': dataset['dataset_id'],
                'dataset_name': dataset['dataset_name'],
                'dataset_description': dataset['dataset_description'],
                'dataset_size': dataset['dataset_size']
            }
            briefs.append(brief)
        return briefs

    @staticmethod
    def get_dataset(dataset_id) -> dict: # Any мб none
        for dataset in db:
            if dataset['dataset_id'] == dataset_id:
                return dataset

        return None