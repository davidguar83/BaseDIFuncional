import sqlite3 as dbapi

try:
    baseconexion = dbapi.connect ("baseDI.dat")
    print (baseconexion)


except dbapi.StandardError as e:
    print (e)
else:
    print ("Base de datos aberta")

try:
    cursor = baseconexion.cursor ()
    print (cursor)

except dbapi.Error as e:
    print (e)
else:
    print ("Cursor preparado")



try:


    cursor.execute("""CREATE TABLE clientes (
    "DNI"	TEXT PRIMARY KEY NOT NULL,
    "nome"	TEXT NOT NULL,
    "apelledos"	TEXT NOT NULL,
    "telf"	INTEGER NOT NULL,
    "deuda"	INTEGER NOT NULL
    )
    """)

    baseconexion.commit()

    cursor.execute("""insert into clientes
                     values ( '53177986p', 'David', 'rodriguez',986123456,150)""")


    cursor.execute("""insert into clientes
                     values ( '53177988x', 'Jose', 'rodriguez',986654321,1000)""")

    baseconexion.commit()


except dbapi.DatabaseError as e:
    print("Erro insertando os datos en clientes: " + str(e))



try:

    cursor.execute("""CREATE TABLE productos (
    "ref"	INTEGER PRIMARY KEY NOT NULL,
    "nome"	TEXT NOT NULL,
    "pvp"	INTEGER NOT NULL
    )
    """)

    baseconexion.commit()




    cursor.execute("""insert into clientes
                     values ( 1, 'patata', 0.25)""")

    cursor.execute("""insert into clientes
                     values ( 2, 'melon', 2.35)""")
    cursor.execute("""insert into clientes
                     values ( 3, 'nocilla', 3.25)""")
    cursor.execute("""insert into clientes
                     values ( 4, 'lentejas', 0.80)""")


    baseconexion.commit()


except dbapi.DatabaseError as e:
    print("Erro insertando os datos en clientes: " + str(e))

try:

    cursor.execute("""CREATE TABLE ventas (
    "ref"	INTEGER PRIMARY KEY NOT NULL,
    "nome"	TEXT NOT NULL,
    "cantidad"	INTEGER NOT NULL
    )
    """)


    baseconexion.commit()




    cursor.execute("""insert into clientes
                     values ( 1, 'patata', 150)""")
    cursor.execute("""insert into clientes
                     values ( 2, 'melon', 150)""")
    cursor.execute("""insert into clientes
                     values ( 3, 'nocilla', 150)""")
    cursor.execute("""insert into clientes
                     values ( 4, 'lentejas', 150)""")


    baseconexion.commit()




except dbapi.DatabaseError as e:
    print("Erro insertando os datos en clientes: " + str(e))



    try:
     cursor.execute("select * from clientes")
        # fetchone a seguinte tupla
        # fetchall devolta un obxecto iterable con todalas tuplas
        # fetcmany numero de tuplas pasado por parametro
     for fila in cursor.fetchall():
            print("DNI: " + fila[0])
            print("Nome: " + fila[1])
            print("Apellidos: " + fila[2])
            print("Telefono: " + str(fila[3]))
            print("Deuda: " + str(fila[4]))


    except dbapi.DatabaseError as e:
        print("Erro facendo a consulta: " + str(e))
    else:
        print("Consulta executada")
        Nome= input("Introduce o nome")
    try:
        consulta = "select * from clientes where Nome= ?"
        print(consulta)
        cursor.execute(consulta,(Nome,))
        for rexistro in cursor.fetchall():
            print(rexistro)
    except dbapi.DatabaseError as e:
        print("Erro facendo a consulta: " + str(e))
    else:
        print("Consulta executada")
        baseconexion.commit()

else:
    print ("Base de datos creada")

finally:
    cursor.close()
    baseconexion.close()