from collections import namedtuple
from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from custom.classes import Material
from .models import UserCourseMaterial, Content

MEDIA_CHOICES_DICT = {'VID':'Video', 'AUD':'Audio', 'PIC':'Picture', 'DOC':'Document', 'XLS':'Excel', 'PPT':'Powerpoint', 'GFORM':'Google form', 'GDOC':'Google document'}

class HomeView(View):
	def get(self, request):
		request.session['year'] = datetime.today().year
		return render(request, 'index.html');

class ProfileView(View):
	def get(self, request):
		return render(request, 'account/profile.html')

class CourseView(View):
	def get(self, request):
		ucms = UserCourseMaterial.objects.filter(user_id=request.user)
		#Material = namedtuple('Material', 'course_title material_title content_label content_url content_type')
		material_list = []
		for ucm in ucms:
			m = Material()
			contents = Content.objects.filter(material=ucm.material.id)
			m.set_course_title(ucm.course.title)
			m.set_material_title(ucm.material.title)
			for c in contents:
				m.set_content_url(c.url)
				m.set_content_type(c.type)
				m.set_content_label(c.label)
				material_list.append(list(m))
		return render(request, 'courses/course_view.html', { 'material_list' : material_list });

