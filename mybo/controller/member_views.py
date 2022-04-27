from flask import Blueprint, session, request, url_for, render_template, flash, g
from werkzeug.utils import redirect
from mybo.forms.member_forms import LoginForm, MemberForm
from mybo.models import Member
from mybo import db

from datetime import datetime
bp = Blueprint('member', __name__, url_prefix='/member')

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
            return redirect(url_for('article._list'))
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

        return redirect(url_for('article._list'))
    return render_template('members/member_form.html', form=form)    

def add_member(form:MemberForm) :
    login_id = form.login_id.data
    login_pw = form.login_pw.data
    nick_name = form.nick_name.data
    real_name = form.real_name.data
    reg_date = datetime.now()

    return Member(login_id=login_id, login_pw=login_pw, nick_name=nick_name, real_name=real_name, reg_date=reg_date)
 