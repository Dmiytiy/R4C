
from django.http import JsonResponse
from django.core.mail import send_mail

#from robots.models import Robot
from orders.models import Order


def send_mail(request):
    robot_serial = request.GET.get('serial')  # Получаем серийный номер робота из параметров запроса

    orders = Order.objects.filter(robot_serial=robot_serial)

    if orders.exists():
        # Робот найден в заказах, отправляем сообщение о наличии
        message = f'Добрый день!\nНедавно вы интересовались нашим роботом модели {robot.model}, версии {robot.version}.' \
                  f'\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами'
        #возвращаем ответ на почту от которого пришёл запрос
        send_mail(message, 'romanov230198d@yandex.ru', [request.user.email])



    return JsonResponse({'status': 'success', 'message': 'Сообщение отправлено'})