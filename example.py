# THIS IS NOT THE PRODUCT
# YOU CAN USE THIS AS THE REFERERENCE
# YOU DON'T NEED TO CREDIT ME

# THIS IS NOT THE PRODUCT
# YOU CAN USE THIS AS THE REFERERENCE
# YOU DON'T NEED TO CREDIT ME

import requests

# Configuration
USERNAME = "example_user" 
QUESTION = "hello world!" 

URL = 'https://ngl.link/api/submit'

payload = {
    'username': USERNAME,
    'question': QUESTION,
    'deviceId': '',
    'gameSlug': '',
    'referrer': ''
}

try:
    response = requests.post(URL, data=payload, timeout=10)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(e)
