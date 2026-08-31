from rest_framework.pagination import PageNumberPagination

class CustomPaginator(PageNumberPagination):
    page_size = 100                     # Default amount returned per page
    max_page_size = 1000                # Maximum amount a user can request
    page_size_query_param = 'page_size' # Allows client to change amount via URL (?page_size=20)
