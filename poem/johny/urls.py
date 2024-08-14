from django.urls import path
from johny import views
urlpatterns=[
    path('<str:x>',views.one)
] 