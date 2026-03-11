import base64
import json
import sys

def decode_part(part):
    part += '=' * (-len(part) % 4)
    return base64.urlsafe_b64decode(part)

token = input("Enter JWT: ")

header, payload, signature = token.split(".")

print("\nHEADER:")
print(json.dumps(json.loads(decode_part(header)), indent=2))

print("\nPAYLOAD:")
print(json.dumps(json.loads(decode_part(payload)), indent=2))