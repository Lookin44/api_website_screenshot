import os

import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .models import Tasks
from .serializers import TasksSerializer

# Настройки web-драйвера
path = f'{os.getcwd()}/chromedriver'
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
browser = webdriver.Chrome(
    executable_path=path,
    options=options
)


# Блок функций по созданию скриншотов
def screenshot(urls):
    """Открытие ссылки и создание скриншота"""
    try:
        file_name = 0
        for link in urls:
            browser.get(link)
            browser.save_screenshot(f'photo/{file_name}.png')
            file_name += 1
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()


def check_nesting_level(url, level):
    """Проверка ссылки на уровень вложеннсти, если она привышает его,
    то функция обрезает ссылку до задонного уровня"""
    if len(url.split('/')) - 3 < level:
        return url
    cut_link = url.split('/')[:2+level]
    return '/'.join(cut_link)


def links_nesting_level(url, level):
    """Сбор всех ссылок в один словарь и вызов функции screenshot"""
    list_link = []
    clear_list_link = []

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    for link in soup.find_all('a'):
        some_link = link.get('href')
        if some_link.startswith(url):
            list_link.append(some_link)
    for link in (sorted(list_link)):
        clear_list_link.append(check_nesting_level(link, level))
    screenshot(sorted(set(clear_list_link)))


@api_view(['GET'])
def check_task(request, pk):
    try:
        task = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TasksSerializer(task)
    return Response(serializer.data['status'])


@api_view(['POST'])
def make_task(request):
    serializer = TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        try:
            return Response({'message': serializer.data['id']})
        finally:
            links_nesting_level(
                request.data['link'],
                serializer.data['level'],
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
