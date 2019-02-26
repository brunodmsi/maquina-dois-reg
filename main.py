import programs

def main():
	while menu != 5:
		print("MENU\n   (1) - Copia\n   (2) - Soma 2\n   (3) - Multiplica por 2\n   (4) - Divide por 2\n   (5) - Sair \n")
		menu = int(input("  -> "))

		handler = program.Program()

		a_value = int(input("\n Insira o valor de A -> "))

		if menu == 1:
			handler.copy()
		else if menu == 2:
			handler.add_2()
		else if menu == 3:
			handler.multiply_2()
		else if menu == 4:
			handler.divide_2()
		else if menu == 5:
			break
		else:
			print("Nao reconhecido")

if __name__ == "__main__":
	main()


