import uuid
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Report
from django.shortcuts import render

@csrf_exempt
def predict_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        content = data.get('content', '')
        category = data.get('category', '')
        created_at = data.get('createdAt', '')
        latitude = data.get('lat')
        longitude = data.get('lng')
        is_privacy = data.get('is_privacy', False)

        payload = {
            "content": content,
            "category_name": category,
            "createdAt": created_at
        }

        fastapi_urls = [
            'http://localhost:8001/predict_proba',
            'https://jaki-reports-ai.up.railway.app/predict_proba',
        ]

        for url in fastapi_urls:
            try:
                response = requests.post(url, json=payload, timeout=5)
                response.raise_for_status()
                prediction_result = response.json()
                break
            except Exception as e:
                prediction_result = None
                continue

        if not prediction_result:
            return JsonResponse({"error": "Gagal memanggil semua endpoint FastAPI"}, status=500)

        probs = prediction_result.get('probabilities', {})
        top_label = max(probs, key=probs.get)
        top_confidence = probs[top_label]

        return JsonResponse({
            "status": "success",
            "prediction": top_label,
            "confidence": top_confidence,
            "report_id": "preview-mode",
            "probabilities": probs
        })

    return JsonResponse({"error": "Invalid method"}, status=400)


def predict_form(request):
    return render(request, 'predict.html')

