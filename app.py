from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def display_candidates_list():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route('/candidate/<int:id>/')
def display_candidate_id(id):
    candidate = get_candidate_by_id(id)
    if not candidate:
        return 'Нет такого кандидата'
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>/')
def display_candidate_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    if not candidates:
        return 'Нет кандидатов с таким именем'
    return render_template("search.html", candidates=candidates)


@app.route('/skill/<skill_name>/')
def display_candidate_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    if not candidates:
        return 'Нет кандидатов с такими скиллами'
    return render_template("skill.html", skill_name=skill_name, candidates=candidates)


if __name__ == '__main__':
    app.run()
