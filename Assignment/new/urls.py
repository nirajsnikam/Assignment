from django.contrib import admin
from django.urls import path
from .import views
from .views import registration
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registration, name='registration'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('search_and_delete_by_name/', views.search_and_delete_by_name, name='search_and_delete_by_name'),
    path('search_and_update_by_name/', views.search_and_update_by_name, name='search_and_update_by_name'),
    path('generate_access_token/<int:user_id>/', views.generate_access_token, name='generate_access_token'),

]