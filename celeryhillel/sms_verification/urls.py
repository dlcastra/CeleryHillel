from django.urls import path

from sms_verification import views


urlpatterns = [
    path("", views.send_sms_view, name="send_sms_view"),
    path("success/", views.success, name="success"),
]
