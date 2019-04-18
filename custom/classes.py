class Material(object):
	def __init__(self, *args, **kwargs):
		self.course_title = ''
		self.material_title = ''
		self.content_url = ''
		self.content_type = ''
		self.content_label = ''

	def set_course_title(self, course_title):
		self.course_title = course_title

	def set_material_title(self, material_title):
		self.material_title = material_title

	def set_content_url(self, content_url):
		self.content_url = content_url

	def set_content_type(self, content_type):
		self.content_type = content_type

	def set_content_label(self, content_label):
		self.content_label = content_label

	def __str__(self):
		return '(%s, %s, %s, %s, %s)' % (self.course_title, self.material_title, self.content_url, self.content_type, self.content_label)

	def __repr__(self):
		return 'Material(course_title=%r, material_title=%r, content_url=%r, content_type=%r, content_label=%r)' % (self.course_title, self.material_title, self.content_url, self.content_type, self.content_label)

	def __iter__(self):
		self.list = [self.course_title, self.material_title, self.content_url, self.content_type, self.content_label]
		self.n = 0
		return self

	def __next__(self):
		if self.n < len(self.list):
			result = self.list[self.n]
			self.n += 1
			return result
		else:
			raise StopIteration		

