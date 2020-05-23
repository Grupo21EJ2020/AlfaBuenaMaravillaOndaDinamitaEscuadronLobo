class Video:
    def __init__(self,idVideo,nombre,url,fechaPublicacion):
        self.__idVideo = idVideo
        self.__nombre = nombre
        self.__url = url
        self.__fechaPublicacion = fechaPublicacion

    @property
    def idVideo(self):
        return self.__idVideo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def url(self):
        return self.__url

    @property
    def fechaPublicacion(self):
        return self.__fechaPublicacion

