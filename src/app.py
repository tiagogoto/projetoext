import os
from flask import Flask, render_template, request, redirect, url_for, render_template
from flask_bcrypt import Bcrypt 

# Cria o aplicativo com as configurações 
from . import db, create_app # from __init__ file

app = create_app(os.getenv("CONFIG_MODE"))


# inicializa
if __name__ == '__main__':
    app.run(debug=True)
    


