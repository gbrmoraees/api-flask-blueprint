from flask import Blueprint
from controller.user import listarTodosUsuario, salvarUsuario, listarApenasUmUsuario, atualizarUmUsuario, removerUmUsuario, login

# Criação de um Blueprint para agrupar rotas relacionadas a usuários
blueprint = Blueprint('blueprint', __name__)

# Rota para listar todos os usuários
# Método: GET
# Endpoint: /usuarios
blueprint.route('/usuarios', methods=['GET'])(listarTodosUsuario)

# Rota para criar um novo usuário
# Método: POST
# Endpoint: /usuario
blueprint.route('/usuario', methods=['POST'])(salvarUsuario)

# Rota para listar um único usuário pelo ID
# Método: GET
# Endpoint: /usuario/<int:id>
blueprint.route('/usuario/<int:id>', methods=['GET'])(listarApenasUmUsuario)

# Rota para atualizar um usuário existente pelo ID
# Método: PUT
# Endpoint: /usuario/<int:id>
blueprint.route('/usuario/<int:id>', methods=['PUT'])(atualizarUmUsuario)

# Rota para remover um usuário pelo ID
# Método: DELETE
# Endpoint: /usuario/<int:id>
blueprint.route('/usuario/<int:id>', methods=['DELETE'])(removerUmUsuario)

# Rota para autenticação de usuário (login)
# Método: POST
# Endpoint: /login
blueprint.route('/login', methods=['POST'])(login)
