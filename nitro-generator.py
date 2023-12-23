import requests
import time

def get_discord_promo_code():
    url = "https://api.discord.gx.games/v1/direct-fulfillment"

    payload = {
        "partnerUserId": "0778c0a9152ccab29e814e5730a1f67a2949ef8826366709271b28005acc450f"
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        response_json = response.json()
        token_value = response_json.get('token')
        if token_value:
            result = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token_value}\n"
            with open('nitro-promo-codes.txt', 'a') as file:
                file.write(result)
            return True
        else:
            print("Token not found in the response JSON.")
            return False
    else:
        print(f"Request failed with status code: {response.status_code}")
        return False

while 1==1:
    get_discord_promo_code()
