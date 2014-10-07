
class EventNoneError(KeyError):
    """docstring for KeyEventNoneExceptionException"""
    def __init__(self,fun_name):
        self.fun_name = fun_name
    def __str__(self):
        print "Observer.events has not {} method ".format(self.fun_name)
        

class Observer(object):
    """
    example :


    @Observer.add_observer
    def dis(n):
        print "you get {}".format(n)

    @Observer.event('dis')
    def add_one(n,m):
        print "n + m =  {}".format(n+m)
        Observer.args = [n]
    
    if __name__ == "__main__":
        add_one(123123)
    """
    events = {}
    args = []
    kargs = {}
    # def __init__(self,**kargs):

    @staticmethod
    def add_observer(f):
        Observer.events[f.__name__] = f     
    
    @staticmethod
    def notify(fun_name,*args,**kargs):
        if fun_name in Observer.events:
            Observer.events[fun_name](*args,**kargs)
        else:
            raise EventNoneError(fun_name)


    @staticmethod
    def event(name=None):
        def _event(method):
            print Observer.events
            def __event(*args,**kargs):

                res = method(*args,**kargs)
                if name in Observer.events:
                    Observer.events[name](*Observer.args,**Observer.kargs)
                else:
                    raise EventNoneError(name)
                return res
            return __event
        return _event
