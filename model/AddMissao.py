# -*- coding: utf-8 -*-
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from model.User import User

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class AddMissao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(25), unique=True, nullable=False)
    descricao = db.Column(db.Text(), nullable=True)
    

    def __repr__(self):
        return '%s'% (self.nome)


    def get_missaadd(self):
        try:
            res = db.session.query(AddMissao).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    def get_total_viatura(self):
        try:
            res = db.session.query(func.count(AddMissao.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res


 