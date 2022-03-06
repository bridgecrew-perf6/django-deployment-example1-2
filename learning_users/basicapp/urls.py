from django.conf.urls import url
from basicapp import views

# teplate url is
app_name = "basicapp"
urlpatterns = [
    url(r"^registration/$", views.registration, name="registration"),
    url(r"^user_login/$", views.user_login, name="user_login"),
]
