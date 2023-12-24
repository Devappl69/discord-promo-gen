import random
import requests

def get_discord_promo_code():
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    payload = {"partnerUserId": "0778c0a9152ccab29e814e5730a1f67a2949ef8826366709271b28005acc450f"}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        response_json = response.json()
        token_value = response_json.get('token')
        result = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token_value}\n"
        print(f"Here is your reward: {result}")
        return True
    else:
        print("Error generating Nitro code")

guess = int(input("Pick a number between 1 and 6: "))

if guess == random.randint(1,6):
    print("You won")
    get_discord_promo_code()
else:
    print("You lost")