import hashlib
import requests


def password_breach(password):

    password_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    query_chars , remaining_chars = password_hash[ 0 : 5 ] , password_hash[ 5 :  ]
    api_response = requests.get("https://api.pwnedpasswords.com/range/" + query_chars)

    api_hashes = [line.split(':') for line in api_response.text.splitlines()]

    for h, count in api_hashes:
        if h == remaining_chars:
            return True
    return False


def read_passwords(passfile):

    with open(passfile , 'r') as f:
        
        counter = 1

        for line in f:
            username , password = line.strip().split(",")

            if password_breach(password):
                print(f"Password number {counter} has been breached...")

            else:
                print(f"Password number {counter} is safe...")

            counter += 1


read_passwords("q4.txt")