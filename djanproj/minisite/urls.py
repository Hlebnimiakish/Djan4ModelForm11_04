from django.urls import path
from minisite.views import HomepageView, AddingFormView

urlpatterns = [
    path('home/', HomepageView.as_view(), name='homepage'),
    path('add/', AddingFormView.as_view(), name='adding'),
]