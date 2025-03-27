from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('about',views.about,name='about'),
    path('edit/<int:pk>/', views.edit,name='edit'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('history/',views.history,name="history"),
    path('delete_all_history',views.delete_all_history,name='delete_all_history'),
    path('restore_all_history/',views.restore_all_history,name='restore_all_history'),
    path('delete_history/<int:pk>/',views.delete_history,name='delete_history'),
    path('details/<int:pk>/',views.details,name='details')
]
