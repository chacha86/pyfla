from mybo import db

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     subject = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text(), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)

# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
#     question = db.relationship('Question', backref=db.backref('answer_set'))
#     content = db.Column(db.Text(), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)

# class Person(db.Model) :
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     address = db.Column(db.String(50), nullable=False)
#     age = db.Column(db.Integer, nullable=False)

# class Car(db.Model) :
#     id = db.Column(db.Integer, primary_key=True)
#     model = db.Column(db.String(30), nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     color = db.Column(db.String(30), nullable=False)
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id', ondelete='CASCADE'))
#     person = db.relationship('Person', backref=db.backref('car_set'))

class Board(db.Model) :
    board_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    reg_date = db.Column(db.DateTime(), nullable=False)


class Article(db.Model) :
    article_id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    member = db.relationship('Member', backref=db.backref('article_list'))
    hit = db.Column(db.Integer, nullable=False)
    reg_date = db.Column(db.DateTime(), nullable=False)

class Member(db.Model) :
    member_id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.String(200), nullable=False)
    login_pw = db.Column(db.String(200), nullable=False)
    nick_name = db.Column(db.String(200), nullable=False)
    real_name = db.Column(db.String(200), nullable=False)
    reg_date = db.Column(db.DateTime(), nullable=False)

class ArticleReply(db.Model) :
    reply_id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'), nullable=False)
    article = db.relationship('Article', backref=db.backref('reply_list'))
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    member = db.relationship('Member', backref=db.backref('reply_list'))
    reg_date = db.Column(db.DateTime(), nullable=False)

