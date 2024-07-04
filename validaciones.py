

def validate_length(texto: str, longitud_min: int, longitud_max: int, reintentos: int) -> str | None:
        """si la cantidad de espacios en el string ingresado es distinta a 0, guarda el string en otra variable
        y cambia los espacios por una a para comprobar que todo sea alphanumerico,sino pasa el codigo comprueba 
        si es alphanumerico y si es retorna el string

        Args:
            string (_type_): mensaje
            minimo (int): numero minimo de caracteres que acepta en el string
            maximo (int): numero maximo de caracteres que acepta en el string
           reintentos (int): cantidad de reintentos

        Returns:
            str | None: _description_
        """
        
        if string.count(" ") != 0:
               string_plano = string.replace(" ", "a")
        else:
               string_plano = string

        string_valido = string_plano.isalpha() 
        
        while (len(string) < longitud_min or len(string) > longitud_max) or not string_valido:
                string = texto
                if string.count(" ") != 0:
                        string_plano = string.replace(" ", "a")
                else:
                        string_plano = string

                string_valido = string_plano.isalpha() 
           
        
        if reintentos == 0:
             string = None

        return string