from django.urls import path
from .views import StockDetailView

urlpatterns = [
    path('<str:symbol>/', StockDetailView.as_view(), name='stock-data'),
]