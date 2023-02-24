# -*- coding: utf-8 -*-
from wtforms.validators import DataRequired

import app
from flask_admin import AdminIndexView, expose
from sqlalchemy import exists, and_
import datetime
from datetime import date

from flask_admin.form import rules
from wtforms import Form, SelectField


from flask_admin.contrib.sqla import ModelView

from flask_admin.helpers import get_redirect_target, get_form_data, is_form_submitted
from flask_login import current_user
from flask import redirect, url_for

from config import app_config, app_active
from model import Role

from model.User import User
from model.Category import Category
from model.Motorista import Motorista

from model.Viatura import Viatura, db
from model.AddMissao import AddMissao

from model.Missao import Missao
from datetime import datetime

from controller.Missao import MissaoController
from controller.Viatura import  ViaturaController

config = app_config[app_active]

class HomeView(AdminIndexView):

    extra_css = [config.URL_MAIN + 'static/css/home.css',
                 'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css']

    @expose('/')
    def index(self):
        self.usuario_logado = current_user

        user_model = User()
        category_model = Category()
        motorista_model = Motorista()
        viatura_model = Viatura()
        addmissao_model = AddMissao()
        missao_model = Missao()
        users = user_model.get_total_users()
        categories = category_model.get_total_categories()
        motorista = motorista_model.get_total_motorista()
        viatura = viatura_model.get_total_viatura()

        addmissao = addmissao_model.get_missaadd()

        missao_controller = MissaoController()
        missao_prevista_controller = MissaoController()

        missao = missao_model.get_total_missao()
        missao_prevista_controller = missao_controller.get_missao_prevista()
        missao_controller = missao_controller.get_missao()
        #print(missao_controller)

        return self.render('home_admin.html', report={
            'users': users[0],
            'categories': categories[0],
            'motorista': motorista[0],
            'missao': missao[0],
            'viatura': viatura[0],
            'addmissao': addmissao[0]

        }, missao_controller=missao_controller, missao_prevista_controller=missao_prevista_controller)

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

def user_formatar(self, request, motorista, *args):
    data_pt = datetime.strftime(motorista.validade_habilitacao, "%d/%m/%y")
    return data_pt

class UserView(ModelView):
    column_exclude_list = ['password', 'recovery_code']
    form_excluded_columns = ['last_update', 'recovery_code']
    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['username', 'email']
    column_filters = ['username', 'email', 'funcao']
    create_modal = True
    edit_modal = True
    can_export = True
    column_editable_list = ['username', 'email', 'active']
    column_sortable_list = ['username']
    column_default_sort = [('username', True), ('date_created', True)]
    column_details_exclude_list = ['password', 'recovery_code']
    column_export_exclude_list = ['password', 'recovery_code']

    export_types = ['json', 'yaml', 'csv', 'xls', 'df']

    column_formatters = {'validade_habilitacao': user_formatar}

    column_labels = {
        'funcao': 'Função',
        'username': 'Nome de usuário',
        'email': 'E-mail',
        'date_created': 'Data de Criação',
        'last_update': 'Última atualização',
        'active': 'Estado',
        'password': 'Senha',
    }

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password

    def create_form(self, obj=None):

        form = super().create_form()
        self.form_widget_args = ''
        form.funcao.query_factory = lambda: User.select_funcao(self)
        return form

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = False
            self.can_delete = False
            return current_user.is_authenticated
        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

class RoleView(ModelView):

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

class CategoryView(ModelView):
    can_view_details = True

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
        elif role == 2:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

def formatar_data_idt(self, request, motorista, *args):
    data_pt = datetime.strftime(motorista.validade_habilitacao, "%d/%m/%y")
    return data_pt

class MotoristaView(ModelView):
    can_view_details = True
    column_editable_list = ['name']
    create_modal = True
    edit_modal = True
    column_formatters = {'validade_habilitacao': formatar_data_idt}
    column_searchable_list = ['name', 'saram']

    column_labels = {
        'name': 'Motorista',
        'saram': 'Nº Ordem',
        'om': 'Org. Militar',
        'validade_habilitacao': 'Validade de Habilitação',
        'categoria_habilitacao': 'Categoria da Habilitação'
    }

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

class ViaturaView(ModelView):
    can_view_details = True
    column_editable_list = ['active']
    column_searchable_list = ['name', 'description']

    column_labels = {
        'name': 'Registro FAB',
        'description': 'Viatura',
        'km_viatura': 'KM de Viatura',
        'active': 'Estado',
    }

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

def formatar_data_saida(self, request, missao, *args):
    data_pt = datetime.strftime(missao.data_saida, "%d/%m/%y  %H:%M")
    return data_pt

# def formatar_data_chegada(self, request, missao, *args):
#     data_pt = datetime.strftime(missao.data_chegada, "%d/%m/%y  %H:%M")
#     return data_pt

def formatar_viatura(self, request, missao, *args):
    straux = missao.viaturas.name + "-" + missao.viaturas.description
    return straux

def formatar_motorista(self, request, missao, *args):
    straux = missao.motoristas.name + "-" + missao.motoristas.om
    return straux


def formatar_ultimo_motorista(self, request, missao, *args):
     #print(missao.ultimo_motorista)
     nomes_motoristas = []
     for i in missao.missao_motorista():
         if i.id == missao.ultimo_motorista:
             nomes_motoristas.append(i.name)
 
     return nomes_motoristas

def formatar_missao(self, request, missao, *args):
     nomes_missao = []
     for i in missao.nome_missao():
         if i.id == missao.missao:
             nomes_missao.append(i.nome)
 
     return nomes_missao

def formatar_usuario(self, request, missao, *args):
     straux = missao.usuario.username
     return straux
   
class AddMissaoView(ModelView):
    can_view_details = True
    column_searchable_list = ['nome', 'descricao']

    column_labels = {
        'nome': 'Nome da Missão',
        'descricao': 'Descrição',
    }

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated
        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

      
   
class MissaoView(ModelView):

    list_template = 'home_list_missao.html'
    create_modal = True
    edit_modal = True
    column_display_pk = True
    can_export = True
    column_editable_list = ['observacao', 'status_']
    column_searchable_list = ['siloms', 'ficha', 'viaturas.description', 'viaturas.name', 'status_.name']
    column_filters = ['data_saida', 'data_chegada', 'status' ]
    column_default_sort = [('status_.name', True),('data_saida', True)]
    form_choices = {'ultimo_motorista': [(str(row), str(row)) for row in range(10000)]}
    column_exclude_list = ['id','motoristas', 'km_viatura', 'ass_motorista_chegada']
    #lista as colununas de missao
    #column_list = ['status_', 'missao', 'viaturas','motorista', 'data_saida', 'observacao', 'data_chegada']
    form_edit_rules = rules.FieldSet =  {
                'status_',
                'data_saida',
                'motoristas',
                'ultimo_motorista',
                #'km_saida',
                'km_chegada',
                'observacao',
                'data_chegada',
   
              }

    form_create_rules = rules.FieldSet =   {
                    'ficha',
                    'siloms',
                    'motoristas',
                    'viaturas',
                    'observacao',
                    'data_saida', 
                    'missoes'
                }

    def on_form_prefill(self, form, id):

        print(form.status_.__dict__, 'teste1')
        print(form.status_.object_data, 'dados do objeto')

        #print(form.km_saida.data, 'km saida')
     
        self.aux = [(str(row.id), row.name) for row in Missao.missao_motorista(self)]
        form.ultimo_motorista.choices = self.aux
        missao = Missao.get_missao_by_id(self,id)
        # if Missao.status == 1:
        #     print('chogou 1')
        #     print(model.id, 'km viatura')
        #     Missao.km_saida = Missao.km_viatura
        #     Missao.km_chegada = form.km_chegada

        if missao.status == 2:
            

            self.form_widget_args = {
                'viaturas': {
                    'disabled': True,
                },
                 'missoes': {
                    'disabled': True,
                },
                'data_chegada': {
                    'disabled': True,
                },
                'km_saida': {
                    'rows': 10,
                    'disabled': True,
                    'style': 'color: red',
                },
                'km_chegada': {
                    'disabled': True,
                },
                'ultimo_motorista': {
                    'disabled': True,
                },
                'status_': {
                    'disabled': False,
                },
                'observacao': {
                    'readonly': False,
                },
            }
        elif missao.status == 4:
             print('chegou')
            
             form.status_.query_factory = lambda: Missao.select_status(self)
             self.form_widget_args = {
                
                'km_saida': {
                    'rows': 10,
                    'readonly': False,
                    'style': 'color: red',
                    'value':"",
                 
                },
                'km_chegada': {
                    'rows': 10,
                    'readonly': True,
                    'disabled': True,
                    'style': 'color: red',
                    'value':"",
                 
                },     
                    'data_chegada': {
                    'rows': 10,
                    'readonly': True,
                    'disabled': True,
                    'style': 'color: red',
                    'value':"",
                 
                },      

                'ultimo_motorista': {
                    'rows': 10,
                    'readonly': True,
                    'disabled': True,
                    'style': 'color: red',
                   # 'value':"",
                 
                },       
                  

            }

        elif missao.status == 1:
            form.status_.query_factory = lambda: Missao.select_status_em_andamento(self)
            print('chegou status 1')

            self.form_widget_args = {
                
                'motoristas': {
                    #'rows': 10,
                    'readonly': True,
                    'disabled': True,
                    'style': 'color: red',
                    #'value':"", 
            },
                    'ultimo_motorista': {
                    #'rows': 10,
                    'required': 'required',
                    #'disabled': True,
                    'style': 'color: red',
                   # 'value':"",
                 
                },    
                    'data_saida': {
                    #'rows': 10,
                    'readonly': True,
                    'disabled': True,
                    'style': 'color: red',
                   # 'value':"",
                 
                },    
                
        
        }
 
        else:
            self.form_widget_args = {
                'viaturas': {
                    'disabled': False,
                },
                'missoes': {
                    'disabled': False,
                },
                'data_chegada': {
                    'disabled': False,
                },
                'km_saida': {
                    'rows': 10,
                    'readonly': True,
                    'style': 'color: red',
                },
                'km_chegada': {
                    'disabled': False,
                },
                'ultimo_motorista': {
                    'disabled': False,
                },
                'status_': {
                    'disabled': False,
                },
                'observacao': {
                    'readonly': False,
                },
                'missoes': {
                    'disabled': False,
                },

            }
        return form

    column_formatters = {
        'data_saida': formatar_data_saida,
        #'data_chegada': formatar_data_chegada,
        'viaturas': formatar_viatura,
        'motoristas': formatar_motorista,
        'ultimo_motorista': formatar_ultimo_motorista,
        'missao': formatar_missao,
        'usuario':formatar_usuario,
                        }

    column_labels = {
        'siloms': 'Nº Siloms',
        'ficha': 'Nº Ficha',
        'viatura': 'RegFab e Viatura',
        'missao': 'adicionar Missão ',
        'km_saida': 'Km de saída',
        'km_chegada': 'Km de Chegada',
        'motoristas': 'Motorista',
        'observacao': 'Observação',
        'ass_motorista_saida': 'Motorista Saida',
        #'ass_motorista_chegada': 'Motorista Chegada',
        'ultimo_motorista': 'Ultimo Motorista',
        'ass_despachante_abrir': 'Abriu Missão',
        'ass_despachante_fechar': 'Fechou Missão',
        'missoes': 'Missões'


    }

    form_widget_args = {
        'km_saida': {
            'rows': 10,
            'readonly': True,
            'style': 'color: red',
        },
    }



    def on_model_change(self, form, model, is_created):
        if  model.status ==  4 :
            print('chogou 0')

        elif model.status == 1:

            print('chogou 1')
            model.km_saida = Missao.km_viatura
            print(form.status_.__dict__)



            #ViaturaController.update_viatura(self, form)
            
        elif model.status == 2:
            print('chogou 2')
            model.ass_motorista_chegada = form.ultimo_motorista._data
            model.ultimo_motorista = form.ultimo_motorista._data
            ViaturaController.update_viatura(model.viaturas)
            
        #o valor vem do banco e atualiza km_viatura no km_saida
        #model.km_saida = model.viaturas.km_viatura
        if is_created:
            print('está criando porcesso inicial')
            print(model.__dict__)
            model.user_created = current_user.id
            model.ass_despachante_abrir = current_user.username
            
            
            # valor de km saída recebido do banco na criação da missão
            # model.km_saida = model.viaturas.km_viatura

            id = form.viaturas.raw_data[0]
            viatura = Missao.get_viatura_by_id(self, id)
            # if model.km_chegada == '' and model.status == '' :
            #     model.km_saida = viatura.km_viatura
            # elif model.status == 1:
            #     model.km_saida = model.km_viatura
            #     model.km_chegada = form.km_chegada
            
            # elif model.status == 2:

            #     model.km_viatura = viatura.km_chegada
            
            #model.km_saida = viatura.km_viatura
            model.status = 4
            
            #model.ass_motorista_saida = form.motoristas._data
            #model.ultimo_motorista = form.motoristas._data

            #model.data_saida = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            #print('hora', datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

            
            #status_missao = int(form.status_.raw_data[0])
            #motorista = Motorista()
            #id_motorista = form.ultimo_motorista.raw_data[0]
            #print(id_motorista, 'teste22')
            #nome_motorista = motorista.get_motorista_by_id(id_motorista)
            # model.ass_motorista_chegada = nome_motorista.name
            # model.ultimo_motorista = nome_motorista.name
            # if status_missao ==2:
            #     viatura = ViaturaController()
            #     result = viatura.update_viatura({'id':model.viatura, 'km_viatura': form.km_chegada.data})
            #     if result:
            #         mensagem = 'Editado'
            #     else:
            #         mensagem = 'Não Editado'

            #     return mensagem
            # elif status_missao == 3:
            #     print('status - 3')



        else:
       
            
            #valor de km saída recebido do banco na criação da missão
            model.km_saida = model.viaturas.km_viatura
            print('ja está criado')
            print(model.status, 'status 2')
            if model.status == 2:
                print('ja está criado status concluída')
                print(form.km_chegada.raw_data[0])
                model.ass_despachante_fechar = current_user.username
                
                model.km_viatura = form.km_chegada.raw_data[0]
                motorista_chegada = Missao.get_motorista_by_id(self,form.ultimo_motorista.raw_data[0])
                model.ass_motorista_chegada = str(motorista_chegada)

                
                viatura = ViaturaController()
                result = viatura.update_viatura({'id':model.viatura, 'km_viatura': model.km_chegada})
                if result:
                    mensagem = 'Editado'
                else:
                    mensagem = 'Não Editado'
                return mensagem

            elif model.status == 1:
                model.ass_motorista_saida = str(form.motoristas._data)
                #model.ultimo_motorista = form.motoristas._data
                
                print('chegou em andamento2')

            elif model.status_ == 'Cancelada':
                
                 model.ass_despachante_fechar = current_user.username

            print(model.__dict__)
            

    def create_form(self, obj=None):

        form = super().create_form()
        self.form_widget_args = ''
        print(form.motoristas.__dict__,'teste 0')
        form.viaturas.query_factory = lambda: Missao.select_viatura(self)

        
        return form

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = False
            return current_user.is_authenticated
        elif role == 2:
            self.can_create = True
            self.can_edit = True
            self.can_delete = False
            return current_user.is_authenticated
        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')

class StatusView(ModelView):
    can_view_details = True
    column_list = {'id', 'name', 'description'}
    column_labels = {
        'name': 'Status da missão',
        'description': 'Observação'
    }

    def is_accessible(self):
        role = current_user.role
        if role == 1:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

        elif role == 5:
            self.can_create = True
            self.can_edit = True
            self.can_delete = True
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        else:
            return redirect('/login')




