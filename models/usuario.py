class Usuario:
    def init(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email

    def get_id_usuario(self):
        return self.id_usuario

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email