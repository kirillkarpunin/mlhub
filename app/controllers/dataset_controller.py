from flask import render_template, Request, Response, make_response

from app.models.DatasetFormValues import DatasetFormValues
from app.services.dataset_service import DatasetService


class DatasetController:
    @staticmethod
    def render_all_datasets() -> str:
        all_datasets_brief: list = DatasetService.get_all_datasets_brief()
        if all_datasets_brief is not None:
            return render_template('all_datasets.html', datasets_brief=all_datasets_brief)
        else:
            return '404'

    @staticmethod
    def render_dataset(dataset_id) -> str:
        dataset: dict = DatasetService.get_dataset(dataset_id)
        if dataset is not None:
            return render_template('one_dataset.html', dataset=dataset)
        else:
            return '404'

    @staticmethod
    def render_add_dataset() -> str:
        return render_template('dataset_properties.html')

    @staticmethod
    def add_dataset(request: Request) -> Response:
        form_data: dict = request.get_json()  # или это не dict, я не ебу если честно :(((((

        dataset_name: str = form_data['dataset-name']
        dataset_description: str = form_data['dataset-description']
        dataset_data: str = form_data['dataset-data']
        dataset_type: str = form_data['dataset-type']

        form_values: DatasetFormValues = DatasetFormValues(dataset_name, dataset_description, dataset_data,
                                                           dataset_type)

        match dataset_type:
            case 'csv':
                DatasetService.add_csv_dataset(form_values)

        response: Response = make_response()
        response.headers['redirect'] = '/datasets/'

        return response
