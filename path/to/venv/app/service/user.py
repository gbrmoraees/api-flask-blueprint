from model.user import listagemTodosUsuarios, salvarUsuario, listarApenasUmUsuario, atualizarUmUsuario, removerUmUsuario, login

def listagemTodosUsuariosService():    
    """
    Serviço para obter a lista de todos os usuários.
    
    Retorna:
    - Resultado da função `listagemTodosUsuarios()` do modelo.
    """
    return listagemTodosUsuarios()

def salvarUserService(usuario):    
    """
    Serviço para salvar um novo usuário.
    
    Argumentos:
    - usuario: Dados do usuário a serem salvos (espera-se que seja um dicionário com os detalhes do usuário).
    
    Retorna:
    - Resultado da função `salvarUsuario(usuario)` do modelo.
    """
    return salvarUsuario(usuario)   

def listarApenasUmUsuarioService(id):    
    """
    Serviço para obter os detalhes de um único usuário pelo ID.
    
    Argumentos:
    - id: ID do usuário a ser listado.
    
    Retorna:
    - Resultado da função `listarApenasUmUsuario(id)` do modelo.
    """
    return listarApenasUmUsuario(id) 

def atualizarUmUsuarioService(id, usuario):
    """
    Serviço para atualizar os detalhes de um usuário existente pelo ID.
    
    Argumentos:
    - id: ID do usuário a ser atualizado.
    - usuario: Dados atualizados do usuário (espera-se que seja um dicionário com os detalhes atualizados).
    
    Retorna:
    - Resultado da função `atualizarUmUsuario(id, usuario)` do modelo.
    """
    return atualizarUmUsuario(id, usuario) 

def removerUmUsuarioService(id):
    """
    Serviço para remover um usuário pelo ID.
    
    Argumentos:
    - id: ID do usuário a ser removido.
    
    Retorna:
    - Resultado da função `removerUmUsuario(id)` do modelo.
    """
    return removerUmUsuario(id) 

def loginService(usuario):
    """
    Serviço para autenticar um usuário.
    
    Argumentos:
    - usuario: Dados do usuário para autenticação (espera-se que seja um dicionário com email e senha).
    
    Retorna:
    - Resultado da função `login(usuario)` do modelo.
    """
    return login(usuario) 
