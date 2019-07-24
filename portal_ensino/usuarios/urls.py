from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import usuarios_list, usuarios_novo, do_logout, do_login, usuarios_update, usuarios_delete


urlpatterns = [
    path('list/', usuarios_list, name='lista_usuarios'),
    path('novo/', usuarios_novo, name="novo_usuario"),
    path('atualizar-usuario/', usuarios_update, name="atualizar_usuario"),
    path('deletar-usuario/<int:id>', usuarios_delete, name="deletar_usuario"),
    path('logout/', do_logout, name="logout"),
    path('login/', do_login, name="login"),

    # PASSWORD RESET
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # possibilita visualizar imagens dos profiles