from app import app, models, db
from flask import request, jsonify, render_template, url_for
from urllib.parse import urlencode


Salary = models.Salary
QUERY_PARAMS = [
    "agency",
    "dept",
    "first_name",
    "middle_name",
    "last_name",
    "title",
]


def _construct_salary_query(args):
    query = Salary.query
    for key in QUERY_PARAMS:
        if key not in args:
            continue
        q_str = r"{0}%".format(args[key])
        query = query.filter(getattr(Salary, key).like(q_str))
    return query


@app.route("/api/salaries")
def get_salaries():
    return jsonify(_get_salaries(request.args))


def _get_salaries(query_params):
    def_limit = 50
    limit = min(int(query_params.get("limit", def_limit)), def_limit)
    page_number = int(query_params.get("page", 1))
    query = _construct_salary_query(query_params)
    page = query.paginate(page=page_number, per_page=limit)
    result = [s for s in page.items]
    to_return = {
        "data": [s.serialize() for s in result],
    }
    if page_number + 1 <= page.pages:
        to_return["next_page"] = page_number + 1
    if 1 <= page_number - 1:
        to_return["prev_page"] = page_number - 1
    return to_return


@app.route("/")
def index():
    return render_template("index.html")
