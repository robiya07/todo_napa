
from django.conf.urls.static import static
from django.urls import path

from root.settings import MEDIA_URL, MEDIA_ROOT
from user.views import home_view, login_view, registration_view, logout_view, profile_view, img_upload, img_delete

urlpatterns = [
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('user/profile/', profile_view, name='profile'),
    path('user/img/upload/', img_upload, name='img_upload'),
    path('delete/img/<int:id>/', img_delete, name="img_delete")

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)