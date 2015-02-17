
import subprocess

def shellmysql(list):
    for a in list:
        # a = """ + str(a) + """
        subprocess.call(["./getsdf2.sh", a])
        