import hashlib
cripto = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000
cripto.update(b'no body inpect')
cripto.update(b'i am abhishek')
cripto.digest()
cripto.hex()
