## historia de usuario 1 / crear registro 
##investigar regex sobre python para la otra semana

##us1/create rigister

users= []

def createUser():
    user = []
    id= int(input("Ingrese su Documento de Identidad: "))
    user.appen(id)
    name = input("Ingrese su Nombre: ")
    user_last_name = input("Ingrese su Apellido: ")
    user.append(user_last_name)
    phone= input("Ingrese su telefono")
    user.append(phone)
    user_email = input("Ingrese su Correo Electronico: ")
    user.append(user_email)
    user_password = input("Ingrese su Contraseña: ")
    user.append(user_password)
    user.aapend(user)

createUser()
createUser()
print(users)


