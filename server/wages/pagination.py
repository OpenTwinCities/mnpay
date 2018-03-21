from rest_framework import pagination
from rest_framework import response


class RawPageNumberPagination(pagination.PageNumberPagination):

    def _get_previous_page(self):
        if not self.page.has_previous():
            return None
        return self.page.previous_page_number()

    def _get_next_page(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_paginated_response(self, data):
        return response.Response({
            'next': self._get_next_page(),
            'previous': self._get_previous_page(),
            'current': self.page.number,
            'count': self.page.paginator.count,
            'results': data
        })
