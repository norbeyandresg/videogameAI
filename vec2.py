class Vec2:
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

		@property
		def x(self):
			return self.__x

		@x.setter
		def x(self, value):
			self.__x = value

		@property
		def y(self):
			return self.__y

		@y.setter
		def y(self, value):
			self.__y = value

	def __add__(self, other):
		types = (int, float)
		if isinstance(self, types):
			return Vec2(self + other.x, self + other.y)
		elif isinstance(other, types):
			return Vec2(self.x + other, self.y + other)
		else:
			return Vec2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		types = (int, float)
		if isinstance(self, types):
			return Vec2(self - other.x, self - other.y)
		elif isinstance(other, types):
			return Vec2(self.x - other, self.y - other)
		else:
			return Vec2(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		types = (int, float)
		if isinstance(self, types):
			return Vec2(self * other.x, self * other.y)
		elif isinstance(other, types):
			return Vec2(self.x * other, self.y * other)
		else:
			return Vec2(self.x * other.x, self.y * other.y)

	def __str__(self):
        return "({0},{1})".format(self.x,self.y)
