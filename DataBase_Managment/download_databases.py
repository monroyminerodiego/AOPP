import os, numpy as np, MySQLdb
from tqdm.auto import tqdm
from conex import conexion
os.system('cls')

file = input(f'''
{"*"*20} {conexion(print_con=True)} {"*"*20}
1) File 1
2) File 2
3) File 3
4) File 4
5) File 5

Please, select one file: 
''')



if file == 'File 1':
    query = f"SELECT column2 FROM table_1"
    crs =conexion(query)
    texts = 'column1,column2'
    download = open(f'../Downloads/File_1.csv','a')
    varlist = []
    varlist.append(texts)
    np.savetxt(download,varlist,fmt='%s',delimiter=',')
    download.close()
    for i in tqdm(crs):
        texts = f'XXXX,{i}'
        download = open(f'../Downloads/File_1.csv','a')
        varlist = []
        varlist.append(texts)
        np.savetxt(download,varlist,fmt='%s',delimiter=',')
        download.close()
elif (file == 'File 2') or (file == 'File 3') or (file == 'File 4'):
    query = f"SELECT MIN(column7) FROM {file}"
    crs = conexion(query)
    from_month = int(str(crs[0])[5:-3])
    from_year = int(str(crs[0])[:4])
    from_date = f'{from_year}-{from_month:02d}-01'
    print(f'Validating from: {from_date} to ',end='')

    query = f"SELECT MAX(column7) FROM {file}"
    crs = conexion(query)
    to_month = int(str(crs[0])[5:-3])+1
    to_year = int(str(crs[0])[:4])
    if to_month>12:
        to_month = to_month-12
        to_year += 1
    to_date = f'{to_year}-{to_month:02d}-01'
    
    x = 0
    validate_month = from_month
    validate_year = from_year
    validate_date = f'{validate_year}-{validate_month:02d}-01'
    while True:
        if validate_date == to_date:
            break
        x += 1
        validate_month += 1
        if validate_month > 12:
            validate_month = 1
            validate_year += 1
        validate_date = f'{validate_year}-{validate_month:02d}-01'

    print(f'{to_date} ({x} months)\n')

    texts = f'column2,column3'
    varlist = []
    varlist.append(texts)
    download = open(f'../Downloads/{file}.csv','a')
    np.savetxt(download,varlist,fmt='%s',delimiter=',')
    download.close()

    for i in range(x):
        to_month = from_month+1
        to_year = from_year
        if to_month > 12:
            to_month = to_month-12
            to_year += 1
        

        query = f"SELECT column3 FROM {file} WHERE column1>='{from_year}-{from_month:02d}-01' AND column1<='{to_year}-{to_month:02d}-01'"
        print(f'Downloading from {from_year}-{from_month:02d}-01 to {to_year}-{to_month:02d}-01', end='\r')
        crs = conexion(query)
        for j in crs:
            texts = f'XXXX,{j}'
            varlist = []
            varlist.append(texts)
            download = open(f'../Downloads/{file}.csv','a')
            np.savetxt(download,varlist,fmt='%s',delimiter=',')
            download.close()
        

        from_month += 1
        if from_month > 12:
            from_month = from_month-12
            from_year += 1
elif file == 'File 5':
    query = f"SELECT MIN(column15) FROM {file}"
    crs = conexion(query)
    from_month = int(str(crs[0])[5:-3])
    from_year = int(str(crs[0])[:4])
    from_date = f'{from_year}-{from_month:02d}-01'
    print(f'Validating from: {from_date} to ',end='')

    query = f"SELECT MAX(column15) FROM {file}"
    crs = conexion(query)
    to_month = int(str(crs[0])[5:-3])+1
    to_year = int(str(crs[0])[:4])
    if to_month>12:
        to_month = to_month-12
        to_year += 1
    to_date = f'{to_year}-{to_month:02d}-01'
    
    x = 0
    validate_month = from_month
    validate_year = from_year
    validate_date = f'{validate_year}-{validate_month:02d}-01'
    while True:
        if validate_date == to_date:
            break
        x += 1
        validate_month += 1
        if validate_month > 12:
            validate_month = 1
            validate_year += 1
        validate_date = f'{validate_year}-{validate_month:02d}-01'

    print(f'{to_date} ({x} months)\n')

    texts = f'column2,column3'
    varlist = []
    varlist.append(texts)
    download = open(f'../Downloads/{file}.csv','a')
    np.savetxt(download,varlist,fmt='%s',delimiter=',')
    download.close()

    for i in range(x):
        to_month = from_month+1
        to_year = from_year
        if to_month > 12:
            to_month = to_month-12
            to_year += 1
        

        query = f"SELECT column3 FROM {file} WHERE column15>='{from_year}-{from_month:02d}-01' AND column15<='{to_year}-{to_month:02d}-01'"
        print(f'Downloading from: {from_year}-{from_month:02d}-01 to {to_year}-{to_month:02d}-01', end='\r')
        crs = conexion(query)
        for j in crs:
            texts = f'XXXX,{j}'
            varlist = []
            varlist.append(texts)
            download = open(f'../Downloads/{file}.csv','a')
            np.savetxt(download,varlist,fmt='%s',delimiter=',')
            download.close()
        

        from_month += 1
        if from_month > 12:
            from_month = from_month-12
            from_year += 1

print('\n\nDone...!!!')