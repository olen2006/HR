#importing user data from system
#https://stackoverflow.com/questions/421618/python-script-to-list-users-and-groups
#https://linuxize.com/post/how-to-list-users-in-linux/
#https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python
#######################################################################
#https://docs.python.org/3.7/library/pwd.html?highlight=pwd#module-pwd#
#######################################################################
import pwd

def fetch_users():
    users = []
    for user in pwd.getpwall():
        #check if it's a system user or not (if id >1000)
        #examples:
        #root:x:0:0:root:/root:/bin/bash
        #cloud_user:x:1002:1003::/home/cloud_user:/usr/bin/bash
        if user.pw_uid>=1000 and 'home' in user.pw_dir:
            #creating a list
            users.append({
                "name":user.pw_name,
                "id":user.pw_uid,
                "home":user.pw_dir,
                "shell":user.pw_shell,
                })
    return users

