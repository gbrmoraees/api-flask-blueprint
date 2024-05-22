from flask import make_response, jsonify, request
from service.user import salvarUserService, listagemTodosUsuariosService, listarApenasUmUsuarioService, atualizarUmUsuarioService, removerUmUsuarioService, loginService

def listarTodosUsuario():    
    return make_response(
        jsonify(
            mensagem = "Listagem de user",
            usuarios = listagemTodosUsuariosService()
        )
    ) 

def salvarUsuario():    
    usuario = request.json     
    if not isinstance(usuario.get('senha'), str):
        return make_response(
            jsonify(
              mensagem = "Senha deve ser uma string"  
            )
        )
       
    salvarUserService(usuario)
    return make_response(
        jsonify(
            mensagem = "Cadastro com sucesso!!"
        )
    )

def listarApenasUmUsuario(id):       
    return make_response(
        jsonify(
            mensagem = "Listagem de user",
            usuario = listarApenasUmUsuarioService(id)
        )
    ) 

def atualizarUmUsuario(id): 
    usuario = request.json
    
    if not isinstance(usuario.get('senha'), str):
        return make_response(
            jsonify(
              mensagem = "Senha deve ser uma string"  
            )
        )
    
    atualizarUmUsuarioService(id, usuario)          
    return make_response(
        jsonify(
            mensagem = "Usuário Atualizado com sucesso!!"
        )
    ) 

def removerUmUsuario(id):     
    removerUmUsuarioService(id)          
    return make_response(
        jsonify(
            mensagem = "Usuário Removido com sucesso!!"
        )
    )

def login():    
    usuario = request.json    
    login = loginService(usuario)
    if login:
        return make_response(
            jsonify(
                mensagem = "Logim feito com Sucesso",
                status = 200
            )
        )
    else:
        return make_response(
            jsonify(
                mensagem = "Email ou senha invalido",
                status = 401
            )
        )
    

#pip install flask mysql-connector-python
#pip install flask-cors
    