from flask import Blueprint, request

from app.controllers.dataset_controller import DatasetController

bp: Blueprint = Blueprint('datasets', __name__)


@bp.route('/datasets/', methods=['GET'])
def get_datasets() -> str:  # Any надо потом сделать
    return DatasetController.render_all_datasets()


@bp.route('/datasets/add/', methods=['GET', 'POST'])
def add_dataset() -> str:  # Any
    if request.method == 'GET':
        return DatasetController.render_add_dataset()
    elif request.method == 'POST':
        return DatasetController.add_dataset(request)


@bp.route('/datasets/<dataset_id>/', methods=['GET'])
def get_dataset(dataset_id) -> str:  # Any надо потом сделать
    return DatasetController.render_dataset(dataset_id)
