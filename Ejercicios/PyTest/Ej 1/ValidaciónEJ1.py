class Validate():
    def validate_password(self, cont):
        mayus = False
        min = False
        num = False
        char = True
        if len(cont) >= 8: 
            for i in range(len(cont)):
                if cont[i].isupper():
                    mayus = True
                elif cont[i].islower():
                    min = True
                elif cont[i] in "1234567890":
                    num = True
                elif cont[i] in "@_!#$%^&*()<>?/\\|}{~:":
                    char = False
            if mayus and min and num and char:
                return True
            else:
                return False
        else:
            return False    