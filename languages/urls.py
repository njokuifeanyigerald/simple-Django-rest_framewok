
from django.urls import path, include
from  rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)

urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),


]
