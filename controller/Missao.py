from datetime import datetime

from model.Missao import Missao
from model.Motorista import Motorista
from model.AddMissao import AddMissao
from  model.Status import Status

class MissaoController():
    def __init__(self):
        self.missao_model = Missao()
        self.motorista_model = Motorista()
        self.status_model = Status()

    def get_missao(self):
        result = []
        try:
            res = self.missao_model.get_missao_motorista_all()
            
            for r in res:
                
                
                missao = r[0]
                motorista = r[1]
                viatura = r[2]
                status = r[3]
                addmissao = r[4]
                
                result.append({
                    'id' : missao.id,
                     'viatura': missao.viatura,
                     #'missao': missao.missao,
                     'km_saida': str(missao.km_saida),
                     'km_chegada': str(missao.km_chegada),
                     'ficha': missao.ficha,
                     'data_saida': missao.data_saida.strftime('%d/%m/%Y  %H:%M'),
                     #'data_chegada': missao.data_chegada.strftime('%d/%m/%Y  %H:%M'),
                     'status':missao.status,
                     'motorista': motorista,
                     'viatura': viatura,
                     'status':status,
                     'missao': addmissao,


                })
            status = 200

        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }


        
    def get_missao_by_id(self, missao_id):
        result = {}
        try:
            self.missao_model.id = missao_id
            res = self.missao_model.get_missao_by_id()

            for r in res:
                print(r)
                missao = r[0]
                motorista = r[1]
                viatura = r[2]
                status = r[3]

            result = {
                'id' : res.id,
                'viatura': res.viatura,
                # 'missao': res.natureza_servico,
                'km_saida': str(res.km_saida),
                'km_chegada': str(res.km_chegada),
                'ficha': res.ficha,
                'data_saida': res.data_saida.strftime('%d/%m/%Y  %H:%M'),
                'data_chegada': res.data_chegada.strftime('%d/%m/%Y  %H:%M'),
                'status':res.status,
                'motorista': motorista,
                'status_':status,
                'observacao': res.observacao,


            }

            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }

    def get_missao_prevista(self):
         result = []
         try:
             res = self.missao_model.get_missao_prevista()
             
             for r in res:
                 
                 
                 missao = r[0]
                 motorista = r[1]
                 viatura = r[2]
                 status = r[3]
                 addmissao = r[4]
                 
                 result.append({
                     'id' : missao.id,
                      'viatura': missao.viatura,
                      'ficha': missao.ficha,
                      'data_saida': missao.data_saida.strftime('%d/%m/%Y  %H:%M'),
                      'status':missao.status,
                      'viatura': viatura,
                      'status':status,
                      'missao': addmissao,
 
 
                 })
             status = 200
 
         except Exception as e:
             print(e)
             result = []
             status = 400
         finally:
             return {
                 'result': result,
                 'status': status
                }