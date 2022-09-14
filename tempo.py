segundos = int(input("Digite o tempo de duração em segundos: "))

conversaoMinutos = int(segundos / 60)
conversaoHoras = int(conversaoMinutos / 60)

print(conversaoHoras,":",conversaoMinutos,":",segundos)