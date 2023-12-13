from rest_framework.paginations import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3 
    
