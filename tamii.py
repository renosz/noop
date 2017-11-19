-*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime, timedelta, date
from urlparse import urlparse
from bs4 import BeautifulSoup
from gtts import gTTS
import time,timeit,random,sys,json,codecs,urllib2,urllib,requests,threading,glob,os,subprocess,multiprocessing,re,calendar
import wikipedia

ki = LINETCR.LINE()
ki.login(token="EmZMiC3V1ZV70KrEMMw6.TZBfSxLpwQmajTfI0hZL5G.11k6S1sUlX9SbdA8oDJustBIJVGyobI+e3SFkBE2g8g=")
ki.loginResult()

ki1 = LINETCR.LINE()
ki1.login(token="EmDyCogmbpnEAkV37Zbb.BNyZ+h9RxCUErhI47z2TsW.XXPN7WZAaav135iokhu+wzO588N8TP7nDozMCJUeQjc=")
ki1.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EmspKirwbEjemqqHJUb7.PxA11UvF6+oIj1J2xHVgHW.DD+N4SDD7wvuasJsGnmW5plCMBHpI1kffIFV9ma44Kc=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EmdpE54Je1ojetkXmKQd.3ZijQj/+HYJ/+9NTGXTdBq.Dkv3tBOnJ4DsvFu6ER5mK2zR7h0FRAW0/FJyZiSD2Fs=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="Emesgp6g4xLptFAcKEe2.HczpEpY3698wuSB+TzCDKG.vFtZpDippE+ZkQxxVEDn1BmpjyM+z+f/x4/Lo+cAFlk=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EmMtwsiInIfBXPVS5fYa.i/2QVqxGpVzmWQXItt4HYG.cfbtejgIlGQE3TTAg7FlMWcE1/6kwokKNe3wDg1gztM=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EmCxepD4zQoJp5IhDbta.DP7HM0ARnuIu/2g0+3pMUG./+3rQ+luem39IsiuASywPOVjmG+0TpJhMpmZowgn8yI=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="Eme45nZDSATx9C6vYxRa.M5S4YxDWvhoYOasbMPWroG.Tq/iSCV68m9567XK4xxEGSXOAOVJEPwNW+odUm/BwT4=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EmIRhD60WnHD3t4FET34.9gH7ABV+xQLJo9i7SbFX5a.Yr0Yii0G3ouW7kOEMdXrPongIIs0Q2ab9Q0xUiRLfHI=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EmLppwNR3nIRHTOtPilb.8udcfgLi7ehlJbE2o+xCkW.QzwPU+t85FDCd/TcU0H5NdPq0MUzuCXRzaZPRp1O/mY=")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="EmYDhAhUQqmCaUB8SZA4.XzkQX6Z6SKas/aWEdxhG9a.HTgYRulRHxXSc+72zLVfT2VLIRVZvh4ImQvEtU6KxBg=")
ki10.loginResult()

ki11 = LINETCR.LINE()
ki11.login(token="EmCXaH6hkxN7L4iWpyGa.M18YOGKVCrQRdiHWLocYoG.Bga5dUzA36+J0GekTRX7Sz5R9vrUWYaxXn7rGrXUPBc=")
ki11.loginResult()

ki12 = LINETCR.LINE()
ki12.login(token="EmjOueAJz9I4iNjWUPm0.xk6CFUa1TffEm+BFjYuhCa.pk6HGOsm6rlBtQLo4D48hQAaLUBlOgUJx0qGfVEpyc8=")
ki12.loginResult()

ki13 = LINETCR.LINE()
ki13.login(token="Em44M0djUhjilmwO5eW4.gNyro7TbVPOq9q7KfxZ6ja.fD1FXX13tI04xIuOkhGBE5+F3sywEuweexo1C/GxJ1U=")
ki13.loginResult()

ki14 = LINETCR.LINE()
ki14.login(token="Emm6NUELDiThHb11mo63.beFYyPfuxT1XkkxB0z7bOW.iKoovhLczCH/Pd0VtVxhYA/x5NpywVyBiceIZwcxI2s=")
ki14.loginResult()

ki15 = LINETCR.LINE()
ki15.login(token="EmTyM8gXpOZkJwy0hnK3.Zcwf6HrGpji9sCc98VTOeW.suZo5gb/3FZ2hEFhe2+t+gomNdr1GnH0566EGnElV58=")
ki15.loginResult()

ki16 = LINETCR.LINE()
ki16.login(token="Emaas45PFxDMQU2svLIa.r5CTm/T+B9J2h3ZXLAhq6G.od8/LyM8B5Luv7HiYiew3n0zS1uLfsyqd5Nja1SeApM=")
ki16.loginResult()

ki17 = LINETCR.LINE()
ki17.login(token="Emwfi9Mdukz6QroWpHQ7.bHov9ONJEzx2Ya/PwMshPW.0DaYTC4xiCU3AaklyQNCVxoRowvu47htNMQNGM/Jpo8=")
ki17.loginResult()

ki18 = LINETCR.LINE()
ki18.login(token="EmLX3yrZguae6q822s49.HKYa3NeUc1iHvq5GaRXJgq.yAuKmCAeoHK8R/5p65i8x1N8Ek1an6ywPurnBBEq/jQ=")
ki18.loginResult()

ki19 = LINETCR.LINE()
ki19.login(token="Emj0RIGQoBz8l2rFURCa.r5rHUZbmm8kdzZrXsPDx/G.cVrIACSFRdtOsjqC0oMT4+8xKPwvu0+yEPqB31QUmF8=")
ki19.loginResult()

ki20 = ki21 = ki22 = ki23 = ki24 = ki25 = ki26 = ki27 = ki28 = ki29 = ki30 = ki31 = ki32 = ki33 = ki34 = ki35 = ki36 = ki37 = ki38 = ki39 = ki40 = ki41 = ki42 = ki1

print "Tamii Bot"
reload(sys)
sys.setdefaultencoding('utf-8')

album = None
image_path = 'tmp/tmp.jpg'
P1=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30,ki31,ki32,ki33,ki34,ki35,ki36,ki37,ki38,ki39,ki40,ki41,ki42]
P2=[ki1,ki2,ki3,ki4,ki5]
P3=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = ki.getProfile().mid
ki1mid = ki1.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
ki11mid = ki11.getProfile().mid
ki12mid = ki12.getProfile().mid
ki13mid = ki13.getProfile().mid
ki14mid = ki14.getProfile().mid
ki15mid = ki15.getProfile().mid
ki16mid = ki16.getProfile().mid
ki17mid = ki17.getProfile().mid
ki18mid = ki18.getProfile().mid
ki19mid = ki19.getProfile().mid
ki20mid = ki20.getProfile().mid
ki21mid = ki21.getProfile().mid
ki22mid = ki22.getProfile().mid
ki23mid = ki23.getProfile().mid
ki24mid = ki24.getProfile().mid
ki25mid = ki25.getProfile().mid
ki26mid = ki26.getProfile().mid
ki27mid = ki27.getProfile().mid
ki28mid = ki28.getProfile().mid
ki29mid = ki29.getProfile().mid
ki30mid = ki30.getProfile().mid
ki31mid = ki31.getProfile().mid
ki32mid = ki32.getProfile().mid
ki33mid = ki33.getProfile().mid
ki34mid = ki34.getProfile().mid
ki35mid = ki35.getProfile().mid
ki36mid = ki36.getProfile().mid
ki37mid = ki37.getProfile().mid
ki38mid = ki38.getProfile().mid
ki39mid = ki39.getProfile().mid
ki40mid = ki40.getProfile().mid
ki41mid = ki41.getProfile().mid
ki42mid = ki42.getProfile().mid
Botsa=[ki1mid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,ki12mid,ki13mid,ki14mid,ki15mid,ki16mid,ki17mid,ki18mid,ki20mid,ki21mid,ki22mid,ki23mid,ki24mid,ki25mid,ki26mid,ki27mid,ki28mid,ki29mid,ki30mid,ki31mid,ki32mid,ki33mid,ki34mid,ki35mid,ki36mid,ki37mid,ki38mid,ki39mid,ki40mid,ki41mid,ki42mid]
Bots=[ki1mid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,ki12mid,ki13mid,ki14mid,ki15mid,ki16mid,ki17mid,ki18mid,ki20mid,ki21mid,ki22mid,ki23mid,ki24mid,ki25mid,ki26mid,ki27mid,ki28mid,ki29mid,ki30mid,ki31mid,ki32mid,ki33mid,ki34mid,ki35mid,ki36mid,ki37mid,ki38mid,ki39mid,ki40mid,ki41mid,ki42mid]
protectname = []
kitsuneurl = []
kitsuneprotection = []
autoCancel = []
kitsuneautoinvite = []
kitsunetalkban = []
kitsunewelcome = []
admsa = "ub736c5b1794f5aa30026d162d07ce5e6"
kitsune = "ub736c5b1794f5aa30026d162d07ce5e6"
with open('1.json', 'r') as fp:
    wait = json.load(fp)
with open('2.json', 'r') as fp:
    wait2 = json.load(fp)
with open('blacklist.json', 'r') as fp:
    wait["blacklist"] = json.load(fp)
with open('bots.json', 'r') as fp:
    wait["bots"] = json.load(fp)
	
mimic = {
    "status":False,
    "target":{},
    "setkey":"",
    "pap":"http://otaku-w9pxf76zfsktmx3e.stackpathdns.com/wp-content/uploads/2017/08/Sarada-1024x576.png",
    }

setTime = {}
setTime = wait2['setTime']
Bots = wait["bots"]

contact = ki.getProfile()
backup = ki.getProfile()
backup.kitsuneName = contact.kitsuneName
backup.kitsuneBio = contact.kitsuneBio
backup.kitsunephotoStatus = contact.kitsunephotoStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "Night Core Aditya K-Music"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+70)
        end_content = s.find(',"ow"',start_content-70)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            page = page[end_content:]
    return items

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = ki.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.kitsunemembers) <= wait["autoCancel"]["kitsunemembers"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.kitsunemembers) <= wait["autoCancel"]["kitsunemembers"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ki.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ki.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            kitsune = msg.to
            if wait["talkban"] == True:
             if msg.from_ in wait["talkblacklist"]:
                try:
                    random.choice(P1).kitsuneText(kitsune,ki.getContact(msg.from_).kitsuneName + " Jangan Ngomong Njing")
                    random.choice(P1).kickoutFromGroup(kitsune,[msg.from_])
                except:
                    try:
                        random.choice(P2).kitsuneText(kitsune,ki.getContact(msg.from_).kitsuneName + " Jangan Ngomong Njing")
                        random.choice(P2).kickoutFromGroup(kitsune,[msg.from_])
                    except:
                        ki.kitsuneText(kitsune,ki.getContact(msg.from_).kitsuneName + " Jangan Ngomong Njing")
                        ki.kickoutFromGroup(kitsune,[msg.from_])
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                text = msg.text
                if text is not None:
                    if msg.contentType == 1:
                        ki.kitsuneImageWithURL(kitsune,mimic["pap"])
                    else:
                        ki.kitsuneText(kitsune,text)
                else:
                    if msg.contentType == 7:
                        msg.contentType = 7
                        msg.text = None
                        msg.contentMetadata = {
                                              'STKID': "15597669",
                                              'STKPKGID': "1403270",
                                              'STKVER': "1" }
                        ki.sendMessage(msg)
                    if msg.contentType == 9:
                        msg.contentType = 9
                        msg.contentMetadata={'PRDTYPE': 'STICKER',
                                            'STKVER': '1',
                                            'MSGTPL': '5',
                                            'STKPKGID': '1380280'}
                        msg.text = None
                        ki.sendMessage(msg)
                    if msg.contentType == 13:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
                        ki.sendMessage(msg)
                    if msg.contentType == 1:
                        ki.kitsuneImageWithURL(kitsune,mimic["pap"])
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            kitsune = msg.to
            print(
            " TO: {}\n".format(msg.to),
            "FROM: {}\n".format(msg.from_),
            "TEXT: {}\n".format(msg.text),
            "CONTENT TYPE: {}\n".format(msg.contentType),
            "METADATA: {}\n".format(msg.contentMetadata),
            "TYPE: {}\n".format(msg.toType),
            "MESSAGE ID: {}\n".format(msg.id),
            "DATE: {}\n\n".format(msg.createdTime)
            )
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                ki.like(url[25:58], url[66:], likeType=1001)
                ki.comment(url[25:58], url[66:], "Auto Like by : Kitsune Bot Control\n\nhttp://line.me/ti/p/%40ryu7435j\nhttp://line.me/ti/p/~fcimicrosoftaditya")
            if msg.contentType == 13:
                if wait["kick"] == True:
                        random.choice(P1).kickoutFromGroup(kitsune,[msg.contentMetadata["mid"]])
                        wait["kick"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Sukses to Kick")
                if wait["talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["talkblacklist"]:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Already in Talkban")
                        wait["talkwblacklist"] = False
                    else:
                        wait["talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["talkwblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Sukses Add to Talkban")
                elif wait["talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["talkblacklist"]:
                        del wait["talkblacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Sukses Delete from Talkban")
                        wait["talkdblacklist"] = False
                    else:
                        wait["talkdblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Not In Talkban")
                if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Already in Blacklist")
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        wait["wblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Sukses Add to Blacklist")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Sukses Delete from Blacklist")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Not In Blacklist")
                elif wait["twblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Already in Blacklist")
                        wait["twblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        wait["twblacklist"] = True
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Sukses Add to Blacklist")
                elif wait["tdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + " Sukses Delete from Blacklist")
                        wait["tdblacklist"] = True
                    else:
                        wait["tdblacklist"] = True
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        ki.kitsuneText(kitsune,contact.kitsuneName + "Not In Blacklist")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'kitsuneName' in msg.contentMetadata:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ki.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ki.kitsuneText(kitsune,"[Display Name]:\n" + msg.contentMetadata["kitsuneName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Status Message]:\n" + contact.kitsuneBio + "\n[Picture Status]:\nhttp://dl.profile.line-cdn.net/" + contact.kitsunephotoStatus + "\n[Cover]:\n" + str(cu))
                    else:
                        contact = ki.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ki.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ki.kitsuneText(kitsune,"Nama:" + contact.kitsuneName + "\n\nUser ID:" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.kitsuneBio)
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    ki.kitsuneText(kitsune,"menempatkan URL\n" + msg.contentMetadata["postEndUrl"])
            elif msg.text is None:
                return
            elif msg.text.lower() == mimic["setkey"]+' help' or msg.text.lower() == mimic["setkey"]+'help':
                    profile = ki.getProfile()
                    ki.kitsuneText(kitsune,"「" + mimic["setkey"].title() + "」\n" \
                    +mimic["setkey"].title()+" help\n" \
                    +mimic["setkey"].title()+" ikkeh\n" \
                    +mimic["setkey"].title()+" steal\n" \
                    +mimic["setkey"].title()+" getinfo\n" \
                    +mimic["setkey"].title()+" getid\n" \
                    +mimic["setkey"].title()+" getpictstatus\n" \
                    +mimic["setkey"].title()+" micall\n" \
                    +mimic["setkey"].title()+" banall\n" \
                    +mimic["setkey"].title()+" unbanall\n" \
                    +mimic["setkey"].title()+" teamall\n" \
                    +mimic["setkey"].title()+" unteamall\n" \
                    +mimic["setkey"].title()+" ban\n" \
                    +mimic["setkey"].title()+" ban repat\n" \
                    +mimic["setkey"].title()+" unban\n" \
                    +mimic["setkey"].title()+" unban repeat\n" \
                    +mimic["setkey"].title()+" talkban\n" \
                    +mimic["setkey"].title()+" untalkban\n" \
                    +mimic["setkey"].title()+" abort\n" \
                    +mimic["setkey"].title()+" ban\n" \
                    +mimic["setkey"].title()+" mimic\n" \
                    +mimic["setkey"].title()+" instagram\n" \
                    +mimic["setkey"].title()+" youtube\n" \
                    +mimic["setkey"].title()+" wikipedia\n" \
                    +mimic["setkey"].title()+" lyric\n" \
                    +mimic["setkey"].title()+" music\n" \
                    +mimic["setkey"].title()+" image\n" \
                    +mimic["setkey"].title()+" say@id\n" \
                    +mimic["setkey"].title()+" autoadd\n" \
                    +mimic["setkey"].title()+" autojoin\n" \
                    +mimic["setkey"].title()+" me\n" \
                    +mimic["setkey"].title()+" bot\n" \
                    +mimic["setkey"].title()+" ourl\n" \
                    +mimic["setkey"].title()+" invite:gcreator\n" \
                    +mimic["setkey"].title()+" bio\n" \
                    +mimic["setkey"].title()+" pictstatus\n" \
                    +mimic["setkey"].title()+" pp\n" \
                    +mimic["setkey"].title()+" sampul\n" \
                    +mimic["setkey"].title()+" mid\n" \
                    +mimic["setkey"].title()+" allbio:\n" \
                    +mimic["setkey"].title()+" myname:\n" \
                    +mimic["setkey"].title()+" mybio:\n" \
                    +mimic["setkey"].title()+" name1: - name42:\n" \
                    +mimic["setkey"].title()+" gn\n" \
                    +mimic["setkey"].title()+" lurking\n" \
                    +mimic["setkey"].title()+" gcreator\n" \
                    +mimic["setkey"].title()+" groups\n" \
                    +mimic["setkey"].title()+" mcheck\n" \
                    +mimic["setkey"].title()+" tcheck\n" \
                    +mimic["setkey"].title()+" mlist\n" \
                    +mimic["setkey"].title()+" friend\n" \
                    +mimic["setkey"].title()+" gcancel1-42\n" \
                    +mimic["setkey"].title()+" clear ban\n" \
                    +mimic["setkey"].title()+" pesan set:\n" \
                    +mimic["setkey"].title()+" pesan cek\n" \
                    +mimic["setkey"].title()+" welcomemessage pict set\n" \
                    +mimic["setkey"].title()+" spam add:\n" \
                    +mimic["setkey"].title()+" spam:<number>\n" \
                    +mimic["setkey"].title()+" spam on <number> <query>\n" \
                    +mimic["setkey"].title()+" spam off <number> <query>\n" \
                    +mimic["setkey"].title()+" spam cek\n" \
                    +mimic["setkey"].title()+" url\n" \
                    +mimic["setkey"].title()+" tr id@en\n" \
                    +mimic["setkey"].title()+" tr en@id\n" \
                    +mimic["setkey"].title()+" tr id@jp\n" \
                    +mimic["setkey"].title()+" tr jp@id\n" \
                    +mimic["setkey"].title()+" tr id@th\n" \
                    +mimic["setkey"].title()+" tr th@id\n" \
                    +mimic["setkey"].title()+" gift\n" \
                    +mimic["setkey"].title()+" kick\n" \
                    +mimic["setkey"].title()+" miclist\n" \
                    +mimic["setkey"].title()+" cium\n" \
                    +mimic["setkey"].title()+" banlist\n" \
                    +mimic["setkey"].title()+" blocklist\n" \
                    +mimic["setkey"].title()+" kiss\n" \
                    +mimic["setkey"].title()+" honey\n" \
                    +mimic["setkey"].title()+" cau\n" \
                    +mimic["setkey"].title()+" contact <on/off>\n" \
                    +mimic["setkey"].title()+" cancel <on/off>\n" \
                    +mimic["setkey"].title()+" qr <on/off>\n" \
                    +mimic["setkey"].title()+" inv <on/off>\n" \
                    +mimic["setkey"].title()+" protect <on/off>\n" \
                    +mimic["setkey"].title()+" share <on/off>\n" \
                    +mimic["setkey"].title()+" welcomemessage <on/off>\n" \
                    +mimic["setkey"].title()+" talkban <on/off>\n" \
                    +mimic["setkey"].title()+" jam <on/off>\n" \
                    +mimic["setkey"].title()+" leave <on/off>\n" \
                    +mimic["setkey"].title()+" namelock <on/off>\n" \
                    +mimic["setkey"].title()+" setkey\n" \
                    +mimic["setkey"].title()+" mayhem\n\nSelfbot\n   " + profile.kitsuneName + "\n   Support:\n   􀬁􀆆􏿿TAMII BOT CONTROL􀬁􀆆􏿿")
 #          Copy Profil
#======================================
            elif "Sampul @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Sampul @","")
                _nametarget = _name.rstrip('  ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ki.getContact(target)
                            cu = ki.channel.getCover(target)
                            path = str(cu)
                            ki.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict " in msg.text:
                umid = msg.text.replace("Midpict ","")
                contact = ki.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    ki.sendImageWithURL(msg.to,image)
                except Exception as error:
                    ki.sendText(msg.to,(error))
                    pass
            elif "Ambilin " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Ambilin ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = ki.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = ki.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    ki.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    ki.sendText(msg.to,(error))
                                    pass
                            except:
                                ki.sendText(msg.to,"Error!")
                                break
                else:
                    ki.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
#======================================
            elif msg.text.lower() == 'welcome':
                ginfo = ki.getGroup(msg.to)
                ki.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                ki.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#======================================
                if not op.param2 in Bots:
                  if["kitsuneprotection"] == True:  
                   try:
                       klist=[ki1mid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,ki12mid,ki13mid,ki14mid,ki15mid,ki16mid,ki17mid,ki18mid]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       ki19.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       ki19.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
#======================================
            elif "Tk " in msg.text:
                       nk0 = msg.text.replace("Tk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ki.getGroup(msg.to)
                       ginfo = ki.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       ki.updateGroup(gs)
                       invsend = 0
                       Ticket = ki.reissueGroupTicket(msg.to)
                       ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki19.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki19.leaveGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    ki.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    ki.updateGroup(gs)
#======================================
            elif msg.text.lower() == mimic["setkey"]+'ikkeh' or msg.text.lower() == mimic["setkey"]+' ikkeh':
                ki.kitsuneText(kitsune,"「Copy Profil」\n"+ "Commands:\n" \
					+mimic["setkey"].title()+" ikkeh on <@|~> \n" \
					+mimic["setkey"].title()+" ikkeh off \n" \
					+mimic["setkey"].title()+" ikkeh setdefault ")
            elif msg.text.lower() == mimic["setkey"]+'steal' or msg.text.lower() == mimic["setkey"]+' steal':
                ki.kitsuneText(kitsune,"「Steal」\n"+ "Usage:" + mimic["setkey"].title()+"get <type> [@\*]\nType: pict, cover, vid")
            elif msg.text.lower() == mimic["setkey"]+'ikkeh setdefault' or msg.text.lower() == mimic["setkey"]+' setdefault':
                ki.kitsuneText(kitsune,"「Backup Profil」\nSukses Setdefault\nDisplayName:" + backup.kitsuneName + "\n「Status」\n" + backup.kitsuneBio + "\n「Picture」")
                ki.kitsuneImageWithURL(kitsune,"http://dl.profile.line-cdn.net/" + backup.kitsunephotoStatus)
            elif msg.text.lower() == mimic["setkey"]+'ikkeh off' or msg.text.lower() == mimic["setkey"]+' ikkeh off':
                    try:
                       ki.updateDisplayPicture(backup.kitsunephotoStatus)
                       ki.updateProfile(backup)
                       ki.kitsuneText(kitsune,"「Backup Profil」\nSukses Backup\nDisplayName:" + backup.kitsuneName + "\n「Status」\n" + backup.kitsuneBio + "\n「Picture」")
                       ki.kitsuneImageWithURL(kitsune,"http://dl.profile.line-cdn.net/" + backup.kitsunephotoStatus)
                    except Exception as e:
                       ki.kitsuneText(kitsune, str(e))
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on5 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on5 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on5') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on5'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki5.cloneContact(target)
                            group = ki5.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki5.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki5.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki5.cloneContact(target)
                else:
                    ki5.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on6 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on6 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on6') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on6'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki6.cloneContact(target)
                            group = ki6.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki6.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki6.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki6.cloneContact(target)
                else:
                    ki6.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on7 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on7 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on7') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on7'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki7.cloneContact(target)
                            group = ki7.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki7.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki7.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki7.cloneContact(target)
                else:
                    ki7.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on8 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on8 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on8') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on8'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki8.cloneContact(target)
                            group = ki8.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki8.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki8.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki8.cloneContact(target)
                else:
                    ki8.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on9 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on9 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on9') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on9'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki9.cloneContact(target)
                            group = ki9.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki9.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki9.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki9.cloneContact(target)
                else:
                    ki9.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on10 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on10 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on10') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on10'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki10.cloneContact(target)
                            group = ki10.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki10.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki10.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki10.cloneContact(target)
                else:
                    ki10.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on11 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on11 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on11') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on11'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki11.cloneContact(target)
                            group = ki11.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki11.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki11.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki11.cloneContact(target)
                else:
                    ki11.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on12 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on12 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on12') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on12'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki12.cloneContact(target)
                            group = ki12.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki12.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki12.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki12.cloneContact(target)
                else:
                    ki12.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on13 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on13 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on13') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on13'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki13.cloneContact(target)
                            group = ki13.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki13.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki13.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki13.cloneContact(target)
                else:
                    ki13.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on14 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on14 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on14') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on14'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki14.cloneContact(target)
                            group = ki14.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki14.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki14.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki14.cloneContact(target)
                else:
                    ki14.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on15 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on15 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on15') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on15'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki15.cloneContact(target)
                            group = ki15.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki15.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki15.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki15.cloneContact(target)
                else:
                    ki15.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on16 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on16 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on16') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on16'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki16.cloneContact(target)
                            group = ki16.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki16.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki16.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki16.cloneContact(target)
                else:
                    ki16.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on17 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on17 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on17') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on17'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki17.cloneContact(target)
                            group = ki17.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki17.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki17.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki17.cloneContact(target)
                else:
                    ki17.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on18 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on18 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on18') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on18'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki18.cloneContact(target)
                            group = ki18.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki18.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki18.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki18.cloneContact(target)
                else:
                    ki18.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on19 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on19 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on19') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on19'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki19.cloneContact(target)
                            group = ki19.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki19.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki19.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki19.cloneContact(target)
                else:
                    ki19.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on20 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on20 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on20') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on20'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki20.cloneContact(target)
                            group = ki20.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki20.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki20.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki20.cloneContact(target)
                else:
                    ki20.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on21 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on21 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on21') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on21'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki21.cloneContact(target)
                            group = ki21.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki21.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki21.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki21.cloneContact(target)
                else:
                    ki21.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on22 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on22 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on22') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on22'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki22.cloneContact(target)
                            group = ki22.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki22.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki22.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki22.cloneContact(target)
                else:
                    ki22.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on23 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on23 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on23') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on23'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki23.cloneContact(target)
                            group = ki23.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki23.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki23.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki23.cloneContact(target)
                else:
                    ki23.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on24 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on24 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on24') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on24'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki24.cloneContact(target)
                            group = ki24.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki24.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki24.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki24.cloneContact(target)
                else:
                    ki24.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on25 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on25 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on25') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on25'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki25.cloneContact(target)
                            group = ki25.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki25.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki25.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki25.cloneContact(target)
                else:
                    ki25.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on26 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on26 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on26') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on26'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki26.cloneContact(target)
                            group = ki26.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki26.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki26.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki26.cloneContact(target)
                else:
                    ki26.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on27 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on27 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on27') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on27'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki27.cloneContact(target)
                            group = ki27.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki27.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki27.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki27.cloneContact(target)
                else:
                    ki27.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on28 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on28 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on28') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on28'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki28.cloneContact(target)
                            group = ki28.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki28.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki28.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki28.cloneContact(target)
                else:
                    ki28.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on29 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on29 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on29') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on29'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki29.cloneContact(target)
                            group = ki29.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki29.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki29.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki29.cloneContact(target)
                else:
                    ki29.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on30 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on30 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on30') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on30'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki30.cloneContact(target)
                            group = ki30.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki30.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki30.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki30.cloneContact(target)
                else:
                    ki30.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on31 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on31 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on31') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on31'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki31.cloneContact(target)
                            group = ki31.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki31.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki31.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki31.cloneContact(target)
                else:
                    ki31.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on32 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on32 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on32') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on32'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki32.cloneContact(target)
                            group = ki32.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki32.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki32.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki32.cloneContact(target)
                else:
                    ki32.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on33 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on33 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on33') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on33'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki33.cloneContact(target)
                            group = ki33.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki33.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki33.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki33.cloneContact(target)
                else:
                    ki33.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on34 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on34 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on34') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on34'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki34.cloneContact(target)
                            group = ki34.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki34.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki34.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki34.cloneContact(target)
                else:
                    ki34.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on35 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on35 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on35') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on35'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki35.cloneContact(target)
                            group = ki35.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki35.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki35.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki35.cloneContact(target)
                else:
                    ki35.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on36 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on36 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on36') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on36'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki36.cloneContact(target)
                            group = ki36.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki36.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki36.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki36.cloneContact(target)
                else:
                    ki36.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on37 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on37 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on37') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on37'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki37.cloneContact(target)
                            group = ki37.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki37.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki37.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki37.cloneContact(target)
                else:
                    ki37.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on38 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on38 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on38') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on38'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki38.cloneContact(target)
                            group = ki38.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki38.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki38.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki38.cloneContact(target)
                else:
                    ki38.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on39 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on39 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on39') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on39'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki39.cloneContact(target)
                            group = ki39.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki39.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki39.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki39.cloneContact(target)
                else:
                    ki39.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on40 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on40 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on40') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on40'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki40.cloneContact(target)
                            group = ki40.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki40.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki40.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki40.cloneContact(target)
                else:
                    ki40.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on41 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on41 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on41') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on41'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki41.cloneContact(target)
                            group = ki41.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki41.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki41.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki41.cloneContact(target)
                else:
                    ki41.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on42 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on42 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on42') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on42'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki42.cloneContact(target)
                            group = ki42.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki42.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki42.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki42.cloneContact(target)
                else:
                    ki42.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on1 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on1 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on1') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on1'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki1.cloneContact(target)
                            group = ki1.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki1.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki1.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki1.cloneContact(target)
                else:
                    ki1.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on2 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on2 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on2') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on2'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki2.cloneContact(target)
                            group = ki2.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki2.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki2.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki2.cloneContact(target)
                else:
                    ki2.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on3 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on3 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on3') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on3'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki3.cloneContact(target)
                            group = ki3.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki3.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki3.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki3.cloneContact(target)
                else:
                    ki3.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on4 ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on4 ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on4') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on4'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki4.cloneContact(target)
                            group = ki4.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki4.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki4.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki4.cloneContact(target)
                else:
                    ki4.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
            elif msg.text.lower().startswith(mimic["setkey"]+'ikkeh on ') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on ') or msg.text.lower().startswith(mimic["setkey"]+'ikkeh on') or msg.text.lower().startswith(mimic["setkey"]+' ikkeh on'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.cloneContact(target)
                            group = ki.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki.kitsuneText(kitsune,"Sukses Copy\nDisplayName:" + group.kitsuneName + "\n「Status」\n" + group.kitsuneBio + "\n「Picture」")
                            ki.kitsuneImageWithURL(kitsune,contact)
                        except:
                            ki.cloneContact(target)
                else:
                    ki.kitsuneText(kitsune,"「Copy Profil」\nYou need to mention a user♪\nUsage:"+mimic["setkey"].title()+" ikkeh on <@|~>")
 #          Steal Profile
            elif msg.text.lower().startswith(mimic["setkey"]+'get cover ') or msg.text.lower().startswith(mimic["setkey"]+' get cover ') or msg.text.lower().startswith(mimic["setkey"]+'get cover') or msg.text.lower().startswith(mimic["setkey"]+' get cover'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = ki.getContact(target)
                            cu = ki.channel.getCover(target)
                            path = str(cu)
                            ki.kitsuneImageWithURL(kitsune, path)
                        except:
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune, group.kitsuneName + " Covernya Eror")
                else:
                    if msg.toType == 2:
                        try:
                            group = ki.getGroup(kitsune)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki.kitsuneImageWithURL(kitsune,contact)
                        except:
                            group = ki.getGroup(kitsune)
                            ki.kitsuneText(kitsune, group.kitsuneName + " Profilenya Eror")
                    else:
                        try:
                            contact = ki.getContact(kitsune)
                            cu = ki.channel.getCover(kitsune)
                            path = str(cu)
                            ki.kitsuneImageWithURL(kitsune, path)
                        except:
                            group = ki.getContact(kitsune)
                            ki.kitsuneText(kitsune, group.kitsuneName + " Covernya Eror")
            elif msg.text.lower().startswith(mimic["setkey"]+'getpictstatus ') or msg.text.lower().startswith(mimic["setkey"]+' getpictstatus ') or msg.text.lower().startswith(mimic["setkey"]+'getpictstatus') or msg.text.lower().startswith(mimic["setkey"]+' getpictstatus'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mi = ki.getContact(key1)
                    ki.kitsuneText(kitsune, "http://dl.profile.line-cdn.net/"  + mi.kitsunephotoStatus)
                else:
                    if msg.toType == 2:
                        try:
                            group = ki.getGroup(kitsune)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki.kitsuneText(kitsune,contact)
                        except:
                            group = ki.getGroup(kitsune)
                            ki.kitsuneText(kitsune, group.kitsuneName + " Profilenya Eror")
                    else:
                        try:
                            group = ki.getContact(kitsune)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki.kitsuneText(kitsune,contact)
                        except:
                            group = ki.getContact(kitsune)
                            ki.kitsuneText(kitsune, group.kitsuneName + " Profilenya Eror")
            elif msg.text.lower().startswith(mimic["setkey"]+'get pict ') or msg.text.lower().startswith(mimic["setkey"]+' get pict '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            group = ki.getContact(target)
                            contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                            ki.kitsuneImageWithURL(kitsune,contact)
                        except:
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune, group.kitsuneName + " Profilenya Eror")
                else:
                    if msg.text.lower().startswith(mimic["setkey"]+' get pict '):
                        foo = mimic["setkey"]+' get pict '
                        key = len(foo)
                        key1 = msg.text[key:]
                        wiki = key1.replace("","")
                        gid = ki.getGroupIdsJoined()
                        for i in gid:
                            h = ki.getGroup(i).name
                            gna = ki.getGroup(i)
                            if h == wiki:
                                ki.kitsuneImageWithURL(kitsune,"http://dl.profile.line-cdn.net/" + gna.kitsunephotoStatus)
                    else:
                        foo = mimic["setkey"]+'get pict '
                        key = len(foo)
                        key1 = msg.text[key:]
                        wiki = key1.replace("","")
                        gid = ki.getGroupIdsJoined()
                        for i in gid:
                            h = ki.getGroup(i).name
                            gna = ki.getGroup(i)
                            if h == wiki:
                                ki.kitsuneImageWithURL(kitsune,"http://dl.profile.line-cdn.net/" + gna.kitsunephotoStatus)
            elif msg.text.lower().startswith(mimic["setkey"]+'accept ') or msg.text.lower().startswith(mimic["setkey"]+' accept '):
                if msg.text.lower().startswith(mimic["setkey"]+' accept '):
                    foo = mimic["setkey"]+' accept  '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    gid = ki.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        h = ki.getGroup(i).name
                        gna = ki.getGroup(i)
                        _list += gid.name
                        if h == wiki:
                            ki.acceptGroupInvitation(i)
                        else:
                            pass
                        ki.kitsuneText(kitsune,"Accept Group Invitation From Group: " + _list)
                else:
                    foo = mimic["setkey"]+'accept '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    gid = ki.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        h = ki.getGroup(i).name
                        gna = ki.getGroup(i)
                        _list += gna.name
                        if h == wiki:
                            ki.acceptGroupInvitation(i)
                        else:
                            pass
                        ki.kitsuneText(kitsune,"Accept Group Invitation From Group: " + _list)
            elif msg.text.lower().startswith(mimic["setkey"]+'getid ') or msg.text.lower().startswith(mimic["setkey"]+' getid '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    mi = ki.getContact(key1)
                    contact = "http://dl.profile.line-cdn.net/" + mi.kitsunephotoStatus
                    cu = ki.channel.getCover(key1)
                    path = str(cu)
                    ki.kitsuneText(kitsune,"「Display Name」\n" + mi.kitsuneName + "\n「Mid」\n" + key1 + "\n「Status」\n" + mi.kitsuneBio)
                    ki.kitsuneImageWithURL(kitsune, path)
                    ki.kitsuneImageWithURL(kitsune, contact)
                else:
                    if msg.text.lower().startswith(mimic["setkey"]+' getid '):
                        foo = mimic["setkey"]+' getid  '
                        key = len(foo)
                        key1 = msg.text[key:]
                        wiki = key1.replace("","")
                        gid = ki.getGroupIdsJoined()
                        for i in gid:
                            h = ki.getGroup(i).name
                            gna = ki.getGroup(i)
                            if h == wiki:
                                try:
                                    GS = gna.creator.mid
                                    msg = Message()
                                    msg.to = msg.to
                                    msg.contentType = 13
                                    msg.contentMetadata = {'mid': GS}
                                    gCreator = gna.creator.kitsuneName
                                except:
                                    W = gna.kitsunemembers[0].mid
                                    msg = Message()
                                    msg.to = msg.to
                                    msg.contentType = 13
                                    msg.contentMetadata = {'mid': W}
                                    gCreator = gna.kitsunemembers[0].kitsuneName
                                if gna.invitee is None:
                                    sinvitee = "0"
                                else:
                                    sinvitee = str(len(gna.invitee))
                                if gna.kitsuneTicket == True:
                                    u = "Disable"
                                else:
                                    u = "line://ti/g/" + ki.reissueGroupTicket(i)
                                contacts = ("「Group Name」\n" + str(gna.name) + "\n\n「Group ID」\n" + i + "\n\n「Group Creator」\n" + gCreator + "\n\nAnggota:" + str(len(gna.kitsunemembers)) + "\nInvitation:" + sinvitee + "\nTicket:" + u )
                                ki.kitsuneText(kitsune,contacts)
                                ki.sendMessage(msg)
                    else:
                        foo = mimic["setkey"]+'getid '
                        key = len(foo)
                        key1 = msg.text[key:]
                        wiki = key1.replace("","")
                        gid = ki.getGroupIdsJoined()
                        for i in gid:
                            h = ki.getGroup(i).name
                            gna = ki.getGroup(i)
                            if h == wiki:
                                try:
                                    GS = gna.creator.mid
                                    M = Message()
                                    M.to = msg.to
                                    M.contentType = 13
                                    M.contentMetadata = {'mid': GS}
                                    gCreator = gna.creator.kitsuneName
                                except:
                                    W = gna.kitsunemembers[0].mid
                                    M = Message()
                                    M.to = msg.to
                                    M.contentType = 13
                                    M.contentMetadata = {'mid': W}
                                    gCreator = gna.kitsunemembers[0].kitsuneName
                                if gna.invitee is None:
                                    sinvitee = "0"
                                else:
                                    sinvitee = str(len(gna.invitee))
                                if gna.kitsuneTicket == True:
                                    u = "Disable"
                                else:
                                    u = "line://ti/g/" + ki.reissueGroupTicket(i)
                                contacts = ("「Group Name」\n" + str(gna.name) + "\n\n「Group ID」\n" + i + "\n\n「Group Creator」\n" + gCreator + "\n\nAnggota:" + str(len(gna.kitsunemembers)) + "\nInvitation:" + sinvitee + "\nTicket:" + u )
                                ki.kitsuneText(kitsune,contacts)
                                ki.sendMessage(M)
            elif msg.text.lower().startswith(mimic["setkey"]+'micall') or msg.text.lower().startswith(mimic["setkey"]+' micall'):
                if msg.text.lower().startswith(mimic["setkey"]+' micall'):
                    foo = mimic["setkey"]+' micall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 mimic["target"][target] = True
                             except:
                                 ki.kitsuneText(kitsune,"Error")
                else:
                    foo = mimic["setkey"]+'micall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 mimic["target"][target] = True
                             except:
                                 ki.kitsuneText(kitsune,"Error")
            elif msg.text.lower().startswith(mimic["setkey"]+'unbanall') or msg.text.lower().startswith(mimic["setkey"]+' unbanall'):
                if msg.text.lower().startswith(mimic["setkey"]+' unbanall'):
                    foo = mimic["setkey"]+' unbanall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["blacklist"][target]
                                 f=codecs.open('blacklist.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
                else:
                    foo = mimic["setkey"]+'unbanall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["blacklist"][target]
                                 f=codecs.open('blacklist.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
            elif msg.text.lower().startswith(mimic["setkey"]+'banall') or msg.text.lower().startswith(mimic["setkey"]+' banall'):
                if msg.text.lower().startswith(mimic["setkey"]+' banall'):
                    foo = mimic["setkey"]+' banall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["blacklist"][target] = True
                                 f=codecs.open('blacklist.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
                else:
                    foo = mimic["setkey"]+'banall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    targets.remove(mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["blacklist"][target] = True
                                 f=codecs.open('blacklist.json','w','utf-8')
                                 json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
            elif msg.text.lower().startswith(mimic["setkey"]+'teamall') or msg.text.lower().startswith(mimic["setkey"]+' teamall'):
                if msg.text.lower().startswith(mimic["setkey"]+' teamall'):
                    foo = mimic["setkey"]+' teamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["bots"][target] = True
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
                else:
                    foo = mimic["setkey"]+'teamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    nk0 = key1.replace("","")
                    _name = nk0
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 wait["bots"][target] = True
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 pass
            elif msg.text.lower().startswith(mimic["setkey"]+'unteamall') or msg.text.lower().startswith(mimic["setkey"]+' unteamall'):
                if msg.text.lower().startswith(mimic["setkey"]+' unteamall'):
                    foo = mimic["setkey"]+' unteamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["bots"][target]
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 ki.kitsuneText(kitsune,"")
                else:
                    foo = mimic["setkey"]+'unteamall'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(kitsune)
                    targets = []
                    for s in gs.kitsunemembers:
                        if _name in s.kitsuneName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(kitsune,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 del wait["bots"][target]
                                 f=codecs.open('bots.json','w','utf-8')
                                 json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                             except:
                                 ki.kitsuneText(kitsune,"")
            elif msg.text.lower().startswith(mimic["setkey"]+'ban ') or msg.text.lower().startswith(mimic["setkey"]+' ban '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,group.kitsuneName + " Succes Add to Blacklist")
                        except:
                            ki.kitsuneText(kitsune,"Error")
                else:
                    pass
            elif msg.text.lower().startswith(mimic["setkey"]+'unban ') or msg.text.lower().startswith(mimic["setkey"]+' unban '):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,group.kitsuneName + " Delete From Blacklist")
                        except:
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,group.kitsuneName +" Not In Blacklist")
                else:
                    wait["dblacklist"] = True
                    ki.kitsuneText(kitsune,"Send a contact to unban")
            elif msg.text.lower().startswith(mimic["setkey"]+'talkban ') or msg.text.lower().startswith(mimic["setkey"]+' talkban ') or msg.text.lower().startswith(mimic["setkey"]+'talkban') or msg.text.lower().startswith(mimic["setkey"]+' talkban'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["talkblacklist"][target] = True
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,group.kitsuneName + " Succes Add to Talkban")
                        except:
                            ki.kitsuneText(kitsune,"Error")
                else:
                    wait["talkwblacklist"] = True
                    ki.kitsuneText(kitsune,"Send a contact to talkban")
            elif msg.text.lower().startswith(mimic["setkey"]+'untalkban ') or msg.text.lower().startswith(mimic["setkey"]+' untalkban ') or msg.text.lower().startswith(mimic["setkey"]+'untalkban') or msg.text.lower().startswith(mimic["setkey"]+' untalkban'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["talkblacklist"][target]
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,group.kitsuneName + " Delete From Talkban")
                        except:
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,group.kitsuneName + " Not In Talkban")
                else:
                    wait["talkdblacklist"] = True
                    ki.kitsuneText(kitsune,"Send a contact to untalkban")
            elif msg.text.lower() == mimic["setkey"]+'ban:repeat' or msg.text.lower() == mimic["setkey"]+' ban:repeat':
                wait["twblacklist"] = True
                ki.kitsuneText(kitsune,"Send a contact to ban")
            elif msg.text.lower() == mimic["setkey"]+'ban' or msg.text.lower() == mimic["setkey"]+' ban':
                wait["wblacklist"] = True
                ki.kitsuneText(kitsune,"Send a contact to ban")
            elif msg.text.lower() == mimic["setkey"]+'unban' or msg.text.lower() == mimic["setkey"]+' unban':
                wait["dblacklist"] = True
                ki.kitsuneText(kitsune,"Send a contact to unban")
            elif msg.text.lower() == mimic["setkey"]+'unban:repeat' or msg.text.lower() == mimic["setkey"]+' unban:repeat':
                wait["tdblacklist"] = True
                ki.kitsuneText(kitsune,"Send a contact to unban")
            elif msg.text.lower() == mimic["setkey"]+'abort' or msg.text.lower() == mimic["setkey"]+' abort':
                wait["twblacklist"] = False
                wait["tdblacklist"] = False
                ki.kitsuneText(kitsune,"「Abort」\nAbort operation♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'mimic add ') or msg.text.lower().startswith(mimic["setkey"]+' mimic add ') or msg.text.lower().startswith(mimic["setkey"]+'mimic add') or msg.text.lower().startswith(mimic["setkey"]+' mimic add'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,"「Mimic」\n" + group.kitsuneName + " Add To Mimic List")
                            ki.sendMessageWithMention(kitsune,target)
                            break
                        except:
                            fail.kitsuneText(kitsune,"")
                            break
                else:
                    ki.kitsuneText(kitsune,"「Mimic」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'mimic del ') or msg.text.lower().startswith(mimic["setkey"]+' mimic del ') or msg.text.lower().startswith(mimic["setkey"]+'mimic del') or msg.text.lower().startswith(mimic["setkey"]+' mimic del'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,"「Mimic」\n" + group.kitsuneName + " Delete From Mimic List")
                            break
                        except:
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune,"「Mimic」\n" + group.kitsuneName + " Not in Mimic List")
                            break
                else:
                    ki.kitsuneText(kitsune,"「Mimic」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'invite ') or msg.text.lower().startswith(mimic["setkey"]+' invite '):
                if msg.text.lower().startswith(mimic["setkey"]+' invite '):
                    foo = mimic["setkey"]+' invite '
                    key = len(foo)
                    key1 = msg.text[key:]
                    contact = ki.getContact(key1)
                    ki.findAndAddContactsByMid(key1)
                    ki.inviteIntoGroup(kitsune, [key1])
                else:
                    foo = mimic["setkey"]+'invite '
                    key = len(foo)
                    key1 = msg.text[key:]
                    contact = ki.getContact(key1)
                    ki.findAndAddContactsByMid(key1)
                    ki.inviteIntoGroup(kitsune, [key1])
            elif msg.text.lower() == mimic["setkey"]+' instagram' or msg.text.lower() == mimic["setkey"]+'instagram':
                ki.kitsuneText(kitsune,"「Instagram」\nUsage:" + mimic["setkey"].title()+" instagram <username>")
            elif msg.text.lower().startswith(mimic["setkey"]+'instagram ') or msg.text.lower().startswith(mimic["setkey"]+' instagram '):
                if msg.text.lower().startswith(mimic["setkey"]+' instagram '):
                    foo = mimic["setkey"]+' instagram '
                    key = len(foo)
                    key1 = msg.text[key:]
                    instagram = key1.replace("","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    ki.kitsuneText(kitsune, detail + user + user1 + followers + following + post + link + details)
                    ki.kitsuneImageWithURL(kitsune, text1[0])
                else:
                    foo = mimic["setkey"]+'instagram '
                    key = len(foo)
                    key1 = msg.text[key:]
                    instagram = key1.replace("","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    ki.kitsuneText(kitsune, detail + user + user1 + followers + following + post + link + details)
                    ki.kitsuneImageWithURL(kitsune, text1[0])
            elif msg.text.lower() == mimic["setkey"]+' youtube' or msg.text.lower() == mimic["setkey"]+'youtube':
                ki.kitsuneText(kitsune,"「Youtube」\nUsage:" + mimic["setkey"].title()+" youtube <payung teduh - akad>")
            elif msg.text.lower().startswith(mimic["setkey"]+'youtube') or msg.text.lower().startswith(mimic["setkey"]+' youtube'):
                if msg.text.lower().startswith(mimic["setkey"]+' youtube'):
                    query = msg.text.split(" ")
                    try:
                        if len(query) == 3:
                            isi = yt(query[2])
                            hasil = isi[int(query[1])-1]
                            ki.kitsuneText(kitsune, hasil)
                        else:
                            isi = yt(query[1])
                            ki.kitsuneText(kitsune, isi[0])
                    except Exception as e:
                        ki.kitsuneText(kitsune, str(e))
                else:
                    query = msg.text.split(" ")
                    try:
                        if len(query) == 3:
                            isi = yt(query[2])
                            hasil = isi[int(query[1])-1]
                            ki.kitsuneText(kitsune, hasil)
                        else:
                            isi = yt(query[1])
                            ki.kitsuneText(kitsune, isi[0])
                    except Exception as e:
                        ki.kitsuneText(kitsune, str(e))
            elif msg.text.lower() == mimic["setkey"]+' image' or msg.text.lower() == mimic["setkey"]+'image':
                ki.kitsuneText(kitsune,"「Google Image」\nUsage:" + mimic["setkey"].title()+" image <sarada>")
            elif msg.text.lower() == mimic["setkey"]+' about' or msg.text.lower() == mimic["setkey"]+'about':
                today = date.today()
                future = date(2057,11,30)
                days = (str(future - today))
                comma = days.find(",")
                days = days[:comma]
                ki.kitsuneText(kitsune,"「About」\nKitsune 'Self' Edition♪\n「Subscription」\nExpired: 2057-11,30" + "\nIn days: " + days + "\nKey:"+mimic["setkey"] + "\n\n「Contact」\n・ LINE: line://ti/p/~fcimicrosoftaditya")
            elif msg.text.lower() == mimic["setkey"]+' get pict' or msg.text.lower() == mimic["setkey"]+'get pict':
                if msg.toType == 2:
                    try:
                        group = ki.getGroup(kitsune)
                        contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                        ki.kitsuneImageWithURL(kitsune,contact)
                    except:
                        group = ki.getGroup(kitsune)
                        ki.kitsuneText(kitsune, group.kitsuneName + " Profilenya Eror")
                else:
                    try:
                        group = ki.getContact(kitsune)
                        contact = "http://dl.profile.line-cdn.net/" + group.kitsunephotoStatus
                        ki.kitsuneImageWithURL(kitsune,contact)
                    except:
                        group = ki.getContact(kitsune)
                        ki.kitsuneText(kitsune, group.kitsuneName + " Profilenya Eror")
            elif msg.text.lower() == mimic["setkey"]+' getid' or msg.text.lower() == mimic["setkey"]+'getid':
                if msg.toType == 2:
                    ki.kepo1(kitsune,"")
                    ki.kepoContact(kitsune,"")
                else:
                    ki.kepo(kitsune,"")
                    ki.kepoContact1(kitsune,"")
            elif msg.text.lower().startswith(mimic["setkey"]+'text cool ') or msg.text.lower().startswith(mimic["setkey"]+' text cool '):
                if msg.text.lower().startswith(mimic["setkey"]+' text cool '):
                    foo = mimic["setkey"]+' text cool '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    ki.sendTeks(kitsune,wiki)
                else:
                    foo = mimic["setkey"]+'text cool '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    ki.sendTeks(kitsune,wiki)
            elif msg.text.lower().startswith(mimic["setkey"]+'image ') or msg.text.lower().startswith(mimic["setkey"]+' image '):
                if msg.text.lower().startswith(mimic["setkey"]+' image '):
                    foo = mimic["setkey"]+' image '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + wiki
                    raw_html =  (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    try:
                        start = timeit.timeit()
                        ki.kitsuneImageWithURL(kitsune,path)
                        ki.kitsuneText(kitsune, "「Google Image」\nType: Search Image\nTime taken: %s" % (start) +"\nTotal Image Links = "+str(len(items)))
                    except Exception as e:
                        ki.kitsuneText(kitsune, str(e))
                else:
                    foo = mimic["setkey"]+'image '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + wiki
                    raw_html =  (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    try:
                        start = timeit.timeit()
                        ki.kitsuneImageWithURL(kitsune,path)
                        ki.kitsuneText(kitsune, "「Google Image」\nType: Search Image\nTime taken: %s" % (start) +"\nTotal Image Links = "+str(len(items)))
                    except Exception as e:
                        ki.kitsuneText(kitsune, str(e))
            elif msg.text.lower().startswith(mimic["setkey"]+'say@id ') or msg.text.lower().startswith(mimic["setkey"]+' say@id '):
                if msg.text.lower().startswith(mimic["setkey"]+' say@id '):
                    foo = mimic["setkey"]+' say@id '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    tts = gTTS(text=wiki, lang='id')
                    tts.save('aditya.mp3')
                    ki.sendAudio(kitsune,'aditya.mp3')
                else:
                    foo = mimic["setkey"]+'say@id '
                    key = len(foo)
                    key1 = msg.text[key:]
                    wiki = key1.replace("","")
                    tts = gTTS(text=wiki, lang='id')
                    tts.save('aditya.mp3')
                    ki.sendAudio(kitsune,'aditya.mp3')
            elif msg.text.lower() == mimic["setkey"]+' wikipedia' or msg.text.lower() == mimic["setkey"]+'wikipedia':
                ki.kitsuneText(kitsune,"「Wikipedia」\nUsage:" + mimic["setkey"].title()+" wikipedia <naruto>")
            elif msg.text.lower().startswith(mimic["setkey"]+'wikipedia ') or msg.text.lower().startswith(mimic["setkey"]+' wikipedia '):
                if msg.text.lower().startswith(mimic["setkey"]+' wikipedia '):
                  try:
                      foo = mimic["setkey"]+' wikipedia '
                      key = len(foo)
                      key1 = msg.text[key:]
                      wiki = key1.replace("","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ki.kitsuneText(kitsune, pesan)
                  except:
                      try:
                          foo = mimic["setkey"]+' wikipedia '
                          key = len(foo)
                          key1 = msg.text[key:]
                          wiki = key1.replace("","")
                          wikipedia.set_lang("en")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          ki.kitsuneText(kitsune, pesan)
                      except:
                          try:
                              pesan="Text Banyak Silahkan Click link ini\n"
                              pesan+=wikipedia.page(wiki).url
                              ki.kitsuneText(kitsune, pesan)
                          except Exception as e:
                              ki.kitsuneText(kitsune, str(e))
                else:
                  try:
                      foo = mimic["setkey"]+'wikipedia '
                      key = len(foo)
                      key1 = msg.text[key:]
                      wiki = key1.replace("","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ki.kitsuneText(kitsune, pesan)
                  except:
                      try:
                          foo = mimic["setkey"]+'wikipedia '
                          key = len(foo)
                          key1 = msg.text[key:]
                          wiki = key1.replace("","")
                          wikipedia.set_lang("en")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          ki.kitsuneText(kitsune, pesan)
                      except:
                          try:
                              pesan="Text Banyak Silahkan Click link ini\n"
                              pesan+=wikipedia.page(wiki).url
                              ki.kitsuneText(kitsune, pesan)
                          except Exception as e:
                              ki.kitsuneText(kitsune, str(e))
            elif msg.text.lower() == mimic["setkey"]+' lyric' or msg.text.lower() == mimic["setkey"]+'lyric':
                ki.kitsuneText(kitsune,"「Lyric」\nUsage:" + mimic["setkey"].title()+" lyric <payung teduh - akad>")
            elif msg.text.lower().startswith(mimic["setkey"]+'lyric ') or msg.text.lower().startswith(mimic["setkey"]+' lyric '):
                if msg.text.lower().startswith(mimic["setkey"]+' lyric '):
                    foo = mimic["setkey"]+' lyric '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ki.kitsuneText(kitsune, hasil)
                else:
                    foo = mimic["setkey"]+'lyric '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ki.kitsuneText(kitsune, hasil)
            elif msg.text.lower() == mimic["setkey"]+' music' or msg.text.lower() == mimic["setkey"]+'music':
                ki.kitsuneText(kitsune,"「Music」\nUsage:" + mimic["setkey"].title()+" music <payung teduh - akad>")
            elif msg.text.lower() == mimic["setkey"]+' say@id' or msg.text.lower() == mimic["setkey"]+'say@id':
                ki.kitsuneText(kitsune,"「Text To Speech」\nUsage:" + mimic["setkey"].title()+" say@id <query>")
            elif msg.text.lower().startswith(mimic["setkey"]+'music ') or msg.text.lower().startswith(mimic["setkey"]+' music '):
                if msg.text.lower().startswith(mimic["setkey"]+' music '):
                    foo = mimic["setkey"]+' music '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        ki.kitsuneText(kitsune, hasil)
                        ki.kitsuneText(kitsune, "Please Wait for audio...")
                        ki.kitsuneAudioWithURL(kitsune, song[4])
                else:
                    foo = mimic["setkey"]+'music '
                    key = len(foo)
                    key1 = msg.text[key:]
                    songname = key1.replace('','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        ki.kitsuneText(kitsune, hasil)
                        ki.kitsuneText(kitsune, "Please Wait for audio...")
                        ki.kitsuneAudioWithURL(kitsune, song[4])
 #          Settings on off
            elif msg.text.lower() == mimic["setkey"]+' autoadd' or msg.text.lower() == mimic["setkey"]+'autoadd':
                if wait['autoAdd'] == True:
                    if wait["autoaddpesan"] == '':
                        msgs="「Auto Add」\nAdd Back: True♪\nAdd Message: False♪\n\n\n"
                    else:
                        msgs="「Auto Add」\nAdd Back: True♪\nAdd Message: True♪"
                        msgs+="\n" + wait['autoaddpesan'] + "\n\n"
                else:
                    if wait["autoaddpesan"] == '':
                        msgs="「Auto Add」\nAdd Back: False♪\nAdd Message: False♪\n\n\n"
                    else:
                        msgs="「Auto Add」\nAdd Back: False♪\nAdd Message: True♪"
                        msgs+="\n" + wait['autoaddpesan'] + "\n\n"
                ki.kitsuneText(kitsune, msgs + "Commands:\n" \
					+mimic["setkey"].title()+" autoadd on\n" \
					+mimic["setkey"].title()+" autoadd off\n" \
					+mimic["setkey"].title()+" autoadd msg set\n" \
					+mimic["setkey"].title()+" autoadd msg clear")
            elif msg.text.lower() == mimic["setkey"]+' autoadd on' or msg.text.lower() == mimic["setkey"]+'autoadd on':
                if wait['autoAdd'] == True:
                    msgs="「Auto Add」\nAuto Add already ENABLED♪"
                else:
                    msgs="「Auto Add」\nAuto Add set to ENABLED♪"
                    wait['autoAdd']=True
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+' autoadd off' or msg.text.lower() == mimic["setkey"]+'autoadd off':
                if wait['autoAdd'] == False:
                    msgs="「Auto Add」\nAuto Add already DISABLED♪\nNote: Auto add message is not affected♪"
                else:
                    msgs="「Auto Add」\nAuto Add set to DISABLED♪\nNote: Auto add message is not affected♪"
                    wait['autoAdd']=False
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower().startswith(mimic["setkey"]+'autoadd msg set\n'):
                foo = mimic["setkey"]+'autoadd msg set\n'
                key = len(foo)
                print(key)
                key1 = msg.text[key:]
                wait["autoaddpesan"] = key1
                ki.kitsuneText(kitsune,"「Auto Add」\nAuto add message has been set to:\n" + wait["autoaddpesan"])
            elif msg.text.lower() == mimic["setkey"]+' autoadd msg clear' or msg.text.lower() == mimic["setkey"]+'autoadd msg clear':
                autoadd = wait["autoaddpesan"]
                msgs="「Auto Add」\nAuto add message DISABLED♪\nMessage backup:"
                msgs+="\n" + autoadd
                ki.kitsuneText(kitsune, msgs)
                wait["autoaddpesan"] = ""
            elif msg.text.lower() == mimic["setkey"]+' mimic' or msg.text.lower() == mimic["setkey"]+'mimic':
                if mimic["target"] == {}:
                    ki.kitsuneText(kitsune,"「Mimic」\nCurrently not mimicking anyone♪\n\nCommands:\n" + mimic["setkey"]+" mimic on\n" +  mimic["setkey"]+" mimic off\n" + mimic["setkey"]+" mimic add <@|~>\n" + mimic["setkey"]+" mimic del <@|~>")
                else:
                    kitsunefriend = ki.getContacts(mimic["target"])
                    ki.kitsuneText(kitsune, "Please wait...")
                    num=1
                    msgs="「Mimic」\nMimicking:"
                    for ids in kitsunefriend:
                        msgs+="\n%i. %s♪" % (num, ids.kitsuneName)
                        num=(num+1)
                    msgs+="\n「Total %i Mimicking」\n" % len(mimic["target"])
                    ki.kitsuneText(kitsune, msgs + "Commands:\n" +  mimic["setkey"]+" mimic on\n" +  mimic["setkey"]+" mimic off\n" + mimic["setkey"]+" mimic add <@|~>\n" + mimic["setkey"]+" mimic del <@|~>")
            elif msg.text.lower() == 'setkey':
                if mimic["setkey"] == '':
                    ki.kitsuneText(kitsune,"Your Key: DISABLED♪\nSetkey set - Set Your Key\nSetkey off - Disable Your Key\nSetkey reset - Reset Your Key")
                else:
                    ki.kitsuneText(kitsune,"Your Key: " + mimic["setkey"].title() + "\nSetKey: - Set Your Key\nSetkey Off - Disable Your Key\nSetkey Reset - Reset Your Key")
            elif msg.text.lower() == mimic["setkey"]+' mimic on' or msg.text.lower() == mimic["setkey"]+'mimic on':
                if mimic["status"] == True:
                    msgs="「Mimic」\nMimic already ENABLED♪"
                else:
                    msgs="「Mimic」\nMimic set to ENABLED♪"
                    mimic["status"]=True
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+' mimic off' or msg.text.lower() == mimic["setkey"]+'mimic off':
                if mimic["status"] == False:
                    msgs="「Mimic」\nMimic already DISABLED♪"
                else:
                    msgs="「Mimic」\nMimic set to DISABLED♪"
                    mimic["status"]=False
                ki.kitsuneText(kitsune, msgs)
 #     bagian replace
            elif msg.text.lower() == mimic["setkey"]+'date':
                ki.kitsuneText(kitsune, " Tanggal " + datetime.now().strftime('%d/%m/%y Jam Is %H:%M:%S') )
            elif msg.text.lower() == mimic["setkey"]+' autojoin' or msg.text.lower() == mimic["setkey"]+'autojoin':
                if wait['autoJoin'] == True:
                        msgs="「Auto Join」\nState: ENABLED♪\n"
                else:
                        msgs="「Auto Join」\nState: DISABLED♪\n"
                ki.kitsuneText(kitsune, msgs + "Commands:\n" \
					+mimic["setkey"].title()+" autojoin on \n" \
					+mimic["setkey"].title()+" autojoin off ")
            elif msg.text.lower() == mimic["setkey"]+' autojoin on' or msg.text.lower() == mimic["setkey"]+'autojoin on':
                if wait['autoJoin'] == True:
                    msgs="「Auto Join」\nAuto Join already set to ENABLED♪"
                else:
                    msgs="「Auto Join」\nAuto Join has been set to ENABLED♪"
                    wait['autoJoin']=True
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+' autojoin off' or msg.text.lower() == mimic["setkey"]+'autojoin off':
                if wait['autoJoin'] == False:
                    msgs="「Auto Join」\nAuto Auto Join already set to DISABLED♪"
                else:
                    msgs="「Auto Join」\nAuto Join has been set to DISABLED♪"
                    wait['autoJoin']=False
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower().startswith(mimic["setkey"]+'hitung'):
                bb = "╠・ @x \n"
                print(len(bb))
                aa = "╔═══════════════\n" + bb
                print(len(aa))
            elif msg.text.lower() == mimic["setkey"]+' me' or msg.text.lower() == mimic["setkey"]+'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+' bot' or msg.text.lower() == mimic["setkey"]+'bot':
                if Botsa == []:
                    ki.kitsuneText(kitsune,"Nothing in the blacklist")
                else:
                    ki.kitsuneText(kitsune,"Daftar Contact Bot Gua")
                    mc = ""
                    for mi_d in Botsa:
						msg.contentType = 13
						msg.contentMetadata = {'mid': mi_d}
						ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'ourl' or msg.text.lower() == mimic["setkey"]+' ourl':
                if msg.toType == 2:
                    group = ki.getGroup(kitsune)
                    group.kitsuneTicket = False
                    ki.updateGroup(group)
                else:
                        ki.kitsuneText(kitsune,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl1':
                if msg.toType == 2:
                    group = ki1.getGroup(kitsune)
                    group.kitsuneTicket = False
                    ki1.updateGroup(group)
                else:
                        ki1.kitsuneText(kitsune,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl2':
                if msg.toType == 2:
                    group = ki2.getGroup(kitsune)
                    group.kitsuneTicket = False
                    ki2.updateGroup(group)
                else:
                        ki2.kitsuneText(kitsune,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl3':
                if msg.toType == 2:
                    group = ki3.getGroup(kitsune)
                    group.kitsuneTicket = False
                    ki3.updateGroup(group)
                else:
                        ki3.kitsuneText(kitsune,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl4':
                if msg.toType == 2:
                    group = ki4.getGroup(kitsune)
                    group.kitsuneTicket = False
                    ki4.updateGroup(group)
                else:
                        ki4.kitsuneText(kitsune,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'ourl5':
                if msg.toType == 2:
                    group = ki5.getGroup(kitsune)
                    group.kitsuneTicket = False
                    ki5.updateGroup(group)
                else:
                        ki5.kitsuneText(kitsune,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'curl' or msg.text.lower() == mimic["setkey"]+' curl':
                if msg.toType == 2:
                    group = ki.getGroup(kitsune)
                    group.kitsuneTicket = True
                    ki.updateGroup(group)
                else:
                        ki.kitsuneText(kitsune,"It can not be used outside the group")
            elif msg.text.lower() == mimic["setkey"]+'invite:gcreator' or msg.text.lower() == mimic["setkey"]+' invite:gcreator':
                if msg.toType == 2:
                       ginfo = ki.getGroup(kitsune)
                       try:
                           gcmid = ginfo.creator.mid
                           ki.inviteIntoGroup(kitsune,[gcmid])
                       except:
                           gcmid = "Error"
                           ki.inviteIntoGroup(kitsune,[gcmid])
            elif msg.text.lower() == mimic["setkey"]+'bot:gcreator' or msg.text.lower() == mimic["setkey"]+' bot:gcreator':
                if msg.toType == 2:
                       ginfo = ki1.getGroup(kitsune)
                       try:
                           gcmid = ginfo.creator.mid
                           ki1.inviteIntoGroup(kitsune,[gcmid])
                       except:
                           gcmid = "Error"
                           ki1.inviteIntoGroup(kitsune,[gcmid])
            elif msg.text.lower() == mimic["setkey"]+'bio' or msg.text.lower() == mimic["setkey"]+' bio':
                    profile = ki.getProfile()
                    ki.kitsuneText(kitsune, profile.kitsuneBio)
            elif msg.text.lower() == mimic["setkey"]+'pictstatus' or msg.text.lower() == mimic["setkey"]+' pictstatus':
                    profile = ki.getProfile()
                    ki.kitsuneText(kitsune, "http://dl.profile.line-cdn.net/"  + profile.kitsunephotoStatus)
            elif msg.text.lower() == mimic["setkey"]+'pp' or msg.text.lower() == mimic["setkey"]+' pp':
                    profile = ki.getProfile()
                    ki.kitsuneImageWithURL(kitsune, "http://dl.profile.line-cdn.net/"  + profile.kitsunephotoStatus)
            elif msg.text.lower() == mimic["setkey"]+'sampul' or msg.text.lower() == mimic["setkey"]+' sampul':
                    h = ki.getHome(mid)
                    objId = h["result"]["homeInfo"]["objectId"]
                    ki.kitsuneImageWithURL(kitsune, "http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + mid + "&oid=" + objId)
            elif msg.text.lower() == mimic["setkey"]+'speeder' or msg.text.lower() == mimic["setkey"]+' speeder':
                start = time.time()
                ki.kitsuneText(kitsune, "「Debug」\nType: speed\nTesting..")
                elapsed_time = time.time() - start
                ki.kitsuneText(kitsune, "「Debug」\nType: speed\nTime taken: %s" % (elapsed_time))
            elif msg.text.lower() == mimic["setkey"]+'speed' or msg.text.lower() == mimic["setkey"]+' speed':
                ki.kitsuneText(kitsune, "「Debug」\nType: speed\nTesting..")
                fakesp = '0123456789'
                sp = "".join([random.choice(fakesp) for x in xrange(8)])
                hsl = random.choice(["0.006","0.007","0.008"]) + sp
                ki.kitsuneText(kitsune, "「Debug」\nType: speed\nTime taken: %s" % (hsl))
                fakesp = '0123456789'
                sp = "".join([random.choice(fakesp) for x in xrange(8)])
                hsl = random.choice(["0.006","0.007","0.008"]) + sp
                ki1.kitsuneText(kitsune, "「Debug」\nType: speed\nTime taken: %s" % (hsl))
                fakesp = '0123456789'
                sp = "".join([random.choice(fakesp) for x in xrange(8)])
                hsl = random.choice(["0.006","0.007","0.008"]) + sp
                ki2.kitsuneText(kitsune, "「Debug」\nType: speed\nTime taken: %s" % (hsl))
                fakesp = '0123456789'
                sp = "".join([random.choice(fakesp) for x in xrange(8)])
                hsl = random.choice(["0.006","0.007","0.008"]) + sp
                ki3.kitsuneText(kitsune, "「Debug」\nType: speed\nTime taken: %s" % (hsl))
                fakesp = '0123456789'
                sp = "".join([random.choice(fakesp) for x in xrange(8)])
                hsl = random.choice(["0.006","0.007","0.008"]) + sp
                ki4.kitsuneText(kitsune, "「Debug」\nType: speed\nTime taken: %s" % (hsl))
            elif msg.text.lower() == mimic["setkey"]+'clone' or msg.text.lower() == mimic["setkey"]+' clone':
                ki.cloneContact(kitsune)
            elif msg.text.lower() == mimic["setkey"]+'mid' or msg.text.lower() == mimic["setkey"]+' mid':
                ki.kitsuneText(kitsune,msg.from_)
            elif msg.text.lower().startswith(mimic["setkey"]+'allbio:'):
                if msg.text.lower().startswith(mimic["setkey"]+' allbio:'):
                    foo = mimic["setkey"]+' allbio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki22.getProfile()
                        profile.kitsuneBio = string
                        ki22.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki1.getProfile()
                        profile.kitsuneBio = string
                        ki1.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki2.getProfile()
                        profile.kitsuneBio = string
                        ki2.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki3.getProfile()
                        profile.kitsuneBio = string
                        ki3.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki4.getProfile()
                        profile.kitsuneBio = string
                        ki4.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki5.getProfile()
                        profile.kitsuneBio = string
                        ki5.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki6.getProfile()
                        profile.kitsuneBio = string
                        ki6.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki7.getProfile()
                        profile.kitsuneBio = string
                        ki7.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki8.getProfile()
                        profile.kitsuneBio = string
                        ki8.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki9.getProfile()
                        profile.kitsuneBio = string
                        ki9.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki10.getProfile()
                        profile.kitsuneBio = string
                        ki10.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki11.getProfile()
                        profile.kitsuneBio = string
                        ki11.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki12.getProfile()
                        profile.kitsuneBio = string
                        ki12.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki13.getProfile()
                        profile.kitsuneBio = string
                        ki13.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki14.getProfile()
                        profile.kitsuneBio = string
                        ki14.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki15.getProfile()
                        profile.kitsuneBio = string
                        ki15.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki16.getProfile()
                        profile.kitsuneBio = string
                        ki16.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki17.getProfile()
                        profile.kitsuneBio = string
                        ki17.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki18.getProfile()
                        profile.kitsuneBio = string
                        ki18.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki21.getProfile()
                        profile.kitsuneBio = string
                        ki21.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki20.getProfile()
                        profile.kitsuneBio = string
                        ki20.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki23.getProfile()
                        profile.kitsuneBio = string
                        ki23.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki24.getProfile()
                        profile.kitsuneBio = string
                        ki24.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki25.getProfile()
                        profile.kitsuneBio = string
                        ki25.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki26.getProfile()
                        profile.kitsuneBio = string
                        ki26.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki33.getProfile()
                        profile.kitsuneBio = string
                        ki33.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki34.getProfile()
                        profile.kitsuneBio = string
                        ki34.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki35.getProfile()
                        profile.kitsuneBio = string
                        ki35.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki37.getProfile()
                        profile.kitsuneBio = string
                        ki37.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki36.getProfile()
                        profile.kitsuneBio = string
                        ki36.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki27.getProfile()
                        profile.kitsuneBio = string
                        ki27.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki38.getProfile()
                        profile.kitsuneBio = string
                        ki38.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki39.getProfile()
                        profile.kitsuneBio = string
                        ki39.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki28.getProfile()
                        profile.kitsuneBio = string
                        ki28.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki40.getProfile()
                        profile.kitsuneBio = string
                        ki40.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki42.getProfile()
                        profile.kitsuneBio = string
                        ki42.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki41.getProfile()
                        profile.kitsuneBio = string
                        ki41.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki29.getProfile()
                        profile.kitsuneBio = string
                        ki29.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki22.getProfile()
                        profile.kitsuneBio = string
                        ki22.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki30.getProfile()
                        profile.kitsuneBio = string
                        ki30.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki31.getProfile()
                        profile.kitsuneBio = string
                        ki31.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki32.getProfile()
                        profile.kitsuneBio = string
                        ki32.updateProfile(profile)
                        ki.kitsuneText(kitsune,"Bio berubah menjadi:\n" + string + "")
                else:
                    foo = mimic["setkey"]+'allbio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki22.getProfile()
                        profile.kitsuneBio = string
                        ki22.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki1.getProfile()
                        profile.kitsuneBio = string
                        ki1.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki2.getProfile()
                        profile.kitsuneBio = string
                        ki2.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki3.getProfile()
                        profile.kitsuneBio = string
                        ki3.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki4.getProfile()
                        profile.kitsuneBio = string
                        ki4.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki5.getProfile()
                        profile.kitsuneBio = string
                        ki5.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki6.getProfile()
                        profile.kitsuneBio = string
                        ki6.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki7.getProfile()
                        profile.kitsuneBio = string
                        ki7.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki8.getProfile()
                        profile.kitsuneBio = string
                        ki8.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki9.getProfile()
                        profile.kitsuneBio = string
                        ki9.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki10.getProfile()
                        profile.kitsuneBio = string
                        ki10.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki11.getProfile()
                        profile.kitsuneBio = string
                        ki11.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki12.getProfile()
                        profile.kitsuneBio = string
                        ki12.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki13.getProfile()
                        profile.kitsuneBio = string
                        ki13.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki14.getProfile()
                        profile.kitsuneBio = string
                        ki14.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki15.getProfile()
                        profile.kitsuneBio = string
                        ki15.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki16.getProfile()
                        profile.kitsuneBio = string
                        ki16.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki17.getProfile()
                        profile.kitsuneBio = string
                        ki17.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki18.getProfile()
                        profile.kitsuneBio = string
                        ki18.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki21.getProfile()
                        profile.kitsuneBio = string
                        ki21.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki20.getProfile()
                        profile.kitsuneBio = string
                        ki20.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki23.getProfile()
                        profile.kitsuneBio = string
                        ki23.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki24.getProfile()
                        profile.kitsuneBio = string
                        ki24.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki25.getProfile()
                        profile.kitsuneBio = string
                        ki25.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki26.getProfile()
                        profile.kitsuneBio = string
                        ki26.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki33.getProfile()
                        profile.kitsuneBio = string
                        ki33.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki34.getProfile()
                        profile.kitsuneBio = string
                        ki34.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki35.getProfile()
                        profile.kitsuneBio = string
                        ki35.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki37.getProfile()
                        profile.kitsuneBio = string
                        ki37.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki36.getProfile()
                        profile.kitsuneBio = string
                        ki36.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki27.getProfile()
                        profile.kitsuneBio = string
                        ki27.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki38.getProfile()
                        profile.kitsuneBio = string
                        ki38.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki39.getProfile()
                        profile.kitsuneBio = string
                        ki39.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki28.getProfile()
                        profile.kitsuneBio = string
                        ki28.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki40.getProfile()
                        profile.kitsuneBio = string
                        ki40.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki42.getProfile()
                        profile.kitsuneBio = string
                        ki42.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki41.getProfile()
                        profile.kitsuneBio = string
                        ki41.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki29.getProfile()
                        profile.kitsuneBio = string
                        ki29.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki22.getProfile()
                        profile.kitsuneBio = string
                        ki22.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki30.getProfile()
                        profile.kitsuneBio = string
                        ki30.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki31.getProfile()
                        profile.kitsuneBio = string
                        ki31.updateProfile(profile)
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki32.getProfile()
                        profile.kitsuneBio = string
                        ki32.updateProfile(profile)
                        ki.kitsuneText(kitsune,"Bio berubah menjadi:\n" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr id@en '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr id@en ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr ja@id '):
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr ja@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr en@id '):
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr en@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr th@id '):
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr th@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr id@jp '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr id@jp ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+' tr id@th '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = str(msg.text.lower().replace(mimic["setkey"]+' tr id@th ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr id@en '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr id@en ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr ja@id '):
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr ja@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr en@id '):
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr en@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr th@id '):
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr th@id ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr id@jp '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr id@jp ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'tr id@th '):
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = str(msg.text.lower().replace(mimic["setkey"]+'tr id@th ',''))
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ki.kitsuneText(kitsune,"════TRANSLATE════\n" + "" + kata + "\n════Terjemahaan════\n" + "" + result + "\n══════SUKSES═════")
            elif msg.text.lower().startswith(mimic["setkey"]+'myname:') or msg.text.lower().startswith(mimic["setkey"]+' myname:'):
                if msg.text.lower().startswith(mimic["setkey"]+' myname:'):
                    foo = mimic["setkey"]+'myname:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500000:
                        profile = ki.getProfile()
                        profile.kitsuneName = string
                        ki.updateProfile(profile)
                        ki.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'myname:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500000:
                        profile = ki.getProfile()
                        profile.kitsuneName = string
                        ki.updateProfile(profile)
                        ki.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'tl:') or msg.text.lower().startswith(mimic["setkey"]+' tl:'):
                if msg.text.lower().startswith(mimic["setkey"]+' tl:'):
                    foo = mimic["setkey"]+' tl:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    tl_text = key1
                    ki.kitsuneText(kitsune,"line://home/post?userMid="+mid+"&postId="+ki.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                else:
                    foo = mimic["setkey"]+'tl:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    tl_text = key1
                    ki.kitsuneText(kitsune,"line://home/post?userMid="+mid+"&postId="+ki.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text.lower().startswith(mimic["setkey"]+'gn ') or msg.text.lower().startswith(mimic["setkey"]+' gn '):
                if msg.text.lower().startswith(mimic["setkey"]+' gn '):
                    foo = mimic["setkey"]+' gn '
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode("utf-8")) <= 500:
                        profile = ki.getGroup(kitsune)
                        profile.name = string
                        ki.updateGroup(profile)
                        ki.kitsuneText(kitsune,"GroupName change to " + string + " success")
                else:
                    foo = mimic["setkey"]+'gn '
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode("utf-8")) <= 500:
                        profile = ki.getGroup(kitsune)
                        profile.name = string
                        ki.updateGroup(profile)
                        ki.kitsuneText(kitsune,"GroupName change to " + string + " success")
            elif msg.text.lower().startswith(mimic["setkey"]+'mybio:') or msg.text.lower().startswith(mimic["setkey"]+' mybio:'):
                if msg.text.lower().startswith(mimic["setkey"]+' mybio:'):
                    foo = mimic["setkey"]+' mybio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki.getProfile()
                        profile.kitsuneBio = string
                        ki.updateProfile(profile)
                        ki.kitsuneText(kitsune,"Update Bio" + string + "")
                else:
                    foo = mimic["setkey"]+'mybio:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 1000:
                        profile = ki.getProfile()
                        profile.kitsuneBio = string
                        ki.updateProfile(profile)
                        ki.kitsuneText(kitsune,"Update Bio" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name1:') or msg.text.lower().startswith(mimic["setkey"]+' name1:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name1:'):
                    foo = mimic["setkey"]+' name1:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki1.getProfile()
                        profile.kitsuneName = string
                        ki1.updateProfile(profile)
                        ki1.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name1:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki1.getProfile()
                        profile.kitsuneName = string
                        ki1.updateProfile(profile)
                        ki1.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name2:') or msg.text.lower().startswith(mimic["setkey"]+' name2:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name2:'):
                    foo = mimic["setkey"]+' name2:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki2.getProfile()
                        profile.kitsuneName = string
                        ki2.updateProfile(profile)
                        ki2.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name2:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki2.getProfile()
                        profile.kitsuneName = string
                        ki2.updateProfile(profile)
                        ki2.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name3:') or msg.text.lower().startswith(mimic["setkey"]+' name3:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name3:'):
                    foo = mimic["setkey"]+' name3:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki3.getProfile()
                        profile.kitsuneName = string
                        ki3.updateProfile(profile)
                        ki3.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name3:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki3.getProfile()
                        profile.kitsuneName = string
                        ki3.updateProfile(profile)
                        ki3.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name4:') or msg.text.lower().startswith(mimic["setkey"]+' name4:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name4:'):
                    foo = mimic["setkey"]+' name4:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki4.getProfile()
                        profile.kitsuneName = string
                        ki4.updateProfile(profile)
                        ki4.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name4:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki4.getProfile()
                        profile.kitsuneName = string
                        ki4.updateProfile(profile)
                        ki4.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name5:') or msg.text.lower().startswith(mimic["setkey"]+' name5:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name5:'):
                    foo = mimic["setkey"]+' name5:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki5.getProfile()
                        profile.kitsuneName = string
                        ki5.updateProfile(profile)
                        ki5.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name5:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki5.getProfile()
                        profile.kitsuneName = string
                        ki5.updateProfile(profile)
                        ki5.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name6:') or msg.text.lower().startswith(mimic["setkey"]+' name6:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name6:'):
                    foo = mimic["setkey"]+' name6:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki6.getProfile()
                        profile.kitsuneName = string
                        ki6.updateProfile(profile)
                        ki6.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name6:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki6.getProfile()
                        profile.kitsuneName = string
                        ki6.updateProfile(profile)
                        ki6.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name7:') or msg.text.lower().startswith(mimic["setkey"]+' name7:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name7:'):
                    foo = mimic["setkey"]+' name7:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki7.getProfile()
                        profile.kitsuneName = string
                        ki7.updateProfile(profile)
                        ki7.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name7:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki7.getProfile()
                        profile.kitsuneName = string
                        ki7.updateProfile(profile)
                        ki7.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name8:') or msg.text.lower().startswith(mimic["setkey"]+' name8:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name8:'):
                    foo = mimic["setkey"]+' name8:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki8.getProfile()
                        profile.kitsuneName = string
                        ki8.updateProfile(profile)
                        ki8.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name8:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki8.getProfile()
                        profile.kitsuneName = string
                        ki8.updateProfile(profile)
                        ki8.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name9:') or msg.text.lower().startswith(mimic["setkey"]+' name9:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name9:'):
                    foo = mimic["setkey"]+' name9:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki9.getProfile()
                        profile.kitsuneName = string
                        ki9.updateProfile(profile)
                        ki9.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name9:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki9.getProfile()
                        profile.kitsuneName = string
                        ki9.updateProfile(profile)
                        ki9.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name10:') or msg.text.lower().startswith(mimic["setkey"]+' name10:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name10:'):
                    foo = mimic["setkey"]+' name10:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki10.getProfile()
                        profile.kitsuneName = string
                        ki10.updateProfile(profile)
                        ki10.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name10:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki10.getProfile()
                        profile.kitsuneName = string
                        ki10.updateProfile(profile)
                        ki10.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name11:') or msg.text.lower().startswith(mimic["setkey"]+' name11:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name11:'):
                    foo = mimic["setkey"]+' name11:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki11.getProfile()
                        profile.kitsuneName = string
                        ki11.updateProfile(profile)
                        ki11.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name11:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki11.getProfile()
                        profile.kitsuneName = string
                        ki11.updateProfile(profile)
                        ki11.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name12:') or msg.text.lower().startswith(mimic["setkey"]+' name12:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name12:'):
                    foo = mimic["setkey"]+' name12:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki12.getProfile()
                        profile.kitsuneName = string
                        ki12.updateProfile(profile)
                        ki12.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name12:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki12.getProfile()
                        profile.kitsuneName = string
                        ki12.updateProfile(profile)
                        ki12.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name13:') or msg.text.lower().startswith(mimic["setkey"]+' name13:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name13:'):
                    foo = mimic["setkey"]+' name13:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki13.getProfile()
                        profile.kitsuneName = string
                        ki13.updateProfile(profile)
                        ki13.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name13:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki13.getProfile()
                        profile.kitsuneName = string
                        ki13.updateProfile(profile)
                        ki13.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name14:') or msg.text.lower().startswith(mimic["setkey"]+' name14:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name14:'):
                    foo = mimic["setkey"]+' name14:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki14.getProfile()
                        profile.kitsuneName = string
                        ki14.updateProfile(profile)
                        ki14.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name14:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki14.getProfile()
                        profile.kitsuneName = string
                        ki14.updateProfile(profile)
                        ki14.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name15:') or msg.text.lower().startswith(mimic["setkey"]+' name15:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name15:'):
                    foo = mimic["setkey"]+' name15:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki15.getProfile()
                        profile.kitsuneName = string
                        ki15.updateProfile(profile)
                        ki15.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name15:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki15.getProfile()
                        profile.kitsuneName = string
                        ki15.updateProfile(profile)
                        ki15.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name16:') or msg.text.lower().startswith(mimic["setkey"]+' name16:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name16:'):
                    foo = mimic["setkey"]+' name16:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki16.getProfile()
                        profile.kitsuneName = string
                        ki16.updateProfile(profile)
                        ki16.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name16:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki16.getProfile()
                        profile.kitsuneName = string
                        ki16.updateProfile(profile)
                        ki16.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name17:') or msg.text.lower().startswith(mimic["setkey"]+' name17:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name17:'):
                    foo = mimic["setkey"]+' name17:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki17.getProfile()
                        profile.kitsuneName = string
                        ki17.updateProfile(profile)
                        ki17.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name17:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki17.getProfile()
                        profile.kitsuneName = string
                        ki17.updateProfile(profile)
                        ki17.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name18:') or msg.text.lower().startswith(mimic["setkey"]+' name18:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name18:'):
                    foo = mimic["setkey"]+' name18:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki18.getProfile()
                        profile.kitsuneName = string
                        ki18.updateProfile(profile)
                        ki18.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name18:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki18.getProfile()
                        profile.kitsuneName = string
                        ki18.updateProfile(profile)
                        ki18.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name19:') or msg.text.lower().startswith(mimic["setkey"]+' name19:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name19:'):
                    foo = mimic["setkey"]+' name19:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki19.getProfile()
                        profile.kitsuneName = string
                        ki19.updateProfile(profile)
                        ki19.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name19:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki19.getProfile()
                        profile.kitsuneName = string
                        ki19.updateProfile(profile)
                        ki19.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name20:') or msg.text.lower().startswith(mimic["setkey"]+' name20:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name20:'):
                    foo = mimic["setkey"]+' name20:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki20.getProfile()
                        profile.kitsuneName = string
                        ki20.updateProfile(profile)
                        ki20.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name20:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki20.getProfile()
                        profile.kitsuneName = string
                        ki20.updateProfile(profile)
                        ki20.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name21:') or msg.text.lower().startswith(mimic["setkey"]+' name21:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name21:'):
                    foo = mimic["setkey"]+' name21:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki21.getProfile()
                        profile.kitsuneName = string
                        ki21.updateProfile(profile)
                        ki21.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name21:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki21.getProfile()
                        profile.kitsuneName = string
                        ki21.updateProfile(profile)
                        ki21.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name22:') or msg.text.lower().startswith(mimic["setkey"]+' name22:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name22:'):
                    foo = mimic["setkey"]+' name22:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki22.getProfile()
                        profile.kitsuneName = string
                        ki22.updateProfile(profile)
                        ki22.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name22:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki22.getProfile()
                        profile.kitsuneName = string
                        ki22.updateProfile(profile)
                        ki22.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name23:') or msg.text.lower().startswith(mimic["setkey"]+' name23:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name23:'):
                    foo = mimic["setkey"]+' name23:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki23.getProfile()
                        profile.kitsuneName = string
                        ki23.updateProfile(profile)
                        ki23.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name23:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki23.getProfile()
                        profile.kitsuneName = string
                        ki23.updateProfile(profile)
                        ki23.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name24:') or msg.text.lower().startswith(mimic["setkey"]+' name24:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name24:'):
                    foo = mimic["setkey"]+' name24:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki24.getProfile()
                        profile.kitsuneName = string
                        ki24.updateProfile(profile)
                        ki24.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name24:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki24.getProfile()
                        profile.kitsuneName = string
                        ki24.updateProfile(profile)
                        ki24.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name25:') or msg.text.lower().startswith(mimic["setkey"]+' name25:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name25:'):
                    foo = mimic["setkey"]+' name25:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki25.getProfile()
                        profile.kitsuneName = string
                        ki25.updateProfile(profile)
                        ki25.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name25:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki25.getProfile()
                        profile.kitsuneName = string
                        ki25.updateProfile(profile)
                        ki25.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name26:') or msg.text.lower().startswith(mimic["setkey"]+' name26:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name26:'):
                    foo = mimic["setkey"]+' name26:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki26.getProfile()
                        profile.kitsuneName = string
                        ki26.updateProfile(profile)
                        ki26.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name26:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki26.getProfile()
                        profile.kitsuneName = string
                        ki26.updateProfile(profile)
                        ki26.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name27:') or msg.text.lower().startswith(mimic["setkey"]+' name27:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name27:'):
                    foo = mimic["setkey"]+' name27:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki27.getProfile()
                        profile.kitsuneName = string
                        ki27.updateProfile(profile)
                        ki27.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name27:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki27.getProfile()
                        profile.kitsuneName = string
                        ki27.updateProfile(profile)
                        ki27.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name28:') or msg.text.lower().startswith(mimic["setkey"]+' name28:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name28:'):
                    foo = mimic["setkey"]+' name28:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki28.getProfile()
                        profile.kitsuneName = string
                        ki28.updateProfile(profile)
                        ki28.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name28:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki28.getProfile()
                        profile.kitsuneName = string
                        ki28.updateProfile(profile)
                        ki28.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name29:') or msg.text.lower().startswith(mimic["setkey"]+' name29:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name29:'):
                    foo = mimic["setkey"]+' name29:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki29.getProfile()
                        profile.kitsuneName = string
                        ki29.updateProfile(profile)
                        ki29.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name29:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki29.getProfile()
                        profile.kitsuneName = string
                        ki29.updateProfile(profile)
                        ki29.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name30:') or msg.text.lower().startswith(mimic["setkey"]+' name30:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name30:'):
                    foo = mimic["setkey"]+' name30:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki30.getProfile()
                        profile.kitsuneName = string
                        ki30.updateProfile(profile)
                        ki30.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name30:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki30.getProfile()
                        profile.kitsuneName = string
                        ki30.updateProfile(profile)
                        ki30.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name31:') or msg.text.lower().startswith(mimic["setkey"]+' name31:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name31:'):
                    foo = mimic["setkey"]+' name31:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki31.getProfile()
                        profile.kitsuneName = string
                        ki31.updateProfile(profile)
                        ki31.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name31:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki31.getProfile()
                        profile.kitsuneName = string
                        ki31.updateProfile(profile)
                        ki31.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name32:') or msg.text.lower().startswith(mimic["setkey"]+' name32:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name32:'):
                    foo = mimic["setkey"]+' name32:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki32.getProfile()
                        profile.kitsuneName = string
                        ki32.updateProfile(profile)
                        ki32.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name32:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki32.getProfile()
                        profile.kitsuneName = string
                        ki32.updateProfile(profile)
                        ki32.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name33:') or msg.text.lower().startswith(mimic["setkey"]+' name33:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name33:'):
                    foo = mimic["setkey"]+' name33:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki33.getProfile()
                        profile.kitsuneName = string
                        ki33.updateProfile(profile)
                        ki33.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name33:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki33.getProfile()
                        profile.kitsuneName = string
                        ki33.updateProfile(profile)
                        ki33.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name34:') or msg.text.lower().startswith(mimic["setkey"]+' name34:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name34:'):
                    foo = mimic["setkey"]+' name34:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki34.getProfile()
                        profile.kitsuneName = string
                        ki34.updateProfile(profile)
                        ki34.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name34:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki34.getProfile()
                        profile.kitsuneName = string
                        ki34.updateProfile(profile)
                        ki34.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name35:') or msg.text.lower().startswith(mimic["setkey"]+' name35:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name35:'):
                    foo = mimic["setkey"]+' name35:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki35.getProfile()
                        profile.kitsuneName = string
                        ki35.updateProfile(profile)
                        ki35.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name35:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki35.getProfile()
                        profile.kitsuneName = string
                        ki35.updateProfile(profile)
                        ki35.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name36:') or msg.text.lower().startswith(mimic["setkey"]+' name36:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name36:'):
                    foo = mimic["setkey"]+' name36:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki36.getProfile()
                        profile.kitsuneName = string
                        ki36.updateProfile(profile)
                        ki36.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name36:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki36.getProfile()
                        profile.kitsuneName = string
                        ki36.updateProfile(profile)
                        ki36.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name37:') or msg.text.lower().startswith(mimic["setkey"]+' name37:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name37:'):
                    foo = mimic["setkey"]+' name37:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki37.getProfile()
                        profile.kitsuneName = string
                        ki37.updateProfile(profile)
                        ki37.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name37:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki37.getProfile()
                        profile.kitsuneName = string
                        ki37.updateProfile(profile)
                        ki37.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name38:') or msg.text.lower().startswith(mimic["setkey"]+' name38:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name38:'):
                    foo = mimic["setkey"]+' name38:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki38.getProfile()
                        profile.kitsuneName = string
                        ki38.updateProfile(profile)
                        ki38.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name38:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki38.getProfile()
                        profile.kitsuneName = string
                        ki38.updateProfile(profile)
                        ki38.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name39:') or msg.text.lower().startswith(mimic["setkey"]+' name39:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name39:'):
                    foo = mimic["setkey"]+' name39:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki39.getProfile()
                        profile.kitsuneName = string
                        ki39.updateProfile(profile)
                        ki39.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name39:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki39.getProfile()
                        profile.kitsuneName = string
                        ki39.updateProfile(profile)
                        ki39.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name40:') or msg.text.lower().startswith(mimic["setkey"]+' name40:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name40:'):
                    foo = mimic["setkey"]+' name40:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki40.getProfile()
                        profile.kitsuneName = string
                        ki40.updateProfile(profile)
                        ki40.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name40:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki40.getProfile()
                        profile.kitsuneName = string
                        ki40.updateProfile(profile)
                        ki40.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name41:') or msg.text.lower().startswith(mimic["setkey"]+' name41:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name41:'):
                    foo = mimic["setkey"]+' name41:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki41.getProfile()
                        profile.kitsuneName = string
                        ki41.updateProfile(profile)
                        ki41.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name41:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki41.getProfile()
                        profile.kitsuneName = string
                        ki41.updateProfile(profile)
                        ki41.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'name42:') or msg.text.lower().startswith(mimic["setkey"]+' name42:'):
                if msg.text.lower().startswith(mimic["setkey"]+' name42:'):
                    foo = mimic["setkey"]+' name42:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki42.getProfile()
                        profile.kitsuneName = string
                        ki42.updateProfile(profile)
                        ki42.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'name42:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        profile = ki42.getProfile()
                        profile.kitsuneName = string
                        ki42.updateProfile(profile)
                        ki42.kitsuneText(kitsune,"Update Names Menjadi :" + string + "")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        ki.kitsuneText(kitsune,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        ki.kitsuneText(kitsune,["kitsunemembers"] + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                except:
                        ki.kitsuneText(kitsune,"Nilai tidak benar")
            elif msg.text.lower().startswith(mimic["setkey"]+'mayhem') or msg.text.lower().startswith(mimic["setkey"]+' mayhem'):
                if msg.text.lower().startswith(mimic["setkey"]+' mayhem'):
                    foo = mimic["setkey"]+' mayhem'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(kitsune)
                    ki.kitsuneText(kitsune,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                    ki.kitsuneText(kitsune,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.kitsunemembers))
                    targets = []
                    for g in gs.kitsunemembers:
                        if _name in g.kitsuneName:
                            targets.append(g.mid)
                    for target in targets:
                        if not target in Bots:
                            try:
                                random.choice(P1).kickoutFromGroup(kitsune,[target])
                                print (kitsune,[g.mid])
                            except:
                                ki.kitsuneText(kitsune,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                                ki.kitsuneText(kitsune,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.kitsunemembers))
                else:
                    foo = mimic["setkey"]+'mayhem'
                    key = len(foo)
                    key1 = msg.text[key:]
                    _name = key1.replace("","")
                    gs = ki.getGroup(kitsune)
                    ki.kitsuneText(kitsune,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                    ki.kitsuneText(kitsune,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.kitsunemembers))
                    targets = []
                    for g in gs.kitsunemembers:
                        if _name in g.kitsuneName:
                            targets.append(g.mid)
                    for target in targets:
                        if not target in Bots:
                            try:
                                random.choice(P1).kickoutFromGroup(kitsune,[target])
                                print (kitsune,[g.mid])
                            except:
                                ki.kitsuneText(kitsune,"「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort ♪""")
                                ki.kitsuneText(kitsune,"「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(gs.kitsunemembers))
            elif msg.text.lower() == mimic["setkey"]+'set' or msg.text.lower() == mimic["setkey"]+' set':
                md = ""
                if mimic["status"] == True: md+="⭕ Mimic:on \n"
                else:md+="❌ Mimic:off \n"
                if wait["talkban"] == True: md+="⭕ Talkban:on \n"
                else:md+="❌ Talkban:off \n"
                if msg.to in wait['pname']: md+="⭕ Namelock:on \n"
                else:md+="❌ Namelock:off \n"
                if wait["timeline"] == True: md+="⭕ Share:on \n"
                else:md+="❌ Share:off \n"
                if msg.to in kitsunewelcome: md+="⭕ Welcomemessage:on \n"
                else:md+="❌ Welcomemessage:off \n"
                if msg.to in kitsuneprotection: md+="⭕ Protection:on \n"
                else:md+="❌ Protection:off \n"
                if msg.to in kitsuneurl: md+="⭕ Link Protect:on \n"
                else:md+="❌ Link Protect:off \n"
                if msg.to in kitsuneautoinvite: md+="⭕ Invitation Protect:on \n"
                else:md+="❌ Invitation Protect:off \n"
                if msg.to in autoCancel: md+="⭕ Cancel Protect:on \n"
                else:md+="❌ Cancel Protect:off \n"
                if wait["contact"] == True: md+="⭕ Contact:on \n"
                else: md+="❌ Contact:off\n"
                if wait["autoJoin"] == True: md+="⭕ Join:on \n"
                else: md +="❌ Join:off\n"
                if wait["autoAdd"] == True: md+="⭕ Autoadd:on \n"
                else: md +="❌ Autoadd:off\n"
                if wait["autoCancel"]["on"] == True:md+="⭕ Auto cancel:" + str(wait["autoCancel"]["kitsunemembers"]) + "\n"
                else: md+= "❌ Auto cancel:off \n"
                if wait["leaveRoom"] == True: md+="⭕ Auto leave:on"
                else: md+="❌ Auto leave:off"
                ki.kitsuneText(kitsune,"「Setting」\n" + md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'lurking' or msg.text.lower() == mimic["setkey"]+' lurking':
                    print "Getting Read and Unread Data..."
                    if msg.to in wait2['readPoint']:
                        ki.kitsuneText(kitsune, "╔════════════════\n║SIDER IN GROUP\n╠════════════════%s\n║\n╚════════════════" % (wait2['readMember'][msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['ROM'][msg.to] = {}
                        ki.kitsuneText(kitsune, "Mencari Sider Otomatis")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['ROM'][msg.to] = {}
                        ki.kitsuneText(kitsune, "Mencari Sider Bosku")
            elif msg.text.lower() == mimic["setkey"]+'creator' or msg.text.lower() == mimic["setkey"]+' creator':
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'gcreator' or msg.text.lower() == mimic["setkey"]+' gcreator':
                try:
                    group = ki.getGroup(kitsune)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    ki.sendMessage(M)
                except:
                    W = group.kitsunemembers[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    ki.sendMessage(M)
                    ki.kitsuneText(kitsune,"Karena pencipta tidak ada saat ini, saya menunjukkan pengguna yang pertama kali masuk ke akun yang ada")
            elif msg.text.lower() == mimic["setkey"]+'groups' or msg.text.lower() == mimic["setkey"]+' groups':
                kitsunefriends = ki.getGroupIdsJoined()
                ki.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups1' or msg.text.lower() == mimic["setkey"]+' groups1':
                kitsunefriends = ki1.getGroupIdsJoined()
                ki1.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki1.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki1.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups3' or msg.text.lower() == mimic["setkey"]+' groups3':
                kitsunefriends = ki3.getGroupIdsJoined()
                ki3.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki3.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki3.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups4' or msg.text.lower() == mimic["setkey"]+' groups4':
                kitsunefriends = ki4.getGroupIdsJoined()
                ki4.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki4.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki4.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups5' or msg.text.lower() == mimic["setkey"]+' groups5':
                kitsunefriends = ki5.getGroupIdsJoined()
                ki5.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki5.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki5.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups6' or msg.text.lower() == mimic["setkey"]+' groups6':
                kitsunefriends = ki6.getGroupIdsJoined()
                ki6.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki6.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki6.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups7' or msg.text.lower() == mimic["setkey"]+' groups7':
                kitsunefriends = ki7.getGroupIdsJoined()
                ki7.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki7.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki7.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups8' or msg.text.lower() == mimic["setkey"]+' groups8':
                kitsunefriends = ki8.getGroupIdsJoined()
                ki8.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki8.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki8.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups9' or msg.text.lower() == mimic["setkey"]+' groups9':
                kitsunefriends = ki9.getGroupIdsJoined()
                ki9.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki9.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki9.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups10' or msg.text.lower() == mimic["setkey"]+' groups10':
                kitsunefriends = ki10.getGroupIdsJoined()
                ki10.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki10.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki10.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups11' or msg.text.lower() == mimic["setkey"]+' groups11':
                kitsunefriends = ki11.getGroupIdsJoined()
                ki11.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki11.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki11.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups113' or msg.text.lower() == mimic["setkey"]+' groups113':
                kitsunefriends = ki113.getGroupIdsJoined()
                ki113.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki113.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki113.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups13' or msg.text.lower() == mimic["setkey"]+' groups13':
                kitsunefriends = ki13.getGroupIdsJoined()
                ki13.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki13.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki13.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups14' or msg.text.lower() == mimic["setkey"]+' groups14':
                kitsunefriends = ki14.getGroupIdsJoined()
                ki14.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki14.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki14.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups15' or msg.text.lower() == mimic["setkey"]+' groups15':
                kitsunefriends = ki15.getGroupIdsJoined()
                ki15.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki15.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki15.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups16' or msg.text.lower() == mimic["setkey"]+' groups16':
                kitsunefriends = ki16.getGroupIdsJoined()
                ki16.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki16.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki16.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups17' or msg.text.lower() == mimic["setkey"]+' groups17':
                kitsunefriends = ki17.getGroupIdsJoined()
                ki17.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki17.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki17.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups18' or msg.text.lower() == mimic["setkey"]+' groups18':
                kitsunefriends = ki18.getGroupIdsJoined()
                ki18.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki18.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki18.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups19' or msg.text.lower() == mimic["setkey"]+' groups19':
                kitsunefriends = ki19.getGroupIdsJoined()
                ki19.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki19.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki19.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups20' or msg.text.lower() == mimic["setkey"]+' groups20':
                kitsunefriends = ki20.getGroupIdsJoined()
                ki20.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki20.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki20.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups21' or msg.text.lower() == mimic["setkey"]+' groups21':
                kitsunefriends = ki21.getGroupIdsJoined()
                ki21.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki21.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki21.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups22' or msg.text.lower() == mimic["setkey"]+' groups22':
                kitsunefriends = ki22.getGroupIdsJoined()
                ki22.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki22.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki22.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups23' or msg.text.lower() == mimic["setkey"]+' groups23':
                kitsunefriends = ki23.getGroupIdsJoined()
                ki23.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki23.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki23.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups24' or msg.text.lower() == mimic["setkey"]+' groups24':
                kitsunefriends = ki24.getGroupIdsJoined()
                ki24.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki24.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki24.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups25' or msg.text.lower() == mimic["setkey"]+' groups25':
                kitsunefriends = ki25.getGroupIdsJoined()
                ki25.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki25.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki25.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups26' or msg.text.lower() == mimic["setkey"]+' groups26':
                kitsunefriends = ki26.getGroupIdsJoined()
                ki26.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki26.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki26.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups27' or msg.text.lower() == mimic["setkey"]+' groups27':
                kitsunefriends = ki27.getGroupIdsJoined()
                ki27.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki27.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki27.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups28' or msg.text.lower() == mimic["setkey"]+' groups28':
                kitsunefriends = ki28.getGroupIdsJoined()
                ki28.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki28.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki28.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups29' or msg.text.lower() == mimic["setkey"]+' groups29':
                kitsunefriends = ki29.getGroupIdsJoined()
                ki29.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki29.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki29.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups30' or msg.text.lower() == mimic["setkey"]+' groups30':
                kitsunefriends = ki30.getGroupIdsJoined()
                ki30.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki21.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki30.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups31' or msg.text.lower() == mimic["setkey"]+' groups31':
                kitsunefriends = ki31.getGroupIdsJoined()
                ki31.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki31.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki31.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups32' or msg.text.lower() == mimic["setkey"]+' groups32':
                kitsunefriends = ki32.getGroupIdsJoined()
                ki32.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki32.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki32.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups33' or msg.text.lower() == mimic["setkey"]+' groups33':
                kitsunefriends = ki33.getGroupIdsJoined()
                ki33.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki33.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki33.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups34' or msg.text.lower() == mimic["setkey"]+' groups34':
                kitsunefriends = ki34.getGroupIdsJoined()
                ki34.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki34.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki34.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups35' or msg.text.lower() == mimic["setkey"]+' groups35':
                kitsunefriends = ki35.getGroupIdsJoined()
                ki35.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki35.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki35.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups36' or msg.text.lower() == mimic["setkey"]+' groups36':
                kitsunefriends = ki36.getGroupIdsJoined()
                ki36.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki36.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki36.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups37' or msg.text.lower() == mimic["setkey"]+' groups37':
                kitsunefriends = ki37.getGroupIdsJoined()
                ki37.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki37.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki37.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups38' or msg.text.lower() == mimic["setkey"]+' groups38':
                kitsunefriends = ki38.getGroupIdsJoined()
                ki38.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki38.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki38.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups39' or msg.text.lower() == mimic["setkey"]+' groups39':
                kitsunefriends = ki39.getGroupIdsJoined()
                ki39.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki39.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki39.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups40' or msg.text.lower() == mimic["setkey"]+' groups40':
                kitsunefriends = ki40.getGroupIdsJoined()
                ki40.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki40.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki40.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups41' or msg.text.lower() == mimic["setkey"]+' groups41':
                kitsunefriends = ki41.getGroupIdsJoined()
                ki41.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki41.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki41.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'groups42' or msg.text.lower() == mimic["setkey"]+' groups42':
                kitsunefriends = ki42.getGroupIdsJoined()
                ki42.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group List」"
                for ids in kitsunefriends:
                    aditya = ki42.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Group ☼」 " % len(kitsunefriends)
                ki42.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'pending' or msg.text.lower() == mimic["setkey"]+' pending':
                kitsunefriends = ki.getGroupIdsInvited()
                ki.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Group Pending」"
                for ids in kitsunefriends:
                    aditya = ki.getGroup(ids)
                    msgs+="\n%i. %s #%s" % (num, aditya.name, len(aditya.kitsunemembers))
                    num=(num+1)
                msgs+="\n「☼ Total %i Pending ☼」 " % len(kitsunefriends)
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'mcheck' or msg.text.lower() == mimic["setkey"]+' mcheck':
                kitsunefriend = ki.getContacts(wait["blacklist"])
                ki.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Black List」"
                for ids in kitsunefriend:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Black List ☼」 " % len(wait["blacklist"])
                ki.kitsuneText(kitsune, msgs) 
            elif msg.text.lower() == mimic["setkey"]+'clear mimic' or msg.text.lower() == mimic["setkey"]+' clear mimic':
                kitsunefriend = ki.getContacts(mimic["target"])
                for ids in kitsunefriend:
                    mimic["target"] = {}
                cd = Message()
                cd.to = msg.to
                cd.text = "「☼ Delete All Mimic List ☼」"
                ki.sendMessage(cd)
            elif msg.text.lower() == mimic["setkey"]+'tcheck' or msg.text.lower() == mimic["setkey"]+' tcheck':
                kitsunefriend = ki.getContacts(wait["talkblacklist"])
                ki.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Talkban List」"
                for ids in kitsunefriend:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Talkban List ☼」 " % len(wait["talkblacklist"])
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'team' or msg.text.lower() == mimic["setkey"]+' team':
                kitsunefriend = ki.getContacts(wait["bots"])
                ki.kitsuneText(kitsune, "Please wait...")
                num=1
                msgs="「User Team List」"
                for ids in kitsunefriend:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Team ☼」 " % len(wait["bots"])
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'friend' or msg.text.lower() == mimic["setkey"]+' friend':
                kitsunefriend = ki.getAllContactIds()
                ki.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」" % len(kontakkitsune)
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'group id' or msg.text.lower() == mimic["setkey"]+' group id':
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s: #%s\n" % (ki.getGroup(i).name,i)
                ki.kitsuneText(kitsune,h)
            elif msg.text.lower() == mimic["setkey"]+' gcancel' or msg.text.lower() == mimic["setkey"]+'gcancel':
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki.sendMessage(cd)
            elif msg.text.lower() == mimic["setkey"]+'clear ban' or msg.text.lower() == mimic["setkey"]+' clear ban':
                kitsunefriend = ki.getContacts(wait["blacklist"])
                for ids in kitsunefriend:
                    wait["blacklist"] = {}
                    f=codecs.open('blacklist.json','w','utf-8')
                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                cd = Message()
                cd.to = msg.to
                cd.text = "「☼ Delete All Black List ☼」"
                ki.sendMessage(cd)
            elif msg.text.lower() == mimic["setkey"]+'clear team' or msg.text.lower() == mimic["setkey"]+' clear team':
                kitsunefriend = ki.getContacts(wait["bots"])
                for ids in kitsunefriend:
                    wait["bots"] = {}
                    f=codecs.open('bots.json','w','utf-8')
                    json.dump(wait["bots"], f, sort_keys=True, indent=4,ensure_ascii=False)
                cd = Message()
                cd.to = msg.to
                cd.text = "「☼ Delete All Team List ☼」"
                ki.sendMessage(cd)
            elif msg.text.lower().startswith(mimic["setkey"]+'pesan set:') or msg.text.lower().startswith(mimic["setkey"]+' pesan set:'):
                if msg.text.lower().startswith(mimic["setkey"]+' pesan set:'):
                    foo = mimic["setkey"]+' pesan set:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["message"] = key1
                    ki.kitsuneText(kitsune,"「Welcome Message」\nWelcome Message has been set to:\n"+wait["message"])
                else:
                    foo = mimic["setkey"]+'pesan set:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["message"] = key1
                    ki.kitsuneText(kitsune,"「Welcome Message」\nWelcome Message has been set to:\n"+wait["message"])
            elif msg.text.lower().startswith(mimic["setkey"]+'spam add:') or msg.text.lower().startswith(mimic["setkey"]+' spam add:'):
                if msg.text.lower().startswith(mimic["setkey"]+' spam add:'):
                    foo = mimic["setkey"]+' spam add:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["spam"] = key1
                    ki.kitsuneText(kitsune,"「Spam Message」\nSpam Message has been set to:\n"+wait["spam"])
                else:
                    foo = mimic["setkey"]+'spam add:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    wait["spam"] = key1
                    ki.kitsuneText(kitsune,"「Spam Message」\nSpam Message has been set to:\n"+wait["spam"])
            elif msg.text.lower().startswith('setkey set ') or msg.text.lower().startswith(' setkey set '):
                if msg.text.lower().startswith(' setkey set '):
                    foo = ' setkey set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["setkey"] = key1
                    ki.kitsuneText(kitsune,"「Setkey」\nSetkey has been set to: "+mimic["setkey"].title())
                else:
                    foo = 'setkey set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["setkey"] = key1
                    ki.kitsuneText(kitsune,"「Setkey」\nSetkey has been set to: "+mimic["setkey"].title())
            elif msg.text.lower() == 'setkey off':
                mimic["setkey"] = ""
                ki.kitsuneText(kitsune,"Key has been set to DISABLED♪")
            elif msg.text.lower() == 'setkey reset':
                mimic["setkey"] = "kitsune"
                ki.kitsuneText(kitsune,"Key has been set to "+mimic["setkey"].title())
            elif msg.text.lower().startswith(mimic["setkey"]+'spam:') or msg.text.lower().startswith(mimic["setkey"]+' spam:'):
                if msg.text.lower().startswith(mimic["setkey"]+' spam:'):
                    foo = mimic["setkey"]+' spam:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    num = int(key1)
                    for var in range(0,num):
                        ki.kitsuneText(kitsune, wait["spam"].title())
                else:
                    foo = mimic["setkey"]+'spam:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    num = int(key1)
                    for var in range(0,num):
                        ki.kitsuneText(kitsune, wait["spam"].title())
            elif msg.text.lower().startswith(mimic["setkey"]+'welcomemessage pict set ') or msg.text.lower().startswith(mimic["setkey"]+' welcomemessage pict set '):
                if msg.text.lower().startswith(' Welcomemessage pict set:'):
                    foo = mimic["setkey"]+' welcomemessage pict set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["pap"] = key1
                    ki.kitsuneText(kitsune,"Welcome Message Picture has been set to")
                    ki.kitsuneImageWithURL(kitsune,mimic["pap"])
                else:
                    foo = mimic["setkey"]+'welcomemessage pict set '
                    key = len(foo)
                    key1 = msg.text[key:]
                    mimic["pap"] = key1
                    ki.kitsuneText(kitsune,"Welcome Message Picture has been set to")
                    ki.kitsuneImageWithURL(kitsune,mimic["pap"])
            elif msg.text.lower().startswith(mimic["setkey"]+'clock:') or msg.text.lower().startswith(mimic["setkey"]+' clock:'):
                if msg.text.lower().startswith(mimic["setkey"]+' clock:'):
                    foo = mimic["setkey"]+' clock:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    string = key1
                    if len(string.decode('utf-8')) <= 500:
                        wait["cName"] = string
                        ki42.kitsuneText(kitsune,"Update Clock Menjadi :" + string + "")
                else:
                    foo = mimic["setkey"]+'clock:'
                    key = len(foo)
                    key1 = msg.text[key:]
                    tulisan = jmlh * (teks+"\n")
                    if len(string.decode('utf-8')) <= 500:
                        wait["cName"] = string
                        ki42.kitsuneText(kitsune,"Update Clock Menjadi :" + string + "")
            elif msg.text.lower().startswith(mimic["setkey"]+'spam ') or msg.text.lower().startswith(mimic["setkey"]+' spam '):
                if msg.text.lower().startswith(mimic["setkey"]+' spam '):
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    foo = mimic["setkey"]+' spam '
                    key = len(foo)
                    key1 = msg.text[key:]
                    teks = key1.replace("" + str(txt[1])+" "+str(jmlh)+ " ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 10000:
                            for x in range(jmlh):
                                ki.kitsuneText(kitsune, teks)
                            else:
                                ki.kitsuneText(kitsune, '')
                    elif txt[1] == "off":
                        if jmlh <= 10000:
                                ki.kitsuneText(kitsune, tulisan)
                        else:
                                ki.kitsuneText(kitsune, '')
                else:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    foo = mimic["setkey"]+'spam '
                    key = len(foo)
                    key1 = msg.text[key:]
                    teks = key1.replace("" + str(txt[1])+" "+str(jmlh)+ " ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 10000:
                            for x in range(jmlh):
                                ki.kitsuneText(kitsune, teks)
                            else:
                                ki.kitsuneText(kitsune, '')
                    elif txt[1] == "off":
                        if jmlh <= 10000:
                                ki.kitsuneText(kitsune, tulisan)
                        else:
                                ki.kitsuneText(kitsune, '')
            elif msg.text.lower() == mimic["setkey"]+'welcomemessage pict' or msg.text.lower() == mimic["setkey"]+' welcomemessage pict':
                ki.kitsuneImageWithURL(kitsune,mimic["pap"])
            elif msg.text.lower() == mimic["setkey"]+'pesan cek' or msg.text.lower() == mimic["setkey"]+' pesan cek':
                    ki.kitsuneText(kitsune, wait["message"])
            elif msg.text.lower() == mimic["setkey"]+'spam cek' or msg.text.lower() == mimic["setkey"]+' spam cek':
                    ki.kitsuneText(kitsune, wait["spam"].title())
            elif msg.text.lower() == mimic["setkey"]+'url' or msg.text.lower() == mimic["setkey"]+' url':
                if msg.toType == 2:
                    g = ki.getGroup(kitsune)
                    gurl = ki.reissueGroupTicket(kitsune)
                    ki.kitsuneText(kitsune,"line://ti/g/" + gurl)
                    if g.kitsuneTicket == True:
                        g.kitsuneTicket = False
                        ki.updateGroup(g)
                else:
                        ki.kitsuneText(kitsune,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text.lower() == mimic["setkey"]+'update' or msg.text.lower() == mimic["setkey"]+' update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = ki.getProfile()
                    profile.kitsuneName = wait["cName"] + nowT
                    ki.updateProfile(profile)
                    ki.kitsuneText(kitsune,"Diperbarui")
                else:
                    ki.kitsuneText(kitsune,"Silahkan Aktifkan Jam")
            elif msg.text.lower().startswith(mimic["setkey"]+'nk ') or msg.text.lower().startswith(mimic["setkey"]+' nk ') or msg.text.lower().startswith(mimic["setkey"]+'nk') or msg.text.lower().startswith(mimic["setkey"]+' nk'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                            try:
                                gs = ki.getGroup(kitsune)
                                gs.kitsuneTicket = False
                                random.choice(P2).updateGroup(gs)
                                invsend = 0
                                Ticket = random.choice(P2).reissueGroupTicket(kitsune)
                                ki19.acceptGroupInvitationByTicket(kitsune,Ticket)
                                ki19.kickoutFromGroup(kitsune,[target])
                                gs.kitsuneTicket = True
                                ki19.updateGroup(gs)
                                ki100.sendText(gs)
                            except:
                                ki19.leaveGroup(kitsune)
                else:
                    ki.kitsuneText(kitsune,"「Kick Mode Siri」\nYou have to mention a user♪")
            elif msg.text.lower() == mimic["setkey"]+'welcome' or msg.text.lower() == mimic["setkey"]+' welcome':
                ginfo = ki.getGroup(kitsune)
                ki.kitsuneImageWithURL(kitsune,mimic["pap"])
                ki.kitsuneText(kitsune,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.kitsuneName )
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                ki.sendMessage(msg)
            elif msg.text.lower().startswith(mimic["setkey"]+'gift ') or msg.text.lower().startswith(mimic["setkey"]+' gift ') or msg.text.lower().startswith(mimic["setkey"]+'gift') or msg.text.lower().startswith(mimic["setkey"]+' gift'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            group = ki.getContact(target)
                            ki.kitsuneText(kitsune, group.kitsuneName + " Check Your Gift")
                            msg.contentType = 9
                            msg.contentMetadata={'PRDTYPE': 'STICKER',
                                                 'STKVER': '1',
                                                 'MSGTPL': '5',
                                                 'STKPKGID': '1380280'}
                            msg.to = target
                            msg.text = None
                            ki.sendMessage(msg)
                        except:
                            pass
                else:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDTYPE': 'STICKER',
                                        'STKVER': '1',
                                        'MSGTPL': '5',
                                        'STKPKGID': '1380280'}
                    msg.text = None
                    ki.sendMessage(msg)
#-----------------------------------------------------------
#------
            elif msg.text.lower().startswith(mimic["setkey"]+'kick1 ') or msg.text.lower().startswith(mimic["setkey"]+' kick1 ') or msg.text.lower().startswith(mimic["setkey"]+'kick1') or msg.text.lower().startswith(mimic["setkey"]+' kick1'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki1.kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            ki1.kitsuneText(kitsune,str(e))
                else:
                    ki1.kitsuneText(kitsune,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick2 ') or msg.text.lower().startswith(mimic["setkey"]+' kick2 ') or msg.text.lower().startswith(mimic["setkey"]+'kick2') or msg.text.lower().startswith(mimic["setkey"]+' kick2'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki2.kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            ki2.kitsuneText(kitsune,str(e))
                else:
                    ki2.kitsuneText(kitsune,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick3 ') or msg.text.lower().startswith(mimic["setkey"]+' kick3 ') or msg.text.lower().startswith(mimic["setkey"]+'kick3') or msg.text.lower().startswith(mimic["setkey"]+' kick3'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki3.kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            ki3.kitsuneText(kitsune,str(e))
                else:
                    ki3.kitsuneText(kitsune,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick4 ') or msg.text.lower().startswith(mimic["setkey"]+' kick4 ') or msg.text.lower().startswith(mimic["setkey"]+'kick4') or msg.text.lower().startswith(mimic["setkey"]+' kick4'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki4.kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            ki4.kitsuneText(kitsune,str(e))
                else:
                    ki4.kitsuneText(kitsune,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick5 ') or msg.text.lower().startswith(mimic["setkey"]+' kick5 ') or msg.text.lower().startswith(mimic["setkey"]+'kick5') or msg.text.lower().startswith(mimic["setkey"]+' kick5'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki5.kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            ki5.kitsuneText(kitsune,str(e))
                else:
                    ki5.kitsuneText(kitsune,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick6 ') or msg.text.lower().startswith(mimic["setkey"]+' kick6 ') or msg.text.lower().startswith(mimic["setkey"]+'kick6') or msg.text.lower().startswith(mimic["setkey"]+' kick6'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki6.kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            ki6.kitsuneText(kitsune,str(e))
                else:
                    ki6.kitsuneText(kitsune,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'makan ') or msg.text.lower().startswith(mimic["setkey"]+' makan ') or msg.text.lower().startswith(mimic["setkey"]+'makan') or msg.text.lower().startswith(mimic["setkey"]+' makan'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            random.choice(P1).kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            random.choice(P1).kitsuneText(kitsune,str(e))
                else:
                    random.choice(P1).kitsuneText(kitsune,"「makan」\nYou need to mention a user♪")
            elif msg.text.lower().startswith(mimic["setkey"]+'kick ') or msg.text.lower().startswith(mimic["setkey"]+' kick ') or msg.text.lower().startswith(mimic["setkey"]+'kick') or msg.text.lower().startswith(mimic["setkey"]+' kick'):
                if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.kickoutFromGroup(kitsune,[target])
                        except Exception as e:
                            ki.kitsuneText(kitsune,str(e))
                else:
                    ki.kitsuneText(kitsune,"「Kick」\nYou need to mention a user♪")
            elif msg.text.lower() == 'responsename':
                profile = ki1.getProfile()
                text = profile.kitsuneName + ""
                ki1.kitsuneText(kitsune, text)
                profile = ki2.getProfile()
                text = profile.kitsuneName + ""
                ki2.kitsuneText(kitsune, text)
                profile = ki3.getProfile()
                text = profile.kitsuneName + ""
                ki3.kitsuneText(kitsune, text)
                profile = ki4.getProfile()
                text = profile.kitsuneName + ""
                ki4.kitsuneText(kitsune, text)
                profile = ki5.getProfile()
                text = profile.kitsuneName + ""
                ki5.kitsuneText(kitsune, text)
                profile = ki6.getProfile()
                text = profile.kitsuneName + ""
                ki6.kitsuneText(kitsune, text)
                profile = ki7.getProfile()
                text = profile.kitsuneName + ""
                ki7.kitsuneText(kitsune, text)
                profile = ki8.getProfile()
                text = profile.kitsuneName + ""
                ki8.kitsuneText(kitsune, text)
                profile = ki9.getProfile()
                text = profile.kitsuneName + ""
                ki9.kitsuneText(kitsune, text)
                profile = ki10.getProfile()
                text = profile.kitsuneName + ""
                ki10.kitsuneText(kitsune, text)
                profile = ki11.getProfile()
                text = profile.kitsuneName + ""
                ki11.kitsuneText(kitsune, text)
                profile = ki12.getProfile()
                text = profile.kitsuneName + ""
                ki12.kitsuneText(kitsune, text)
                profile = ki13.getProfile()
                text = profile.kitsuneName + ""
                ki13.kitsuneText(kitsune, text)
                profile = ki14.getProfile()
                text = profile.kitsuneName + ""
                ki14.kitsuneText(kitsune, text)
                profile = ki15.getProfile()
                text = profile.kitsuneName + ""
                ki15.kitsuneText(kitsune, text)
                profile = ki16.getProfile()
                text = profile.kitsuneName + ""
                ki16.kitsuneText(kitsune, text)
                profile = ki17.getProfile()
                text = profile.kitsuneName + ""
                ki17.kitsuneText(kitsune, text)
                profile = ki18.getProfile()
                text = profile.kitsuneName + ""
                ki18.kitsuneText(kitsune, text)
                profile = ki20.getProfile()
                text = profile.kitsuneName + ""
                ki20.kitsuneText(kitsune, text)
                profile = ki21.getProfile()
                text = profile.kitsuneName + ""
                ki21.kitsuneText(kitsune, text)
                profile = ki22.getProfile()
                text = profile.kitsuneName + ""
                ki22.kitsuneText(kitsune, text)
                profile = ki23.getProfile()
                text = profile.kitsuneName + ""
                ki23.kitsuneText(kitsune, text)
                profile = ki24.getProfile()
                text = profile.kitsuneName + ""
                ki24.kitsuneText(kitsune, text)
                profile = ki25.getProfile()
                text = profile.kitsuneName + ""
                ki25.kitsuneText(kitsune, text)
                profile = ki26.getProfile()
                text = profile.kitsuneName + ""
                ki26.kitsuneText(kitsune, text)
                profile = ki27.getProfile()
                text = profile.kitsuneName + ""
                ki27.kitsuneText(kitsune, text)
                profile = ki28.getProfile()
                text = profile.kitsuneName + ""
                ki28.kitsuneText(kitsune, text)
                profile = ki29.getProfile()
                text = profile.kitsuneName + ""
                ki29.kitsuneText(kitsune, text)
                profile = ki30.getProfile()
                text = profile.kitsuneName + ""
                ki30.kitsuneText(kitsune, text)
                profile = ki31.getProfile()
                text = profile.kitsuneName + ""
                ki31.kitsuneText(kitsune, text)
                profile = ki32.getProfile()
                text = profile.kitsuneName + ""
                ki32.kitsuneText(kitsune, text)
                profile = ki33.getProfile()
                text = profile.kitsuneName + ""
                ki33.kitsuneText(kitsune, text)
                profile = ki34.getProfile()
                text = profile.kitsuneName + ""
                ki34.kitsuneText(kitsune, text)
                profile = ki35.getProfile()
                text = profile.kitsuneName + ""
                ki35.kitsuneText(kitsune, text)
                profile = ki36.getProfile()
                text = profile.kitsuneName + ""
                ki36.kitsuneText(kitsune, text)
                profile = ki37.getProfile()
                text = profile.kitsuneName + ""
                ki37.kitsuneText(kitsune, text)
                profile = ki38.getProfile()
                text = profile.kitsuneName + ""
                ki38.kitsuneText(kitsune, text)
                profile = ki39.getProfile()
                text = profile.kitsuneName + ""
                ki39.kitsuneText(kitsune, text)
                profile = ki40.getProfile()
                text = profile.kitsuneName + ""
                ki40.kitsuneText(kitsune, text)
                profile = ki41.getProfile()
                text = profile.kitsuneName + ""
                ki41.kitsuneText(kitsune, text)
                profile = ki42.getProfile()
                text = profile.kitsuneName + ""
                ki42.kitsuneText(kitsune, text)
            elif msg.text.lower() == 'ping':
                ki1.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki2.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki3.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki4.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki5.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki6.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki7.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki8.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki9.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki10.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki11.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki12.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki13.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki14.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki15.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki16.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki17.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki18.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki20.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki21.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki22.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki23.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki24.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki25.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki26.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki27.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki28.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki29.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki30.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki31.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki32.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki33.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki34.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki35.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki36.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki37.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki38.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿") 
                ki39.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki40.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki41.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
                ki42.kitsuneText(kitsune,"Hooh 􀠁􀆩􏿿")
            elif msg.text.lower() == mimic["setkey"]+' miclist' or msg.text.lower() == mimic["setkey"]+'miclist':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                mimictag(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                mimictag(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                mimictag(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                mimictag(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                mimictag(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                mimictag(kitsune, nm5)
            elif 'contact ' in msg.text.lower():
                spl = msg.text.lower().replace('contact ','')
                if spl == 'on':
                    if wait['contact'] == True:
                        msgs="contact already on"
                    else:
                        msgs="contact set to on"
                        wait['contact']=True
                    ki.kitsuneText(kitsune, msgs)
                elif spl == 'off':
                    if wait['contact'] == False:
                        msgs="contact already off"
                    else:
                        msgs="contact set to off"
                        wait['contact']=False
                    ki.kitsuneText(kitsune, msgs)
            elif 'cancel ' in msg.text.lower():
                spl = msg.text.lower().replace('cancel ','')
                if spl == 'on':
                    if msg.to in autoCancel:
                        msgs="Cancel Invitation already on"
                    else:
                        autoCancel.append(msg.to)
                        msgs="Cancel Invitation set to on"
                    ki.kitsuneText(kitsune,"「Cancel Invitation」\n" + msgs)
                elif spl == 'off':
                    if msg.to in autoCancel:
                        autoCancel.remove(msg.to)
                        msgs="Cancel Invitation already off"
                    else:
                        msgs="Cancel Invitation already off"
                    ki.kitsuneText(kitsune,"「Cancel Invitation」\n" + msgs)
            elif 'welcomemessage ' in msg.text.lower():
                spl = msg.text.lower().replace('welcomemessage ','')
                if spl == 'on':
                    if msg.to in kitsunewelcome:
                        msgs="Welcome Message already on"
                    else:
                        kitsunewelcome.append(msg.to)
                        msgs="Welcome Message set to on"
                    ki.kitsuneText(kitsune,"「Welcome Message」\n" + msgs)
                elif spl == 'off':
                    if msg.to in kitsunewelcome:
                        kitsunewelcome.remove(msg.to)
                        msgs="Welcome Message already off"
                    else:
                        msgs="Welcome Message already off"
                    ki.kitsuneText(kitsune,"「Welcome Message」\n" + msgs)
            elif 'protect ' in msg.text.lower():
                spl = msg.text.lower().replace('protect ','')
                if spl == 'on':
                    if msg.to in kitsuneprotection:
                        msgs="Protect already on"
                    else:
                        kitsuneprotection.append(msg.to)
                        msgs="Protect set to on"
                    ki.kitsuneText(kitsune,"「Protect」\n" + msgs)
                elif spl == 'off':
                    if msg.to in kitsuneprotection:
                        kitsuneprotection.remove(msg.to)
                        msgs="Protect already off"
                    else:
                        msgs="Protect already off"
                    ki.kitsuneText(kitsune,"「Protect」\n" + msgs)
            elif 'inv ' in msg.text.lower():
                spl = msg.text.lower().replace('inv ','')
                if spl == 'on':
                    if msg.to in kitsuneautoinvite:
                        msgs="Invitation protect already on"
                    else:
                        kitsuneautoinvite.append(msg.to)
                        msgs="Invitation protect set to on"
                    ki.kitsuneText(kitsune,"「Protect Invitation」\n" + msgs)
                elif spl == 'off':
                    if msg.to in kitsuneautoinvite:
                        kitsuneautoinvite.remove(msg.to)
                        msgs="Invitation protect set to off"
                    else:
                        msgs="Invitation protect already off"
                    ki.kitsuneText(kitsune,"「Protect Invitation」\n" + msgs)
            elif 'qr ' in msg.text.lower():
                spl = msg.text.lower().replace('qr ','')
                if spl == 'on':
                    if msg.to in kitsuneurl:
                        msgs="Link protect already on"
                    else:
                        kitsuneurl.append(msg.to)
                        msgs="Link protect set to on"
                    ki.kitsuneText(kitsune,"「Protect Qr」\n" + msgs)
                elif spl == 'off':
                    if msg.to in kitsuneurl:
                        kitsuneurl.remove(msg.to)
                        msgs="Link protect set to off"
                    else:
                        msgs="Link protect already off"
                    ki.kitsuneText(kitsune,"「Protect Qr」\n" + msgs)
            elif 'jam ' in msg.text.lower():
                spl = msg.text.lower().replace('jam ','')
                if spl == 'on':
                    if wait['clock'] == True:
                        msgs="Jam already on"
                    else:
                        msgs="Jam set to on"
                        wait['clock']=True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"༺%H:%M༻")
                        profile = ki.getProfile()
                        profile.kitsuneName = wait["cName"] + nowT
                        ki.updateProfile(profile)
                    ki.kitsuneText(kitsune, msgs)
                elif spl == 'off':
                    if wait['clock'] == False:
                        msgs="Jam already off"
                    else:
                        msgs="Jam set to off"
                        wait['clock']=False
                    ki.kitsuneText(kitsune, msgs)
            elif 'talkban ' in msg.text.lower():
                spl = msg.text.lower().replace('talkban ','')
                if spl == 'on':
                    if wait['talkban'] == True:
                        msgs="「Talkban」\nTalkban already Not For chat"
                    else:
                        msgs="「Talkban」\nTalkban set to Not For chat"
                        wait['talkban']=True
                    ki.kitsuneText(kitsune, msgs)
                elif spl == 'off':
                    if wait['talkban'] == False:
                        msgs="「Talkban」\nTalkban already Allow For chat"
                    else:
                        msgs="「Talkban」\nTalkban set to Allow For chat"
                        wait['talkban']=False
                    ki.kitsuneText(kitsune, msgs)
            elif 'leave ' in msg.text.lower():
                spl = msg.text.lower().replace('leave ','')
                if spl == 'on':
                    if wait['leaveRoom'] == True:
                        msgs="「Auto Leave」\nAuto Leave Multichat already ENABLED♪"
                    else:
                        msgs="「Auto Leave」Auto Leave Multichat set to ENABLED♪"
                        wait['leaveRoom']=True
                    ki.kitsuneText(kitsune, msgs)
                elif spl == 'off':
                    if wait['leaveRoom'] == False:
                        msgs="「Auto Leave」Auto Leave Multichat already DISABLED♪"
                    else:
                        msgs="「Auto Leave」Auto Leave Multichat set to DISABLED♪"
                        wait['leaveRoom']=False
                    ki.kitsuneText(kitsune, msgs)
            elif 'share ' in msg.text.lower():
                spl = msg.text.lower().replace('share ','')
                if spl == 'on':
                    if wait['timeline'] == True:
                        msgs="「Share」\nShare already ENABLED♪"
                    else:
                        msgs="「Share」\nShare set to ENABLED♪"
                        wait['timeline']=True
                    ki.kitsuneText(kitsune, msgs)
                elif spl == 'off':
                    if wait['timeline'] == False:
                        msgs="「Share」\nShare already DISABLED♪"
                    else:
                        msgs="「Share」\nShare set to DISABLED♪"
                        wait['timeline']=False
                    ki.kitsuneText(kitsune, msgs)
            elif 'namelock ' in msg.text.lower():
                spl = msg.text.lower().replace('namelock ','')
                if spl == 'on':
                    if msg.to in wait['pname']:
                        msgs="「Name Lock」\nName Lock already ENABLED♪"
                    else:
                        msgs="「Name Lock」\nName Lock set to ENABLED♪"
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = ki.getGroup(msg.to).name
                    ki.kitsuneText(kitsune, msgs)
                elif spl == 'off':
                    if msg.to in wait['pname']:
                        msgs="「Name Lock」\nName Lock set to DISABLED♪"
                        del wait['pname'][msg.to]
                    else:
                        msgs="「Name Lock」\nName Lock already DISABLED♪"
                    ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'blcheck' or msg.text.lower() == mimic["setkey"]+' blcheck':
                if wait["blacklist"] == {}:
                    ki.kitsuneText(kitsune,"Nothing in the blacklist")
                else:
                    ki.kitsuneText(kitsune,"Daftar Contact Yang Ke Ban")
                    mc = ""
                    for mi_d in wait["blacklist"]:
						msg.contentType = 13
						msg.contentMetadata = {'mid': mi_d}
						ki.sendMessage(msg)
            elif msg.text.lower() == mimic["setkey"]+'blocklist' or msg.text.lower() == mimic["setkey"]+' blocklist':
                blockedlist = ki.getBlockedContactIds()
                ki.kitsuneText(kitsune, "Please wait...")
                kontak = ki.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                ki.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == mimic["setkey"]+'kill' or msg.text.lower() == mimic["setkey"]+' kill':
                if msg.toType == 2:
                    group = ki.getGroup(kitsune)
                    gMembMids = [contact.mid for contact in group.kitsunemembers]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.kitsuneText(kitsune,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            random.choice(P1).kickoutFromGroup(kitsune,[jj])
                            print (kitsune,[jj])
                        except:
                            pass
            elif msg.text.lower() == mimic["setkey"]+' banlist' or msg.text.lower() == mimic["setkey"]+'banlist':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                bltag(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                bltag(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                bltag(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                bltag(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                bltag(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                bltag(kitsune, nm5)
            elif msg.text.lower() == mimic["setkey"]+' cium' or msg.text.lower() == mimic["setkey"]+'cium':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium(kitsune, nm5)
            elif msg.text.lower() == mimic["setkey"]+'cancel' or msg.text.lower() == mimic["setkey"]+' cancel':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(kitsune, gInviMids)
            elif msg.text.lower() == mimic["setkey"]+'kiss' or msg.text.lower() == mimic["setkey"]+' kiss':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki1.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki2.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki3.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki4.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki5.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki6.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki7.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki8.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki9.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki10.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki11.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki12.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki13.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki14.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki15.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki16.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki17.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki18.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki20.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        random.choice(P1).updateGroup(G)
                        G.kitsuneTicket(G)
                        random.choice(P1).updateGroup(G)
            elif msg.text.lower() == mimic["setkey"]+'all' or msg.text.lower() == mimic["setkey"]+' all':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki1.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki2.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki3.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki4.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki5.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki6.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki7.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki8.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki9.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki10.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki11.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki12.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki13.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki14.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki15.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki16.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki17.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki18.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki20.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki21.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki22.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki23.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki24.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki25.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki26.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki27.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki28.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki29.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki30.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki31.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki32.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki33.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki34.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki35.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki36.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki37.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki38.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki39.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki40.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki41.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki42.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        random.choice(P1).updateGroup(G)
                        G.kitsuneTicket(G)
                        random.choice(P1).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text.lower() == mimic["setkey"]+'honey' or msg.text.lower() == mimic["setkey"]+' honey':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki1.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki2.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki3.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki4.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki5.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki1.updateGroup(G)
                        G.kitsuneTicket(G)
                        ki1.updateGroup(G)
            elif msg.text.lower() == mimic["setkey"]+'cipok' or msg.text.lower() == mimic["setkey"]+' cipok':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki1.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki2.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki3.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki4.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki5.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki6.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki7.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki8.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki9.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki10.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki1.updateGroup(G)
                        G.kitsuneTicket(G)
                        ki1.updateGroup(G)
            elif msg.text.lower() == mimic["setkey"]+'desah' or msg.text.lower() == mimic["setkey"]+' desah':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki1.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki2.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki3.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki4.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki5.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki6.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki7.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki8.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki9.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki10.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki11.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki12.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki13.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki14.acceptGroupInvitationByTicket(kitsune,Ticket)
                        ki15.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki1.updateGroup(G)
                        G.kitsuneTicket(G)
                        ki1.updateGroup(G)
            elif msg.text.lower() == mimic["setkey"]+'bye' or msg.text.lower() == mimic["setkey"]+' bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'cau':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki1.leaveGroup(kitsune)
                        ki2.leaveGroup(kitsune)
                        ki3.leaveGroup(kitsune)
                        ki4.leaveGroup(kitsune)
                        ki5.leaveGroup(kitsune)
                        ki6.leaveGroup(kitsune)
                        ki7.leaveGroup(kitsune)
                        ki8.leaveGroup(kitsune)
                        ki9.leaveGroup(kitsune)
                        ki10.leaveGroup(kitsune)
                        ki11.leaveGroup(kitsune)
                        ki12.leaveGroup(kitsune)
                        ki13.leaveGroup(kitsune)
                        ki14.leaveGroup(kitsune)
                        ki15.leaveGroup(kitsune)
                        ki16.leaveGroup(kitsune)
                        ki17.leaveGroup(kitsune)
                        ki18.leaveGroup(kitsune)
                        ki20.leaveGroup(kitsune)
                        ki21.leaveGroup(kitsune)
                        ki22.leaveGroup(kitsune)
                        ki23.leaveGroup(kitsune)
                        ki24.leaveGroup(kitsune)
                        ki25.leaveGroup(kitsune)
                        ki26.leaveGroup(kitsune)
                        ki27.leaveGroup(kitsune)
                        ki28.leaveGroup(kitsune)
                        ki29.leaveGroup(kitsune)
                        ki30.leaveGroup(kitsune)
                        ki31.leaveGroup(kitsune)
                        ki32.leaveGroup(kitsune)
                        ki33.leaveGroup(kitsune)
                        ki34.leaveGroup(kitsune)
                        ki35.leaveGroup(kitsune)
                        ki36.leaveGroup(kitsune)
                        ki37.leaveGroup(kitsune)
                        ki38.leaveGroup(kitsune)
                        ki39.leaveGroup(kitsune)
                        ki40.leaveGroup(kitsune)
                        ki41.leaveGroup(kitsune)
                        ki42.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k1':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki1mid}
                       try:
                           ki1.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k2':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki2mid}
                       try:
                           ki2.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k3':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki3mid}
                       try:
                           ki3.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k4':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki4mid}
                       try:
                           ki4.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k5':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki5mid}
                       try:
                           ki5.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k6':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki6mid}
                       try:
                           ki6.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k7':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki7mid}
                       try:
                           ki7.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k8':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki8mid}
                       try:
                           ki8.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k9':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki9mid}
                       try:
                           ki9.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k10':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki10mid}
                       try:
                           ki10.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k11':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki11mid}
                       try:
                           ki11.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k12':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki12mid}
                       try:
                           ki12.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k13':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki13mid}
                       try:
                           ki13.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k14':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki14mid}
                       try:
                           ki14.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k15':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki15mid}
                       try:
                           ki15.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k16':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki16mid}
                       try:
                           ki16.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k33':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki33mid}
                       try:
                           ki33.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'myifc':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    ki.kitsuneText(kitsune, botKernel + "\n\n􀬁􀆆􏿿TAMII BOT CONTROL NetStatus􀬁􀆆􏿿")
            elif msg.text.lower() == 'mysystem':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    ki.kitsuneText(kitsune, botKernel + "\n\n􀬁􀆆􏿿TAMII BOT CONTROL System􀬁􀆆􏿿")
            elif msg.text.lower() == 'mykernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    ki.kitsuneText(kitsune, botKernel + "\n\n􀬁􀆆􏿿TAMII BOT CONTROL Kernel􀬁􀆆􏿿")
            elif msg.text.lower() == 'mycpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    ki.kitsuneText(kitsune, botKernel + "\n\n􀬁􀆆􏿿TAMII BOT CONTROL CPU INFO 􀬁􀆆􏿿")
            elif msg.text.lower() == 'k34':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki34mid}
                       try:
                           ki34.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k35':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki35mid}
                       try:
                           ki35.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k36':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki36mid}
                       try:
                           ki36.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k37':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki37mid}
                       try:
                           ki37.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k17':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki17mid}
                       try:
                           ki17.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k18':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki18mid}
                       try:
                           ki18.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k20':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki20mid}
                       try:
                           ki20.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k21':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki21mid}
                       try:
                           ki21.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k22':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki22mid}
                       try:
                           ki22.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k23':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki23mid}
                       try:
                           ki23.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k24':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki24mid}
                       try:
                           ki24.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k25':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki25mid}
                       try:
                           ki25.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k26':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki26mid}
                       try:
                           ki26.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k27':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki27mid}
                       try:
                           ki27.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k28':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki28mid}
                       try:
                           ki28.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k29':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki29mid}
                       try:
                           ki29.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k30':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki30mid}
                       try:
                           ki30.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k38':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki38mid}
                       try:
                           ki38.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k39':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki39mid}
                       try:
                           ki39.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k40':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki40mid}
                       try:
                           ki40.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k41':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki41mid}
                       try:
                           ki41.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k42':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki42mid}
                       try:
                           ki42.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k31':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki31mid}
                       try:
                           ki31.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'k32':
                if msg.toType == 2:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': ki32mid}
                       try:
                           ki32.sendMessage(msg)
                       except:
                           ki.sendMessage(msg)
            elif msg.text.lower() == 'hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15134150",
                                     "STKPKGID": "1388272",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15659375",
                                     "STKPKGID": "1405277",
                                     "STKVER": "2" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'siap bos':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'reboot':
                    print "[Command]Like executed"
                    try:
                        ki1.kitsuneText(kitsune,"Restart Program")
                        restart_program()
                    except:
                        ki.kitsuneText(kitsune,"Restart Program")
                        restart_program()
                        pass
            elif msg.text.lower() == 'thx':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846759",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'lol':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846776",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'sip':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "50738",
                                     "STKPKGID": "2212",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'tidak':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'no':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'suntuk':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875040",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'apa':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14904525",
                                     "STKPKGID": "7934",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'apa?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
            elif msg.text.lower() == '?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'pose dulu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875030",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                ki.sendMessage(msg)
            elif msg.text.lower() == 'clone1':
                ki1.cloneContact(kitsune)
            elif msg.text.lower() == 'clone2':
                ki2.cloneContact(kitsune)
            elif msg.text.lower() == 'clone3':
                ki3.cloneContact(kitsune)
            elif msg.text.lower() == 'clone4':
                ki4.cloneContact(kitsune)
            elif msg.text.lower() == 'clone5':
                ki5.cloneContact(kitsune)
            elif msg.text.lower() == 'clone6':
                ki6.cloneContact(kitsune)
            elif msg.text.lower() == 'clone7':
                ki7.cloneContact(kitsune)
            elif msg.text.lower() == 'clone8':
                ki8.cloneContact(kitsune)
            elif msg.text.lower() == 'clone9':
                ki9.cloneContact(kitsune)
            elif msg.text.lower() == 'clone10':
                ki10.cloneContact(kitsune)
            elif msg.text.lower() == 'clone11':
                ki11.cloneContact(kitsune)
            elif msg.text.lower() == 'clone12':
                ki12.cloneContact(kitsune)
            elif msg.text.lower() == 'clone13':
                ki13.cloneContact(kitsune)
            elif msg.text.lower() == 'clone14':
                ki14.cloneContact(kitsune)
            elif msg.text.lower() == 'clone15':
                ki15.cloneContact(kitsune)
            elif msg.text.lower() == 'clone16':
                ki16.cloneContact(kitsune)
            elif msg.text.lower() == 'clone17':
                ki17.cloneContact(kitsune)
            elif msg.text.lower() == 'clone18':
                ki18.cloneContact(kitsune)
            elif msg.text.lower() == 'clone20':
                ki20.cloneContact(kitsune)
            elif msg.text.lower() == 'clone21':
                ki21.cloneContact(kitsune)
            elif msg.text.lower() == 'clone22':
                ki22.cloneContact(kitsune)
            elif msg.text.lower() == 'clone23':
                ki23.cloneContact(kitsune)
            elif msg.text.lower() == 'clone24':
                ki24.cloneContact(kitsune)
            elif msg.text.lower() == 'clone25':
                ki25.cloneContact(kitsune)
            elif msg.text.lower() == 'clone26':
                ki26.cloneContact(kitsune)
            elif msg.text.lower() == 'clone27':
                ki27.cloneContact(kitsune)
            elif msg.text.lower() == 'clone28':
                ki28.cloneContact(kitsune)
            elif msg.text.lower() == 'clone29':
                ki29.cloneContact(kitsune)
            elif msg.text.lower() == 'clone30':
                ki30.cloneContact(kitsune)
            elif msg.text.lower() == 'clone31':
                ki31.cloneContact(kitsune)
            elif msg.text.lower() == 'clone32':
                ki32.cloneContact(kitsune)
            elif msg.text.lower() == 'clone33':
                ki33.cloneContact(kitsune)
            elif msg.text.lower() == 'clone34':
                ki34.cloneContact(kitsune)
            elif msg.text.lower() == 'clone35':
                ki35.cloneContact(kitsune)
            elif msg.text.lower() == 'clone36':
                ki36.cloneContact(kitsune)
            elif msg.text.lower() == 'clone37':
                ki37.cloneContact(kitsune)
            elif msg.text.lower() == 'clone38':
                ki38.cloneContact(kitsune)
            elif msg.text.lower() == 'clone39':
                ki39.cloneContact(kitsune)
            elif msg.text.lower() == 'clone40':
                ki40.cloneContact(kitsune)
            elif msg.text.lower() == 'clone41':
                ki41.cloneContact(kitsune)
            elif msg.text.lower() == 'clone42':
                ki42.cloneContact(kitsune)
            elif msg.text.lower() == 'friend1':
                kitsunefriend = ki1.getAllContactIds()
                ki1.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki1.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki1.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend2':
                kitsunefriend = ki2.getAllContactIds()
                ki2.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki2.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki2.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend3':
                kitsunefriend = ki3.getAllContactIds()
                ki3.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki3.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki3.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend4':
                kitsunefriend = ki4.getAllContactIds()
                ki4.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki4.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki4.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend5':
                kitsunefriend = ki5.getAllContactIds()
                ki5.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki5.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki5.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend6':
                kitsunefriend = ki6.getAllContactIds()
                ki6.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki6.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki6.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend7':
                kitsunefriend = ki7.getAllContactIds()
                ki7.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki7.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki7.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend8':
                kitsunefriend = ki8.getAllContactIds()
                ki8.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki8.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki8.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend9':
                kitsunefriend = ki9.getAllContactIds()
                ki9.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki9.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki9.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend10':
                kitsunefriend = ki10.getAllContactIds()
                ki10.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki10.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki10.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend11':
                kitsunefriend = ki11.getAllContactIds()
                ki11.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki11.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki11.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend12':
                kitsunefriend = ki12.getAllContactIds()
                ki12.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki12.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki12.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend13':
                kitsunefriend = ki13.getAllContactIds()
                ki13.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki13.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki13.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend14':
                kitsunefriend = ki14.getAllContactIds()
                ki14.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki14.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki14.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend15':
                kitsunefriend = ki15.getAllContactIds()
                ki15.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki15.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki15.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend16':
                kitsunefriend = ki16.getAllContactIds()
                ki16.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki16.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki16.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend17':
                kitsunefriend = ki17.getAllContactIds()
                ki17.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki17.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki17.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend18':
                kitsunefriend = ki18.getAllContactIds()
                ki18.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki18.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki18.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend20':
                kitsunefriend = ki20.getAllContactIds()
                ki20.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki20.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki20.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend21':
                kitsunefriend = ki21.getAllContactIds()
                ki21.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki21.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki21.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend22':
                kitsunefriend = ki22.getAllContactIds()
                ki22.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki22.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki22.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend23':
                kitsunefriend = ki23.getAllContactIds()
                ki23.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki23.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki23.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend24':
                kitsunefriend = ki24.getAllContactIds()
                ki24.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki24.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki24.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend25':
                kitsunefriend = ki25.getAllContactIds()
                ki25.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki25.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki25.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend26':
                kitsunefriend = ki26.getAllContactIds()
                ki26.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki26.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki26.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend27':
                kitsunefriend = ki27.getAllContactIds()
                ki27.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki27.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki27.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend28':
                kitsunefriend = ki28.getAllContactIds()
                ki28.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki28.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki28.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend29':
                kitsunefriend = ki29.getAllContactIds()
                ki29.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki29.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki29.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend30':
                kitsunefriend = ki30.getAllContactIds()
                ki30.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki30.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki30.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend31':
                kitsunefriend = ki31.getAllContactIds()
                ki31.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki31.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki31.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend33':
                kitsunefriend = ki33.getAllContactIds()
                ki33.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki33.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki33.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend33':
                kitsunefriend = ki33.getAllContactIds()
                ki33.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki33.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki33.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend34':
                kitsunefriend = ki34.getAllContactIds()
                ki34.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki34.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki34.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend38':
                kitsunefriend = ki38.getAllContactIds()
                ki38.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki38.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki38.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend39':
                kitsunefriend = ki39.getAllContactIds()
                ki39.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki39.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki39.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend42':
                kitsunefriend = ki42.getAllContactIds()
                ki42.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki42.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki42.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend41':
                kitsunefriend = ki41.getAllContactIds()
                ki41.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki41.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki41.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend35':
                kitsunefriend = ki35.getAllContactIds()
                ki35.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki35.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki35.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend36':
                kitsunefriend = ki36.getAllContactIds()
                ki36.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki36.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki36.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'friend37':
                kitsunefriend = ki37.getAllContactIds()
                ki37.kitsuneText(kitsune, "Please wait...")
                kontakkitsune = ki37.getContacts(kitsunefriend)
                num=1
                msgs="「User Friend List」"
                for ids in kontakkitsune:
                    msgs+="\n%i. %s" % (num, ids.kitsuneName)
                    num=(num+1)
                msgs+="\n「☼ Total %i Teman ☼」 " % len(kontakkitsune)
                ki37.kitsuneText(kitsune, msgs)
            elif msg.text.lower() == 'o11':
                gid = ki11.getGroupIdsJoined()
                for i in gid:
                    ki11.leaveGroup(i)
            elif msg.text.lower() == 'o12':
                gid = ki12.getGroupIdsJoined()
                for i in gid:
                    ki12.leaveGroup(i)
            elif msg.text.lower() == 'o13':
                gid = ki13.getGroupIdsJoined()
                for i in gid:
                    ki13.leaveGroup(i)
            elif msg.text.lower() == 'o14':
                gid = ki14.getGroupIdsJoined()
                for i in gid:	
                    ki14.leaveGroup(i)
            elif msg.text.lower() == 'o21':
                gid = ki21.getGroupIdsJoined()
                for i in gid:
                    ki21.leaveGroup(i)
            elif msg.text.lower() == 'o22':
                gid = ki22.getGroupIdsJoined()
                for i in gid:
                    ki22.leaveGroup(i)
            elif msg.text.lower() == 'o23':
                gid = ki23.getGroupIdsJoined()
                for i in gid:
                    ki23.leaveGroup(i)
            elif msg.text.lower() == 'o24':
                gid = ki24.getGroupIdsJoined()
                for i in gid:	
                    ki24.leaveGroup(i)
            elif msg.text.lower() == 'o15':
                gid = ki15.getGroupIdsJoined()
                for i in gid:
                    ki15.leaveGroup(i)
            elif msg.text.lower() == 'o16':
                gid = ki16.getGroupIdsJoined()
                for i in gid:
                    ki16.leaveGroup(i)
            elif msg.text.lower() == 'o17':
                gid = ki17.getGroupIdsJoined()
                for i in gid:
                    ki17.leaveGroup(i)
            elif msg.text.lower() == 'o18':
                gid = ki18.getGroupIdsJoined()
                for i in gid:
                    ki18.leaveGroup(i)
            elif msg.text.lower() == 'o19':
                gid = ki19.getGroupIdsJoined()
                for i in gid:
                    ki19.leaveGroup(i)
            elif msg.text.lower() == 'o1':
                gid = ki1.getGroupIdsJoined()
                for i in gid:
                    ki1.leaveGroup(i)
            elif msg.text.lower() == 'o2':
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                    ki2.leaveGroup(i)
            elif msg.text.lower() == 'o3':
                gid = ki3.getGroupIdsJoined()
                for i in gid:
                    ki3.leaveGroup(i)
            elif msg.text.lower() == 'o4':
                gid = ki4.getGroupIdsJoined()
                for i in gid:
                    ki4.leaveGroup(i)
            elif msg.text.lower() == 'o5':
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki5.leaveGroup(i)
            elif msg.text.lower() == 'o6':
                gid = ki6.getGroupIdsJoined()
                for i in gid:
                    ki6.leaveGroup(i)
            elif msg.text.lower() == 'o33':
                gid = ki33.getGroupIdsJoined()
                for i in gid:
                    ki33.leaveGroup(i)
            elif msg.text.lower() == 'o34':
                gid = ki34.getGroupIdsJoined()
                for i in gid:
                    ki34.leaveGroup(i)
            elif msg.text.lower() == 'o40':
                gid = ki40.getGroupIdsJoined()
                for i in gid:
                    ki40.leaveGroup(i)
            elif msg.text.lower() == 'o41':
                gid = ki41.getGroupIdsJoined()
                for i in gid:
                    ki41.leaveGroup(i)
            elif msg.text.lower() == 'o42':
                gid = ki42.getGroupIdsJoined()
                for i in gid:
                    ki42.leaveGroup(i)
            elif msg.text.lower() == 'o39':
                gid = ki39.getGroupIdsJoined()
                for i in gid:
                    ki39.leaveGroup(i)
            elif msg.text.lower() == 'o38':
                gid = ki38.getGroupIdsJoined()
                for i in gid:
                    ki38.leaveGroup(i)
            elif msg.text.lower() == 'o35':
                gid = ki35.getGroupIdsJoined()
                for i in gid:
                    ki35.leaveGroup(i)
            elif msg.text.lower() == 'o36':
                gid = ki36.getGroupIdsJoined()
                for i in gid:
                    ki36.leaveGroup(i)
            elif msg.text.lower() == 'o37':
                gid = ki37.getGroupIdsJoined()
                for i in gid:
                    ki37.leaveGroup(i)
            elif msg.text.lower() == 'o38':
                gid = ki38.getGroupIdsJoined()
                for i in gid:
                    ki38.leaveGroup(i)
            elif msg.text.lower() == 'o39':
                gid = ki39.getGroupIdsJoined()
                for i in gid:
                    ki39.leaveGroup(i)
            elif msg.text.lower() == 'o7':
                gid = ki7.getGroupIdsJoined()
                for i in gid:
                    ki7.leaveGroup(i)
            elif msg.text.lower() == 'o8':
                gid = ki8.getGroupIdsJoined()
                for i in gid:
                    ki8.leaveGroup(i)
            elif msg.text.lower() == 'o9':
                gid = ki9.getGroupIdsJoined()
                for i in gid:
                    ki9.leaveGroup(i)
            elif msg.text.lower() == 'o25':
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki5.leaveGroup(i)
            elif msg.text.lower() == 'o26':
                gid = ki6.getGroupIdsJoined()
                for i in gid:
                    ki6.leaveGroup(i)
            elif msg.text.lower() == 'o27':
                gid = ki27.getGroupIdsJoined()
                for i in gid:
                    ki27.leaveGroup(i)
            elif msg.text.lower() == 'o28':
                gid = ki28.getGroupIdsJoined()
                for i in gid:
                    ki28.leaveGroup(i)
            elif msg.text.lower() == 'o29':
                gid = ki9.getGroupIdsJoined()
                for i in gid:
                    ki9.leaveGroup(i)
            elif msg.text.lower() == 'o10':
                gid = ki10.getGroupIdsJoined()
                for i in gid:
                    ki10.leaveGroup(i)
            elif msg.text.lower() == 'o30':
                gid = ki30.getGroupIdsJoined()
                for i in gid:
                    ki30.leaveGroup(i)
            elif msg.text.lower() == 'o31':
                gid = ki31.getGroupIdsJoined()
                for i in gid:
                    ki31.leaveGroup(i)
            elif msg.text.lower() == 'o32':
                gid = ki32.getGroupIdsJoined()
                for i in gid:
                    ki32.leaveGroup(i)
            elif msg.text.lower() == 'gcancel1':
                gid = ki1.getGroupIdsInvited()
                for i in gid:
                    ki1.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki1.sendMessage(cd)
            elif msg.text.lower() == 'gcancel2':
                gid = ki2.getGroupIdsInvited()
                for i in gid:
                    ki2.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki2.sendMessage(cd)
            elif msg.text.lower() == 'gcancel3':
                gid = ki3.getGroupIdsInvited()
                for i in gid:
                    ki3.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki3.sendMessage(cd)
            elif msg.text.lower() == 'gcancel4':
                gid = ki4.getGroupIdsInvited()
                for i in gid:
                    ki4.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki4.sendMessage(cd)
            elif msg.text.lower() == 'gcancel5':
                gid = ki5.getGroupIdsInvited()
                for i in gid:
                    ki5.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki5.sendMessage(cd)
            elif msg.text.lower() == 'gcancel6':
                gid = ki6.getGroupIdsInvited()
                for i in gid:
                    ki6.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki6.sendMessage(cd)
            elif msg.text.lower() == 'gcancel7':
                gid = ki7.getGroupIdsInvited()
                for i in gid:
                    ki7.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki7.sendMessage(cd)
            elif msg.text.lower() == 'gcancel8':
                gid = ki8.getGroupIdsInvited()
                for i in gid:
                    ki8.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki8.sendMessage(cd)
            elif msg.text.lower() == 'gcancel9':
                gid = ki9.getGroupIdsInvited()
                for i in gid:
                    ki9.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki9.sendMessage(cd)
            elif msg.text.lower() == 'gcancel10':
                gid = ki10.getGroupIdsInvited()
                for i in gid:
                    ki10.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki10.sendMessage(cd)
            elif msg.text.lower() == 'gcancel11':
                gid = ki11.getGroupIdsInvited()
                for i in gid:
                    ki11.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki11.sendMessage(cd)
            elif msg.text.lower() == 'gcancel12':
                gid = ki12.getGroupIdsInvited()
                for i in gid:
                    ki12.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki12.sendMessage(cd)
            elif msg.text.lower() == 'gcancel13':
                gid = ki13.getGroupIdsInvited()
                for i in gid:
                    ki13.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki13.sendMessage(cd)
            elif msg.text.lower() == 'gcancel14':
                gid = ki14.getGroupIdsInvited()
                for i in gid:
                    ki14.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki14.sendMessage(cd)
            elif msg.text.lower() == 'gcancel15':
                gid = ki15.getGroupIdsInvited()
                for i in gid:
                    ki15.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki15.sendMessage(cd)
            elif msg.text.lower() == 'gcancel16':
                gid = ki16.getGroupIdsInvited()
                for i in gid:
                    ki16.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki16.sendMessage(cd)
            elif msg.text.lower() == 'gcancel17':
                gid = ki17.getGroupIdsInvited()
                for i in gid:
                    ki17.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki17.sendMessage(cd)
            elif msg.text.lower() == 'gcancel18':
                gid = ki18.getGroupIdsInvited()
                for i in gid:
                    ki18.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki18.sendMessage(cd)
            elif msg.text.lower() == 'gcancel19':
                gid = ki19.getGroupIdsInvited()
                for i in gid:
                    ki19.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki19.sendMessage(cd)
            elif msg.text.lower() == 'gcancel20':
                gid = ki20.getGroupIdsInvited()
                for i in gid:
                    ki20.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki20.sendMessage(cd)
            elif msg.text.lower() == 'gcancel22':
                gid = ki22.getGroupIdsInvited()
                for i in gid:
                    ki22.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki22.sendMessage(cd)
            elif msg.text.lower() == 'gcancel22':
                gid = ki22.getGroupIdsInvited()
                for i in gid:
                    ki22.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki22.sendMessage(cd)
            elif msg.text.lower() == 'gcancel23':
                gid = ki23.getGroupIdsInvited()
                for i in gid:
                    ki23.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki23.sendMessage(cd)
            elif msg.text.lower() == 'gcancel24':
                gid = ki24.getGroupIdsInvited()
                for i in gid:
                    ki24.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki24.sendMessage(cd)
            elif msg.text.lower() == 'gcancel25':
                gid = ki25.getGroupIdsInvited()
                for i in gid:
                    ki25.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki25.sendMessage(cd)
            elif msg.text.lower() == 'gcancel26':
                gid = ki26.getGroupIdsInvited()
                for i in gid:
                    ki26.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki26.sendMessage(cd)
            elif msg.text.lower() == 'gcancel27':
                gid = ki27.getGroupIdsInvited()
                for i in gid:
                    ki27.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki27.sendMessage(cd)
            elif msg.text.lower() == 'gcancel28':
                gid = ki28.getGroupIdsInvited()
                for i in gid:
                    ki28.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki28.sendMessage(cd)
            elif msg.text.lower() == 'gcancel29':
                gid = ki29.getGroupIdsInvited()
                for i in gid:
                    ki29.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki29.sendMessage(cd)
            elif msg.text.lower() == 'gcancel30':
                gid = ki30.getGroupIdsInvited()
                for i in gid:
                    ki30.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki30.sendMessage(cd)
            elif msg.text.lower() == 'gcancel33':
                gid = ki33.getGroupIdsInvited()
                for i in gid:
                    ki33.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki33.sendMessage(cd)
            elif msg.text.lower() == 'gcancel33':
                gid = ki33.getGroupIdsInvited()
                for i in gid:
                    ki33.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki33.sendMessage(cd)
            elif msg.text.lower() == 'gcancel33':
                gid = ki33.getGroupIdsInvited()
                for i in gid:
                    ki33.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki33.sendMessage(cd)
            elif msg.text.lower() == 'gcancel34':
                gid = ki34.getGroupIdsInvited()
                for i in gid:
                    ki34.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki34.sendMessage(cd)
            elif msg.text.lower() == 'gcancel38':
                gid = ki38.getGroupIdsInvited()
                for i in gid:
                    ki38.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki38.sendMessage(cd)
            elif msg.text.lower() == 'gcancel39':
                gid = ki39.getGroupIdsInvited()
                for i in gid:
                    ki39.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki39.sendMessage(cd)
            elif msg.text.lower() == 'gcancel40':
                gid = ki40.getGroupIdsInvited()
                for i in gid:
                    ki40.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki40.sendMessage(cd)
            elif msg.text.lower() == 'gcancel35':
                gid = ki35.getGroupIdsInvited()
                for i in gid:
                    ki35.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki35.sendMessage(cd)
            elif msg.text.lower() == 'gcancel36':
                gid = ki36.getGroupIdsInvited()
                for i in gid:
                    ki36.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki36.sendMessage(cd)
            elif msg.text.lower() == 'gcancel37':
                gid = ki37.getGroupIdsInvited()
                for i in gid:
                    ki37.rejectGroupInvitation(i)
                cd = Message()
                cd.to = msg.to
                cd.text = "Reject %i Invitation" % len(gid)
                ki37.sendMessage(cd)
            elif msg.text.lower() == 'cium1':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(ki1mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium1(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium1(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium1(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium1(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium1(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium1(kitsune, nm5)
            elif msg.text.lower() == 'cium2':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(ki2mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium2(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium2(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium2(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium2(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium2(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium2(kitsune, nm5)
            elif msg.text.lower() == 'cium3':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(ki3mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium3(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium3(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium3(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium3(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium3(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium3(kitsune, nm5)
            elif msg.text.lower() == 'cium4':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(ki4mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium4(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium4(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium4(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium4(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium4(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium4(kitsune, nm5)
            elif msg.text.lower() == 'cium5':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(ki5mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium5(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium5(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium5(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium5(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium5(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium5(kitsune, nm5)
            elif msg.text.lower() == 'cium6':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(ki6mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium6(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium6(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium6(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium6(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium6(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium6(kitsune, nm5)
            elif msg.text.lower() == 'cium7':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nama.remove(ki7mid)
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium7(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium7(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium7(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium7(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium7(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium7(kitsune, nm5)
            elif msg.text.lower() == 'cium8':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium8(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium8(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium8(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium8(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium8(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium8(kitsune, nm5)
            elif msg.text.lower() == 'cium9':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium9(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium9(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium9(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium9(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium9(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium9(kitsune, nm5)
            elif msg.text.lower() == 'cium10':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium10(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium10(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium10(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium10(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium10(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium10(kitsune, nm5)
            elif msg.text.lower() == 'cium11':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium11(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium11(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium11(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium11(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium11(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium11(kitsune, nm5)
            elif msg.text.lower() == 'cium12':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium12(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium12(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium12(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium12(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium12(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium12(kitsune, nm5)
            elif msg.text.lower() == 'cium13':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium13(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium13(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium13(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium13(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium13(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium13(kitsune, nm5)
            elif msg.text.lower() == 'cium14':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium14(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium14(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium14(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium14(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium14(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium14(kitsune, nm5)
            elif msg.text.lower() == 'cium15':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium15(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium15(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium15(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium15(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium15(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium15(kitsune, nm5)
            elif msg.text.lower() == 'cium16':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium16(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium16(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium16(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium16(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium16(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium16(kitsune, nm5)
            elif msg.text.lower() == 'cium17':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium17(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium17(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium17(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium17(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium17(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium17(kitsune, nm5)
            elif msg.text.lower() == 'cium18':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium18(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium18(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium18(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium18(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium18(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium18(kitsune, nm5)
            elif msg.text.lower() == 'cium20':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium20(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium20(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium20(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium20(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium20(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium20(kitsune, nm5)
            elif msg.text.lower() == 'cium21':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium21(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium21(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium21(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium21(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium21(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium21(kitsune, nm5)
            elif msg.text.lower() == 'cium22':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium22(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium22(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium22(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium22(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium22(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium22(kitsune, nm5)
            elif msg.text.lower() == 'cium23':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium23(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium23(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium23(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium23(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium23(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium23(kitsune, nm5)
            elif msg.text.lower() == 'cium24':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium24(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium24(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium24(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium24(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium24(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium24(kitsune, nm5)
            elif msg.text.lower() == 'cium25':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium25(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium25(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium25(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium25(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium25(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium25(kitsune, nm5)
            elif msg.text.lower() == 'cium26':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium26(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium26(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium26(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium26(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium26(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium26(kitsune, nm5)
            elif msg.text.lower() == 'cium27':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium27(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium27(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium27(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium27(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium27(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium27(kitsune, nm5)
            elif msg.text.lower() == 'cium28':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium28(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium28(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium28(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium28(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium28(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium28(kitsune, nm5)
            elif msg.text.lower() == 'cium29':
             group = ki.getGroup(kitsune)
             nama = [contact.mid for contact in group.kitsunemembers]
             nm1, nm2, nm3, nm4,  nm5, jml = [], [], [], [],  [], len(nama)
             if jml <= 150:
                cium29(kitsune, nama)
             if jml > 150 and jml < 500:
                for i in range(0, 150):
                      nm1 += [nama[i]]
                cium29(kitsune, nm1)
                for j in range(149, len(nama)-1):
                       nm2 += [nama[j]]
                cium29(kitsune, nm2)
                for k in range(298, len(nama)-2):
                       nm3 += [nama[k]]
                cium29(kitsune, nm3)
                for l in range(447, len(nama)-3):
                       nm4 += [nama[l]]
                cium29(kitsune, nm4)
                for m in range(500, len(nama)-4):
                       nm5 += [nama[m]]
                cium29(kitsune, nm5)
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki1.kitsuneText(kitsune,(bctxt))
				ki2.kitsuneText(kitsune,(bctxt))
				ki3.kitsuneText(kitsune,(bctxt))
				ki4.kitsuneText(kitsune,(bctxt))
				ki5.kitsuneText(kitsune,(bctxt))
				ki6.kitsuneText(kitsune,(bctxt))
				ki7.kitsuneText(kitsune,(bctxt))
				ki8.kitsuneText(kitsune,(bctxt))
				ki9.kitsuneText(kitsune,(bctxt))
				ki10.kitsuneText(kitsune,(bctxt))
				ki11.kitsuneText(kitsune,(bctxt))
				ki12.kitsuneText(kitsune,(bctxt))
				ki13.kitsuneText(kitsune,(bctxt))
				ki14.kitsuneText(kitsune,(bctxt))
				ki15.kitsuneText(kitsune,(bctxt))
				ki16.kitsuneText(kitsune,(bctxt))
				ki17.kitsuneText(kitsune,(bctxt))
				ki18.kitsuneText(kitsune,(bctxt))
				ki20.kitsuneText(kitsune,(bctxt))
				ki21.kitsuneText(kitsune,(bctxt))
				ki22.kitsuneText(kitsune,(bctxt))
				ki23.kitsuneText(kitsune,(bctxt))
				ki24.kitsuneText(kitsune,(bctxt))
				ki25.kitsuneText(kitsune,(bctxt))
				ki26.kitsuneText(kitsune,(bctxt))
				ki27.kitsuneText(kitsune,(bctxt))
				ki28.kitsuneText(kitsune,(bctxt))
				ki29.kitsuneText(kitsune,(bctxt))
				ki30.kitsuneText(kitsune,(bctxt))
				ki33.kitsuneText(kitsune,(bctxt))
				ki32.kitsuneText(kitsune,(bctxt))
				ki33.kitsuneText(kitsune,(bctxt))
				ki34.kitsuneText(kitsune,(bctxt))
				ki35.kitsuneText(kitsune,(bctxt))
				ki36.kitsuneText(kitsune,(bctxt))
				ki37.kitsuneText(kitsune,(bctxt))
				ki38.kitsuneText(kitsune,(bctxt))
				ki39.kitsuneText(kitsune,(bctxt))
				ki40.kitsuneText(kitsune,(bctxt))
				ki41.kitsuneText(kitsune,(bctxt))
				ki42.kitsuneText(kitsune,(bctxt))
            elif msg.text.lower() == '1':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki1.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki1.updateGroup(G)
            elif msg.text.lower() == '2':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki2.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki2.updateGroup(G)
            elif msg.text.lower() == '3':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki3.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki3.updateGroup(G)
            elif msg.text.lower() == '4':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki4.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki4.updateGroup(G)
            elif msg.text.lower() == '5':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki5.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki5.updateGroup(G)
            elif msg.text.lower() == '6':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki6.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki6.updateGroup(G)
            elif msg.text.lower() == '7':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki7.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki7.updateGroup(G)
            elif msg.text.lower() == '8':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki8.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki8.updateGroup(G)
            elif msg.text.lower() == '9':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki9.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki9.updateGroup(G)
            elif msg.text.lower() == '11':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki11.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki11.updateGroup(G)
            elif msg.text.lower() == '12':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki12.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki12.updateGroup(G)
            elif msg.text.lower() == '13':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki13.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki13.updateGroup(G)
            elif msg.text.lower() == '14':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki14.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki14.updateGroup(G)
            elif msg.text.lower() == '15':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki15.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki15.updateGroup(G)
            elif msg.text.lower() == '16':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki16.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki16.updateGroup(G)
            elif msg.text.lower() == '17':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki17.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki17.updateGroup(G)
            elif msg.text.lower() == '18':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki18.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki18.updateGroup(G)
            elif msg.text.lower() == '19':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki19.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki19.updateGroup(G)
            elif msg.text.lower() == '10':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki10.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki10.updateGroup(G)
            elif msg.text.lower() == '20':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki20.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                        print "ki1cker ok"
                        G.kitsuneTicket(G)
                        ki20.updateGroup(G)
            elif msg.text.lower() == '21':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki21.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki21.updateGroup(G)
            elif msg.text.lower() == '22':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki22.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki22.updateGroup(G)
            elif msg.text.lower() == '23':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki23.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki23.updateGroup(G)
            elif msg.text.lower() == '24':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki24.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki24.updateGroup(G)
            elif msg.text.lower() == '25':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki25.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki25.updateGroup(G)
            elif msg.text.lower() == '26':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki26.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki26.updateGroup(G)
            elif msg.text.lower() == '27':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki27.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki27.updateGroup(G)
            elif msg.text.lower() == '28':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki28.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki28.updateGroup(G)
            elif msg.text.lower() == '30':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki30.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki30.updateGroup(G)
            elif msg.text.lower() == '29':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki29.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki29.updateGroup(G)
            elif msg.text.lower() == '31':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki31.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki31.updateGroup(G)
            elif msg.text.lower() == '32':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki32.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki32.updateGroup(G)
            elif msg.text.lower() == '33':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki33.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki33.updateGroup(G)
            elif msg.text.lower() == '34':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki34.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki34.updateGroup(G)
            elif msg.text.lower() == '35':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki35.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki35.updateGroup(G)
            elif msg.text.lower() == '36':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki36.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki36.updateGroup(G)
            elif msg.text.lower() == '37':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki37.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki37.updateGroup(G)
            elif msg.text.lower() == '38':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki38.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki38.updateGroup(G)
            elif msg.text.lower() == '39':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki39.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki39.updateGroup(G)
            elif msg.text.lower() == '41':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki41.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki41.updateGroup(G)
            elif msg.text.lower() == '42':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki42.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki42.updateGroup(G)
            elif msg.text.lower() == '40':
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(kitsune)
                        ki40.acceptGroupInvitationByTicket(kitsune,Ticket)
                        G = ki.getGroup(kitsune)
                        ginfo = ki.getGroup(kitsune)
                        G.kitsuneTicket = True
                        ki40.updateGroup(G)
            elif msg.text.lower() == 'k1 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki1.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k2 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki2.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k3 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki3.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k4 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki4.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k5 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki5.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k6 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki6.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k7 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki7.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k8 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki8.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k9 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki9.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k20 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki20.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k21 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki21.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k22 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki22.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k23 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki23.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k24 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki24.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k25 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki25.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k26 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki26.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k27 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki27.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k28 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki28.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k29 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki29.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k10 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki10.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k11 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki11.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k12 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki12.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k13 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki13.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k14 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki14.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k15 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki15.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k16 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki16.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k17 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki17.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k18 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki18.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k30 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki30.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k33 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki33.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k32 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki32.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k33 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki33.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k34 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki34.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k35 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki35.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k36 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki36.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k37 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki37.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k38 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki38.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k39 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki39.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k40 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki40.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k41 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki41.leaveGroup(kitsune)
                    except:
                        pass
            elif msg.text.lower() == 'k42 bye':
                if msg.toType == 2:
                    ginfo = ki.getGroup(kitsune)
                    try:
                        ki42.leaveGroup(kitsune)
                    except:
                        pass
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki1.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki1.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki1.updateGroup(G)
                        Ticket = ki1.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki1.updateGroup(G)
                    except:
                        try:
                            G = ki2.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki2.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki2.updateGroup(G)
                            Ticket = ki2.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki2.updateGroup(G)
                        except:
                            try:
                                G = ki3.getGroup(op.param1)
                                wait["blacklist"][op.param2] = True
                                f=codecs.open('blacklist.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki3.kickoutFromGroup(op.param1,[op.param2])
                                G.kitsuneTicket = False
                                ki3.updateGroup(G)
                                Ticket = ki3.reissueGroupTicket(op.param1)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G.kitsuneTicket = True
                                ki3.updateGroup(G)
                            except:
                                pass
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki1mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki2.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki2.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki2.updateGroup(G)
                    except:
                        try:
                            G = ki3.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki3.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki3.updateGroup(G)
                            Ticket = ki3.reissueGroupTicket(op.param1)
                            ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki3.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki2mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki3.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki3.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki3.updateGroup(G)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        except:
                            G = ki4.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki4.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki4.updateGroup(G)
                            Ticket = ki4.reissueGroupTicket(op.param1)
                            ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki4.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki3mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki4.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki4.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki4.updateGroup(G)
                    except:
                        try:
                            G = ki5.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki5.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki5.reissueGroupTicket(op.param1)
                            ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki5.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki4mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki5.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki5.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki5.updateGroup(G)
                    except:
                        try:
                            G = ki6.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki6.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki6.updateGroup(G)
                            Ticket = ki6.reissueGroupTicket(op.param1)
                            ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki6.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki5mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki6.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki6.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki6.updateGroup(G)
                    except:
                        try:
                            G = ki7.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki7.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki7.updateGroup(G)
                            Ticket = ki7.reissueGroupTicket(op.param1)
                            ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki7.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki6mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki7.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki7.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki7.updateGroup(G)
                    except:
                        try:
                            G = ki8.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki8.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki8.updateGroup(G)
                            Ticket = ki8.reissueGroupTicket(op.param1)
                            ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki8.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki7mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki8.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki8.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki8.updateGroup(G)
                    except:
                        try:
                            G = ki9.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki9.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki9.updateGroup(G)
                            Ticket = ki9.reissueGroupTicket(op.param1)
                            ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki9.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki8mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki9.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki9.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki9.updateGroup(G)
                    except:
                        try:
                            G = ki10.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki10.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki10.updateGroup(G)
                            Ticket = ki10.reissueGroupTicket(op.param1)
                            ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki10.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki9mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki10.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki10.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki10.updateGroup(G)
                    except:
                        try:
                            G = ki11.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki11.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki11.updateGroup(G)
                            Ticket = ki11.reissueGroupTicket(op.param1)
                            ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki11.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki10mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki11.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki11.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki11.updateGroup(G)
                    except:
                        try:
                            G = ki12.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki12.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki12.updateGroup(G)
                            Ticket = ki12.reissueGroupTicket(op.param1)
                            ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki12.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki11mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki12.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki12.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki12.updateGroup(G)
                    except:
                        try:
                            G = ki13.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki13.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki13.updateGroup(G)
                            Ticket = ki13.reissueGroupTicket(op.param1)
                            ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki13.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki12mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki13.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki13.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki13.updateGroup(G)
                    except:
                        try:
                            G = ki14.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki14.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki14.updateGroup(G)
                            Ticket = ki14.reissueGroupTicket(op.param1)
                            ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki14.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki13mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki14.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki14.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki14.updateGroup(G)
                    except:
                        try:
                            G = ki15.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki15.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki15.updateGroup(G)
                            Ticket = ki15.reissueGroupTicket(op.param1)
                            ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki15.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki14mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki15.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki15.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki15.updateGroup(G)
                    except:
                        try:
                            G = ki16.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki16.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki16.updateGroup(G)
                            Ticket = ki16.reissueGroupTicket(op.param1)
                            ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki16.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki15mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki16.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki16.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki16.updateGroup(G)
                        Ticket = ki16.reissueGroupTicket(op.param1)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki16.updateGroup(G)
                    except:
                        try:
                            G = ki17.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki17.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki17.updateGroup(G)
                            Ticket = ki17.reissueGroupTicket(op.param1)
                            ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki17.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki16mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki17.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki17.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki17.updateGroup(G)
                        Ticket = ki17.reissueGroupTicket(op.param1)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki17.updateGroup(G)
                    except:
                        try:
                            G = ki18.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki18.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki18.reissueGroupTicket(op.param1)
                            ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki18.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki17mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki18.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki18.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki18.updateGroup(G)
                        Ticket = ki18.reissueGroupTicket(op.param1)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki18.updateGroup(G)
                    except:
                        try:
                            G = ki20.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki20.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki20.updateGroup(G)
                            Ticket = ki20.reissueGroupTicket(op.param1)
                            ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki20.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki18mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki20.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki20.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki20.updateGroup(G)
                        Ticket = ki20.reissueGroupTicket(op.param1)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki20.updateGroup(G)
                    except:
                        try:
                            G = ki21.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki21.updateGroup(G)
                            Ticket = ki21.reissueGroupTicket(op.param1)
                            ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki21.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki20mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki21.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki21.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki21.updateGroup(G)
                        Ticket = ki21.reissueGroupTicket(op.param1)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki21.updateGroup(G)
                    except:
                        try:
                            G = ki22.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki22.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki22.updateGroup(G)
                            Ticket = ki22.reissueGroupTicket(op.param1)
                            ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki22.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki21mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki22.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki22.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki22.updateGroup(G)
                        Ticket = ki22.reissueGroupTicket(op.param1)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki22.updateGroup(G)
                    except:
                        try:
                            G = ki23.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki23.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki23.reissueGroupTicket(op.param1)
                            ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki23.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki22mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki23.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki23.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki23.updateGroup(G)
                        Ticket = ki23.reissueGroupTicket(op.param1)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki23.updateGroup(G)
                    except:
                        try:
                            G = ki24.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki24.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki24.updateGroup(G)
                            Ticket = ki24.reissueGroupTicket(op.param1)
                            ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki24.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki23mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki24.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki24.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki24.updateGroup(G)
                        Ticket = ki24.reissueGroupTicket(op.param1)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki24.updateGroup(G)
                    except:
                        try:
                            G = ki25.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki25.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki25.updateGroup(G)
                            Ticket = ki25.reissueGroupTicket(op.param1)
                            ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki25.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki24mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki25.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki25.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki25.updateGroup(G)
                        Ticket = ki25.reissueGroupTicket(op.param1)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki25.updateGroup(G)
                    except:
                        try:
                            G = ki26.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki26.updateGroup(G)
                            Ticket = ki26.reissueGroupTicket(op.param1)
                            ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki26.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki25mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki26.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki26.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki26.updateGroup(G)
                        Ticket = ki26.reissueGroupTicket(op.param1)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki26.updateGroup(G)
                    except:
                        try:
                            G = ki27.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki27.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki27.updateGroup(G)
                            Ticket = ki27.reissueGroupTicket(op.param1)
                            ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki27.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki26mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki27.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki27.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki27.updateGroup(G)
                        Ticket = ki27.reissueGroupTicket(op.param1)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki27.updateGroup(G)
                    except:
                        try:
                            G = ki28.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki28.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki28.updateGroup(G)
                            Ticket = ki28.reissueGroupTicket(op.param1)
                            ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki28.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki27mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki28.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki28.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki28.updateGroup(G)
                        Ticket = ki28.reissueGroupTicket(op.param1)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki28.updateGroup(G)
                    except:
                        try:
                            G = ki29.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki29.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki29.updateGroup(G)
                            Ticket = ki29.reissueGroupTicket(op.param1)
                            ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki29.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki28mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki29.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki29.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki29.updateGroup(G)
                        Ticket = ki29.reissueGroupTicket(op.param1)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki29.updateGroup(G)
                    except:
                        try:
                            G = ki30.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki30.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki30.updateGroup(G)
                            Ticket = ki30.reissueGroupTicket(op.param1)
                            ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki30.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki29mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki30.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki30.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki30.updateGroup(G)
                        Ticket = ki30.reissueGroupTicket(op.param1)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki30.updateGroup(G)
                    except:
                        try:
                            G = ki31.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki31.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki31.updateGroup(G)
                            Ticket = ki31.reissueGroupTicket(op.param1)
                            ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki31.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki30mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki31.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki31.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki31.updateGroup(G)
                        Ticket = ki31.reissueGroupTicket(op.param1)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki31.updateGroup(G)
                    except:
                        try:
                            G = ki32.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki32.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki32.updateGroup(G)
                            Ticket = ki32.reissueGroupTicket(op.param1)
                            ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki32.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki31mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki32.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki32.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki32.updateGroup(G)
                        Ticket = ki32.reissueGroupTicket(op.param1)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki32.updateGroup(G)
                    except:
                        try:
                            G = ki33.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki33.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki33.reissueGroupTicket(op.param1)
                            ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki33.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki32mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki33.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki33.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki33.updateGroup(G)
                        Ticket = ki33.reissueGroupTicket(op.param1)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki33.updateGroup(G)
                    except:
                        try:
                            G = ki34.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki34.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki34.updateGroup(G)
                            Ticket = ki34.reissueGroupTicket(op.param1)
                            ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki34.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki33mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki34.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki34.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki34.updateGroup(G)
                        Ticket = ki34.reissueGroupTicket(op.param1)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki34.updateGroup(G)
                    except:
                        try:
                            G = ki35.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki35.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki35.updateGroup(G)
                            Ticket = ki35.reissueGroupTicket(op.param1)
                            ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki35.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki34mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki35.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki35.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki35.updateGroup(G)
                        Ticket = ki35.reissueGroupTicket(op.param1)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki35.updateGroup(G)
                    except:
                        try:
                            G = ki36.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki36.updateGroup(G)
                            Ticket = ki36.reissueGroupTicket(op.param1)
                            ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki36.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki35mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki36.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki36.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki36.updateGroup(G)
                        Ticket = ki36.reissueGroupTicket(op.param1)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki36.updateGroup(G)
                    except:
                        try:
                            G = ki37.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki37.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki37.updateGroup(G)
                            Ticket = ki37.reissueGroupTicket(op.param1)
                            ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki37.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki36mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki37.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki37.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki37.updateGroup(G)
                        Ticket = ki37.reissueGroupTicket(op.param1)
                        ki36.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki37.updateGroup(G)
                    except:
                        try:
                            G = ki38.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki38.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki38.updateGroup(G)
                            Ticket = ki38.reissueGroupTicket(op.param1)
                            ki36.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki38.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki36.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki37mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki38.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki38.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki38.updateGroup(G)
                        Ticket = ki38.reissueGroupTicket(op.param1)
                        ki37.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki38.updateGroup(G)
                    except:
                        try:
                            G = ki39.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki39.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki39.updateGroup(G)
                            Ticket = ki39.reissueGroupTicket(op.param1)
                            ki37.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki39.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki37.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki38mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki39.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki39.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki30.updateGroup(G)
                        Ticket = ki30.reissueGroupTicket(op.param1)
                        ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki30.updateGroup(G)
                    except:
                        try:
                            G = ki40.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki40.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki40.updateGroup(G)
                            Ticket = ki40.reissueGroupTicket(op.param1)
                            ki38.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki40.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki38.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki39mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki40.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki40.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki40.updateGroup(G)
                        Ticket = ki40.reissueGroupTicket(op.param1)
                        ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki40.updateGroup(G)
                    except:
                        try:
                            G = ki41.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki41.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki41.updateGroup(G)
                            Ticket = ki41.reissueGroupTicket(op.param1)
                            ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki41.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki39.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki40mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki41.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki41.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki41.updateGroup(G)
                        Ticket = ki41.reissueGroupTicket(op.param1)
                        ki40.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki41.updateGroup(G)
                    except:
                        try:
                            G = ki42.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki42.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki42.updateGroup(G)
                            Ticket = ki42.reissueGroupTicket(op.param1)
                            ki40.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki42.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki40.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki41mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki42.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki42.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki42.updateGroup(G)
                        Ticket = ki42.reissueGroupTicket(op.param1)
                        ki41.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki42.updateGroup(G)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki1.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki1.updateGroup(G)
                            Ticket = ki1.reissueGroupTicket(op.param1)
                            ki41.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki1.updateGroup(G)
                        except:
                            G = ki.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki41.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki.updateGroup(G)
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if ki42mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        G = ki.getGroup(op.param1)
                        wait["blacklist"][op.param2] = True
                        f=codecs.open('blacklist.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        ki.kickoutFromGroup(op.param1,[op.param2])						
                        G.kitsuneTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ki42.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.kitsuneTicket = True
                        ki.updateGroup(G)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                            wait["blacklist"][op.param2] = True
                            f=codecs.open('blacklist.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki1.kickoutFromGroup(op.param1,[op.param2])						
                            G.kitsuneTicket = False
                            ki1.updateGroup(G)
                            Ticket = ki1.reissueGroupTicket(op.param1)
                            ki42.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G.kitsuneTicket = True
                            ki1.updateGroup(G)
                        except:
                            pass
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                if Bots in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            wait["blacklist"][op.param2] = True
                        except:
                            pass


            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if op.param1 in kitsuneprotection:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
			G = ki.getGroup(op.param1)
			G.kitsuneTicket = True
			random.choice(P1).updateGroup(G)
		   except:
			try:
			    random.choice(P2).kickoutFromGroup(op.param1,[op.param2])
			    G = ki.getGroup(op.param1)
			    G.kitsuneTicket = True
			    random.choice(P2).updateGroup(G)
			except:
			    ki.kickoutFromGroup(op.param1,[op.param2])
			    G = ki.getGroup(op.param1)
			    G.kitsuneTicket = True
			    ki.updateGroup(G)
			    pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if op.param1 in kitsunewelcome:
		if op.param2 not in Bots:
		   try:
		    ginfo = ki.getGroup(op.param1)
		    random.choice(P1).kitsuneImageWithURL(op.param1,mimic["pap"])
		    random.choice(P1).kitsuneText(op.param1,wait['message'].title())
		    random.choice(P1).kitsuneText(op.param1,"Group Creator " + str(ginfo.name) + " :\n" + ginfo.creator.kitsuneName )
		    msg = Message()
		    msg.to = op.param1
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': ginfo.creator.mid}
		    random.choice(P1).sendMessage(msg)
		   except:
			try:
			    ginfo = ki.getGroup(op.param1)
			    random.choice(P2).kitsuneImageWithURL(op.param1,mimic["pap"])
			    random.choice(P2).kitsuneText(op.param1,wait['message'].title())
			    random.choice(P2).kitsuneText(op.param1,"Group Creator " + str(ginfo.name) + " :\n" + ginfo.creator.kitsuneName )
			    msg = Message()
			    msg.to = op.param1
			    msg.contentType = 13
			    msg.contentMetadata = {'mid': ginfo.creator.mid}
			    random.choice(P2).sendMessage(msg)
			except:
			    ginfo = ki.getGroup(op.param1)
			    random.choice(P3).kitsuneImageWithURL(op.param1,mimic["pap"])
			    random.choice(P3).kitsuneText(op.param1,wait['message'].title())
			    random.choice(P3).kitsuneText(op.param1,"Group Creator " + str(ginfo.name) + " :\n" + ginfo.creator.kitsuneName )
			    msg = Message()
			    msg.to = op.param1
			    msg.contentType = 13
			    msg.contentMetadata = {'mid': ginfo.creator.mid}
			    random.choice(P3).sendMessage(msg)
			    pass
	    else:
		pass
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in kitsuneurl:
		   try:
		    wait ["blacklist"][op.param2] = True
		    f=codecs.open('blacklist.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.kitsuneTicket = True
		    random.choice(P2).updateGroup(G)
		    random.choice(P2).kickoutFromGroup(op.param1,[op.param2])
		   except:
		    wait ["blacklist"][op.param2] = True
		    f=codecs.open('blacklist.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.kitsuneTicket = True
		    ki.updateGroup(G)
		    random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in wait['pname']:
		   try:
		    wait["blacklist"][op.param2] = True
		    f=codecs.open('blacklist.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.name = wait['pro_name'][op.param1]
		    random.choice(P1).updateGroup(G)
		   except:
		    wait["blacklist"][op.param2] = True
		    f=codecs.open('blacklist.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    G = ki.getGroup(op.param1)
		    G.name = wait['pro_name'][op.param1]
		    ki.updateGroup(G)
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in kitsuneprotection:
		    wait ["blacklist"][op.param2] = True
		    random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
		else:
		    ki.kitsuneText(op.param1,"")
	    else:
		ki.kitsuneText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif op.param1 in kitsuneautoinvite:
		    wait ["blacklist"][op.param2] = True
		    f=codecs.open('blacklist.json','w','utf-8')
		    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		    random.choice(P1).kickoutFromGroup(op.param1,[op.param2])
            if op.param2 not in Bots:
       	        if op.param2 in Bots:
       	           pass
                elif op.param1 in autoCancel:
                   ki.cancelGroupInvitation(op.param1,[contact.mid for contact in ki.getGroup(op.param1).invitee])
        if op.type == 5:
            if wait["autoAdd"] == True:
                ki.findAndAddContactsByMid(op.param1)
                if (wait["autoaddpesan"] in [""," ","\n",None]):
                    pass
                else:
                    ki.kitsuneText(op.param1,str(wait["autoaddpesan"].title()))
            else:
                if (wait["autoaddpesan"] in [""," ","\n",None]):
                    pass
                else:
                    ki.kitsuneText(op.param1,str(wait["autoaddpesan"].title()))
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = ki.getContact(op.param2).kitsuneName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠・" + Name
                else:
                    ki.kitsuneText
            except:
                pass
#------------------------------------------------------------------------------------
        if op.type == 59:
            pass


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = ki.getProfile()
                profile.kitsuneName = wait["cName"] + nowT
                ki.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def mimictag(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    matched_list = []
    for tag in mimic["target"]:
        matched_list+=filter(lambda str: str == tag, nm)
    cocoa = ""
    for mm in matched_list:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention Mimic」 \n"+bb + "    「 Total: " + str(len(matched_list)) +  " Mimic List 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki.sendMessage(msg)
    except Exception as error:
       print error

def bltag(to, nama):
    aa = ""
    bb = ""
    strt = int(22)
    akh = int(22)
    nm = nama
    matched_list = []
    for tag in wait["blacklist"]:
        matched_list+=filter(lambda str: str == tag, nm)
    cocoa = ""
    for mm in matched_list:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention Blacklist」\n"+bb + "    「 Total: " + str(len(matched_list)) +  " Blacklist 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki.sendMessage(msg)
    except Exception as error:
       print error

def cium(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
       ki.sendMessage(msg)
    except Exception as error:
       print error

def cium1(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki1.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki1.sendMessage(msg)
    except Exception as error:
       print error

def cium2(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki2.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki2.sendMessage(msg)
    except Exception as error:
       print error

def cium3(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki3.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki3.sendMessage(msg)
    except Exception as error:
       print error

def cium4(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki4.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki4.sendMessage(msg)
    except Exception as error:
       print error

def cium5(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki5.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki5.sendMessage(msg)
    except Exception as error:
       print error

def cium6(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki6.sendMessage(msg)
    except Exception as error:
       print error

def cium7(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki7.sendMessage(msg)
    except Exception as error:
       print error

def cium8(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki8.sendMessage(msg)
    except Exception as error:
       print error

def cium9(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki9.sendMessage(msg)
    except Exception as error:
       print error

def cium10(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki10.sendMessage(msg)
    except Exception as error:
       print error

def cium11(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki11.sendMessage(msg)
    except Exception as error:
       print error

def cium12(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki12.sendMessage(msg)
    except Exception as error:
       print error

def cium13(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki13.sendMessage(msg)
    except Exception as error:
       print error

def cium14(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki14.sendMessage(msg)
    except Exception as error:
       print error

def cium15(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki15.sendMessage(msg)
    except Exception as error:
       print error

def cium16(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki16.sendMessage(msg)
    except Exception as error:
       print error

def cium17(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki17.sendMessage(msg)
    except Exception as error:
       print error

def cium18(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = bb + "「Mention By KITSUNE」\n"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki18.sendMessage(msg)
    except Exception as error:
       print error

def cium19(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki19.sendMessage(msg)
    except Exception as error:
       print error

def cium20(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki20.sendMessage(msg)
    except Exception as error:
       print error

def cium21(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki21.sendMessage(msg)
    except Exception as error:
       print error

def cium22(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki22.sendMessage(msg)
    except Exception as error:
       print error

def cium23(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki23.sendMessage(msg)
    except Exception as error:
       print error

def cium24(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki24.sendMessage(msg)
    except Exception as error:
       print error

def cium25(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki25.sendMessage(msg)
    except Exception as error:
       print error

def cium26(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki26.sendMessage(msg)
    except Exception as error:
       print error

def cium27(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki27.sendMessage(msg)
    except Exception as error:
       print error

def cium28(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki28.sendMessage(msg)
    except Exception as error:
       print error

def cium29(to, nama):
    aa = ""
    bb = ""
    strt = int(19)
    akh = int(19)
    nm = nama
    print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "・ @x \n"
    aa = (aa[:int(len(aa)-1)])
    profile = ki.getProfile()
    text = profile.kitsuneName
    msg = Message()
    msg.to = to
    msg.text = "「Mention All」   \n"+bb + "    「 Total: " + str(len(nm)) +  " Mention 」"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print msg
    try:
       ki29.sendMessage(msg)
    except Exception as error:
       print error

while True:
    try:
        Ops = ki.fetchOps(ki.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ki.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ki.Poll.rev = max(ki.Poll.rev, Op.revision)
            bot(Op)
