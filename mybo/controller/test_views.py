from datetime import datetime
from mybo import db
from mybo.models import *
from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('gugu')
def gugu_test() :
    return render_template('test/gugu.html') 

@bp.route("create_test")
def test_data() :

    member = db.session.query(Member).filter(Member.member_id == 1).first()
    for i in range(300) :
        a = Article(title="테스트 데이터입니다.[%03d]" % i, body='내용무', member = member, reg_date=datetime.now(), hit=0, board_id=1)
        db.session.add(a)

    db.session.commit()
    return redirect(url_for('test.list_test'))

   
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

@bp.route('url_for')
def _url_for() :
    dic1 = {
        "key1" : "aaa"
    }
    str2 = url_for('test.list_test', data=dic1)
    print(str2)

    return str2