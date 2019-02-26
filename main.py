import program

def main():
	menu = 0

	while menu != 5:
		print("\n\n --> MAQUINA DOIS REG <--\n")
		print("   (1) - Copia\n   (2) - Soma 2\n   (3) - Multiplica por 2\n   (4) - Divide por 2\n   (5) - Sair \n")
		menu = int(input("  -> "))

		a_value = int(input("\n Insira o valor de A -> "))

		handler = program.Program(a_value)

		print("\n")

		if menu == 1:
			print("Copiar valor {0} de A para B".format(a_value))
			handler.copy()
		elif menu == 2:
			print("Somar 2 ao valor de {0}".format(a_value))
			handler.add_2()
		elif menu == 3:
			print("Multiplicar valor {0}".format(a_value))
			handler.multiply_2()
		elif menu == 4:
			print("Dividir valor {0}".format(a_value))
			handler.divide_2()
		elif menu == 5:
			print("SAINDO...")
			break
		else:
			print("Nao reconhecido")

if __name__ == "__main__":
	main()


