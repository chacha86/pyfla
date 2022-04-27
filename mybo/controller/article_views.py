from datetime import datetime
from mybo import db
from mybo.models import *
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from mybo.forms.article_forms import ArticleForm

bp = Blueprint('article', __name__, url_prefix='/article')

@bp.route('list')
def _list() :
    keyword = request.args.get('keyword', type=str, default='')
    page = request.args.get('page', type=int, default=1)
    article_list = db.session.query(Article).order_by(Article.reg_date.desc())
    if keyword != None:
        article_list = db.session.query(Article).filter(Article.title.like('%{}%'.format(keyword)))
    print(article_list)
    article_list = article_list.paginate(page, per_page=10)
    return render_template('articles/list.html', article_list=article_list, keyword=keyword) 

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
        return redirect(url_for('article._list'))

    return render_template('articles/article_form.html', form=form)

@bp.route('/search')
def search():
    keyword = request.args["keyword"]
    page = request.args.get('page', type=int, default=1)
    article_list = db.session.query(Article).filter(Article.title.like('%{}%'.format(keyword)))
    article_list = article_list.paginate(page, per_page=10)
    
    return render_template('articles/list.html', article_list=article_list)

