from django.urls import path
from .views import note_list, note_create, note_update, note_delete

urlpatterns = [
    path('notes/', note_list, name='note_list'),
    path('notes/create/', note_create, name='note_create'),
    path('notes/update/<int:pk>/', note_update, name='note_update'),
    path('notes/delete/<int:pk>/', note_delete, name='note_delete'),
]
