"""
Структура для хранения данных для визуализации датасета.
"""
import pandas as pd


class VisualisationDataCSV:
    """
    Структура для хранения данных для визуализации датасета.
    """
    def __init__(self, df: pd.DataFrame):
        self.data: list = []

        for column in df.columns:
            column_data = {
                'column_name': column
            }

            if pd.api.types.is_numeric_dtype(df[column]):
                column_data['column_type'] = 'numeric'
                column_data['column_values'] = df[column].astype(str).tolist()
            else:
                column_data['column_type'] = 'object'
                column_data['column_values'] = df[column].astype(str).tolist()

                value_counts: pd.Series = df[column].value_counts()
                # column_data['column_labels'] = value_counts.index.astype(str).tolist()
                # column_data['column_values'] = value_counts.values.astype(int).tolist()

                column_data['column_most_common'] = str(value_counts.idxmax())
                column_data['column_most_common_count'] = str(value_counts.max())

            self.data.append(column_data)

    def to_dict(self) -> dict:
        """
        Метод для представления объекта класса в виде словаря.
        """
        return self.__dict__
