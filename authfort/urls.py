from django.urls import path
from authfort.views import CustomLoginView, CustomLogoutView

app_name = 'authfort'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]