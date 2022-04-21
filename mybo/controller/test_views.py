from ast import keyword
from datetime import datetime
from mybo import db
from mybo.models import *
from flask import Blueprint, render_template, request, url_for, session, flash, g
from werkzeug.utils import redirect
from mybo.forms.article_forms import ArticleForm, MemberForm, LoginForm

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('list')
def list_test() :
    # keyword = request.args['keyword']
    page = request.args.get('page', type=int, default=1)
    article_list = db.session.query(Article).order_by(Article.reg_date.desc())
    # if not keyword:
    #     article_list = db.session.query(Article).filter(Article.title.like('%{}%'.format(keyword)))
    article_list = article_list.paginate(page, per_page=10)
    return render_template('articles/list.html', article_list=article_list) 

@bp.route('gugu')
def gugu_test() :
    return render_template('test/gugu.html') 

@bp.route('detail/<int:article_id>/')
def detail_test(article_id) :

    article = db.session.query(Article).filter(Article.article_id == article_id).first()
    return render_template('articles/detail.html', article=article) 

@bp.route('article_form/', methods=('GET', 'POST'))
def article_form() :
    form = ArticleForm()
    if request.method == 'POST' and form.validate_on_submit() :
        title = form.title.data
        body = form.body.data
        member_id = form.member_id.data
        member = db.session.query(Member).filter(Member.member_id == member_id).first()
        article = Article(title=title, body=body, member=member, reg_date=datetime.now(), hit=0, board_id=1)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('test.list_test'))

    return render_template('articles/article_form.html', form=form)

@bp.route("create_test")
def test_data() :

    member = db.session.query(Member).filter(Member.member_id == 1).first()
    for i in range(300) :
        a = Article(title="테스트 데이터입니다.[%03d]" % i, body='내용무', member = member, reg_date=datetime.now(), hit=0, board_id=1)
        db.session.add(a)

    db.session.commit()
    return redirect(url_for('test.list_test'))

@bp.route('/search')
def search():
    keyword = request.args["keyword"]
    page = request.args.get('page', type=int, default=1)
    article_list = db.session.query(Article).filter(Article.title.like('%{}%'.format(keyword)))
    article_list = article_list.paginate(page, per_page=10)
    
    return render_template('articles/list.html', article_list=article_list)

@bp.before_app_request
def ssss() :
    print('aaaaaaaa')

@bp.before_app_request
def load_logged_in_user() :
    member_id = session.get('member_id')
    if member_id is None :
        g.member = None
    else :
        g.member = db.session.query(Member).get(member_id)

@bp.route('login', methods=("POST", "GET"))
def login() :
    form = LoginForm()
    print(form.validate_on_submit())
    print(request.method)
    if request.method == "POST" and form.validate_on_submit() :
        member = get_login_member(form)
        print(member)
        error = None 
        if member == None :
            error = "잘못된 회원정보입니다."
        else :
            session.clear()
            session['member_id'] = member.member_id
            return redirect(url_for('test.list_test'))
        flash(error)
        
    return render_template('members/login_form.html', form=form) 

def get_login_member(form:LoginForm) :
    login_id = form.login_id.data
    login_pw = form.login_pw.data

    member = db.session.query(Member).filter(Member.login_id == login_id and Member.login_pw == login_pw).first()

    return member
    
@bp.route('signup', methods=("POST", "GET"))
def signup() :
    form = MemberForm()
    print(request.method)
    print(form.validate_on_submit())
    if request.method == "POST" and form.validate_on_submit() :
        member = add_member(form)
        db.session.add(member)
        db.session.commit()

        return redirect(url_for('test.list_test'))
    return render_template('members/member_form.html', form=form)    

def add_member(form:MemberForm) :
    login_id = form.login_id.data
    login_pw = form.login_pw.data
    nick_name = form.nick_name.data
    real_name = form.real_name.data
    reg_date = datetime.now()

    return Member(login_id=login_id, login_pw=login_pw, nick_name=nick_name, real_name=real_name, reg_date=reg_date)
    
@bp.route('extends')
def extends() :
    
    return render_template('test/extendsTest.html')

@bp.route('include')
def include() :
    return render_template('test/includeTest.html')

    
result = 0
@bp.route("accumulate/<int:num>")
def accumulate(num) :
    global result
    result += num

    return str(result)
