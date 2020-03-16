class AuthenticationModel:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginModel(AuthenticationModel):
    def __init__(self, username, password):
        super().__init__(username, password)

class RegisterModel(AuthenticationModel):
    def __init__(self, username, password, role):
        super().__init__(username, password)
        self.role = role
        