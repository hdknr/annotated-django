## SNS の通知を検証する

- [pyca/cryptography](https://github.com/pyca/cryptography) を使う

注意: 実際のメッセージを改変しているので、実際の検証はエラーになります

~~~py
##  通知されたJSON

MESSAGE = '''
{ "Type" : "SubscriptionConfirmation",
  "MessageId" : "8d70422f-d1b5-4af9-ac42-b6e0885f6b10",
  "Token" : "2336412f37fb687f5d51e6e241d44a2dc112867306c6c662ae6f206215109ce37c384c61b4d4e229591b30fe228c65f9f91132b67c4a3ea2a3c45ba060a69bc72c323265cbe05b283b4e135775fe6a0059931f5cdf6c4c30da872f02c1a58c90f2c3aa1247de2d455e7203c48e2fc66ac6e6de98d1102bc39553b1af68b5559e",
  "TopicArn" : "arn:aws:sns:us-west-2:013213997695:LafogliaSes-Bounce-topic",
  "Message" : "You have chosen to subscribe to the topic arn:aws:sns:us-west-2:013213997695:LafogliaSes-Bounce-topic.\\nTo confirm the subscription, visit the SubscribeURL included in this message.",
  "SubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-west-2:013213997695:LafogliaSes-Bounce-topic&Token=2336412f37fb687f5d51e6e241d44a2dc112867306c6c662ae6f206215109ce37c384c61b4d4e229591b30fe228c65f9f91132b67c4a3ea2a3c45ba060a69bc72c323265cbe05b283b4e135775fe6a0059931f5cdf6c4c30da872f02c1a58c90f2c3aa1247de2d455e7203c48e2fc66ac6e6de98d1102bc39553b1af68b5559e",
  "Timestamp" : "2016-10-27T09:37:27.213Z",
  "SignatureVersion" : "1",
  "Signature" : "EPLcYboizPcc+B6TXlieQhVf3iGFGwJv9i7omCK71lhDSpPXw2KC6rUkPHiRyvvEaEERC/XN1cWwJU4Nckt49x2ld+geOFb2LyA33a91PZAY4S50Ar5zvv78xPK5pwQVC5D9me5GhkWlnpOljrHvLpQNjKDwMtauRdkI9yTr5efS1PHmuGCIP/7U7YOnVpyy10A8xWx/magA/DaUZ+fiiurDuzznS36lysgoEs0Z0pJSkKEmKpkPMqEemAhO+neiRZCK+7KGn0mh3im1j9upT5qc2/yazzMx/yn8ILahDSIorX49Enk0G0V+m4vrx2YNsc7h79TKpIPdF6TiBpHqvg==",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-b95095beb82e8f6a046b3aafc7f4149a.pem"
}
'''

## 署名入力の並び
NOTIFICATION_SIGNING_INPUT_KEY = [
    "Message",
    "MessageId",
    "Subject",
    "SubscribeURL",
    "Timestamp",
    "Token",
    "TopicArn",
    "Type",
]

## 署名入力を作る

def NOTIFICATION_SIGNING_INPUT(jobj):
    return "".join([
        "{}\n{}\n".format(k, jobj.get(k))
        for k in NOTIFICATION_SIGNING_INPUT_KEY
        if k in jobj
    ])
import json
message = json.loads(MESSAGE)
signing_input = NOTIFICATION_SIGNING_INPUT(message).encode()

## 署名のデコード(BASE64)
from base64 import standard_b64decode
signature = standard_b64decode(message['Signature'])


## SigningCertURL から取得したPEM

CERT = '''
-----BEGIN CERTIFICATE-----
MIIF5DCCBMygAwIBAgIQMlyV8Y5saUjyFgu3K5kFwTANBgkqhkiG9w0BAQsFADB+
MQswCQYDVQQGEwJVUzEdMBsGA1UEChMUU3ltYW50ZWMgQ29ycG9yYXRpb24xHzAd
BgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxLzAtBgNVBAMTJlN5bWFudGVj
IENsYXNzIDMgU2VjdXJlIFNlcnZlciBDQSAtIEc0MB4XDTE2MDcyNzAwMDAwMFoX
DTE3MDgyMjIzNTk1OVowazELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0
b24xEDAOBgNVBAcMB1NlYXR0bGUxGTAXBgNVBAoMEEFtYXpvbi5jb20sIEluYy4x
GjAYBgNVBAMMEXNucy5hbWF6b25hd3MuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAmYrVPHC2QSE/OR8w9UfnjdPqEoAfOxhwJna/2W+/C+vTrMzd
4R9E3kfA3arf43LZFTSQ23Ed3Tao8srh/iK7DFv87bR+5uPnEO4fcHXDiJ1n3WMU
kjo+BEKXwSdR4AfIRUrJB2hk3mhXJoGkYJp3WBZ2ieoYBqwxpxuFRtNQW4ttqNwt
q4mONfxg0840e1kY+xFQa7ya8zg9FGaVgeLiN+e/gv5YYdrk8JG4P6kbzil9bETm
Xm+PXoxWy6cMAT3Coz1NNkPGQrKfNfGZSdPGh1d/89IwRh+eNUEIJ8PdnhzcvgN7
RQ5zs70V6u7StvrNukYftMwY0hIELlMUHYqRbQIDAQABo4ICbzCCAmswHAYDVR0R
BBUwE4IRc25zLmFtYXpvbmF3cy5jb20wCQYDVR0TBAIwADAOBgNVHQ8BAf8EBAMC
BaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMGEGA1UdIARaMFgwVgYG
Z4EMAQICMEwwIwYIKwYBBQUHAgEWF2h0dHBzOi8vZC5zeW1jYi5jb20vY3BzMCUG
CCsGAQUFBwICMBkMF2h0dHBzOi8vZC5zeW1jYi5jb20vcnBhMB8GA1UdIwQYMBaA
FF9gz2GQVd+EQxSKYCqy9Xr0QxjvMCsGA1UdHwQkMCIwIKAeoByGGmh0dHA6Ly9z
cy5zeW1jYi5jb20vc3MuY3JsMFcGCCsGAQUFBwEBBEswSTAfBggrBgEFBQcwAYYT
aHR0cDovL3NzLnN5bWNkLmNvbTAmBggrBgEFBQcwAoYaaHR0cDovL3NzLnN5bWNi
LmNvbS9zcy5jcnQwggEFBgorBgEEAdZ5AgQCBIH2BIHzAPEAdgDd6x0reg1PpiCL
ga2BaHB+Lo6dAdVciI09EcTNtuy+zAAAAVYpz1FWAAAEAwBHMEUCIFYpMqHzT/IG
WKgBt6SwXJhfYmj3JKtAJWq5dabI7TuKAiEAqYyWQUjlFuKkIwEhx8x1I+WJz+hp
npW7Na0CzyUvZWMAdwCkuQmQtBhYFIe7E6LMZ3AKPDWYBPkb37jjd80OyA3cEAAA
AVYpz1H+AAAEAwBIMEYCIQCY+492bMMCU3kRQPDQ27TRv5x+YuVkg+6ULi1Ddyea
KgIhANIVUCbM918/jMu0xc2cvrfov6SNAgPIjRLDGmDkLdJ1MA0GCSqGSIb3DQEB
CwUAA4IBAQBpQS/LverJ6gD2vuESrRi1COa4ABSLf584sL1yHLTNtf1GCUfZUgO+
CKacKGHcqxALOUi3m4PPQmuiNa20i6ttu7Q6+aj9zbq3VfJYwISFP1jLGjkiFtR2
ufBiIuB2T6dbZeYJ7Yg9DDTwwEgxHMjlT/DLyKPPPRFa0I/l3PmXMZh8iJNuxGiY
qOSxwAm9QMCaBJj+64HLyw4ZwO4rTgAxqtI/muZC3vw1nGoL7fer2X6MdW6PtYD/
ysixQTQtyDdNpB6yOGYFJv+Sf/0AcZST1a7HwfHt14JD+0I180FhGV1qFtx7KRUE
6Kw4sQp+ZMgtgzM8l3fDTMEgqpLSQH+2
-----END CERTIFICATE-----
'''

## PEMより公開鍵を取得する
pem_data = CERT.encode()            # to byte array
# pip install cryptography
#
# https://cryptography.io/en/latest/x509/reference/#cryptography.x509.load_der_x509_certificate
from cryptography import x509
from cryptography.hazmat.backends import default_backend
cert = x509.load_pem_x509_certificate(pem_data, default_backend())
public_key = cert.public_key()

## 公開鍵を使って　PKCSV1.5でSHA1されたダイジェストを検証する
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/?highlight=pkcs#verification
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
try:
    public_key.verify(
        signature,
        signing_input,
        padding.PKCS1v15(),
        hashes.SHA1()
    )
    # 正常の場合なにもおこらず
    print("Valid Signature")
except InvalidSignature:
    # 不正の場合は例外
    print('Invalid Signatire')
~~~
