import requests
import threading

def get_discord_promo_code():
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    payload = {
        "partnerUserId": "0778c0a9152ccab29e814e5730a1f67a2949ef8826366709271b28005acc450f"
    }
    
    collected_codes = []
    try:
        while len(collected_codes) < 10:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                response_json = response.json()
                token_value = response_json.get('token')
                if token_value:
                    result = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token_value}\n"
                    collected_codes.append(result)
                else:
                    print("Token not found in the response JSON.")
            else:
                print(f"Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    
    if collected_codes:
        with open('nitro-promo-codes.txt', 'a') as file:
            for code in collected_codes:
                file.write(code)

def run_get_discord_promo_code():
    while True:
        get_discord_promo_code()

promo_thread = threading.Thread(target=run_get_discord_promo_code)
promo_thread.daemon = True
promo_thread.start()

input("Press Enter to exit...\n")
