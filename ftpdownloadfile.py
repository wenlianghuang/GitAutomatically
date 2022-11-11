import ftplib

from ftppassword import FTPpassword

if __name__ == '__main__':
    print("Start")
    #server = ftplib.FTP("61.218.64.189","gaiaadmin","3edc$RFV")
    server = ftplib.FTP(FTPpassword.IPName(),FTPpassword.Account(),FTPpassword.Password())
    server.encoding='utf-8'
    server.cwd("/Matt/URANOSWeb/uploadfile")
    test = "result.txt"
    with open('D:/uranosweb/tempdownload/downloadresult.txt','wb') as f:
        server.retrbinary(f'RETR {test}',f.write)
        f.close()
    with open('D:/uranosweb/tempdownload/downloadresult.txt','r') as file:
        alllines = file.readlines()
        allsub = []
        for i in range(len(alllines)):
            alllines[i] = alllines[i].split('\n')[0]
            allsub.append(alllines[i].split('\\')[-1])
        file.close()
    for i in range(len(allsub)):
        if allsub[i].find('result.txt') != -1:
            continue
        else:
            tempheader = alllines[i].split("\\www\\Uranos\\URANOSWeb\\")[0]
            templast = alllines[i].split("\\www\\Uranos\\URANOSWeb\\")[1]
            temptotal = tempheader + "\\uranosweb\\" + templast
            with open("{}".format(temptotal),'wb') as f:
                server.retrbinary(f'RETR {allsub[i]}',f.write)
                f.close()
    print(allsub)
    print(alllines)
    for i in range(len(allsub)):
        server.delete(allsub[i])
    server.quit()
    
    