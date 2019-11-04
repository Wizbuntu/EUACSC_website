from django.urls import path
from .views import index, EbookSearchList, contact, admission, course_module, staff_profile


# urlpatterns
urlpatterns = [
    path('', index, name='index'),
    path('ebooks/', EbookSearchList.as_view(), name='ebooks'),
    path('contact/', contact, name='contact'),
    path('admission/', admission, name='admission'),
    path('course_module/', course_module, name='course_module'),
    path('staff_profile/', staff_profile, name='staff_profile'),
]
