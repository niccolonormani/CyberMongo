import hashlib, os, binascii
from pymongo import MongoClient
from Account import Account

class AccountDao:
    
    def __init__(self):
        srv_atlas_path = ""
        self.db = MongoClient(srv_atlas_path).cybermongo.cybermongo

    def addAccount(self, username, password):
        self.db.insert_one(Account(username, password).toJSON())
    
    def findAccount(self, username):
        return self.db.find_one({"username": username})
    
    def verifyAccount(self, stored_password, password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        hashkey = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        hashpwd = binascii.hexlify(hashkey).decode('ascii')
        return hashpwd == stored_password[64:]