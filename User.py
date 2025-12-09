# Class representing account

import hashlib
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.password = None

    def set_password(self, password):
        self.password = self.hash_password(password) 

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
