# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc, asc, distinct, and_, or_, exists
from sqlalchemy.orm import relationship


from config import app_active, app_config
from model.User import User
from model.Category import Category
from model.Motorista import Motorista
from model.Viatura import Viatura
from model.AddMissao import AddMissao

from model.Status import Status
from datetime import datetime

config = app_config[app_active]
db = SQLAlchemy(config.APP)

def logado():
    from admin.Views import User
    return User

class Missao(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    ficha = db.Column(db.Integer, autoincrement=True, unique=True,  nullable=False)
    siloms = db.Column(db.Integer, unique=True, nullable=False)
    km_viatura = db.Column(db.Numeric(10,2), nullable=False)
    missao = db.Column(db.Integer, db.ForeignKey(AddMissao.id), nullable=False)
    km_saida = db.Column(db.Numeric(10,2), nullable=True)
    km_chegada = db.Column(db.Numeric(10,2), nullable=True)
    data_saida = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    data_chegada = db.Column(db.DateTime(6), nullable=True)
    observacao = db.Column(db.Text(500), nullable=True)
    user_created = db.Column(db.Integer,db.ForeignKey(User.id), bake_queries=False, nullable=False)
    motorista = db.Column(db.Integer, db.ForeignKey(Motorista.id), nullable=True)
    ultimo_motorista = db.Column(db.Integer, nullable=True)
    viatura = db.Column(db.Integer, db.ForeignKey(Viatura.id), nullable=False)
    status = db.Column(db.Integer, db.ForeignKey(Status.id), nullable=False)
    ass_motorista_saida = db.Column(db.String(30), nullable=True)
    ass_motorista_chegada = db.Column(db.String(30), nullable=False)
    ass_despachante_abrir = db.Column(db.String(30), nullable=True)
    ass_despachante_fechar = db.Column(db.String(30), nullable=False)    
    
    usuario = relationship(User)

    motoristas = relationship(Motorista)
    viaturas = relationship(Viatura)
    missoes = relationship(AddMissao)
    status_ = relationship(Status)

    def __repr__(self):
        return '%s' % (self.viaturas)
    def get_all(self, limit):
        try:
            if limit is None:
                res = db.session.query(Missao).order_by(desc(Missao.data_saida)).all()
            else:
                res = db.session.query(Missao).order_by(desc(Missao.data_saida)).limit(limit).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()

            return res

    def get_missao_motorista_all(self):
        try:
            res = db.session.query(Missao, Motorista, Viatura, Status, AddMissao).join(Motorista, Viatura, Status, AddMissao).filter(
               Missao.status == '1').order_by(desc(Missao.data_saida)).all()  # ULTIMAS MISSAO EM ANDAMENTO
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()

            return res

    def get_total_missao(self):
        try:
            res = db.session.query(func.count(Missao.id)).filter(Missao.status == '1').first()  # MISSAO EM ANDAMENTO
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_last_missao(self):
        try:
            res = db.session.query(Missao, Motorista, Viatura).join(Motorista, Viatura).filter(
                Missao.motorista == Motorista.id).order_by(desc(Missao.data_saida)).all()
            print(res)
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_missao_by_id(self, id):
        try:
            res = db.session.query(Missao).filter_by(id=id).order_by(desc(Missao.data_saida)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_viatura_by_id(self, id):
        try:
            res = db.session.query(Viatura).filter_by(id=id).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_motorista_by_id(self, id):
        try:
            res = db.session.query(Motorista).filter_by(id=id).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def missao_motorista(self):
        try:
            res = []
            res = db.session.query(Motorista) \
                .with_entities(
                Motorista.id,
                Motorista.name,

            ). \
                distinct(Motorista.id)
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
            
    def nome_missao(self):
        try:
            res = []
            res = db.session.query(AddMissao) \
                .with_entities(
                AddMissao.id,
                AddMissao.nome,

            ). \
                distinct(AddMissao.id)
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def select_viatura(self):
        try:
            res = db.session.query(Viatura).\
            filter(~exists().where(
            and_(Missao.viatura == Viatura.id,Missao.status == 1 ))).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    
    def select_status(self):
        try:
            res = db.session.query(Status).filter(Status.id.in_([1,3]))
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def select_status_em_andamento(self):
        
        try:
            res = db.session.query(Status).filter(Status.id.in_([2,3]))
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res

    def get_missao_prevista(self):
         try:
             res = db.session.query(Missao, Motorista, Viatura, Status, AddMissao).join(Motorista, Viatura, Status, AddMissao).filter(
                Missao.status == 4).order_by(desc(Missao.data_saida)).all()  # ULTIMAS MISSAO PREVISTAS
         except Exception as e:
             res = []
             print(e)
         finally:
             db.session.close()
             return res
    