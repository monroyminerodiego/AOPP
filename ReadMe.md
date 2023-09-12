# AOPP (Automatization Of Processes with Python)

## Description
The purpose of this repository is to showcase the creation of one of my professional projects. This project focuses on the automation of a business process where too many human resources were being spent. The implementation of a software that can automate this process generated an impact on the daily performance of activities and increased sales results by 80%.

>[!IMPORTANT]
>
>The documentation and publication of some file are still in progress; This is not the final version.

--- 

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

--- 

## Detailed Description of files and functions
### DataBase_Managment
   - **conex.py** This file is where my connection to my remote database is, according to a set of rules, we could determine if it is needed to use server 1 or server 2.
   
<table>
    <thead>
        <tr>
            <th>Function Name</th>
            <th>Inputs</th>
            <th>Outputs</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">conexion()</td>
            <td align="center">
               * query: class 'str'. Here you can put the query as SQL code and the function will read it properly<br>
               * data: class 'str'. Can be also pased a list or a tuple. It is usefull to insert multiple different rows to a database<br>
               * con: class 'str'. Server to connect. By Default it is connected to server1, but it can be changed.<br>
               * print_con: class 'bool'. By Default is set to False,<br>but when set to True, it will print a confirmation message <br>
            </td>
            <td align="center">
               * This function does not gives any output when functioning properly. The only visual confirmation (via console) that something in the function is working would be when 'print_con' is set to True.
            </td>
            <td align="center">
               - If 'con' is equal to 'server1', then  
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

### Downloads
   - **download_1.csv:**
   - **download_2.csv:**
   - **download_3.csv:**
   - **download_4.csv:**
   - **download_5.csv:**
   - **download_6.csv:**
   - **download_7.csv:**

### Files
   - **file_1.csv:**
   - **file_2.csv:**
   - **file_3.csv:**
   - **file_4.csv:**
   - **file_5.csv:**
   - **file_6.csv:**
   - **file_7.csv:**

--- 

## Change Log (Commit description)
### 2023-09-11:
- Added files to start making the structure of this repository.
- Added documentation.

### 2023-09-12:
- DataBase_Managment\:Added 2 files, conex.py and download_databases.py