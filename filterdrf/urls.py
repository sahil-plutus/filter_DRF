from django.contrib import admin
from django.urls import include, path
# from rest_framework.routers import DefaultRouter
from home import views


# router = DefaultRouter()

# router.register('stu', views.StudentApi, basename = "student")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/', views.StudentApi.as_view()),
]
