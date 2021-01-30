# Clear-Text-Password-Scanner-in-Windows-Share-Drive
Clear text password is always an issue to corporate environment and from time to time we will see clear text password stored in windows share drive that has beens shared to public. To identify these password files, a script was created to automatically manage it. 

The scripts are written in Python 3. 

# Indexing the directory 
1. You will need to amend the `dirlist.py` to edit the directory you want to scan through 
    ````python
    # put your path here 
    # Network SMB path you want to search 
    root_dir = ("xxxxxx", "etc.")
    # location where you want to put the result 
    stored_dir = 'xxxxxxxxx'
    # exception you want to filter
    exception_path = ["snapshot"]
    ````
2. Run the script 
   `python dirlist.py`
   It can take a few days to complete the scanning for > 1M files and over hundreds folder. Afterwards, it will be broken down into multiple files with all the files listed. Each of the file will have 1000 entries.

# Identify Clear-Text Passwords in the directory 
1. Install pandas
    ````python 
    pip install pandas 
    ````
2. Edit scan.py to include the directory and keywords you want to scan
   ````python 
    # Please input the keywords you want to search here: 
    keyword= ['password:','pwd:','pass:','pwd=','password=','pass=','password>','pwd>']
    # Please input the path for the searched list of directory 
    path = "C:\\Temp\\dir"
    date2 = datetime.datetime.now()
    date = date2.strftime("%Y-%m-%d")
    # Any exception you want to exclude, please put it down here. 
    exceptionpath = 'C:\\~file\\'
    # Output File format and location 
    outputfile ='C:\\Temp\\result\\tempresult' + date+ '.txt'
    errorfile = 'C:\\Temp\\result\\error' + date + '.txt'
    finalfile = 'C:\\Temp\\result\\finalresult' + date + '.csv'
    # the type of file supported
    textract_ext = ['docx','eml','epub','msg','pptx','ps','txt','xlsx','xls','rtf','pdf']
    native_ext = ['template','conf','config','deploy','bat','vbs','LOG','xml','cmd','vb','py','pl','csv','html','json','htm']
    # Known false positive you want to exclude 
    fp = 'C:\\Temp\\result\\fp.csv'
    # Knwon folder owner and their email address 
    softfolder = 'C:\\Temp\\result\\folder_owner.csv'
3. After editing it you could run it by typing `python scan.py`
