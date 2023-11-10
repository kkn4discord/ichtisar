#real
import requests, random, time , colorama ,sys , fade 
from colorama import Fore
from dhooks import Webhook 

def logo():
    colorama.deinit()

    for char in banner:
        time.sleep(0.004)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("Discord/gg/b9")
banner = fade.water("""



                                         _______    ______  
                                         |       \  /      \ 
                                         | $$$$$$$\|  $$$$$$
                                         | $$__/ $$| $$__/ $$
                                         | $$    $$ \$$    $$
                                         | $$$$$$$\ _\$$$$$$$
                                         | $$__/ $$|  \__/ $$
                                         | $$    $$ \$$    $$
                                         \$$$$$$$   \$$$$$$ 
                    
                    
                    
                                                                            
                                                                            

                         
                                                                                                                                                    
            +------------------------------------+------------------------------------------------------------+
            |        Vanity Cecker               |                     B9 STORE                              |
            +====================================+============================================================+
            |         link Server : B9          |                  D i o r ♔ SHANAB                          |
            +------------------------------------+------------------------------------------------------------+
     
""")

logo()


proxy_servers = { # اذا عندك بروكسيات ضيفها بنفس طريقة
    'http': '20.54.56.26:8080',
    'http': '113.50.66.19:9091',
    'http': '123.183.160.83:9091',
    'http': '117.160.250.130:9999',
    'http': '95.255.64.21:8081',
    'http': '117.160.250.133:8081',
    'http': '112.54.47.55:9091',
    'http': '123.183.160.83:9091',
    'http': '117.160.250.134:80',
    'http': '36.67.168.117:8080',
    'http': '117.160.250.130:81',
    'http': '41.59.97.53:9999',
    'http': '151.80.250.185:8080',
    'http': '103.155.196.137:3125',
    'http': '101.68.119.42:8085',
    'http': '117.160.250.133:8081',
    'http': '36.95.79.7:41890',
    'http': '39.185.232.150:9091',
    'http': '1.4.198.2:8080',
    'http': '103.231.78.36:80',
    'http':  '51.91.157.66:80',
    'http':  '149.202.172.113:80',
    'http':  '159.203.84.241:3128',
    'http':  '18.190.155.129:80',
    'http':  '41.65.0.218:1976',
    'http':  '163.116.158.213:8081',
    'http':  '47.244.2.19:3128',
    'http':  '58.247.6.106:9002',
    'http':  '42.98.75.138:80',
    'http':  '175.6.173.23:9002',
    'http':  '47.114.89.183:8080',
    'http':  '34.213.226.46:9002',
    'http':  '117.12.49.114:9091',   
}

error = 0
while True:
    user = "" 
    time.sleep(1) # كل عشرين ثانيه يفحص يفضل تخليها كل دقيقه

   # random في حال تبغى الفحص على ارقام فقط شيل الاحروف الي بفونكشن 
    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=2): # 3 في حال تبغى الفحص يكون على ثلاثيات غير القيمة الى 
        user = user + character
        

 
    response = requests.get(f"https://discord.com/api/v9/invites/{user}",proxies=proxy_servers)
    
    if (response.status_code == 200):
        error += 1
        print(Fore.RED + f"NOT FOUND: {user}" + Fore.RESET)
        print( error ) 

        
   

    elif (response.status_code == 404):
        print(Fore.GREEN + f"USER FOUND : {user}" + Fore.RESET)
       # print(f"USER FOUND : {user} " )
        Special = Webhook("https://canary.discord.com/api/webhooks/1170484880879145111/wXoTJmFgkHBbFsOX9cNbQe_NZ0qUdYVg2g5vtJWqaZmO81CKUbFpGPRL6gJJxMuHMpyi")

        #    في حال تبي تضيف ويب هوك  للسيرفرات ثانية او بنفس سيرفرك كرر نفس العملية الي تحت 

      #  Special1 = Webhook("") 

       
        data =(user)
        Special.send(F"**||@everyone|| From B9 STORE**  : `{user}` ")

        #Special1.send(F"**Free Vanity : `{user}` <a:99uf48:1030438397782794330>**")

    else:
        print("Error") # اذا انطبع الايرور هاذا البروكسيات انحرقت