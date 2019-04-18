from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from django.views.static import serve
from courses.views import *

urlpatterns = [
	path('', HomeView.as_view()),
	path('admin/', admin.site.urls),
	re_path(r'^account[s]?/', include('allauth.urls')),
	path('accounts/profile/', login_required(ProfileView.as_view())),
	path('accounts/profile/courses/', login_required(CourseView.as_view())),
	#https://stackoverflow.com/questions/6014663/django-static-file-not-found
	re_path(r'^static/(?P<path>.*)$', serve, {'document_root', settings.STATIC_ROOT}),
]
