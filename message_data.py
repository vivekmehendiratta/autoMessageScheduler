

api_key = 'your_api_key'


def createPayload(message, language, numbers):
    sender_id = 'sender_id=FSTSMS'
    message = message.replace(' ', '%20')
    message = 'message=' + message
    language = 'language=' + language
    route = 'route=p'
    numbers = 'numbers='+numbers

    payload = '&'.join([sender_id, message, language, route, numbers])

    return payload


def createHeaders():
    headers = {
        'authorization': api_key,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }

    return headers
