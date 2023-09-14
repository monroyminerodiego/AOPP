# AOPP (Automatization Of Processes with Python)

## Description
The purpose of this repository is to showcase the creation of one of my professional projects. This project focuses on the automation of a business process where too many human resources were being spent. The implementation of a software that can automate this process generated an impact on the daily performance of activities and increased sales results by 80%.

>[!IMPORTANT]
>
>The documentation and publication of some file are still in progress; This is not the final version.



## Requirements
These are the requirements for this project to function properly:
   ### Libraries
   - wheel
   - pyautogui
   - pyperclip
   - bs4
   - opencv-python
   - pywin32
   - pillow
   - mysqlclient
   - python-dotenv mysqlclient

   ### Security Certificates
   - Click here to download [CA certificates extracted from Mozilla](https://curl.se/docs/caextract.html)

## Detailed Description of files and functions
### DataBase_Managment
   - **conex.py** This file is where my connection to my remote database is, according to a set of rules, we could determine if it is needed to use server 1 or server 2.
   
<table>
   <thead>
      <tr>
         <th>Function Name</th>
         <th>Inputs</th>
         <th>Output</th>
         <th>Description</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>conexion(<br>query='',<br>data='',<br>con='server1',<br>print_con=False<br>)</td>
         <td>
            - query: class 'str'. Here you can put the query as SQL code and the function will read it properly<br><br>
            - data: class 'str'. Can be also pased a list or a tuple. It is usefull to insert multiple different rows to a database<br><br>
            - con: class 'str'. Server to connect. By Default it is connected to server1, but it can be changed.<br><br>            - print_con: class 'bool'. By Default is set to False,<br>but when set to True, it will print a confirmation message<br><br>
         </td>
         <td>
            - class 'list': If a query was expecting something to return, the function will return it in a list.
         </td>
         <td>
            1. If 'con' is equal to 'server1', then it will get the info to make the connection to 'server1'; If 'con' is equal to 'server2', then it will be connected to the other server. <br><br>
            2. Makes the cursor, no matter the server, to have autocommit's turned on.<br><br>
            3. If flag activated, it'll print the name of the server which the connection will occur.<br><br>
            4. According to the nature of the SQL query, it will determine whether 'executemany' or 'execute' method should be used.<br><br>
            5. If 'execute' method was called, the function will return a list with all the elements of the cursor.
         </td>
      </tr>
   </tbody>
</table>

   - **download_databases.py:** 
   - **Process_1.py:** 
   - **update_link.py:** 
   - **upload_databases.py:** 

### Deployed_Robot
   - **Images**
      - **System_1:**
      - **loading.png:**
   - **(AOOP)Process_1.py**
   - **conex.py**

### Downloads
   - **download_1.csv:** File where it will download the data of table 1
   - **download_2.csv:** File where it will download the data of table 2
   - **download_3.csv:** File where it will download the data of table 3
   - **download_4.csv:** File where it will download the data of table 4
   - **download_5.csv:** File where it will download the data of table 5
   - **download_6.csv:** File where it will download the data of table 6
   - **download_7.csv:** File where it will download the data of table 7

### Files
   - **file_1.csv:** File to store data to upload it to table 1
   - **file_2.csv:** File to store data to upload it to table 2
   - **file_3.csv:** File to store data to upload it to table 3
   - **file_4.csv:** File to store data to upload it to table 4
   - **file_5.csv:** File to store data to upload it to table 5
   - **file_6.csv:** File to store data to upload it to table 6
   - **file_7.csv:** File to store data to upload it to table 7

--- 

## Change Log
### 2023-09-14
- DataBase_Managment\conex.py: Modification of function to only make one 'cnx.autocommit(True)' statement. Added documentation about operation
- Downloads\\: Added documentation about files
- Files\\: Added documentation about files

### 2023-09-12
- DataBase_Managment\\:Added 2 files, 'conex.py' and 'download_databases.py'

### 2023-09-11
- Added files to start making the structure of this repository.
- Added documentation.