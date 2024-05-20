from flask import Flask, make_response, jsonify, request
from db.db import Users

def index():    
    return make_response(
        jsonify(
            mensagem = "Listagem de user",
            user = Users
        )
    )
    

def create():
    user = request.json    
    Users.append(user)
    return index()
    
    