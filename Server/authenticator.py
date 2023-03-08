import datetime
import jwt

tokenList = []
encryptionKey = 'encryptionKey'

def generate_token(user_id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=600),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    token = jwt.encode(
        payload,
        encryptionKey,
        algorithm="HS256"
    )
    addTokenToList(token)
    return token

def decode_auth_token(auth_token):
    payload = jwt.decode(auth_token, encryptionKey, algorithms="HS256")
    return payload['sub']

def addTokenToList(token):
    tokenList.append(token)

def isTokenValid(token):
    if token in tokenList:
        try:
            decode_auth_token(token)
            print("Principal ")
            return True
        except:
            print("UwU2")
            tokenList.remove(token)
            return False
    print("UwI")
    return False