from apoyo_membresia import _crear_nueva_membresia

class Membresia:
    """
    Clase abstracta que define la estructura base para las membresías de usuarios.
    """

    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        """
        Constructor de la clase `Membresia`.

        Args:
            correo_electronico (str): Correo electronico del suscriptor.
            numero_tarjeta (str): Numero de tarjeta de credito del suscriptor.
        """
        self.__correo_electronico = correo_electronico
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_electronico(self):
        """
        Getter del atributo `correo_electronico`.

        Returns:
            str: Correo electronico del suscriptor.
        """
        return self.__correo_electronico

    @property
    def numero_tarjeta(self):
        """
        Getter del atributo `numero_tarjeta`.

        Returns:
            str: Numero de tarjeta de credito del suscriptor.
        """
        return self.__numero_tarjeta

    def cambiar_suscripcion(self, tipo_membresia_nueva: int) -> Membresia:
        """
        Metodo que permite cambiar la suscripcion del usuario a un nuevo tipo de membresia.

        Args:
            tipo_membresia_nueva (int): Identificador numerico del tipo de membresia nueva.

        Returns:
            Membresia: Instancia de la nueva membresía creada.
        """
        raise NotImplementedError("Método `cambiar_suscripcion` no implementado.") # En Python, la palabra clave raise se utiliza para generar una excepcion manualmente dentro de una funcion.

    def cancelar_suscripcion(self): Membresia:
        """
        Metodo que permite cancelar la suscripcion del usuario.

        Returns:
            Membresia: Instancia de la membresía Gratis creada al cancelar la suscripción.
        """
        raise NotImplementedError("Método `cancelar_suscripcion` no implementado.")

class Gratis(Membresia):
    """
    Clase que representa la membresía de tipo Gratis.
    """

    costo = 0
    dispositivos_maximos = 1

    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia_nueva: int) -> Membresia:
        """
        Sobrescribe el método `cambiar_suscripcion` de la clase `Membresia`.

        Args:
            tipo_membresia_nueva (int): Identificador numérico del tipo de membresía nueva.

        Returns:
            Membresia: Instancia de la nueva membresía creada.
        """

        if 1 <= tipo_membresia_nueva <= 4:
            return _crear_nueva_membresia(
                tipo_membresia_nueva, self.correo_electronico, self.numero_tarjeta
            )
        else:
            return self

class Basica(Membresia):
    """
    Clase que representa la membresía de tipo Básica.
    """

    costo = 3000
    dispositivos_maximos = 2

    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)

    def cambiar_suscripcion(self, tipo_membresia_nueva: int) -> Membresia:
        """
        Sobrescribe el método `cambiar_suscripcion` de la clase `Membresia`.

        Args:
            tipo_membresia_nueva (int): Identificador numérico del tipo de membresía nueva.

        Returns:
            Membresia: Instancia de la nueva membresía creada.
        """

        if 2 <= tipo_membresia_nueva <= 4:
            return _crear_nueva_membresia(
                tipo_membresia_nueva, self.correo_electronico, self.numero_tarjeta
            )
        else:
            return self

class Familiar(Basica):
    """
    Clase que representa la membresía de tipo Familiar.
    """

    costo = 5000
    dispositivos_maximos = 5

    dias_regalo = 7  # Atributo de instancia que almacena los días de regalo

    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)
        self.dias_regalo = 7

    def


class SinConexion(Basica):
    costo = 3500

class Pro(Familiar, SinConexion):
    pass

g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))