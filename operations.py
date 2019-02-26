class Operations():
	def __init__(self,number):
		self.a = number
		self.b = 0

	def a_zero(self):
		if self.a == 0:
			return True
		else: 
			return False

	def add_b(self):
		print("( a , b )  =  ( {0} , {1} + 1 )".format(self.a,self.b))
		self.b = self.b + 1
		print("( a , b )  =  ( {0} , {1} )".format(self.a,self.b))

	def sub_a(self):
		print("( a , b )  =  ( {0} - 1 , {1} )".format(self.a,self.b))
		self.a = self.a - 1
		print("( a , b )  =  ( {0} , {1} )".format(self.a,self.b))