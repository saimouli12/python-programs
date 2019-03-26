class Test:
	h=2
	
	def _init_(self):
		self.h=6

	def my_func(self,k):
		print("hi! i am member of the class")
		self.h=k
		print(self.h)
o=Test()
print(o.h)
o1=Test()
print(o1.h)
o.my_func(2)
o1.my_func(4)
o3=Test()
print(o3.h)
o3.my_func( 8)
print(o3.h)