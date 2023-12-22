# -*- coding: utf-8 -*-
from flask import Flask, request,url_for, make_response, redirect, render_template,jsonify, Response, json, abort, session, request, send_file, send_from_directory, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, current_user
from functools import wraps
# para gerar pdf
import pdfkit
#gear csv
import csv
from bs4 import BeautifulSoup
import time
from automacao.teste_selenium import ImportAuto
# config import
from config import app_config, app_active

# controllers
from controller.User import UserController
from controller.Etp40 import Etp40Controller
from controller.Etp94 import Etp94Controller
from controller.Product import ProductController
from admin.Admin import start_views
from flask_bootstrap import Bootstrap
#Selenium
import time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import os
config = app_config[app_active]

def create_app(config_name):
    config = app_config[config_name]
    app = Flask(__name__, template_folder='templates')
    app.url_map.strict_slashes = False
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   #app.config["SQLALCHEMY_ECHO"] = True
  #  app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'
    app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'America/Sao_Paulo'
    
    db = SQLAlchemy(config.APP)
    db.init_app(app)
    migrate = Migrate(app, db)
    start_views(app,db)

    Bootstrap(app)

    #db.create_all()


    @app.after_request
    def after_request(response):
        #response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    def auth_token_required(f):
        @wraps(f)
        def verify_token(*args, **kwargs):
            user = UserController()
            try:
                result = user.verify_auth_token(request.headers['access_token'])
                if result['status'] == 200:
                    return f(*args, **kwargs)
                else:
                    abort(result['status'], result['message'])
            except KeyError as e:
                abort(401, 'Você precisa enviar um token de acesso')

        return verify_token
    

    @app.route('/')
    def index():
        if current_user.is_authenticated:
            user_id = current_user.id
            limpar_sessoes()
            session['user_id'] = user_id
        
        return render_template('/jchc/index.html')
    
    @app.route('/etp94')
    def etp94():
        if current_user.is_authenticated:
            user_id = current_user.id
            #limpar_sessoes()
            session['user_id'] = user_id
            return render_template('/etp94/etp94.html')
        else:
            return render_template('/etp94/etp94.html')
    
    @app.route('/etp40')
    def etp40():
        
        if current_user.is_authenticated:
            user_id = current_user.id
            # limpar_sessoes()
            session['user_id'] = user_id
            return render_template('/etp40/etp40.html',)
        else:
            return render_template('/etp40/etp40.html')
       
        
    
    @app.route('/informacoes1-40',methods=['POST', 'GET'])
    def informacoes1_40():

        return render_template('etp40/1informacoes-40.html')
    
    @app.route('/necessidade2-40',methods=['POST', 'GET'])
    def necessidade2_40():
        
        return render_template('etp40/2necessidade-40.html')
    
    @app.route('/necessidade3-40',methods=['POST', 'GET'])
    def necessidade3_40():

        return render_template('etp40/3necessidade-40.html')
    
    @app.route('/necessidade4-40',methods=['POST', 'GET'])
    def necessidade4_40():

        return render_template('etp40/4necessidade-40.html')

    @app.route('/solucao5-40',methods=['POST', 'GET'])
    def solucao5_40():
        return render_template('etp40/5solucao-40.html')
    
    @app.route('/solucao6-40',methods=['POST', 'GET'])
    def solucao6_40():
        return render_template('etp40/6solucao-40.html')
    
    @app.route('/solucao7-40',methods=['POST', 'GET'])
    def solucao7_40():
        return render_template('etp40/7solucao-40.html')
       
    @app.route('/solucao8-40',methods=['POST', 'GET'])
    def solucao8_40():
        return render_template('etp40/8solucao-40.html')
    
    @app.route('/solucao9-40',methods=['POST', 'GET'])
    def solucao9_40():
        return render_template('etp40/9solucao-40.html')
    
    @app.route('/solucao10-40',methods=['POST', 'GET'])
    def solucao10_40():
        return render_template('etp40/10solucao-40.html')    
    
    @app.route('/solucao11-40',methods=['POST', 'GET'])
    def solucao11_40():
        return render_template('etp40/11solucao-40.html')  
    
    @app.route('/planejamento12-40',methods=['POST', 'GET'])
    def planejamento12_40():
        return render_template('etp40/12planejamento-40.html') 
    
    @app.route('/planejamento13-40',methods=['POST', 'GET'])
    def planejamento13_40():
        return render_template('etp40/13planejamento-40.html') 
    
    @app.route('/planejamento14-40',methods=['POST', 'GET'])
    def planejamento14_40():
        return render_template('etp40/14planejamento-40.html') 
    
    @app.route('/viabilidade15-40',methods=['POST', 'GET'])
    def viabilidade15_40():
        return render_template('etp40/15viabilidade-40.html') 

    @app.route('/viabilidade16-40',methods=['POST', 'GET'])
    def viabilidade16_40():
        return render_template('etp40/16viabilidade-40.html') 
 
    @app.route('/process_form',methods=['POST', 'GET'])
    def login_selenium():
        data = request.form  # Use .json diretamente para obter os dados

        processed_data = UserController.process_form_data(data)
        print(processed_data)
        
        usuario = processed_data['username']
        senha = processed_data['password']
        id_form = processed_data['id_form']
        etp= processed_data['etp']

        result = ImportAuto.import_automatic_etp(usuario, senha, id_form,etp)

        print('chamou etp40', result,' ', session['8'])

    @app.route('/pagina_selenium',methods=['POST', 'GET'])
    def pagina_selenium():    
    
        return 'OK' #render_template('etp40/login-selenium.html') 
       
    @app.route('/salvar-conteudo', methods=['POST'])
    def salvar_conteudo():
        dados = request.get_json()
        conteudo = dados.get('conteudo')
        print(conteudo)
        # Faça o processamento necessário com o conteúdo recebido
        # Por exemplo, você pode salvar o conteúdo em um banco de dados ou em um arquivo
        
        return 'Conteúdo salvo com sucesso'
    
    @app.route('/gerar_csv', methods=['GET', 'POST'])
    def gerar_csv():
        carregar_dados = carregar_pdf()

        quill_content = {
            '1': 'Informações Básicas',
            '2': 'Descrição da necessidade',
            '3': 'Área Requisitante',   
            '4': 'Descrição dos Requisitos da Contratação',
            '5': 'Levantamento de Mercado',
            '6': 'Descrição da solução como um todo',
            '7': 'Estimativa das Quantidades a serem contratadas',
            '8': 'Estimativa do Valor da Contratação',
            '9': 'Justificativa para o Parcelamento ou não da Solução',
            '10': 'Contratações Correlatas e/ou Interdependentes',
            '11': 'Alinhamento entre a Contratação e o Planejamento',
            '12': 'Benefícios a serem alcançados com a contratação',
            '13': 'Providências a serem adotadas',
            '14': 'Possíveis Impactos Ambientais',
            '15': 'Declaração de Viabilidade',
            '16': 'Responsáveis'
        }
        
        csv_data = []

        for session_number in range(1, 17):
            if str(session_number) in session:
                content = session[str(session_number)]
                content = remove_html_tags(content)  # Remove as tags HTML
                if content.strip() == '':
                    content = ' '
                csv_data.append([quill_content[str(session_number)], content])
        
       
        output_path = 'static/csv/etp40/etp40.csv'

        csv_filename = output_path

        # Cria o arquivo CSV
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)
  
        
        return send_file(csv_filename, as_attachment=False)
    
    
    def remove_html_tags(text):
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text()
    

    @app.route('/baixar_pdf', methods=['POST', 'GET'])
    def baixar_pdf():

        carregar_dados = carregar_pdf()
        quill_content = {}
        # Exemplo de uso:

        for etapa in range(1, 17):  # Loop para percorrer as 16 sessões
            conteudo_editor = session.get(str(etapa), '')
            if etapa == 8:
                input_value = request.args.get('valor')
                if input_value is not None:
                    conteudo_editor = input_value

            if conteudo_editor is not None:
                if conteudo_editor.strip() == '' or conteudo_editor.strip() == '<br>':
                    conteudo_editor = ' '  # Define como vazio se o conteúdo for vazio ou contiver apenas <br>
            else:
                conteudo_editor = ' '

            quill_content[str(etapa)] = conteudo_editor

        temp_file_path = 'temp.html'

        output_path = 'static/pdf/etp40/etp40.pdf'
        sections = {
            'Informações Básicas': [1],
            'Necessidade': list(range(2, 5)),
            'Solução': list(range(5, 12)),
            'Planejamento': list(range(12, 15)),
            'Viabilidade': [15, 16]
        }
        quill_content = {
            '1': 'Informações Básicas',
            '2': 'Descrição da Necessidade',
            '3': 'Área Requisitante',
            '4': 'Descrição dos Requisitos da Contratação',
            '5': 'Levantamento de Mercado',
            '6': 'Descrição da Solução Como um Todo',
            '7': 'Estimativa das Quantidades a Serem Contratadas',
            '8': 'Estimativa do Valor da Contratação',
            '9': 'Justificativa para o Parcelamento ou Não da Solução',
            '10': 'Contratações Correlatas e/ou Interdependentes',
            '11': 'Alinhamento entre a Contratação e o Planejamento',
            '12': 'Benefícios a serem Alcançados com a Contratação',
            '13': 'Providências a Serem Adotadas',
            '14': 'Possíveis Impactos Ambientais',
            '15': 'Declaração de Viabilidade',
            '16': 'Responsáveis'
        }
        with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n')
            temp_file.write('<style>body { background-color: #FFFFFF; }</style>')  # Definindo o estilo de fundo
            temp_file.write('</head>\n<body>\n')
            
            for section_title, section_sessions in sections.items():
                temp_file.write(f'<div><h1>{section_title}</h1>\n')
                
                for session_number in section_sessions:
                    content = quill_content.get(str(session_number), '')
                    session_content = session.get(str(session_number), '')
                    
                    # Substitui <br> por " "
                    session_content = session_content.replace('<br>', ' ')

                    if session_content.strip() == '':
                        session_content = ' '
                    
                    temp_file.write(f'<h2>{session_number}. {content}</h2>\n')
                    temp_file.write(f'<p>{session_content}</p>\n')
                
                temp_file.write('</div>\n')
            
            temp_file.write('</body>\n</html>')

        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
        }
        


        pdf_bytes = pdfkit.from_file(temp_file_path, False, options=options)
        # Criar uma resposta com os bytes do PDF
        response = make_response(pdf_bytes)
        
        # Definir o cabeçalho Content-Type para application/pdf
        response.headers['Content-Type'] = 'application/pdf'
        
        # Definir o cabeçalho Content-Disposition para realizar o download do arquivo
        response.headers['Content-Disposition'] = 'attachment; filename=meu_pdf.pdf'
        
        return response

    @app.route('/gerar_pdf', methods=['POST', 'GET'])
    def gerar_pdf():
            
        quill_content = {}

        for etapa in range(1, 17):  # Loop para percorrer as 16 sessões
            conteudo_editor = session.get(str(etapa), '')
            if etapa == 8:
                input_value = request.args.get('valor')
                if input_value is not None:
                    conteudo_editor = input_value

            if conteudo_editor is not None:
                if conteudo_editor.strip() == '' or conteudo_editor.strip() == '<br>':
                    conteudo_editor = ''  # Define como vazio se o conteúdo for vazio ou contiver apenas <br>
            else:
                
                session['editor_vazio'] =[str(etapa)]
                conteudo_editor = ' '

            quill_content[str(etapa)] = conteudo_editor

        temp_file_path = 'temp.html'

        output_path = 'static/pdf/etp40/etp40.pdf'
        sections = {
            'Informações Básicas': [1],
            'Necessidade': list(range(2, 5)),
            'Solução': list(range(5, 12)),
            'Planejamento': list(range(12, 15)),
            'Viabilidade': [15, 16]
        }
        quill_content = {
            '1': 'Informações Básicas',
            '2': 'Descrição da Necessidade',
            '3': 'Área Requisitante',
            '4': 'Descrição dos Requisitos da Contratação',
            '5': 'Levantamento de Mercado',
            '6': 'Descrição da Solução Como um Todo',
            '7': 'Estimativa das Quantidades a Serem Contratadas',
            '8': 'Estimativa do Valor da Contratação',
            '9': 'Justificativa para o Parcelamento ou Não da Solução',
            '10': 'Contratações Correlatas e/ou Interdependentes',
            '11': 'Alinhamento entre a Contratação e o Planejamento',
            '12': 'Benefícios a serem Alcançados com a Contratação',
            '13': 'Providências a Serem Adotadas',
            '14': 'Possíveis Impactos Ambientais',
            '15': 'Declaração de Viabilidade',
            '16': 'Responsáveis'
        }
        with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n')
            temp_file.write('<style>body { background-color: #FFFFFF; }</style>')  # Definindo o estilo de fundo
            temp_file.write('</head>\n<body>\n')
            
            for section_title, section_sessions in sections.items():
                temp_file.write(f'<div><h1>{section_title}</h1>\n')
                
                for session_number in section_sessions:
                    content = quill_content.get(str(session_number), '')
                    session_content = session.get(str(session_number), '')
                    
                    # Substitui <br> por " "
                    session_content = session_content.replace('<br>', ' ')

                    if session_content.strip() == '':
                        session_content = ' '
                    
                    temp_file.write(f'<h2>{session_number}. {content}</h2>\n')
                    temp_file.write(f'<p>{session_content}</p>\n')
                
                temp_file.write('</div>\n')
            
            temp_file.write('</body>\n</html>')

        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
        }

        # timestamp = int(time.time())  # Obtém o timestamp atual
        ultimo_id = 0
        if current_user.is_active:

                user_id = current_user.id
                
                 # salva no banco
                result = Etp40Controller.save_etp40()
                ultimo_id = Etp40Controller.ultimo_id_formulario()
                ultimo_id = ultimo_id.id
                        #caso seja positivo o resultado gerar o csv
                if result:
                    os.remove(temp_file_path)

                    limpar_sessoes()
                # Define o objeto current_user novamente na sessão
                    session['user_id'] = user_id
                    variavel = "Foi criado o ETP 40 nº " + str(ultimo_id)

                    flash(variavel)  # Armazena a variável para uso no próximo request
                    return redirect(url_for('admin.index'))
                else: 
                    print(result)
                    return "Não foi salvo o ETP 40 procure o administrador do sistema."

        else:
            return redirect('/registre-se')
       
    @app.route('/profile',methods=['POST', 'GET'])
    def profile():
        return render_template('etp40/users-profile.html') 
    
    @app.route('/carregar_pdf',methods=['POST', 'GET'])
    def carregar_pdf():
        status = ''
        id_form = request.form.get('id_form')
        session['id_form'] = id_form
        status = request.form.get('status')
        session['status'] = status
        result = Etp40Controller.retomar_session_etp40(id_form)

        return result
    
    @app.route('/retomar_dados',methods=['POST', 'GET'])
    def retomar_dados():
        status = ''
        id_form = request.form.get('id_form')
        session['id_form'] = id_form
        status = request.form.get('status')
        session['status'] = status
        result = Etp40Controller.retomar_session_etp40(id_form)

        return render_template('etp40/1informacoes-40.html', status=status) 
    
    @app.route('/salvar_edicao',methods=['POST', 'GET'])
    def salvar_edicao():
        id_form = session['id_form']
        result = Etp40Controller.salvar_edicao_etp40(id_form)

        if current_user.is_active:
                user_id = current_user.id
                if result:
                    
                    limpar_sessoes()
                # Define o objeto current_user novamente na sessão
                    session['user_id'] = user_id
                    variavel = "Foi editado o ETP-40 nº " + str(id_form)

                    flash(variavel)  # Armazena a variável para uso no próximo request
                    return redirect(url_for('admin.index'))
                else: 
                    print(result)
                    return "Não foi salvo a edição do ETP 40 procure o administrador do sistema."

        else:
            return redirect('/registre-se')
       
    @app.route('/registre-se',methods=['POST', 'GET'])
    def registre_se():
        return render_template('etp40/pages-register.html') 
    
    @app.route('/rota1', methods=['POST', 'GET'])
    
    def rota1():
        if request.method == 'POST':
            conteudo = request.form.get('conteudo')
            session['conteudo'] = conteudo
     
            return redirect('/rota1')

    # Verificar se a informação está armazenada na sessão
        conteudo = session.get('conteudo')
        
        return render_template('rota1.html', conteudo=conteudo)
        #return render_template('rota1.html')

    @app.route('/rota2', methods=['POST', 'GET'])
    def rota2():
         if request.method == 'POST':
            conteudo = request.form.get('conteudo')
            session['conteudo'] = conteudo
            #print(conteudo2)
            return redirect('/rota2')

    # Verificar se a informação está armazenada na sessão
         conteudo = session.get('conteudo')

         return render_template('rota2.html', conteudo=conteudo)
     
    @app.route('/rota3', methods=['POST', 'GET'])
    def rota3():
        if request.method == 'POST':
            conteudo2 = request.form.get('conteudo2')
            session['conteudo2'] = conteudo2
            print(conteudo2)
            return redirect('/rota3')

        # Verificar se a informação está armazenada na sessão
        conteudo2 = session.get('conteudo2')

        return render_template('rota3.html', conteudo2=conteudo2)
            #return render_template('rota1.html')


    @app.route('/ultima', methods=['POST'])
    def ultima():
        print(session)
        conteudo = session.get('conteudo')
        print(conteudo)
        sessoes = ['conteudo', 'conteudo2']
        for sessao in sessoes:
            session.pop(sessao, None)
        return render_template('ultima.html')
    
    @app.route('/login/')
    def login():
        return render_template('login.html', data={'status': 200, 'msg': None, 'type': None})

    @app.route('/login/', methods=['POST'])
    def login_post():
        user = UserController()

        email = request.form['email']
        password = request.form['password']

        result = user.login(email, password)

        if result:
            if result.role == 4:
                return render_template('login.html', data={'status': 401, 'msg': 'Seu usuário não tem permissão para acessar o admin', 'type':2})
            else:
                login_user(result)
                return redirect('/')
        else:
            return render_template('login.html', data={'status': 401, 'msg': 'Dados de usuário incorretos', 'type': 1})

    @app.route('/recovery-password/')
    def recovery_password():
        # Capítulo 11
        return render_template('recovery.html', data={'status': 200, 'msg': None, 'type': None})

    @app.route('/recovery-password/', methods=['POST'])
    def send_recovery_password():
        user = UserController()

        result = user.recovery(request.form['email'])

        # Capítulo 11 - Alterar parâmetros
        if result['status_code'] == 200 or result['status_code'] == 202:
            return render_template('recovery.html', data={'status': result['status_code'], 'msg': 'Você receberá um e-mail em sua caixa para alteração de senha.', 'type': 3})
        else:
            return render_template('recovery.html', data={'status': result['status_code'], 'msg': result['body'], 'type': 1})
    
    @app.route('/new-password/<recovery_code>')
    def new_password(recovery_code):
        user = UserController()
        result = user.verify_auth_token(recovery_code)
        
        if result['status'] == 200:
            res = user.get_user_by_recovery(str(recovery_code))
            if res is not None:
                return render_template('new_password.html', data={'status': result['status'], 'msg': None, 'type': None, 'user_id': res.id})
            else:
                return render_template('recovery.html', data={'status': 400, 'msg': 'Erro ao tentar acessar os dados do usuário. Tente novamente mais tarde.', 'type': 1})
        else:
            return render_template('recovery.html', data={'status': result['status'], 'msg': 'Token expirado ou inválido, solicite novamente a alteração de senha', 'type': 1})

    @app.route('/new-password/', methods=['POST'])
    def send_new_password():
        user = UserController()
        user_id = request.form['user_id']
        password = request.form['password']

        result = user.new_password(user_id, password)

        if result:
            return render_template('login.html', data={'status': 200, 'msg': 'Senha alterada com sucesso!', 'type': 3, 'user_id': user_id})
        else:
            return render_template('new_password.html', data={'status': 401, 'msg': 'Erro ao alterar senha.', 'type': 1, 'user_id': user_id})

    @app.route('/products/', methods=['GET'])
    @app.route('/products/<limit>', methods=['GET'])
    @auth_token_required
    def get_products(limit=None):
        header = {
            'access_token': request.headers['access_token'],
            "token_type": "JWT"
        }

        product = ProductController()
        response = product.get_products(limit=limit)
        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

    @app.route('/product/<product_id>', methods=['GET'])
    @auth_token_required
    def get_product(product_id):
        header = {
            'access_token': request.headers['access_token'],
            "token_type": "JWT"
        }
        
        product = ProductController()
        response = product.get_product_by_id(product_id = product_id)

        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

    @app.route('/user/<user_id>', methods=['GET'])
    @auth_token_required
    def get_user_profile(user_id):
        header = {
            'access_token': request.headers['access_token'],
            "token_type": "JWT"
        }

        user = UserController()
        response = user.get_user_by_id(user_id=user_id)

        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), response['status'], header

    @app.route('/login_api/', methods=['POST'])
    def login_api():
        header = {}
        user = UserController()

        email = request.json['email']
        password = request.json['password']

        result = user.login(email, password)
        code = 401
        response = {"message": "Usuário não autorizado", "result": []}

        if result:
            if result.active:
                result = {
                    'id': result.id,
                    'username': result.username,
                    'email': result.email,
                    'date_created': result.date_created,
                    'active': result.active
                }

                header = {
                    "access_token": user.generate_auth_token(result),
                    "token_type": "JWT"
                }
                code = 200
                response["message"] = "Login realizado com sucesso"
                response["result"] = result

        return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json'), code, header
    
    @app.route('/logout')
    def logout_send():
        logout_user()
        return render_template('login.html', data={'status': 200, 'msg': 'Usuário deslogado com sucesso!', 'type':3})

    @login_manager.user_loader
    def load_user(user_id):
        user = UserController()
        return user.get_admin_login(user_id)

    @app.route('/minha_funcao')
    def minha_funcao():
    # Coloque o código que gera o HTML desejado aqui
        
        codigo_html = render_template('/etp40/aside.html', )

        # Realize a modificação no código HTML
        codigo_html = codigo_html.replace('id="' + 'info_basico-nav' + '" class="nav-content collapse', 'id="' + 'info_basico-nav' + '" class="nav-content collapse show')
        
        return codigo_html

    app.jinja_env.globals.update(minha_funcao=minha_funcao)

# Registre a função no Jinja2

    # @app.route('/salvar', methods=['POST'])
    # def salvar():
    #     conteudo_editor = request.form.get('conteudo_editor')
    #     session['conteudo_editor'] = conteudo_editor
    #     print(conteudo_editor)
    #     return 'OK'

    # @app.route('/recuperar', methods=['GET'])
    # def recuperar():
    #     conteudo_editor = session.get('conteudo_editor', '')
    #     print(conteudo_editor)
    #     return conteudo_editor

    # Rota para salvar o conteúdo do editor Quill em uma sessão específica
    @app.route('/salvar/<int:etapa>', methods=['POST'])
    def salvar(etapa):
        print(etapa)
        
        conteudo_editor = request.form.get('conteudo_editor')
        
        if conteudo_editor is None:
            conteudo_editor = request.form.get('inputValue')

        conteudo_editor = remove_html_tags(conteudo_editor)
        session[str(etapa)] = conteudo_editor
        return 'OK'

    # Rota para recuperar o conteúdo do editor Quill de uma sessão específica
    @app.route('/recuperar/<int:etapa>', methods=['GET'])
    def recuperar(etapa):
        conteudo_editor = session.get(str(etapa), '')
        input_value = request.args.get('valor')

        if input_value is not None:
            conteudo_editor = input_value

        return conteudo_editor
    
    @app.route('/salvar_94/<int:etapa>', methods=['POST'])
    def salvar_94(etapa):
        conteudo_editor_94 = request.form.get('conteudo_editor_94')

        if conteudo_editor_94 is None:
            conteudo_editor_94 = request.form.get('inputValue_94')

        print('salvar ' + conteudo_editor_94)
        #etapa94 = str(etapa)
        session[str(etapa)] = conteudo_editor_94
        return 'OK'

    # Rota para recuperar o conteúdo do editor Quill de uma sessão específica
    @app.route('/recuperar_94/<int:etapa>', methods=['GET'])
    def recuperar_94(etapa):
        #etapa94 = str(etapa)

        conteudo_editor_94 = session.get(str(etapa), '')
        input_value_94 = request.args.get('valor')
        print('entrou')
        
        print('vaxio' + str(input_value_94))
        if input_value_94 is not None:
            conteudo_editor_94 = input_value_94
        
        print('recupera conteudo_editor_94 ' + conteudo_editor_94)
        return conteudo_editor_94
    
    @app.route('/editor_session')
    def editor_session():
        return render_template('etp40/editor_session.html')

    ##################################################################
    @app.route('/download_etp40/<path:filename>')
    def download_file_etp40(filename):
        directory = 'templates/etp40/assets/documents/'
        return send_from_directory(directory, filename, as_attachment=True)
    
    @app.route('/download_etp94/<path:filename>')
    def download_file_etp94(filename):
        directory = 'templates/etp94/assets/documents/'
        return send_from_directory(directory, filename, as_attachment=True)

    @app.route('/termo-de-uso-etptic')
    def quando_usar_etp94():
        if current_user.is_active:
            return render_template('/etp94/quando-usar-etp94.html')
        else: 
            return render_template('login.html', data={'status': 200, 'msg': None, 'type': None})
        
    @app.route('/termo-de-uso-etp')
    def quando_usar_etp40():
        if current_user.is_active:
            return render_template('/etp40/quando-usar-etp40.html')
        else: 
            return render_template('login.html', data={'status': 200, 'msg': None, 'type': None})
        
    
    @app.route('/informacao1-94', methods=['POST', 'GET'])
    def informacao1_94():

        return render_template('etp94/1informacao-94.html')
    
    @app.route('/necessidade2-94', methods=['POST', 'GET'])
    def necessidade2_94():
        
        return render_template('etp94/2necessidade-94.html')
    
    @app.route('/necessidade3-94', methods=['POST', 'GET'])
    def necessidade3_94():
        
        return render_template('etp94/3necessidade-94.html')
    
    @app.route('/necessidade4-94', methods=['POST', 'GET'])
    def necessidade4_94():
        
        return render_template('etp94/4necessidade-94.html')
    
    @app.route('/necessidade5-94', methods=['POST', 'GET'])
    def necessidade5_94():

        return render_template('etp94/5necessidade-94.html')
    
    @app.route('/necessidade6-94', methods=['POST', 'GET'])
    def necessidade6_94():

        return render_template('etp94/6necessidade-94.html')
    
    @app.route('/necessidade7-94', methods=['POST', 'GET'])
    def necessidade7_94():

        return render_template('etp94/7necessidade-94.html')
    
    @app.route('/solucao8-94', methods=['POST', 'GET'])
    def solucao8_94():

        return render_template('etp94/8solucao-94.html')
    
    @app.route('/solucao9-94', methods=['POST', 'GET'])
    def solucao9_94():

        return render_template('etp94/9solucao-94.html')
    
    @app.route('/solucao10-94', methods=['POST', 'GET'])
    def solucao10_94():

        return render_template('etp94/10solucao-94.html')
    
    @app.route('/solucao11-94', methods=['POST', 'GET'])
    def solucao11_94():

        return render_template('etp94/11solucao-94.html')
    
    @app.route('/solucao12-94', methods=['POST', 'GET'])
    def solucao12_94():

        return render_template('etp94/12solucao-94.html')
    
    @app.route('/solucao13-94', methods=['POST', 'GET'])
    def solucao13_94():

        return render_template('etp94/13solucao-94.html')
    
    @app.route('/solucao14-94', methods=['POST', 'GET'])
    def solucao14_94():

        return render_template('etp94/14solucao-94.html')
    
    @app.route('/solucao15-94', methods=['POST', 'GET'])
    def solucao15_94():

        return render_template('etp94/15solucao-94.html')
    
    @app.route('/planejamento16-94', methods=['POST', 'GET'])
    def planejamento16_94():

        return render_template('etp94/16planejamento-94.html')
    
    @app.route('/planejamento17-94', methods=['POST', 'GET'])
    def planejamento17_94():

        return render_template('etp94/17planejamento-94.html')
       
    @app.route('/viabilidade18-94', methods=['POST', 'GET'])
    def viabilidade18_94():

        return render_template('etp94/18viabilidade-94.html')
    
    @app.route('/viabilidade19-94', methods=['POST', 'GET'])
    def viabilidade19_94():

        return render_template('etp94/19viabilidade-94.html')
    
    @app.route('/gerar_pdf_94',methods=['POST', 'GET'])
    def gerar_pdf_94():
            
        quill_content = {}

        for etapa in range(1, 20):
            conteudo_editor_94 = session.get(str(etapa), '')
            if etapa == 13:
                input_value_94 = request.args.get('valor')
                if input_value_94 is not None:
                    conteudo_editor_94 = input_value_94

            if conteudo_editor_94 is not None:
                if conteudo_editor_94.strip() == '' or conteudo_editor_94.strip() == '<br>':
                    conteudo_editor_94 = ' '  # Define como vazio se o conteúdo for vazio ou contiver apenas <br>
            else:
                conteudo_editor_94 = ' '

            quill_content[str(etapa)] = conteudo_editor_94

        temp_file_path = 'temp.html'
        #last_id+=1

        #print(last_id,'last id 94 +1')
        #output_path = 'static/pdf/etp94/etp94'+str(last_id)+'.pdf'
        output_path = 'static/pdf/etp94/etp94.pdf'
        sections = {
            'Informações Básicas': [1],
            'Necessidade': list(range(2, 8)),
            'Solução': list(range(8, 16)),
            'Planejamento': list(range(16, 18)),
            'Viabilidade': [18, 19]
        }
        quill_content = {
            '1': 'Informações Básicas',
            '2': 'Descrição da Necessidade',
            '3': 'Área Requisitante',
            '4': 'Necessidades de Negócio',
            '5': 'Necessidades Tecnológicas',
            '6': 'Demais Requisitos Necessários e Suficientes à Escolha da Solução de TIC',
            '7': 'Estimativa da Demanda - Quantidade de Bens e Serviço',
            '8': 'Levantamento de Soluções',
            '9': 'Análise Comparativa de Soluções',
            '10': 'Registro de Soluções Consideradas Inviáveis',
            '11': 'Análise Comparativa de Custos (TCO)',
            '12': 'Descrição da Solução de TIC a Ser Contratada',
            '13': 'Estimativa de Custo Total da Contratação',
            '14': 'Justificativa Técnica da Escolha da Solução',
            '15': 'Justificativa Econômica da Escolha da Solução',
            '16': 'Benefícios a Serem Alcançados com a Contratação',
            '17': 'Providências a Serem Adotadas',
            '18': 'Declaração de Viabilidade',
            '19': 'Responsáveis'
        }
        with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n')
            temp_file.write('<style>body { background-color: #FFFFFF; }</style>')  # Definindo o estilo de fundo
            temp_file.write('</head>\n<body>\n')
            
            for section_title, section_sessions in sections.items():
                temp_file.write(f'<div><h1>{section_title}</h1>\n')
                
                for session_number in section_sessions:
                    content = quill_content.get(str(session_number), '')
                    session_content = session.get(str(session_number), '')
                    
                    # Substitui <br> por " "
                    session_content = session_content.replace('<br>', ' ')

                    if session_content.strip() == '':
                        session_content = ' '
                    
                    temp_file.write(f'<h2>{session_number}. {content}</h2>\n')
                    temp_file.write(f'<p>{session_content}</p>\n')

                temp_file.write('</div>\n')
            
            temp_file.write('</body>\n</html>')

        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
        }

        # pdfkit.from_file(temp_file_path, output_path, options=options)

        # os.remove(temp_file_path)
        # timestamp = int(time.time())  # Obtém o timestamp atual
        # return render_template('etp94/etp-pdf.html', timestamp=timestamp)   
        if current_user.is_active:
                user_id = current_user.id
                
                 # salva no banco
                result = Etp94Controller.save_etp94()
                ultimo_id = Etp94Controller.ultimo_id_formulario()
               
                    
                        #caso seja positivo o resultado gerar o csv
                if result:
                    #gera  o pdf no local específico
                    #pdfkit.from_file(temp_file_path, output_path, options=options)
                    os.remove(temp_file_path)
                    #gera o csv local específico

                    #print(last_id,'last id 94 vai entra no csv')
                    #gerar_csv_94(last_id)
                    #fazer uma funcao para verificar se o usuario está logado
                    # Limpa a sessão
                    limpar_sessoes()
                # Define o objeto current_user novamente na sessão
                    session['user_id'] = user_id
                    ultimo_id = ultimo_id.id
                        #caso seja positivo o resultado 
                    variavel = "Foi criado o ETP 94 nº " + str(ultimo_id)
                    flash(variavel)  # Armazena a variável para uso no próximo request
                    return redirect(url_for('admin.index'))
                else: 
                    print(result)
                    return "Não foi salvo o ETP 40 procure o administrador do sistema."

        else:
            return redirect('/registre-se')


    @app.route('/editor-session')
    def editor_session_94():
        return render_template('etp94/editor_session.html')

    @app.route('/gerar_csv_94', methods=['GET', 'POST'])
    def gerar_csv_94():
        carregar_dados = carregar_pdf_94()

        quill_content = {
            '1': 'Informações Básicas',
            '2': 'Descrição da Necessidade',
            '3': 'Área Requisitante',
            '4': 'Necessidades de Negócio',
            '5': 'Necessidades Tecnológicas',
            '6': 'Demais Requisitos Necessários e Suficientes à Escolha da Solução de TIC',
            '7': 'Estimativa da Demanda - Quantidade de Bens e Serviço',
            '8': 'Levantamento de Soluções',
            '9': 'Análise Comparativa de Soluções',
            '10': 'Registro de Soluções Consideradas Inviáveis',
            '11': 'Análise Comparativa de Custos (TCO)',
            '12': 'Descrição da Solução de TIC a Ser Contratada',
            '13': 'Estimativa de Custo Total da Contratação',
            '14': 'Justificativa Técnica da Escolha da Solução',
            '15': 'Justificativa Econômica da Escolha da Solução',
            '16': 'Benefícios a Serem Alcançados com a Contratação',
            '17': 'Providências a Serem Adotadas',
            '18': 'Declaração de Viabilidade',
            '19': 'Responsáveis'
        }
        
        csv_data = []
        
        for session_number in range(1, 20):
            if str(session_number) in session:
                content = session[str(session_number)]
                content = remove_html_tags(content)  # Remove as tags HTML
                if content.strip() == '':
                    content = ' '
                csv_data.append([quill_content[str(session_number)], content])

        output_path = 'static/csv/etp94/etp94.csv'
        
        csv_filename = output_path
        
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)

        return send_file(csv_filename, as_attachment=False)
       
    @app.route('/retomar_dados_94',methods=['POST', 'GET'])
    def retomar_dados_94():
        status = ''
        id_form = request.form.get('id_form')
        session['id_form'] = id_form
        status = request.form.get('status')
        session['status'] = status
        result = Etp94Controller.retomar_session_etp94(id_form)

        return render_template('etp94/1informacao-94.html', status=status) 
    
    @app.route('/salvar_edicao_94',methods=['POST', 'GET'])
    def salvar_edicao_94():
        id_form = session['id_form']
        result = Etp94Controller.salvar_edicao_etp94(id_form)
        
        if current_user.is_active:
                user_id = current_user.id
                if result:
                    
                    limpar_sessoes()
                # Define o objeto current_user novamente na sessão
                    session['user_id'] = user_id
                    variavel = "Foi editado o ETP-94 nº " + str(id_form)

                    flash(variavel)  # Armazena a variável para uso no próximo request
                    return redirect(url_for('admin.index'))
                else: 
                    print(result)
                    return "Não foi salvo a edição do ETP 94 procure o administrador do sistema."

        else:
            return redirect('/registre-se')

    @app.route('/carregar_pdf_94',methods=['POST', 'GET'])
    def carregar_pdf_94():
        status = ''
        id_form = request.form.get('id_form')
        session['id_form'] = id_form
        status = request.form.get('status')
        session['status'] = status
        result = Etp94Controller.retomar_session_etp94(id_form)

        return result
    
    @app.route('/baixar_pdf_94', methods=['POST', 'GET'])
    def baixar_pdf_94():

        carregar_dados = carregar_pdf_94()
        quill_content = {}
        # Exemplo de uso:

        for etapa in range(1, 20):  # Loop para percorrer as 16 sessões
            conteudo_editor_94 = session.get(str(etapa), '')
            if etapa == 13:
                input_value_94 = request.args.get('valor')
                if input_value_94 is not None:
                    conteudo_editor_94 = input_value_94

            if conteudo_editor_94 is not None:
                if conteudo_editor_94.strip() == '' or conteudo_editor_94.strip() == '<br>':
                    conteudo_editor_94 = ' '  # Define como vazio se o conteúdo for vazio ou contiver apenas <br>
            else:
                conteudo_editor_94 = ' '

            quill_content[str(etapa)] = conteudo_editor_94

        temp_file_path = 'temp.html'

        output_path = 'static/pdf/etp94/etp94.pdf'
        sections = {
            'Informações Básicas': [1],
            'Necessidade': list(range(2, 8)),
            'Solução': list(range(8, 16)),
            'Planejamento': list(range(16, 18)),
            'Viabilidade': [18, 19]
        }
        quill_content = {
            '1': 'Informações Básicas',
            '2': 'Descrição da Necessidade',
            '3': 'Área Requisitante',
            '4': 'Necessidades de Negócio',
            '5': 'Necessidades Tecnológicas',
            '6': 'Demais Requisitos Necessários e Suficientes à Escolha da Solução de TIC',
            '7': 'Estimativa da Demanda - Quantidade de Bens e Serviço',
            '8': 'Levantamento de Soluções',
            '9': 'Análise Comparativa de Soluções',
            '10': 'Registro de Soluções Consideradas Inviáveis',
            '11': 'Análise Comparativa de Custos (TCO)',
            '12': 'Descrição da Solução de TIC a Ser Contratada',
            '13': 'Estimativa de Custo Total da Contratação',
            '14': 'Justificativa Técnica da Escolha da Solução',
            '15': 'Justificativa Econômica da Escolha da Solução',
            '16': 'Benefícios a Serem Alcançados com a Contratação',
            '17': 'Providências a Serem Adotadas',
            '18': 'Declaração de Viabilidade',
            '19': 'Responsáveis'
        }
        with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n')
            temp_file.write('<style>body { background-color: #FFFFFF; }</style>')  # Definindo o estilo de fundo
            temp_file.write('</head>\n<body>\n')
            
            for section_title, section_sessions in sections.items():
                temp_file.write(f'<div><h1>{section_title}</h1>\n')
                
                for session_number in section_sessions:
                    content = quill_content.get(str(session_number), '')
                    session_content = session.get(str(session_number), '')
                    
                    # Substitui <br> por " "
                    session_content = session_content.replace('<br>', ' ')

                    if session_content.strip() == '':
                        session_content = ' '
                    
                    temp_file.write(f'<h2>{session_number}. {content}</h2>\n')
                    temp_file.write(f'<p>{session_content}</p>\n')
                
                temp_file.write('</div>\n')
            
            temp_file.write('</body>\n</html>')

        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
        }
        


        pdf_bytes = pdfkit.from_file(temp_file_path, False, options=options)
        # Criar uma resposta com os bytes do PDF
        response = make_response(pdf_bytes)
        
        # Definir o cabeçalho Content-Type para application/pdf
        response.headers['Content-Type'] = 'application/pdf'
        
        # Definir o cabeçalho Content-Disposition para realizar o download do arquivo
        response.headers['Content-Disposition'] = 'attachment; filename=etp94.pdf'
        
        return response

    @app.route('/retomar_dados_import',methods=['POST', 'GET'])
    def retomar_dados_import():
        data = request.form  # Use .json diretamente para obter os dados

        processed_data = UserController.process_form_data(data)
        print(processed_data)
        
        usuario = processed_data['username']
        senha = processed_data['password']
        id_form = processed_data['id_form']
        etp= processed_data['etp']

        result, detalhe = ImportAuto.import_automatic_etp(usuario, senha, id_form, etp)
        # result = 'warning'
        # print('chamou etp40', result,' ', detalhe)
        
        if result == 'success':
            # return 'ok' #render_template('etp94/1informacao-94.html', status=status)
            return  jsonify({'status': 'success', 'message': 'Concluido com Sucesso', 'retorno': str(detalhe), 'tag':'success' })
        elif result == 'warning':
            return  jsonify({'status': 'success', 'message': 'Processo Não Completado', 'retorno': str(detalhe), 'tag':'warning'})
        else:
            return  jsonify({'status': 'error', 'message': 'Erro no Processo', 'error': str(detalhe)})
    
    @app.route('/retomar_dados_import_94',methods=['POST', 'GET'])
    def retomar_dados_import_94():
        data = request.form  # Use .json diretamente para obter os dados

        processed_data = UserController.process_form_data(data)
        print(processed_data)
        
        usuario = processed_data['username']
        senha = processed_data['password']
        id_form = processed_data['id_form']
        etp= processed_data['etp']

        result, detalhe = ImportAuto.import_automatic_etp(usuario, senha, id_form, etp)

        #print('chamou etp94', result,' ', session['13'])
        
        if result == 'success':
            #return 'ok' #render_template('etp94/1informacao-94.html', status=status)
            return  jsonify({'status': 'success', 'message': 'Concluido com Sucesso', 'retorno': str(detalhe), 'tag':'success' })
        elif result == 'warning':
            return  jsonify({'status': 'success', 'message': 'Processo Não Completado', 'retorno': str(detalhe), 'tag':'warning'})
        else:
            return  jsonify({'status': 'error', 'message': 'Erro no Processo', 'error': str(detalhe)})
       
    @app.route('/deletar_etp94',methods=['POST', 'GET'])
    def deletar_etp94():
        id_form = request.form.get('id_form') 
        # id_form = session['id_form']
        result = Etp94Controller.deletar_etp94(id_form)

        if result:
            print('deletou') 

        # return
        return redirect(url_for('admin.index'))
  
    @app.route('/deletar_etp40',methods=['POST', 'GET'])
    def deletar_etp40():
        id_form = request.form.get('id_form') 
        # id_form = session['id_form']
        result = Etp40Controller.deletar_etp40(id_form)

        if result:
            print('deletou') 

        # return
        return redirect(url_for('admin.index'))

    def limpar_sessoes():
        session.clear()


    return app
