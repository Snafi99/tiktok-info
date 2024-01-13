import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json, time

print("""

                 ,  ,
              #▄▓██████▀
            "▀███████████▄L
           ▄R████████████▄▄
            ▄▀█████████▓▀▀N
             ' ▀█▀███▀█ ▀
                ' ▀█▌"
                   ▐█
                   ██
                   ██
    ""▀▀▀██▄▄   ▄▄▄██▄a▄▄   ,▄▄██▀▀""
           "▀██▄⌠▀▀▀▀▀'¡▄██▀"
               ▀██▄  ▄██▀`
                  ████"
               ▄▄█▌▀╙██▄▄
          ██▄▄██▀█    █▀███▀█▌

     [ Made By GIVT . ]
     [ + ] Telegram : givtt
     [ + ] Instagram : we62
     [ ! ] You are not entitled to sell the Tool [ ! ]
""")
time.sleep(2)

class LordGivt:
    def __init__(self, username: str):
        self.username = username
        self.json_data = None

        if "@" in self.username:
            self.username = self.username.replace("@", "")

        self.admin()

    def admin(self):
        self.send_request()
        self.output()

    def send_request(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 GIVT"}
        r = requests.get(f"https://www.tiktok.com/@{self.username}", headers=headers)

        try:
            soup = BeautifulSoup(r.text, 'html.parser')
            script_tag = soup.find('script', {'id': '__UNIVERSAL_DATA_FOR_REHYDRATION__'})
            script_text = script_tag.text.strip()
            self.json_data = json.loads(script_text)["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
        except:
            input("[X] Error : Username Not Found .")
            exit()

    def get_user_id(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return str(self.json_data["user"]["id"])
        except IndexError:
            return "Unknown"

    def get_name(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return self.json_data["user"]["nickname"]
        except IndexError:
            return "Unknown"

    def is_verified(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            check = self.json_data["user"]["verified"]
            if check == "false" or check is False:
                return "No"
            else:
                return "Yes"
        except:
            return "Unknown"

    def secUid(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return self.json_data["user"]["secUid"]
        except:
            return "Unknown"

    def is_private(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            check = self.json_data["user"]["privateAccount"]
            if check == "true" or check is True:
                return "Yes"
            else:
                return "No"
        except:
            return "Unknown"

    def followers(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return self.json_data["stats"]["followerCount"]
        except:
            return "Unknown"

    def following(self):
        try:
            return self.json_data["stats"]["followingCount"]
        except:
            return "Unknown"

    def user_create_time(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            url_id = int(self.get_user_id())
            binary = "{0:b}".format(url_id)
            i = 0
            bits = ""
            while i < 31:
                bits += binary[i]
                i += 1
            timestamp = int(bits, 2)
            dt_object = datetime.fromtimestamp(timestamp)
            return dt_object
        except:
            return "Unknown"

    def last_change_name(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            time = self.json_data["user"]["nickNameModifyTime"]
            check = datetime.fromtimestamp(int(time))
            return check
        except:
            return "Unknown"

    def account_region(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return self.json_data["user"]["region"]
        except:
            return "Unknown"

    def video_count(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return self.json_data["stats"]["videoCount"]
        except:
            return "Unknown"

    def open_favorite(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            check = self.json_data["user"]["openFavorite"]
            if check is False or check == "false":
                return "No"
            return "Yes"
        except:
            return "Unknown"

    def see_following(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            check = str(self.json_data["user"]["followingVisibility"])
            if check == "1":
                return "Yes"
            return "No"
        except:
            return "Unknown"

    def language(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return str(self.json_data["user"]["language"])
        except:
            return "Unknown"

    def heart_count(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        try:
            return str(self.json_data["stats"]["heart"])
        except:
            return "Unknown"

    def output(self):
        "لا تحط حقوقك وتكتب برمجتك ياسبيكة هههههه"
        print(f"[ Get Info For @{self.username} ] ..\n\n")
        print(f"[ + ] UserID : {self.get_user_id()}")
        print(f"[ + ] Nickname : {self.get_name()}")
        print(f"[ + ] is verified : {self.is_verified()}")
        print(f"[ + ] is private : {self.is_private()}")
        print(f"[ + ] secUid : {self.secUid()}")
        print(f"[ + ] Followers : {self.followers()}")
        print(f"[ + ] Following : {self.following()}")
        print(f"[ + ] Likes : {self.heart_count()}")
        print(f"[ + ] Video Count : {self.video_count()}")
        print(f"[ + ] Open Favorite : {self.open_favorite()}")
        print(f"[ + ] Can See Following list : {self.see_following()}")
        print(f"[ + ] User Language : {self.language()}")
        print(f"[ + ] User Create Time : {self.user_create_time()}")
        print(f"[ + ] Last Time Change Nickname : {self.last_change_name()}")
        print(f"[ + ] Account Region : {self.account_region()}\n\n")
        input("[ + ] Done Sir ..")
        exit()

print("\n")
username = input("[?] Please Enter Username : ")
print("\n")
LordGivt(username=username)
