from django.urls import path
from .views import *

urlpatterns = [
    path('addstud',StudentAddView.as_view(),name='stdadd'),
    path('deletstd/<int:sid>',StudentDelView.as_view(),name='stddel'),
    path('editstd/<int:sid>',StudentEditView.as_view(),name='stdedit'),
    path('profile',ProfileView.as_view(),name='pro')

]