import requests

with open("Nitro.txt") as f:
    for line in f:
        nitro = line.strip("\n")
#You can rename the .txt to whatever you want you just have to change the name in the code aswell.

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
#Just that you know that gives you a rate limit.
        
        r = requests.get(url)
        	
        if r.status_code == 200:
        	print(" Valid | {} ".format(line.strip("\n")))
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))
#Put Nitro Gift Codes into the Nitro.txt and then start the script.
