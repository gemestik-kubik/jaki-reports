import uuid
from django.http import JsonResponse
from .models import Report
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def predict_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '')

        # Dummy prediksi
        prediction = "DINAS SUMBER DAYA AIR"
        confidence = 0.82

        report = Report.objects.create(
            code=f"JK{uuid.uuid4().hex[:10].upper()}",
            content=content,
            category_name=data.get('category'),
            is_privacy=data.get('is_privacy', False),
            latitude=data.get('lat'),
            longitude=data.get('lng'),
            predicted_zone_name=prediction,
            confidence_score=confidence,
        )

        return JsonResponse({
            "status": "success",
            "prediction": prediction,
            "confidence": confidence,
            "report_id": str(report.id),
        })
    return JsonResponse({"error": "Invalid method"}, status=400)
