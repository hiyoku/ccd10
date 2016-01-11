
import threading


class Locker:

    class __impl:
        """
            Implementation of Singleton Interface
        """

        def __init__(self):
            self.lock = threading.Lock()
            self.finished = False

        def set_acquire(self):
            self.lock.acquire()
            self.finished = False

        def set_release(self):
            self.lock.release()
            self.finished = True

        def is_locked(self):
            return self.lock.locked()

        def printID(self):
            return id(self.lock)

    # Storage for the instance reference
    __instance = None

    def __init__(self):
        # Creating the Singleton instance
        if Locker.__instance is None:
            Locker.__instance = Locker.__impl()

        self.__dict__["_Singleton__Instance"] = Locker.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)

    # Testing
    def set_acquire(self):
        pass

    def set_release(self):
        pass

    def is_locked(self):
        pass