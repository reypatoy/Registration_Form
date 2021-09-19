from django.urls import path


from . import views

app_name = "admin_panel"

urlpatterns = [
    path('add_account/',views.create_account,name="create_account"),
    path('login/',views.login_view, name="login_view"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('logout/',views.logout_view, name="logout_view")
    ]