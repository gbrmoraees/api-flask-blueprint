from config.config import get_db_connection

def listagemTodosUsuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    items = cursor.fetchall()
    conn.close()
    return items

def salvarUsuario(user):    
    name = user.get('nome')
    email = user.get('email')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (nome, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    conn.close()