import ephem


class EphemObserverFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_observer(longitude=None, latitude=None, elevation=None):
        global o
        try:
            o = ephem.Observer()
            o.lon = longitude
            o.lat = latitude
            o.elevation = float(elevation)
        except Exception as e:
            print(e)
            o.lon = 0
            o.lat = 0
            o.elevation = 0
        return o

    @staticmethod
    def set_observer_parameters(observer, obsLongitude, obsLatitude, obsElevation):
        try:
            observer.lon = obsLongitude
            observer.lat = obsLatitude
            observer.elevation = float(obsElevation)
        except Exception as e:
            print(e)
            observer.lon = 0
            observer.lat = 0
            observer.elevation = 0