"""
Настройки маршрутов проекта SciMaster
Copyright (c) 2025 Artem Fomin
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import PasswordResetView

from django.conf import settings
from .views import *

urlpatterns = [
    # маршрут к админке Django
    path('admin/', admin.site.urls),
    # маршрут к главной странице
    path('', include('home.urls')),
    # маршрут к документам
    path('documents/<str:filename>', serve_documents, name='serve_documents'),
    # маршрут к аккаунтам пользователей
    path('account/', include('users.urls')),
]

# добавление маршрута к медиафайлам
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# добавление маршрута к медиафайлам в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls аутентификации сайта Django (для входа, выхода, управления паролями)
urlpatterns += [
    path('accounts/password_reset/', PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'), name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# url для django-simple-captcha
urlpatterns += [
    path('captcha/', include('captcha.urls')),
]

# обработчик ошибки 404
handler404 = "sci_master.views.page_not_found_view"