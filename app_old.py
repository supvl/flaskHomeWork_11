from utils import get_all, get_by_pk, get_by_skill
from flask import Flask


app = Flask(__name__)


# Выводим на главную страницу список всех кандидатов
@app.route("/")
def main_page():
    withdrawing_all_candidates = get_all()
    return withdrawing_all_candidates


# Выводим на страницу "/candidates/<x>" данные кандидата с персональным номером "х"
@app.route("/candidates/<int:pk>")
def select_one_candidate(pk):
    one_candidate = get_by_pk(pk)
    return one_candidate


# Выводим на страницу "skills/<skill>" данные кандидатов с заданным скилом "skill"
@app.route("/skills/<skill>")
def select_skill_candidate(skill):
    skill_candidate = get_by_skill(skill)
    return skill_candidate


app.run()
