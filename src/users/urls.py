from django.urls import path
from .views import *

# Регистрация и активация пользователя
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='profile_signup'),
    path('signup-modal/', SignupModalView.as_view(), name='profile_signup_modal'),
    path('email-confirm-done/', email_confirm_done, name='email_confirm_done'),
    path('profile-activate/<uidb64>/<token>/', profile_activate, name='profile_activate'),
]

# Вход и выход пользователя
urlpatterns += [
    path('login/', CustomLoginView.as_view(), name='profile_login'),
    path('login-modal/', LoginModalView.as_view(), name='profile_login_modal'),
    path('profile-logout/', CustomLogoutView.as_view(), name='profile_logout'),
]

# Удаление учетных записей пользователей
urlpatterns += [
    path('profile-delete_confirmation/', ProfileDeleteConfirmation.as_view(), name='profile_delete_confirmation'),
    path('superuser-delete_denied/', SuperuserDeleteDenied.as_view(), name='superuser_delete_denied'),
    path('profile-delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('delete-inactive_profiles/', DeleteAllInactiveUsersView.as_view(), name='delete_inactive_profiles'),
]

# Профиль пользователя
urlpatterns += [
    # path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/<str:tab>/', ProfileUpdateView.as_view(), name='profile')
]

# Все пользователи
urlpatterns += [
    path('all-users/', AllUsersView.as_view(), name='all_users'),
]