from django.urls import path
from . import views
app_name='plants'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('all/', views.plant_list_view, name='plant_list_view'),
    path('<int:plant_id>/detail/', views.plant_detail_view, name='plant_detail_view'),
    path('new/', views.add_plant_view, name='add_plant_view'),
    path('<int:plant_id>/update/', views.update_plant_view, name='update_plant_view'),
    path('<int:plant_id>/delete/', views.delete_plant_view, name='delete_plant_view'),
    path('search/', views.search_plants_view, name='search_plants_view'),
]