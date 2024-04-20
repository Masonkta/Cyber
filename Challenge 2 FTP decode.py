from ftplib import FTP

METHOD = 7

ftp_ip = '138.47.161.43'  
ftp_user = 'anonymous'
ftp_password = ''

ftp = FTP()
ftp.connect(ftp_ip)
ftp.login(ftp_user, ftp_password)

#ftp.cwd('files')
#if(METHOD == 7):
 #   ftp.cwd('7')
#if(METHOD == 10):
 #   ftp.cwd('10')

directory_listing = []
ftp.dir(directory_listing.append)

ftp.quit()

permissions_list = []
for line in directory_listing:
    parts = line.split(maxsplit=8)
    if len(parts) >= 9:
        permissions = parts[0]
        permissions_list.append(permissions)

if(METHOD == 7):
    message = ""
    for permission in permissions_list:
        binary = ""
        if(permission[0] != "-" or permission[1] != "-" or permission[2] != "-"):
            continue
        i = 1
        while(i < (len(permission))):
            if(permission[i] == '-'):
                binary += "0"
            else:
                binary += "1"
            i += 1
        convert = int(binary, 2)
        bin = convert.to_bytes(7, "big")
        ascii = bin.decode()
        message += ascii
    print(message)
if(METHOD == 10):
    message = ""
    allb = ""
    for permission in permissions_list:
        binary = ""
        i = 0
        while(i < (len(permission))):
            if(permission[i] == '-'):
                binary += "0"
            else:
                binary += "1"
            i += 1
        allb += binary
    j = 0
    k = 0
    Sevbit = ""
    while(j < len(allb)):
        Sevbit += allb[j]
        j += 1
        k += 1
        if(k == 7):
            convert = int(Sevbit, 2)
            bin = convert.to_bytes(7, "big")
            ascii = bin.decode()
            message += ascii
            k = 0
            Sevbit = ""
    print(message)