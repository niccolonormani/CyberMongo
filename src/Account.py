import hashlib, os, binascii

class Account:

    def __init__(self, username, password):
        print("New Account being created")
        self.username = username
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        self.password = (salt + pwdhash).decode('ascii')

    def __str__(self):
        return "Account -> Username: {}, Password: {}".format(self.username, self.password)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def toJSON(self):
        return {"username":self.username, "password":self.password}