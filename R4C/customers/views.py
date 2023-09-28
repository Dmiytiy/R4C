import pandas as pd
from robots.models import Robot
from django.http import HttpResponse


def create_robot_data_excel(request):
    if request.method == 'GET':
        # Обработка GET-запроса
        robots = Robot.objects.all()

        # Преобразование данных в DataFrame/Created имеет формат datatime, поэтому пришлось преобразовать
        data = {
            'Serial': [robot.serial for robot in robots],
            'Model': [robot.model for robot in robots],
            'Version': [robot.version for robot in robots],
            'Created': [robot.created.replace(tzinfo=None) for robot in robots],
        }

        df = pd.DataFrame(data)

        # Создание Excel-файла
        excel_file = "robot_data.xlsx"
        df.to_excel(excel_file, index=False, engine='openpyxl')

        # Отправить файл пользователю
        with open(excel_file, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{excel_file}"'

        return response

