import json

from app.models.Dataset import Dataset

# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.json'))
# try:
#     with open(file_path, 'r', encoding='utf-8') as file:
#         db = json.load(file)  # Any
# except FileNotFoundError:
#     db = None

db = []


class DatasetRepository:
    @staticmethod
    def get_all_datasets_brief() -> list:  # Any он еще none может вернуть
        briefs: list = []
        for index, dataset_str in enumerate(db):
            dataset: dict = json.loads(dataset_str)

            brief: dict = {
                'dataset_id': index,
                'dataset_name': dataset['dataset_name'],
                'dataset_description': dataset['dataset_description'],
                'dataset_size': dataset['dataset_size']
            }
            briefs.append(brief)
        return briefs

    @staticmethod
    def get_dataset(dataset_id) -> dict:  # Any мб none
        if int(dataset_id) >= len(db):
            return None

        return json.loads(db[int(dataset_id)])


    @staticmethod
    def add_dataset(dataset: Dataset):
        db.append(json.dumps(dataset.to_dict()))
