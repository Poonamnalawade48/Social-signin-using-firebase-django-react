"""
This file is used as common utility functionality.
"""
import firebase_admin

from firebase_admin import credentials

from firebase_admin import auth

from firebase_admin.auth import (ExpiredIdTokenError,
                                 UserNotFoundError,)

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "fir-authentication-38dcd",
    "private_key_id": "73b476b2dd792eb0349abd7bfcb78d9fb37b7007",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDz44tBsHnO9Xnf"
                   "\nLg1C5BTqEv9v8FRlAMfwRltsRCHMuR/woRRAFJbEpISUCz2ZX8Zs+rwJRv3Dc1kp\nqC"
                   "/8PSRMTRApBEG0bTUM95CzMf9I9ei2HEwPSlDkqtwYqAWBcoaH3Qci6jNWPgah"
                   "\nZ9ZFprM1Dc6W4GxQx1e1i70uYJeeV4CCocNMqIen8F7nmlqeoFbmMLelhxX8QXqZ\nR/swwD9LbL5H67MPjXG2Vo4TliH5b"
                   "+Zjp8n6cW56L2g9JT7A4i6lxqG1BIBMuQxM\ntw9WvtU1aCBGppkT34Ea85TJyvwOVatI3xITJXOrSc8jqsC6KXE"
                   "+5uYiwFllO3GC\nFu50x+H1AgMBAAECggEAKvrvOCjfFotpKl0lxiOG0gd+D56VaOVd1ui3RNmu8TKw\nv8nLVU2rkkUB"
                   "/ksK1IQt5le7mpDxuKeTz4UNy9CEnJO6JNhUsfTK9BmO3R2TBSsd\nEzbiapFotxurRQcbTUg/ECNyFgOa"
                   "/3hX18sCVmz9yPxBa5JqVEQFH3/cW5d3MNaX\nwyncWTpFBjKz4XFnZuWMT34FFBlVWAyfxN3ZTxeUBDxyG/5"
                   "/74Nkzddg3pc0GBm/\nY/aC2v62ScC5fNzfHtQ7Ep5Lh+rtaogTJ6CPEHAN4ILwk+mtedwf3qH6KWl383yR\nAwTJXkwiB1XK"
                   "+sekiVvPAoUNBuiDBHIRegH9HtSDEwKBgQD7mDpjcwZaQcW6Js1/\nIlc36j"
                   "/23NgjlfFavHQycI2gDIl6ue5fOaDi4eOJRQDXDD9d4a0ocfUJW3rtJNxf"
                   "\n0unTCrRkRHYLeLFmbjXeOKEt1xGAgBUVqTDyd82ieFme/4GJELT8zx0CSmjvD66t\n391/E4AroLoQGrZaN"
                   "+XSm7yVDwKBgQD4KMZR5R+pWVxqE/KY9dS/bY2jfVhNqE+1\nFKjS2TPwQOIrjQAzEE"
                   "/JIYO6E6kEDoqAx0U7ncCPAJqhbZdvyZmUm4om3tpMlncr\nWFftNr0xnPANLTMt+qfH0Yho+7"
                   "+OIhy5wG5YF78RZxa1TuXS1r4XBf7njI1i7Sg1\nVVpYQ4kAuwKBgQClsKMDS4Ure5VT+qnqyBrYYBSv5tEQ3naMYv"
                   "/DGAytEpSXlks9\nux4RTOIkTKU4+n/gu/blY+cTuoNCGbxn/uaubaZPQibbdyidZIdlSbYcEj8ceT1p"
                   "\nfnsVs4BhNxEOfQY51h7bPyrDj217wsAvEfc08Qq/sKHYaT8eOyHHiXiwUQKBgQCX\no9rkCj2Zr0hgbcYNoBKb0yb840hFU"
                   "/c48OHkzeMGCa/q6uNXUL1ga0FiQEdEelo6\nLQpqTpBvEfBreltSbP+TJqR58i21JTC25On9wzhDC+JIOvmOPB"
                   "+wY6KWfFdmVAP3\nodYLsJ8J1FO1APxBJQXNbdWAyotPCxpJ1Nk7HDGopwKBgHsUQpnLFSnZCV9u2EHK"
                   "\npbY1N3jPIk3Zj1Tt8fMdcQmVHrSqFevNkgMt7ZomUiGH6kzfP/9NRxWd8HXxDepi\n5vkSMi5ibSnx78M5Egb1aNPABLBAX0"
                   "/aDtpvKVIWegdzxis9xVquerpr9DouATOI\n60IvpM8ihot2X3hJuEN9BSWz\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-lti13@fir-authentication-38dcd.iam.gserviceaccount.com",
    "client_id": "106497936557274312101",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lti13%40fir"
                            "-authentication-38dcd.iam.gserviceaccount.com "

})

default_app = firebase_admin.initialize_app(cred)


def firebase_validation(id_token):
    """
    This function receives id token sent by firebase and
    validate the id token then check if the user exist on
    firebase or not if exist it returns True else False
    """
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        provider = decoded_token['firebase']['sign_in_provider']
        image = None
        name = None
        if "name" in decoded_token:
            name = decoded_token['name']
        if "picture" in decoded_token:
            image = decoded_token['picture']
        try:
            user = auth.get_user(uid)
            email = user.email
            if user:
                return {
                    "status": True,
                    "uid": uid,
                    "email": email,
                    "name": name,
                    "provider": provider,
                    "image": image
                }
            else:
                return False
        except UserNotFoundError:
            print("user not exist")
    except ExpiredIdTokenError:
        print("invalid token")


class ResponseInfo(object):
    """
    Class for setting how API should send response.
    """

    def __init__(self, user=None, **args):
        self.response = {
            "status_code": args.get('status', 200),
            "error": args.get('error', None),
            "data": args.get('data', []),
            "message": [args.get('message', 'Success')]
        }