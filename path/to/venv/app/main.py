from flask import Blueprint
from controller.user import index, create

blueprint = Blueprint('blueprint',__name__)
blueprint.route('/user', methods=['GET'])(index)
blueprint.route('/user', methods=['POST'])(create)