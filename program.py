import operations

class Program(operations.Operations):
	def __init__(self, number):
		super().__init__(number)

	def copy(self):
		while(True):
			if(super().a_zero()):
				break
			else:
				super().sub_a()
				super().add_b()			

	def divide_2(self):
		while(True):
			if(super().a_zero()):
				break
			else:
				super().sub_a()
				if(super().a_zero()):
					break
				super().sub_a()
				super().add_b()

	def add_2(self):
		while(True):
			if(super().a_zero()):
				break
			else:
				super().sub_a()
				super().add_b()
		super().add_b()
		super().add_b()

	def multiply_2(self):
		while(True):
			if(super().a_zero()):
				break
			else:
				super().sub_a()
				super().add_b()
				super().add_b()

	

