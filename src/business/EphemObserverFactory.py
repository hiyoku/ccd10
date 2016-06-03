import ephem


class EphemObserverFactory:
    def __init__(self):
        pass

    def create_observer(self, longitude=None, latitude=None, elevation=None):
        o = ephem.Observer()
        o.lon = longitude
        o.lat = latitude
        o.elevation = elevation
        return o

    def set_observer_parameters(self, observer, obsLongitude, obsLatitude, obsElevation):
        observer.lon = obsLongitude
        observer.lat = obsLatitude
        observer.elevation = obsElevation