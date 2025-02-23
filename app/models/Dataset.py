from app.models.DatasetFormValues import DatasetFormValues


class Dataset:
    def __init__(self, form_values: DatasetFormValues):
        self.dataset_name: str = form_values.dataset_name

        self.dataset_description: str = form_values.dataset_description if form_values.dataset_description != '' else '(пусто)'
        self.dataset_type: str = form_values.dataset_type

    def to_dict(self):
        pass
