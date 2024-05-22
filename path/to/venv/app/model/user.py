from config.config import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash


def listagemTodosUsuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def salvarUsuario(usuario):    
    email = usuario.get('email')
    senhaHashed = generate_password_hash(usuario.get('senha'), method='pbkdf2:sha256')
    altura = usuario.get('altura')
    peso = usuario.get('peso')
    objetivo = usuario.get('objetivo')
    obs = usuario.get('obs')

    conn = get_db_connection()
    cursor = conn.cursor() 
    cursor.execute(
        'INSERT INTO usuarios (email, senha, altura, peso, objetivo, obs) VALUES (%s, %s,%s, %s,%s, %s)',
          (email, senhaHashed, altura, peso, objetivo, obs))
    conn.commit()
    conn.close()


def listarApenasUmUsuario(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)    
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    user = cursor.fetchone()
    conn.close()
    return user         

def atualizarUmUsuario(id, usuario):
    
    email = usuario.get('email')
    senhaHashed = generate_password_hash(usuario.get('senha'), method='pbkdf2:sha256')
    altura = usuario.get('altura')
    peso = usuario.get('peso')
    objetivo = usuario.get('objetivo')
    obs = usuario.get('obs')

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE usuarios SET email = %s, senha = %s, altura = %s, peso = %s, objetivo = %s, obs = %s WHERE id = %s", (email, senhaHashed, altura,peso,objetivo,obs,id))
    connection.commit()
    cursor.close()
    connection.close()

def removerUmUsuario(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()


def login(usuario):
    
    email = usuario.get('email')
    senha = usuario.get('senha')
    
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if user and check_password_hash(user['senha'], senha):
        return True
    else:
        return False