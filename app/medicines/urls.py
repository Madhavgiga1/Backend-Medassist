from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include
)
from medicines import views
router=DefaultRouter()
app_name='medicines'

router.register('medicine',views.MedicinesViewSet)