import pandas as pd
from .models import CsvData
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CsvDataSerializer

def index(request):
    return HttpResponse('boże, to się stało.')

def chart_view(request):
    csv_file_path = r'D:\OneDrive\Desktop\PrądoRys\static\data.csv'
    
    df = pd.read_csv(csv_file_path)
    
    chart_data = {
        'labels': df['time'].tolist(),
        'max_current': df['max current'].tolist(),
        'average_current': df['average current'].tolist()
    }
    x_min = min(df['time'].tolist())
    x_max = max(df['time'].tolist())
    return render(request, 'chart.html', {'chart_data': chart_data, 'x_max': x_max,'x_min': x_min})

@csrf_exempt
def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        df = pd.read_csv(uploaded_file)
        
        CsvData.objects.all().delete()
        
        for _, row in df.iterrows():
            CsvData.objects.create(
                time=row['time'],
                max_current=row['max current'],
                avg_current=row['average current']
            )
        return JsonResponse({'message': 'File uploaded and data saved to database successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@api_view(['GET'])
def read_chart_data(request):
    if request.method == 'GET':
        chart_data = CsvData.objects.all()
        serializer = CsvDataSerializer(chart_data, many=True)
        return Response(serializer.data)
    