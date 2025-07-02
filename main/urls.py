from django.urls import path
from . import views
from .views import generate_sql_view

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("db/connect/", views.db_connect, name="db_connect"),
    path("db/<int:db_id>/query/", views.query, name="query"),
    path("db/<int:db_id>/history/", views.query_history, name="history"),
    path('generate-sql/', generate_sql_view, name='generate_sql'),
    path('db/delete/<int:db_id>/', views.db_delete, name='db_delete'),
    path('history/<int:db_id>/clear/', views.clear_history, name='clear_history'),
    path('db/<int:db_id>/overview/', views.db_overview, name='db_overview'),
]