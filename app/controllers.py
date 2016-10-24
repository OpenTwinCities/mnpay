from app import app, models, db
from flask import request, jsonify, render_template

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
    def_limit = 100
    limit = min(int(request.args.get("limit", def_limit)), def_limit)
    cont = int(request.args.get("batch_continue", 0))
    query = _construct_salary_query(request.args)
    query = query.filter(Salary.id > cont)
    result = [s for s in query.order_by(Salary.id).limit(limit)]
    to_return = {
        "data": [s.serialize() for s in result],
    }
    if len(result) > 0:
        max_id = result[-1].id
        to_return["batch_continue"] = max_id + 1
    return jsonify(to_return)


@app.route("/api/add_salary", methods=["post"])
def add_salary():
    first_name = request.args.get('first_name', "")
    last_name = request.args.get('last_name', "")
    agency = request.args.get('agency', "")
    dept = request.args.get('dept', "")
    wages = request.args.get('wages', "")
    year = request.args.get('year', "")
    title = request.args.get('title', "")
    s = models.Salary(first_name=first_name,
                      last_name=last_name,
                      agency=agency,
                      dept=dept,
                      wages=wages,
                      year=year,
                      title=title)
    db.session.add(s)
    db.session.commit()
    return jsonify(data="Success", status="OK")


@app.route("/")
def index():
    return render_template("index.html")
