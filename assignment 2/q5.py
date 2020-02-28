class triangle:
	def input_sides(self):
		self.a,self.b,self.c = (map(float,input("Enter the sides of the triangle:").split()))

class area(triangle):
	def total_area(self):
		s = (self.a+self.b+self.c)/2
		tot_area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
		print(tot_area)

t2 = area()
t2.input_sides()
t2.total_area()
