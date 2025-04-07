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

        # --- Kirim request ke FastAPI ---
        fastapi_url = 'http://localhost:8001/predict_proba'  # sesuaikan port FastAPI
        payload = {
            "content": content,
            "category_name": category,
            "createdAt": created_at
        }

        try:
            response = requests.post(fastapi_url, json=payload)
            prediction_result = response.json()
        except Exception as e:
            return JsonResponse({"error": "Failed to call prediction API", "detail": str(e)}, status=500)

        # Ambil label dengan skor tertinggi
        probs = prediction_result.get('probabilities', {})
        top_label = max(probs, key=probs.get)
        top_confidence = probs[top_label]

        # Simpan ke database
        report = Report.objects.create(
            code=f"JK{uuid.uuid4().hex[:10].upper()}",
            content=content,
            category_name=category,
            is_privacy=data.get('is_privacy', False),
            latitude=data.get('lat'),
            longitude=data.get('lng'),
            predicted_zone_name=top_label,
            confidence_score=top_confidence,
        )

        return JsonResponse({
            "status": "success",
            "prediction": top_label,
            "confidence": top_confidence,
            "report_id": str(report.id),
            "probabilities": probs
        })

    return JsonResponse({"error": "Invalid method"}, status=400)


def predict_form(request):
    return render(request, 'reports/predict.html')

