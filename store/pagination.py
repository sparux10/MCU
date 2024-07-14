from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # عدد العناصر لكل صفحة
    page_size_query_param = 'page_size'
    max_page_size = 300  # حد أقصى لحجم الصفحة