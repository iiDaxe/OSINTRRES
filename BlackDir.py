from urllib import request
import argparse
def logo():
	print("""
\x1b[32m
 ____  _            _    ____  _      
| __ )| | __ _  ___| | _|  _ \(_)_ __ 
|  _ \| |/ _` |/ __| |/ / | | | | '__|
| |_) | | (_| | (__|   <| |_| | | |   
|____/|_|\__,_|\___|_|\_\____/|_|_| version:0.1  

==================================================
C0ded By RedVirus[@redvirus0]
Group:BlackPearl[@bp.team]
Site:blackpreal.team
==================================================
BlackDir.py --url : url to find Directory
ex:
BlackDir.py --url http://google.com                                                                                                     
""")
def Dir(url,list):

    for i in list:
        Purl = url+"/"+i
        try:
            open = request.urlopen(Purl)
            print("\x1b[32mFound[+]")
            print(Purl)
        except:
            pass
parser = argparse.ArgumentParser("Find Directory")
parser.add_argument("-url","--url")
args = parser.parse_args()
url = args.url
lists = open("list.txt","r")
if args.url == None:
	logo()
else:
	print("\x1b[32mPlease wait we find Directory .. ")
	Dir(url,lists)
