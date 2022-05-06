from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

db = None
migrate = None 

def create_app() :    
    app = Flask(__name__)
    # app.config.from_object(myconfig)
    app.config.from_envvar('APP_CONFIG_FILE')
    # BASE_DIR = os.path.dirname(__file__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'mybo.db'))
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SECRET_KEY'] = "dev"
    global db
    global migrate

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    from . import models
    # from .models import Question, Person
    
    # if Question.query.count() == 0 :
    #     data_init(db)

    # if Person.query.count() == 0 :
    #     data_init2(db)
        
    from .controller import home_controller, test_views, article_views, member_views

    app.register_blueprint(home_controller.bp)
    app.register_blueprint(article_views.bp)
    app.register_blueprint(member_views.bp)
    # app.register_blueprint(question_controller.bp)
    # app.register_blueprint(answer_views.bp)
    app.register_blueprint(test_views.bp)

    return app


# def data_init(db:SQLAlchemy) :
#     from datetime import datetime 
#     from .models import Question, Answer

#     q1 = Question(subject='플라스크 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())
#     q2 = Question(subject='나는 할 수 있다. 욕심 내지 말고..', content='난 왜 잘하죠?', create_date=datetime.now())
#     a1 = Answer(question=q1, content='네 자동으로 생성됩니다.', create_date=datetime.now())
#     a2 = Answer(question=q2, content='당신은 천재니까요.', create_date=datetime.now())

#     db.session.add(q1)
#     db.session.add(q2)
#     db.session.add(a1)
#     db.session.add(a2)
#     db.session.commit()
    

# def data_init2(db:SQLAlchemy) :
#     from .models import Car, Person
#     p1 = Person(name="홍길동", address="대전", age=20)
#     c1 = Car(model="모닝", price=1000, color="은색", person=p1)
#     c2 = Car(model="아반떼", price=2000, color="검정색", person=p1)
#     c3 = Car(model="싼타페", price=3000, color="파란색", person=p1)

#     db.session.add(p1)
#     db.session.add(c1)
#     db.session.add(c2)
#     db.session.add(c3)
#     db.session.commit()

       