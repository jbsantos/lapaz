from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from controller.Missao import MissaoController
from model.Role import Role
from model.User import User
from model.Motorista import Motorista
from model.Viatura import Viatura
from model.Status import Status
from model.Missao import Missao
from model.AddMissao import AddMissao
from admin.Views import UserView, HomeView, RoleView, MissaoView, MotoristaView, ViaturaView, StatusView, AddMissaoView

def start_views(app, db):
    admin = Admin(app, name='MISSÕES STS - CONTROLE DESPACHANTE', base_template='admin/base.html', template_mode='bootstrap3', index_view=HomeView())

    admin.add_view(RoleView(Role, db.session, "Funções",  category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    
    admin.add_view(MissaoView(Missao, db.session, "Missões", category="Gerenciar"))
    
    admin.add_view(ViaturaView(Viatura, db.session, 'Viatura', category="Gerenciar"))
    admin.add_view(MotoristaView(Motorista, db.session, 'Motorista', category="Gerenciar"))
    admin.add_view(StatusView(Status, db.session, 'Status', category="Gerenciar"))
    
    admin.add_view(AddMissaoView(AddMissao, db.session, name='Add Missões', category="Gerenciar"))
    
    #admin.add_sub_category(name="teste", parent_name="Gerenciar")
    
    #admin.add_link(MenuLink(name='add', url='/admin/addmissao', category='Missões', ))
    
    admin.add_link(MenuLink(name='Logout', url='/logout'))