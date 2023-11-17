#To-Do List: Crea una aplicación de lista de tareas pendientes que permita a los usuarios agregar, editar y eliminar tareas.

import os,time 

#Listas vacias
tareas = []

def agregar_tareas():
    limpiar()
    print("""
        ---------------------------------------
        | VAMOS A AGREGAR TAREAS TO- DO - LIST |
        ---------------------------------------
        """)
    
    tareas_add = input('Ingrese la tarea para agregar: ')
    if tareas_add not in tareas:
        tareas.append(tareas_add)
        print(f'Perfecto, agregamos ===> {tareas_add} <=== a la lista')
    else:
        print(f'La tarea "{tareas_add}" ya está en la lista.')

def editar_tareas():
    limpiar()
    print("""
        ---------------------------------------
        | VAMOS A EDITAR TAREAS TO- DO - LIST |
        ---------------------------------------
        """)
    if tareas:
        print(f'Estas son las tareas que usted agregó -> {tareas}\n')
        edit = input('¿Qué tarea deseas editar?: ')

        if edit in tareas:
            print(f'¿Qué valor deseas asignar a la tarea {edit}?: ', end='')
            nuevo_valor = input()
            index_tarea = tareas.index(edit)
            tareas[index_tarea] = nuevo_valor
            print(f'Tarea {edit} editada correctamente.')
        else:
            print('La tarea no está en la lista :(')
    else:
        print('No hay tareas.')


def eliminar_tareas():
       limpiar()
       print("""
        -----------------------------------------
        | VAMOS A ELIMINAR TAREAS TO- DO - LIST |
        -----------------------------------------
        """)
       print('tareas disponibles: ------------>',tareas)
       delete_task_all = input('Deseas eliminar todas las tareas? si/no ').lower()
       if delete_task_all == 'si':
         tareas.clear()
         print('eliminamos todas las tareas disponibles')
       elif delete_task_all == 'no':
         delete_task = input('¿Qué tarea deseas eliminar? (deja en blanco para cancelar): ')
         if delete_task == '':
          print('Operación cancelada.')
       else:
            delete_task = input('Que tarea desea eliminar? : ')
            if delete_task in tareas:
                    indice = tareas.index(delete_task)
                    del tareas[indice]
                    print(f"Se elimina {delete_task}")
            elif delete_task == '':
                print('esta vacio.')
            else:
                    print("La tarea no existe :( ")
       

def visualizar_tareas():
    limpiar()
    print("""
        ----------------------------------------
        |VAMOS A VISUALIZAR TAREAS TO - DO- LIST|
        ----------------------------------------""")
    #un bucle for para que se fije que en la variable tareas todo lo que tiene guardado.
    if tareas:
        print('-------------------------------------------------------')
        print("Tareas Disponibles:")
        for tarea in set(tareas):  # Usamos set para eliminar duplicados
            print(f"- {tarea}") 
        print('-------------------------------------------------------')
        time.sleep(2)
    else:
        print("No hay tareas en la lista.")

  


def main():
    while True:
        #Obtenemos la hora actual y actualizada del sistema.
        hora_actual = time.strftime("%H:%M:%S")
        dia_actual = time.strftime("%Y-%m-%d")

        time.sleep(1)
        print(f"""
        PERMITE A LOS USUARIOS AGREGAR/EDITAR/ELIMINAR/VISUALIZAR
        =================================================
                    |   TO-DO LIST     |
        ================================================
        |1) Agregar una tarea
        |2) Editar una tarea
        |3) Eliminar tarea
        |4) Visualizar Tareas
        |5) Salir
        |6) Limpiar pantalla.         Hora: {hora_actual} // Dia: {dia_actual}
        ================================================    
              """)
    
        usuario = input('Ingrese una opcion -> ')
        if usuario == '1':
            agregar_tareas()
        elif usuario == '2':
            editar_tareas()
        elif usuario == '3':
            eliminar_tareas()
        elif usuario == '4':
            visualizar_tareas()
        elif usuario == '5':
            print('chau')
            break
        elif usuario == '6':
            limpiar()
        else:
            print('**Opcion Incorrecta**')
    

def limpiar():
    print('**LIMPIANDO SU PANTALLA**')
    time.sleep(0)
    os.system('cls')
    

if __name__ == '__main__':
    main()
   

