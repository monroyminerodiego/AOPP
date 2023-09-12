import MySQLdb, sys, os, numpy as np, pyautogui as py, time
from tqdm.auto import tqdm
from datetime import date, timedelta
from calendar import monthrange
from getpass import getuser
from dotenv import load_dotenv
from conex import conexion
load_dotenv()
os.system('cls')
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

def date4_table2():
    actual_month = int(time.localtime().tm_mon)
    actual_year = int(time.localtime().tm_year)

    working_month = actual_month+3
    working_year = actual_year

    if working_month>12:
        working_month = working_month-12
        working_year += 1

    if int(time.localtime().tm_mday) > int(monthrange(working_year,working_month)[1]):
        return False
    else:
        return f'{working_year}-{working_month:02d}-{time.localtime().tm_mday:02d}'

def date4_table4(before = True):
    actual_month = int(time.localtime().tm_mon)
    actual_year = int(time.localtime().tm_year)

    if before:
        working_month = actual_month-2
    elif before == False:
        working_month = actual_month-6

    working_year = actual_year

    if working_month<1:
        working_month = 12+working_month
        working_year -= 1

    if int(time.localtime().tm_mday) > int(monthrange(working_year,working_month)[1]):
        return False
    else:
        return f'{working_year}-{working_month:02d}-{time.localtime().tm_mday:02d}'

def Process_2():
  conexion(print_con=True)

  print(f"\n{'-'*10} Downloading database {'-'*10}")
  rows_database = []

  if ',' in sys.argv[1]:
    variable_list = sys.argv[1].split(',')
    date = ""
    x = 0
    for day in variable_list:
      date = f"{date.today() - timedelta(days=int(day))}" if x==0 else f"{date}' OR column1='{date.today() - timedelta(days=int(day))}"
      x += 1
  else:
    days = int(sys.argv[1])
    date = date.today() - timedelta(days=days)

  date2delete_table4 = preprocess_table4()
  
  worked_data = []

  crs = conexion(f"SELECT column3 FROM table3 WHERE column1='{date}'")
  print('\ntable 3 Server2: ')
  for i in tqdm(crs):
    worked_data.append(i[0])

  crs = conexion(f"SELECT column3 FROM table2 WHERE column1='{date}'")
  print('table2 Server2: ')
  for i in tqdm(crs):
    worked_data.append(i[0])

  crs = conexion(f"SELECT column3 FROM table4 WHERE column1='{date}'")
  print('table4 Server2: ')
  for i in tqdm(crs):
    worked_data.append(i[0])

  date = date.replace('column1','FECHA') if ',' in sys.argv[1] else date
  crs = conexion(f"SELECT column3 FROM table5 WHERE FECHA='{date}'")
  print('Duplicados Server2: ')
  for i in tqdm(crs):
    worked_data.append(i[0])

  print(f'\nWorked data: {len(worked_data)}')

  file_1 = open(f'../Downloads/WorkedFile_{str((date.today()).day)}_{months[((date.today()).month)-1]}_Server2.csv','a')
  text_1 = 'column2,column3,column4,column5,column6,column7,column8,column9,column10,column11,column12'
  rows_database.append(text_1)
  np.savetxt(file_1,rows_database,fmt='%s',delimiter=',')
  rows_database.clear()

  file_2 = open(f'../Downloads/column14File_{str((date.today()).day)}_{months[((date.today()).month)-1]}_Server2.csv','w')
  texts_2 = 'column4,column14'
  rows_database.append(texts_2)
  np.savetxt(file_2,rows_database,fmt='%s',delimiter=',')
  rows_database.clear()

  conexion(f"UPDATE table4 SET column15='State1' WHERE column5>={93}")
  conexion(f"UPDATE table4 SET column15='State2' WHERE (column1='{date.today()-timedelta(days=1)}' AND column5 = {93}) OR (column1='{date.today()-timedelta(days=2)}' AND column5 = {94}) OR (column1='{date.today()-timedelta(days=3)}' AND column5 = {95})")

  crs = conexion(f"SELECT * FROM table4 WHERE column15='State1'")
  print('\nFiltered data: ')
  for i in tqdm(crs):
    text_1 = f"{i[1]}, {i[2]}, {i[3]}, {i[4] if int(i[4]) <= 92 else 92}, {i[5]}, {i[6]}, {i[7]}, {i[8]}, {i[9]}, {i[10]}, {i[11]}"
    rows_database.append(text_1)
    np.savetxt(file_1,rows_database,fmt='%s',delimiter=',')
    rows_database.pop(0)
    
    texts_2 = f"{i[3]},{i[13]}"
    rows_database.append(texts_2)
    np.savetxt(file_2,rows_database,fmt='%s',delimiter=',')
    rows_database.pop(0)

  file_1.close()
  file_2.close()

  print(f"\n\n{'-'*10} Validating table1 {'-'*10}")
  duplicated_data = []
  unique_data = []

  crs = conexion("SELECT column3 FROM table1")
  for i in tqdm(crs):
    if i[0] in worked_data:
      duplicated_data.append(i[0])
    else:
      unique_data.append(i[0])
  print(f'Unique: {len(duplicated_data)} // Duplicated: {len(unique_data)}')

  print(f"\n\n{'-'*10} Filling missing data of table1 with table2 {'-'*10}")
  date_table2 = date4_table2()
  if date_table2:
    crs = conexion(f"SELECT * FROM table2 WHERE column7<='{date_table2}'")
    print('Downloading table2:')
    for i in tqdm(crs):
      unique_data.append(i[1])
    
  print(f"\n\n{'-'*10} Filling missing data of table1 with table4 {'-'*10}")
  date_table4 = date4_table4(True)
  if date_table4:
    crs = conexion(f"SELECT * FROM table4 WHERE (column1 <= '{date_table4}') AND (  column13 ='STATE 3' OR   column13 ='STATE 2' OR   column13 ='STATE 3.1' OR   column13 ='STATE 2.1')")
    print('\Downloading table4 3M y 2M:')
    for i in tqdm(crs):
      unique_data.append(i[2])


  fecha_0m = date4_table4(False)
  if fecha_0m:
    crs = conexion(f"SELECT * FROM table4 WHERE (column1 <= '{fecha_0m}') AND ( column13 ='STATE 1' OR  column13 ='STATE 0' OR  column13 ='STATE 1.1' OR  column13 ='STATE 0.1')")
    print('\nDescargando table4 1M y 0M:')
    for i in tqdm(crs):
      unique_data.append(i[2])


  limite_contactos = 5500

  contactos_faltantes = limite_contactos - len(unique_data)
  if contactos_faltantes > 0:
    crs = conexion(f'SELECT column3 FROM series ORDER BY AGREGADO LIMIT {int(contactos_faltantes)}')
    print('\nDescargando series:')
    for i in tqdm(crs):
      unique_data.append(i[0])


    crs = conexion('SELECT COUNT(*) FROM series')
    for i in crs:
      contactos_series = i[0]
      break
    print(f'Quedan {contactos_series} series')


  lista_diario = []
  for i in unique_data:
    lista_diario.append(i)
  duplicated_data.clear()
  unique_data.clear()
  lista_diario.sort()
  cliente_anterior = ''

  while True:
    for i in lista_diario:
      if i == cliente_anterior:
        duplicated_data.append(i)
      else:
        unique_data.append(i)
      cliente_anterior = i

    if len(duplicated_data)==0:
      break

    if len(unique_data) < limite_contactos:
      crs = conexion(f"SELECT * FROM na LIMIT {limite_contactos - len(unique_data)}")
      print('\nAcompletando archivo diario con na:')
      x = 1
      for i in tqdm(crs):
        unique_data.append(i[1])
        x += 1
      
      conexion(f"DELETE FROM na LIMIT {x}")

    lista_diario.clear()
    for i in unique_data:
      lista_diario.append(i)
    duplicated_data.clear()
    unique_data.clear()
    lista_diario.sort()
    cliente_anterior = ''



  print(f"\n\n{'-'*10} Guardando archivo diario ({len(unique_data)}) Server2 {'-'*10}")

  file = open(f'../archivo/diario_Server2.csv','w')
  file.close()

  for i in tqdm(unique_data):
    variable_list = []
    textos = f'XXXX,{i}'
    variable_list.append(textos)
    descarga = open(f'../archivo/diario_Server2.csv','a',encoding='utf-8')
    np.savetxt(descarga,variable_list,fmt='%s',delimiter=',')
    descarga.close()

  print(f"\n\n{'-'*10} Subiendo diario {'-'*10}")
  conexion("TRUNCATE TABLE diario")
  conexion("TRUNCATE TABLE table5")
  file = open(f'../archivos/diario_Server2.csv','r')
  variable_list = []
  x = 0
  compu = 1
  for row in tqdm(file):
    compu = (compu+1) if (compu < 12) else 1
    compu = (compu+1) if (compu==2) else compu
    row = row.split(',')
    tupla = (row[0],row[1].replace('\n',''),f'AR-{compu:02d}','PENDIENTE')
    variable_list.append(tupla)
    x += 1

    if x == 500:
      conexion("REPLACE INTO diario(column2,column3,COMPU,ESTATUS) VALUES(%s,%s,%s,%s)",data=variable_list)
      variable_list.clear()
      x = 0

  if x != 0:
    conexion("REPLACE INTO diario(column2,column3,COMPU,ESTATUS) VALUES(%s,%s,%s,%s)",data=variable_list)
    variable_list.clear()

  print(f"\n\n{'-'*10} Borrando información {'-'*10}")
  conexion("UPDATE table4 SET ARCHIVO='USADO' WHERE ARCHIVO='POR USAR'")
  conexion(f"DELETE FROM table4 WHERE column1 <= '{date2delete_table4}'")
  print('Listo table4...!!!')
  if date_table2:
    conexion(f"DELETE FROM table2 WHERE TERMINO<='{date_table2}'")
    print('\nListo table2...!!!')
  if date_table4:
    conexion(f"DELETE FROM table4 WHERE (column1 <= '{date_table4}') AND (MESES='3M' OR MESES='2M')")
    print('\nListo 3M y 2M...!!!')
  if fecha_0m:
    conexion(f"DELETE FROM table4 WHERE (column1 <= '{fecha_0m}') AND (MESES='1M' OR MESES='0M')")
    print('\nListo 1M y 0M...!!!')
  


  print(f'\n\nTerminado cartera Server2!')


def cartera_sim():
  conexion(con='sim',imprimir_conexion=True)

  print(f"\n{'-'*10} Downloading database {'-'*10}")


  if ',' in sys.argv[1]:
    lista = sys.argv[1].split(',')
    fecha = ""
    x = 0
    for dia in lista:
      fecha = f"{date.today() - timedelta(days=int(dia))}" if x==0 else f"{fecha}' OR column1='{date.today() - timedelta(days=int(dia))}"
      x += 1
  else:
    dias = int(sys.argv[1])
    fecha = date.today() - timedelta(days=dias)

  lista = []

  crs = conexion(f"SELECT * FROM na WHERE column1='{fecha}'",con='sim')
  file = open('../archivos/na_Server2.csv','w')
  file.close()
  print('Descargando Na SIM: ')
  for i in tqdm(crs):
    file = open('../archivos/na_Server2.csv','a',encoding='utf-8')
    lista.append(f'{i[0]},{i[1]},{i[2]},{i[3]}')
    np.savetxt(file,lista,fmt='%s',delimiter=',')
    lista.clear()
    file.close()

  lista.clear()
  crs = conexion(f"SELECT * FROM table2 WHERE column1='{fecha}'",con='sim')
  file = open('../archivos/table2_Server2.csv','w',encoding='latin-1')
  file.close()
  print('Descargando table2 SIM: ')
  for i in tqdm(crs):
    file = open('../archivos/table2_Server2.csv','a',encoding='latin-1')
    lista.append(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]}')
    np.savetxt(file,lista,fmt='%s',delimiter=',')
    lista.clear()
    file.close()

  lista.clear()
  crs = conexion(f"SELECT * FROM table4 WHERE column1='{fecha}'", con='sim')
  file = open('../archivos/table4_Server2.csv','w')
  file.close()
  print('Descargando table4 SIM:')
  for i in tqdm(crs):
    file = open('../archivos/table4_Server2.csv','a',encoding='utf-8')
    lista.append(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]},{i[10]},{i[11]},{i[12]},{i[13]},'POR USAR'")
    np.savetxt(file,lista,fmt='%s',delimiter=',')
    lista.clear()
    file.close()

  print(f"\n{'-'*10} Subiendo cartera {'-'*10}")

  file = open('../archivos/na_Server2.csv','r')
  x = 0
  lista.clear()
  print('Subiendo Na SIM: ')
  for row in tqdm(file):
    row = row.split(',')
    tupla = (row[0],row[1],row[2],row[3])
    lista.append(tupla)
    x += 1
    if x%500 == 0:
      conexion("REPLACE INTO na(column2,column3,ESTADO,column1) VALUES(%s,%s,%s,%s)",lista)
      lista.clear()
  if x%500 != 0:
      conexion("REPLACE INTO na(column2,column3,ESTADO,column1) VALUES(%s,%s,%s,%s)",lista)
      lista.clear()

  file = open('../archivos/table2_Server2.csv','r')
  x = 0
  lista.clear()
  print('Subiendo table2 SIM: ')
  for row in tqdm(file):
    row = row.split(',')
    tupla = (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    lista.append(tupla)
    x += 1
    if x%500 == 0:
      conexion("REPLACE INTO table2(column2,column3,column4,ADENDUM,TERMINO,PLAZO,column1) VALUES(%s,%s,%s,%s,%s,%s,%s)",lista)
      lista.clear()
  if x%500 != 0:
      conexion("REPLACE INTO table2(column2,column3,column4,ADENDUM,TERMINO,PLAZO,column1) VALUES(%s,%s,%s,%s,%s,%s,%s)",lista)
      lista.clear()

  file = open('../archivos/table4_Server2.csv','r')
  x = 0
  lista.clear()
  print('Subiendo table4 SIM:')
  for row in tqdm(file):
    row = row.split(',')
    tupla = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],'POR USAR')
    lista.append(tupla)
    x += 1
    if x%500 == 0:
      conexion("INSERT IGNORE INTO table4(column1,column2,column3,column4,DIAS,ADENDUM,TERMINO,ESTADO,CUOTA,FINANCIAMIENTO,PLAN,PLAZO,MESES,column14,ARCHIVO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",lista)
      lista.clear()
  if x%500 != 0:
      conexion("INSERT IGNORE INTO table4(column1,column2,column3,column4,DIAS,ADENDUM,TERMINO,ESTADO,CUOTA,FINANCIAMIENTO,PLAN,PLAZO,MESES,column14,ARCHIVO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",lista)
      lista.clear()



  print('\n\n\nTerminado cartera SIM!')


def preprocess_table4():
  fecha = date.today() - timedelta(weeks=15)
  lista = []
  file = open('../archivos/series_sim.csv','w',encoding='utf-8'); file.close()
  file = open('../archivos/series_sim.csv','a',encoding='utf-8')

  crs = conexion(query=f"SELECT column3 FROM table4 WHERE column1 <= '{fecha}'")
  print('\nDescargando números de más de 15 semanas: ')
  x = 1
  for data_type1 in tqdm(crs):
    data_type1 = data_type1[0]
    textos = f"{data_type1}"
    lista.append(textos)
    np.savetxt(file,lista,fmt='%s',delimiter=',')
    lista.pop(0)
    x == x+1 if x<500 else 1

  file.close()
  file = open('../archivos/series_sim.csv','r',encoding='utf-8')

  x = 0
  lista = []
  print('\nSubiendo series a Sim: ')
  for data_type1 in tqdm(file):
    data_type1 = data_type1.replace('\n','')
    tupla = ('XXXX',data_type1,date.today()-timedelta(days=x))
    lista.append(tupla)
    x += 1
    if x == 500:
      conexion("REPLACE INTO series(column2,column3,AGREGADO) VALUES(%s,%s,%s)",lista,con='sim')
      lista.clear()
      x = 0
  if x != 0:
    conexion("REPLACE INTO series(column2,column3,AGREGADO) VALUES(%s,%s,%s)",lista,con='sim')
    lista.clear()
  
  return fecha
  


cartera_sim()
print(f'\n\n\n{"*"*30} Empezando con otra {"*"*30}\n\n\n')
Process_2()