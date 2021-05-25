官方教程https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial01/
0、安装Django  py -m pip install Django
1、创建项目 django-admin startproject mysite
2、运行命令python manage.py runserver
3、运行在指定端口python manage.py runserver 8000
4、可被外部IP访问python manage.py runserver 0.0.0.0:8000
5、创建应用 python manage.py startapp polls
