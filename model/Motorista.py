# -*- coding: utf-8 -*-
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form

from config import app_active, app_config

from model.User import User

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Motorista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    saram = db.Column(db.Integer,  nullable=False)
    om = db.Column(db.String(20),  nullable=False)
    validade_habilitacao = db.Column(db.DateTime(8), default=db.func.current_timestamp(), nullable=False)
    categoria_habilitacao = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return '%s' % (self.name)

    def get_total_motorista(self):
        try:
            res = db.session.query(func.count(Motorista.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_motorista(self):
        try:
            res = db.session.query(Motorista).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_motorista_by_id(self,id):
        try:
            res = db.session.query(Motorista).filter_by(id=id).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

