from model.user import listagemTodosUsuarios, salvarUsuario, listarApenasUmUsuario, atualizarUmUsuario, removerUmUsuario, login

def listagemTodosUsuariosService():    
    return listagemTodosUsuarios()

def salvarUserService(usuario):    
    return salvarUsuario(usuario)   

def listarApenasUmUsuarioService(id):    
    return listarApenasUmUsuario(id) 

def atualizarUmUsuarioService(id, usuario):
    return atualizarUmUsuario(id, usuario) 

def removerUmUsuarioService(id):
    return removerUmUsuario(id) 

def loginService(usuario):
    return login(usuario) 
