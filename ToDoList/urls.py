from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls import url, static
from django.conf import settings

urlpatterns = [
    path('ToDoList/app/', include('app.urls')),
    path('ToDoList/admin/', admin.site.urls),
    path('ToDoList/accounts/', include('accounts.urls')),
    path('ToDoList/accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='ToDoList/app/')),
]
