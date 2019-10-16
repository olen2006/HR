#importing user data from system
#https://stackoverflow.com/questions/421618/python-script-to-list-users-and-groups
#https://linuxize.com/post/how-to-list-users-in-linux/
import os,pwd, grp


#for p in pwd.getpwall():
   # print (p[0], grp.getgrgid(p[3])[0])

groups = grp.getgrall()
#def get_username ():
for group in groups:
    for user in group[3]:
        print (user, group[0])


   # return pwd.getpwuid(os.getuid())[0]

print("--------------------")

#https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python

