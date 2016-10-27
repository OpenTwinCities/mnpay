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
    page = query.paginate(page=page_number, per_page=def_limit)
    result = [s for s in page.items]
    to_return = {
        "data": [s.serialize() for s in result],
    }
    if page_number + 1 <= page.pages:
        to_return["next_page"] = page_number + 1
    if 1 <= page_number - 1:
        to_return["prev_page"] = page_number + 1
    return to_return


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
    print("foo")
    return render_template("index.html")


@app.route("/noreact")
def no_react():
    args = {}
    for key in request.args:
        args[key] = request.args.get(key)
    template_params = {}
    salary_data = _get_salaries(args)
    print(args.keys())
    template_params["data"] = salary_data["data"]
    if "next_page" in salary_data:
        args["page"] = salary_data["next_page"]
        next_url = url_for("no_react", **args)
        template_params["next_url"] = next_url
    if "prev_page" in salary_data:
        args["page"] = salary_data["prev_page"]
        prev_url = url_for("no_react", **args)
        template_params["prev_url"] = prev_url
    print(template_params.keys())
    return render_template("no_react.html",
                           **template_params)
