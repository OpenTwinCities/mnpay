from app import app, models, db
from flask import request, jsonify, render_template, url_for
from urllib.parse import urlencode


Salary = models.Salary
QUERY_PARAMS = [
    "agency",
    "dept",
    "first_name",
    "last_name",
    "title",
]
SORTABLE_FIELDS = [
    "agency",
    "dept",
    "first_name",
    "last_name",
    "title",
    "wages"
]
DIRECTIONS = [
    "desc",
    "asc"
]


def _construct_salary_query(args):
    query = Salary.query
    for key in QUERY_PARAMS:
        if key not in args:
            continue
        q_str = r"{0}%".format(args[key])
        query = query.filter(getattr(Salary, key).like(q_str))
    query = _apply_order_to_query(query,
                                  args.get("sortby", None),
                                  args.get("direction", None))
    return query


def _apply_order_to_query(query, field, direction):
    if field in SORTABLE_FIELDS:
        model_field = getattr(Salary, field)
        if direction in DIRECTIONS:
            order_func = getattr(model_field, direction)
            query = query.order_by(order_func())
        else:
            query = query.order_by(model_field)
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
