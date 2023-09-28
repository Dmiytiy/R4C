
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Robot


@csrf_exempt
def create_robot(request):
    #Добавление в базу данных при помощи метода POST
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            model = data.get('model')
            version = data.get('version')
            created = data.get('created')

            # Валидация данных здесь

            robot = Robot(model=model, version=version, created=created)
            robot.save()

            return JsonResponse({'message': 'Робот успешно создан '})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    elif request.method == 'GET':
        # Обработка GET-запроса
        robots = Robot.objects.all()
        my_robots = [{'model': robot.model, 'version': robot.version, 'created': robot.created} for robot in
                             robots]
        return JsonResponse({'robots': my_robots})
    return JsonResponse({'error': 'Недопустимый метод запроса'}, status=405)
