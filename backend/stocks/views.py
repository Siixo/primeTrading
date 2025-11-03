import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import StockSerializer
from django.conf import settings

class StockDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={settings.ALPHA_VANTAGE_API_KEY}'
        response = requests.get(url)
        data = response.json().get('Time Series (Daily)', {})

        processed = []
        for date, values in data.items():
            processed.append({
                'date': date,
                'open': float(values['1. open']),   
                'high': float(values['2. high']),
                'low': float(values['3. low']),
                'close': float(values['4. close']),
                'volume': int(values['5. volume']),
            })
        serializer = StockSerializer(data=processed, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)