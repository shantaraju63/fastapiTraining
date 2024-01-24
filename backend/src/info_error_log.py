import logging
import datetime

def info_log():
    x = datetime.datetime.now()

    y=str(x.strftime("%c"))
    s = y.replace(' ', '_')
    print(s)
    s=s[0:10]
    print(s)
    log_file=f"C:/Users/SGovindappa/Desktop/backend/src/INFO_log_file/{s}.log"
    logging.basicConfig(filename=log_file ,level=logging.INFO,
					format='%(asctime)s - %(levelname)s - %(message)s',
					filemode='a')
    logger = logging.getLogger()
    logger.info("--> create_movie(m:Movie)")


def error_logs():
    x = datetime.datetime.now()

    y=str(x.strftime("%c"))
    s = y.replace(' ', '_')
    s="error_"+s[0:10]
    print(s)
    er=f"C:/Users/SGovindappa/Desktop/backend/src/ERROR_log_file/{s}.log"
    logging.basicConfig(filename=er ,level=logging.ERROR,
					format='%(asctime)s - %(levelname)s - %(message)s',
					filemode='a')
    logger = logging.getLogger()
    logger.error("fields are reqired")

# import httpx

# async def make_request(url1:str):
#     url =url1
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)

#         # Access the response attributes as needed
#         status_code = response.status_code
#         content = response.text

#         # Handle the response data
#         print(f"Status Code: {status_code}")
        

# # Run the asynchronous function
# import asyncio
# asyncio.run(make_request())