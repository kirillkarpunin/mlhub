import pandas as pd


class VisualisationDataCSV:
    def __init__(self, df: pd.DataFrame):
        self.visualisation_data = []

        for column in df.columns:
            column_data = {
                'column_name': column
            }

            if pd.api.types.is_numeric_dtype(df[column]):
                column_data['column_type'] = 'numeric'
                column_data['column_values'] = df[column].astype(float).tolist()
            else:
                column_data['column_type'] = 'object'

                value_counts: pd.Series = df[column].value_counts()
                column_data['column_labels'] = value_counts.index.astype(str).tolist()
                column_data['column_values'] = value_counts.values.astype(int).tolist()
                column_data['column_most_freq'] = str(value_counts.idxmax())
                column_data['column_most_freq_count'] = int(value_counts.max())

            self.visualisation_data.append(column_data)

    def to_dict(self):
        return self.__dict__
