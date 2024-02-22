import requests;
from colorama import init, Fore, Back, Style

init();


with open('./dictionary.txt','r' , encoding='utf-8') as dictionary:
    words = dictionary.read().split('\n');


for word in words: 
    
    url = f'https://google.com/{word}';
    response = requests.get(url)

    if(response.status_code == 200): 
        print(Fore.GREEN + f'Operational Page: {url}' + Fore.RESET)

    elif(response.status_code == 301 or response.status_code == 302 or response.status_code == 307):
        print(Fore.MAGENTA + f'Page Redirectec {url}' + Fore.MAGENTA)

    elif(response.status_code == 401):
        print(Fore.YELLOW + f'Unauthorized Page {url}' + Fore.RESET);

    elif(response.status_code == 404):
        print(Fore.RED + f'Page not found {url}' + Fore.RESET)

