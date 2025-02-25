"""
Настраивает пути для endpoint'ов приложения. Сохраняет их в blueprint.
"""

from typing import Union

from flask import Blueprint, request, Response

from app.controllers.dataset_controller import DatasetController

bp: Blueprint = Blueprint('datasets', __name__)


@bp.route('/datasets/', methods=['GET'])
def get_datasets() -> str:
    """
    Обращается с методу контроллера для отображения страницы со всеми датасетами.
    """
    return DatasetController.render_all_datasets()


@bp.route('/datasets/add/', methods=['GET', 'POST'])
def add_dataset() -> Union[str, Response]:
    """
    Обращается к методам контроллера:
        GET - для отображения страницы для добавления датасета.
        POST - для добавления датасаета в БД. Информация о датасете содержится в передаваемом request.
    """
    if request.method == 'GET':
        return DatasetController.render_add_dataset()
    elif request.method == 'POST':
        return DatasetController.add_dataset(request)
    else:
        return DatasetController.render_error('Invalid request')


@bp.route('/datasets/edit/<dataset_id>/', methods=['GET', 'PATCH'])
def edit_dataset(dataset_id: str) -> str:
    """
    Обращается к методам контроллера:
        GET - для отображения страницы для редактирования датасета.
    """
    if request.method == 'GET':
        return DatasetController.render_edit_dataset(dataset_id)
    else:
        return DatasetController.render_error('Invalid request')


@bp.route('/datasets/<dataset_id>/', methods=['GET'])
def get_dataset(dataset_id: str) -> str:
    """
    Обращается с методу контроллера для отображения страницы с датасетом с индексом dataset_id.
    """
    return DatasetController.render_dataset(dataset_id)
