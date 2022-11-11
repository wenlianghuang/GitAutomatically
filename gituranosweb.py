# No need password when push to Gitlab https://superuser.com/questions/1010542/how-to-make-git-not-prompt-for-passphrase-for-ssh-key
import subprocess

if __name__ == '__main__':
    
    proc = subprocess.Popen(['git','status'],stdout=subprocess.PIPE)
    print(proc)
    lines = proc.stdout.readlines()
    for i in range(len(lines)):
        lines[i] = str(lines[i],encoding='utf-8').split('\n')[0]
    newormodifiedfile = []
    for i in range(len(lines)):
        #if lines[i].find('modified: ') != -1 or lines[i].find("new file: ") != -1:
        #    #newormodifiedfile.append(lines[i].split('/')[-1])
        #    searchindex = lines[i].find('')
        if lines[i].find('modified: ') != -1:
            searchindex = lines[i].find('modified:')
            lines[i] = lines[i][searchindex:]
            newormodifiedfile.append(lines[i].split('modified: ')[-1])
        elif lines[i].find('new file: ') != -1:
            searchindex = lines[i].find('new file: ')
            lines[i] = lines[i][searchindex:]
            newormodifiedfile.append(lines[i].split('new file:')[-1])

    for i in range(len(newormodifiedfile)):
        temp = newormodifiedfile[i].replace('/','\\')
        temp = temp.replace(' ','')
        print(temp)
        args = [
            'git',
            'add',
            '{}'.format(temp)
        ]
        subprocess.run(args,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        argscommit = [
            'git',
            'commit',
            '-m',
            'modified file {}'.format(temp)
        ]
        subprocess.run(argscommit,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    print("Add all new file to the branch of git")
    args = [
        'git',
        'add',
        '.'
    ]
    subprocess.run(args,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    print("All the file are the newest in the folder uranosweb")
    args = [
        'git',
        'commit',
        '-m'
        'commit all the new file',
    ]
    subprocess.run(args,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    
