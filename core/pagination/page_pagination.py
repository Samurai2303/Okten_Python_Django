import math

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        total_items = self.page.paginator.count
        total_pages = math.ceil(total_items / self.get_page_size(self.request))
        return Response({
            'total_items': total_items,
            'total_pages': total_pages,
            'prev': self.get_previous_link(),
            'next': self.get_next_link(),
            'data': data
        }, status=status.HTTP_200_OK)
