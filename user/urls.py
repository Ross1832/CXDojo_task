from django.urls import path
from .views import (upload_file,
                    ListUserView,
                    UpdateUserView,
                    DeleteUserView,
                    DetailUserForm,
                    CreateUserView,
                    export_csv, )

app_name = 'user'

urlpatterns = [
    path('', ListUserView.as_view(), name='list'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailUserForm.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='delete'),
    path('upload/', upload_file, name='upload'),
    path('export_csv/', export_csv, name='export-csv'),
]
