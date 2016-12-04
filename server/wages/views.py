from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wages.models import Wage


DEFAULT_LIMIT = 50

SINGLE_SIDED_QUERY_PARAMS = [
    "first_name",
    "last_name",
]
FOREIGN_QUERY_PARAMS = [
    "agency",
    "dept",
    "title",
]
STRICT_QUERY_PARAMS = [
    "year",
]
SORTABLE_FIELDS = [
    "agency",
    "dept",
    "first_name",
    "last_name",
    "title",
    "wage",
    "year"
]
DIRECTIONS = {
    "desc": "-",
    "asc": ""
}


def _construct_wage_query(query_params):
    query = Wage.objects
    params = {}
    for key in SINGLE_SIDED_QUERY_PARAMS:
        if key not in query_params:
            continue
        params["{0}__istartswith".format(key)] = query_params[key]
    for key in FOREIGN_QUERY_PARAMS:
        if key not in query_params:
            continue
        params["{0}__name__icontains".format(key)] = query_params[key]
    for key in STRICT_QUERY_PARAMS:
        if key not in query_params:
            continue
        params["{0}".format(key)] = query_params[key]
    query = query.filter(**params)
    query = _apply_order_to_query(query,
                                  query_params.get("sortby", None),
                                  query_params.get("direction", None))
    return query


def _apply_order_to_query(query, field, direction):
    dir_sig = ""
    if direction in DIRECTIONS:
        dir_sig = DIRECTIONS[direction]
    if field in SORTABLE_FIELDS:
        order_str = "{dir_sig}{field}".format(
            dir_sig=dir_sig,
            field=field
        )
        query = query.order_by(order_str)
    return query


def get_wages(request):
    return JsonResponse(_get_wages_serialized(request.GET))


def _get_wages_serialized(query_params):
    req_limit = _safe_cast(query_params.get("limit"),
                           int,
                           DEFAULT_LIMIT)
    if req_limit < 1:
        req_limit = DEFAULT_LIMIT
    limit = min(req_limit, DEFAULT_LIMIT)
    query = _construct_wage_query(query_params)
    paginator = Paginator(query, limit)

    min_page = 1
    req_page = _safe_cast(query_params.get("page", 1),
                          int,
                          min_page)
    page_number = _shift_to_interval(req_page, min_page, paginator.num_pages)
    wages = paginator.page(page_number)

    result = [w for w in wages]
    to_return = {
        "data": [w.serialize() for w in result],
    }
    to_return["cur_page"] = wages.number
    to_return["last_page"] = paginator.num_pages
    return to_return


def _safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def _shift_to_interval(val, min_point, max_point):
    if val < min_point:
        val = min_point
    elif val > max_point:
        val = max_point
    return val
