from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('snkrs/', views.snkr_index, name='snkr-index'),
    path('snkrs/<int:snkr_id>/', views.snkr_detail, name='snkr-detail'),
    path('snkrs/create/', views.SnkrCreate.as_view(), name='snkr-create'),
    path('snkrs/<int:pk>/update/', views.SnkrUpdate.as_view(), name='snkr-update'),
    path('snkrs/<int:pk>/delete/', views.SnkrDelete.as_view(), name='snkr-delete'),
    path('snkrs/<int:snkr_id>/add-cleaning/', views.add_cleaning, name='add-cleaning'),
    path('accounts/signup/', views.signup, name='signup'),

]  
