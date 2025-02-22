import json
from io import StringIO

import pandas as pd

from app.models.Dataset import Dataset
from app.models.DatasetFormValues import DatasetFormValues
from app.models.VisualisationDataCSV import VisualisationDataCSV


class DatasetCSV(Dataset):
    def __init__(self, form_values: DatasetFormValues):
        super().__init__(form_values)

        df: pd.DataFrame = pd.read_csv(StringIO(form_values.dataset_data))

        self.dataset_rows: int = df.shape[0]
        self.dataset_columns: int = df.shape[1]

        self.dataset_json_data: str = df.to_json(orient='records')

        self.dataset_size: float = round(len(form_values.dataset_data.encode()) / 1024, 2)

        self.visualisation_data = VisualisationDataCSV(df)

    def to_dict(self):
        return {
            'dataset_name': self.dataset_name,
            'dataset_description': self.dataset_description,
            'dataset_type': self.dataset_type,
            'dataset_rows': self.dataset_rows,
            'dataset_columns': self.dataset_columns,
            'dataset_json_data': json.loads(self.dataset_json_data),
            'dataset_size': self.dataset_size,
            'visualisation_data': self.visualisation_data.to_dict()
        }
