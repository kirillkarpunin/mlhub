class DatasetBrief:
    def __init__(
            self,
            dataset_id: int,
            dataset_name: str,
            dataset_description: str,
            dataset_type: str,
            dataset_size: str
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.dataset_description = dataset_description
        self.dataset_type = dataset_type
        self.dataset_size = dataset_size
