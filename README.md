# findAFile
Script that finds files on a machine. If the file is found, the script sends an email using gmail's SMTP.
You can also use the lib [pyinstall][pyinstaller] to build executables of this script and run on machines that don't have python installed. 

## How to Run:
```bash
python findAFile.py sender_email email_password recipient_email file_name1,file_name2... 
``` 
OR if you have build an executable:
```bash
findAFile.exe sender_email email_password recipient_email file_name1,file_name2... 
```

[pyinstaller]: https://www.pyinstaller.org/