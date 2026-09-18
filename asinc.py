import httpx, time, asyncio

async def gettree():
    start_time=time.time()
    async with httpx.AsyncClient() as client:
        result=await asyncio.gather(
        client.get("https://jsonplaceholder.typicode.com/posts/1"),
        client.get("https://jsonplaceholder.typicode.com/posts/2"),
        client.get("https://jsonplaceholder.typicode.com/posts/3"))
    end_time=time.time()
    all_time=end_time-start_time
    print(all_time)
asyncio.run(gettree())