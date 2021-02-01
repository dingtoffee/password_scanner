import textract 
import datetime
import os
import pandas as pd 

# Please input the keywords you want to search here: 
keyword= ['password:','pwd:','pass:','pwd=','password=','pass=','password>','pwd>']

# Please input the path for the searched list of directory 
path = "C:\\Temp\\dir"
date2 = datetime.datetime.now()
date = date2.strftime("%Y-%m-%d") 

# Any exception you want to exclude, please put it down here. 
exceptionpath = 'z:\\~keywords\\'

# Output File format and location 
outputfile ='C:\\Temp\\result\\tempresult' + date+ '.txt'
errorfile = 'C:\\Temp\\result\\error' + date + '.txt'
finalfile = 'C:\\Temp\\result\\finalresult' + date + '.csv' 

# Keywords to extract 
textract_ext = ['docx','eml','epub','msg','pptx','ps','txt','xlsx','xls','rtf','pdf']
native_ext = ['template','conf','config','deploy','bat','vbs','LOG','xml','cmd','vb','py','pl','csv','html','json','htm']

# Static File do not modify 
fp = 'C:\\Temp\\result\\fp.csv'
softfolder = 'C:\\Temp\\result\\Soft_Folder_review.csv'

# To search for any cleartext password
def searchstring(): 
    for paths in os.listdir(path) : 
        f = open(path+"\\"+paths,'r', encoding='utf-8', errors='ignore')
        lines = f.read().splitlines()
      
        f.close()
  
        for line in lines:
            try: 
                if exceptionpath in line:
                    with open (errorfile, 'a+', encoding = 'utf-8', errors = 'ignore') as e :
                        
                       e.write(': Known False Positive. Path:' + line + '\n')
                       e.close()
                ext = line.rsplit('.',1)
                
           
                if ext[1] in textract_ext:
                    text = textract.process(ext[0]+'.'+ext[1]).decode('utf-8')
                     
                    for x in keyword:
                             
                            if x in text:
                                
                                time = datetime.datetime.now()
                                with open(outputfile,'a+',encoding='utf-8', errors='ignore') as w: 
                                
                                    w.write(str(time)+ '||' + str(ext[0])+'.'+str(ext[1])+'||'+str(x)+'\n')
                                    w.close()
                            
           
                        
                elif ext[1] in native_ext: 
               
                   open_file=open(ext[0] + '.' + ext[1],'r',encoding='utf-8',errors='ignore')
                   read_file=open_file.read()
               
                   for x in keyword:
                           if x in read_file:
                          
                                time = datetime.datetime.now() 
                          
                                with open(outputfile,'a+',encoding='utf-8', errors='ignore') as w: 
                                
                                    w.write(str(time)+ '||' + str(ext[0])+'.'+str(ext[1])+'||'+str(x)+'\n') 
                                    w.close()
                    
               
                else:
                    with open (errorfile, 'a+', encoding = 'utf-8', errors = 'ignore') as e :
                        time = datetime.datetime.now()
                        e.write(str(time)+ '||'+ 'File Type not support:' + line+ '\n')
                        e.close()
                    
 
            except Exception as e:
                
                with open (errorfile, 'a+', encoding = 'utf-8', errors = 'ignore') as k :
                    time = datetime.datetime.now() 
                    k.write(str(time)+ '||' + str(e) + '\n')
                    k.close()
            
                continue;
# Filtering with known false positve and identify folder owner 
def validation():

# Load and read the known false positive. Transform into pandas dataframe. 
    df = pd.read_csv(fp)

# Load and read the existing unfiltered result and also load the soft folder owners.  
    df3 = pd.DataFrame(columns=['timestamp','path','keywords', 'FolderName', 'FolderOwner', 'EmailAddress', 'AttachementName'])
    df2 = pd.read_csv(outputfile,sep='\|\|', engine='python',header=None)
    df2.columns = ['timestamp', 'path' ,'keywords']
    df6 = pd.read_csv (softfolder)

# Identify the owner and email address 
    for index, row in df2.iterrows():
        y = row['path']
        x = df[df['FP']== y].empty
        if x is True:
            rows = pd.DataFrame(data=[row])
            rows['FolderName'] = [x.split('\\')[5] for x in rows['path']]
            rows['FolderOwner'] = rows['FolderName'].map(df6.set_index('Folder')['Owner'])
            rows['EmailAddress'] = rows['FolderName'].map(df6.set_index('Folder')['Email'])
            rows['AttachementName'] = rows['EmailAddress']+ ' result.txt'
            df3 = pd.concat([df3,rows],ignore_index=True)
    df3.to_csv(finalfile, index=False) 


def main():
    searchstring()
    validation()

if __name__== "__main__":
    main() 


