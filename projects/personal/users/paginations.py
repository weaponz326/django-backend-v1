from django.conf import settings

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class TablePagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })
