import MySQLdb, os
from dotenv import load_dotenv
load_dotenv()

def conexion(query='',data='',con='server1',print_con=False):
  if con.lower() == 'server1':
    cnx = MySQLdb.connect(
      host   = os.getenv("HOST_S1"),
      user   = os.getenv("USERNAME_S1"),
      passwd = os.getenv("PASSWORD_S1"),
      db     = os.getenv("DATABASE_S1"),
      ssl    = os.getenv("UNIVERSAL_SSL"))
    cnx.autocommit(True)
    crs = cnx.cursor()
    if print_con:
      print('Connected to: Server 1')
  elif con.lower() == 'server2':
    cnx = MySQLdb.connect(
      host   = os.getenv("HOST_S2"),
      user   = os.getenv("USERNAME_S2"),
      passwd = os.getenv("PASSWORD_S2"),
      db     = os.getenv("DATABASE_S2"),
      ssl    = os.getenv("UNIVERSAL_SSL"))
    cnx.autocommit(True)
    crs = cnx.cursor()
    if print_con:
      print("Connected to: Server 2")

  if data!='':
    crs.executemany(query,data)
  elif query!='':
    crs.execute(query)
    lista = []
    for i in crs:
      lista.append(i)
    return lista
  
if __name__ == '__main__':
  print(os.getenv("HOST_S1"))
  conexion(print_con=True)