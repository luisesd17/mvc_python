from Controller.personaController import personaController

lista=["maria","flores","89455612","F","0014",2]
enlace=personaController()
#enlace.crearRegistro(lista)
listaRegistros=enlace.listarRegistros() # se obtiene los registros
for i in range(len(listaRegistros)):
    print("cod: ",listaRegistros[i][0])
    print("nombre: ",listaRegistros[i][1])
    print("apellido: ",listaRegistros[i][2])
    print("dni: ",listaRegistros[i][3])
    print("sexo: ",listaRegistros[i][4])
    print("ciclo: ",listaRegistros[i][5])
    print("*****************************")
