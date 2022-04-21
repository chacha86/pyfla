from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from ..models import Question
from ..forms import AnswerForm, QuestionForm

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list() :
    question_list = Question.query.order_by(Question.create_date.desc())
    print(question_list)
    return render_template('question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id) :
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit() :
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('question_form.html', form=form)