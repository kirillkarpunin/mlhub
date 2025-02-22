class DatasetInfo:
    def __init__(
            self,
            dataset_id: int,
            dataset_name: str,
            dataset_description: str,
            dataset_type: str,
            dataset_size: str,
            dataset_columns: str,
            dataset_rows: str,
            visualisation_data: list
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.dataset_description = dataset_description
        self.dataset_type = dataset_type
        self.dataset_size = dataset_size
        self.dataset_columns = dataset_columns
        self.dataset_rows = dataset_rows
        self.visualisation_data = visualisation_data
