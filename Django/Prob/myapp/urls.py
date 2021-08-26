from django.urls import path
from .views import NewPage, RubricPage

urlpatterns = [
    path('mane_page/', NewPage.as_view(), name='mane_page'),
    path('<int:rubric_id>/', RubricPage.as_view(), name='rubric_page'),
]