from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SurveyResponse
import json
import random
# import forbackend

@csrf_exempt
def save_survey_response(request):
    if request.method == 'POST':
        # Parse the JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        # print(request.body)
        # Create a new SurveyResponse object and save it to the database
        t=random.randint(0,1)
        try:
            survey_response = SurveyResponse.objects.create(
                age=data.get('age'),
                gender=data.get('gender'),
                country=data.get('country'),
                state=data.get('state'),
                self_employed=data.get('self_employed'),
                family_history=data.get('family_history'),
                treatment=data.get('treatment'),
                work_interfere=data.get('work_interfere'),
                no_employees=data.get('no_employees'),
                remote_work=data.get('remote_work'),
                tech_company=data.get('tech_company'),
                benefits=data.get('benefits'),
                care_options=data.get('care_options'),
                wellness_program=data.get('wellness_program'),
                seek_help=data.get('seek_help'),
                anonymity=data.get('anonymity'),
                leave=data.get('leave'),
                mental_health_consequence=data.get('mental_health_consequence'),
                phys_health_consequence=data.get('phys_health_consequence'),
                coworkers=data.get('coworkers'),
                supervisor=data.get('supervisor'),
                mental_health_interview=data.get('mental_health_interview'),
                phys_health_interview=data.get('phys_health_interview'),
                mental_vs_physical=data.get('mental_vs_physical'),
                obs_consequence=data.get('obs_consequence'),
                comments=data.get('comments', '')
            )
            return JsonResponse({'message': 'Survey response saved successfully','verdict':t})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)