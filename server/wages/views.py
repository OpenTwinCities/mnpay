from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wages.models import Wage


def index(request):
    return HttpResponse("Hello world. You're at the polls index.")


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
    def_limit = 50
    limit = min(int(query_params.get("limit", def_limit)), def_limit)
    page_number = query_params.get("page", 1)
    query = _construct_wage_query(query_params)
    paginator = Paginator(query, limit)
    try:
        wages = paginator.page(page_number)
    except PageNotAnInteger:
        wages = paginator.page(1)
    except EmptyPage:
        wages = paginator.page(paginator.num_pages)
    result = [w for w in wages]
    to_return = {
        "data": [w.serialize() for w in result],
    }
    to_return["cur_page"] = page_number
    to_return["last_page"] = paginator.num_pages
    return to_return
