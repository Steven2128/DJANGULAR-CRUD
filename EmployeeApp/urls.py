#Django
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#Views
from EmployeeApp.views import deparmentApi, employeetApi, save_file


urlpatterns = [
    path('department/', deparmentApi),
    path('department/<int:id>', deparmentApi),
    path('employee/', employeetApi),
    path('employee/<int:id>', employeetApi),
    path('save-file/', save_file)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
