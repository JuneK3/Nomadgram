from django.conf.urls import url
from . import views
from nomadgram.users import serializers as user_serializers
app_name = "notifications"

urlpatterns = [
    url(
        regex=r'^$',
        view=views.Notifications.as_view(),
        name='notifications'
    )
]
