"""
Содержит контроллеры приложения. Контроллер является связным звеном между запросами с клиента и бизнес-логикой.
"""

from typing import List
from typing import Optional

from flask import render_template, Request, Response, make_response

from app.models.DatasetBrief import DatasetBrief
from app.models.DatasetFormValues import DatasetFormValues
from app.models.DatasetInfo import DatasetInfo
from app.services.dataset_service import DatasetService


class DatasetController:
    """
    Класс-контроллер для запросов, связанных с датасетами.
    """

    @staticmethod
    def render_all_datasets() -> str:
        """
        Обращается к методу сервиса для получения списка Brief'ов всех датасетов в БД. Отображает страницу с полученными датасетами.
        """
        all_datasets_brief: List[DatasetBrief] = DatasetService.get_all_datasets_brief()
        return render_template('all_datasets.html', datasets_brief=all_datasets_brief)

    @staticmethod
    def render_dataset(dataset_id: str) -> str:
        """
        Обращается к методу сервиса для получения объекта Info для датасета с индексом dataset_id.
        Если такой датасет есть - отображает страницу с полученным датасетом,
        иначе - отображает страницу с ошибкой с соответствующим сообщением.
        """
        dataset_info: Optional[DatasetInfo] = DatasetService.get_dataset(dataset_id)
        if dataset_info is not None:
            return render_template('one_dataset.html', dataset_info=dataset_info)
        else:
            return DatasetController.render_error(f'No dataset with id \'{dataset_id}\'')

    @staticmethod
    def render_add_dataset() -> str:
        """
        Отображает страницу добавления датасета.
        """
        return render_template('dataset_properties.html')

    @staticmethod
    def add_dataset(request: Request) -> Response:
        """
        Обращается к методу сервиса для добавления датасета в БД.
        Данные о датасете достаются из request, из них создается объект DatasetFormData.
        В зависимости от типа добавляемого датасета вызывается соответствующий метод сервиса.
        Метод возвращает response, содержащий URL страницы, открываемой после добавления.
        """
        form_data: dict = request.get_json()

        dataset_name: str = form_data['dataset-name']
        dataset_description: str = form_data['dataset-description']
        dataset_data: str = form_data['dataset-data']
        dataset_type: str = form_data['dataset-type']

        form_values: DatasetFormValues = DatasetFormValues(dataset_name, dataset_description, dataset_data,
                                                           dataset_type)

        match dataset_type:
            case 'CSV':
                DatasetService.add_csv_dataset(form_values)

        response: Response = make_response()
        response.headers['redirect'] = '/datasets/'

        return response

    @staticmethod
    def render_edit_dataset(dataset_id: str) -> str:
        """
        Обращается к методу сервиса для получения объекта Brief для датасета с индексом dataset_id.
        """
        dataset_brief: DatasetBrief = DatasetService.get_dataset_brief(dataset_id)
        return render_template('dataset_properties.html', dataset_brief=dataset_brief)

    @staticmethod
    def render_error(error_message) -> str:
        """
        Отображает страницу ошибки с сообщением error_message
        """
        return render_template('error.html', error_message=error_message)
