from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("submit", views.submit_reason, name="submit"),
    path("modrate", views.modrate_reasons, name="approve reason"),
    path("approve_reason/<int:reason_id>", views.approved, name="approved"),
    path("denie_reason/<int:reason_id>", views.denied, name="approved"),
]
