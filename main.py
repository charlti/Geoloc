import ipinfo
import sys

my_token = "your_token"

try:
    ip = sys.argv[1]

except  Exception:
    ip = None
    print("You must enter an IP address as an argument for the script !\n")
    print("Usage : python main.py <IP>")

handler = ipinfo.getHandler(my_token)
detail = handler.getDetails(ip)
print(f"IP : {detail.ip}")
print(f"Pays : {detail.country_name}")
print(f"Region : {detail.region}")
print(f"Ville : {detail.city}")
print(f"Localisation : {detail.loc}")
