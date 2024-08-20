import mysql.connector

def get_db_connection():
    """
    Estabelece uma conexão com o banco de dados MySQL.

    Retorna:
    - Uma conexão com o banco de dados MySQL, configurada com os parâmetros especificados.
    """
    return mysql.connector.connect(
        host='127.0.0.1',         # Endereço do servidor MySQL. '127.0.0.1' refere-se ao servidor local.
        user='root',             # Nome de usuário para autenticação no banco de dados.
        password='root',         # Senha do usuário para autenticação no banco de dados.
        database='lp_trainer',   # Nome do banco de dados ao qual conectar.
        port=8889                # Porta na qual o servidor MySQL está ouvindo (porta padrão do MAMP).
    )
