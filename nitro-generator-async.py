import asyncio
import aiohttp
import ssl
import time

concurrency = 1

async def get_discord_promo_code(session):
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    payload = {
        "partnerUserId": "0778c0a9152ccab29e814e5730a1f67a2949ef8826366709271b28005acc450f"
    }
    
    try:
        async with session.post(url, json=payload, ssl=ssl.SSLContext(ssl.PROTOCOL_TLS)) as response:
            data = await response.text()
            promo_link = ""
            start_index = data.find('{') + 10
            end_index = data.rfind('}') - 1

            if start_index != -1 and end_index != -1:
                content_within_brackets = data[start_index:end_index]
                if content_within_brackets != "":
                    promo_link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{content_within_brackets}"

                    with open('nitro-promo-codes.txt', 'a') as file:
                        file.write("\n")
                        file.write(promo_link)
                else:
                    print("Rate Limit exceeded (error 429)")
                    
            else:
                print("No content within curly brackets found in the response.")
    except aiohttp.ClientError as e:
        print(f"Client Error: {e}")

async def run_get_discord_promo_code():
    global concurrency
    async with aiohttp.ClientSession() as session:
        tasks = [get_discord_promo_code(session) for _ in range(concurrency)]
        await asyncio.gather(*tasks)

asyncio.run(run_get_discord_promo_code())
print(f"Successfully generated {concurrency} Discord promotion codes!")