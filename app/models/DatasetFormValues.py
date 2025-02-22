class DatasetFormValues:
    def __init__(self, dataset_name: str, dataset_description: str, dataset_data: str, dataset_type: str):
        self.dataset_name: str = dataset_name
        self.dataset_description: str = dataset_description
        self.dataset_data: str = dataset_data
        self.dataset_type: str = dataset_type
