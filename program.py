import operations

class Program(operations.Operations):
	def __init__(self, numero):
		super().__init__(numero)

	def copy(self):
		while(!super().a_zero()):
			super().sub_a()
			super().add_b()

	def divide_2(self):
		while(!super().a_zero()):
			super().sub_a()
			if(super().a_zero()):
				break
			super().sub_a()
			super().add_b()

	def add_2(self):
		while(!super().a_zero()):
			super().sub_a()
			super().add_b()
		super().add_b()
		super().add_b()

	def multiply_2(self):
		while(!super().a_zero()):
			super().sub_a()
			super().add_b()
			super().add_b()

	

