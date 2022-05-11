from django.urls import path
from .views import List_medico, Update_medico, Create_medico

url_patterns = [
    path('', List_medico, name='list_medico'),
    path('new', Create_medico, name='create_medico'),
    path('Update', Update_medico, name='update_medico'),


]
#Crude de médicos