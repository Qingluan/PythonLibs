
class Observer(object):
    Observers = {}
    def add_observable(self,cls):
        self.Observers[cls] = False

    def notify_observer(self,*args,**karg):
        for key in self.Observers:
            if self.Observers[key] == False:
                key.update(*args,**karg)
                self.Observers[key] = True

    def changed(self):
        [self._changed(key) for key in self.Observers ]
    def _changed(self,key): 
        self.Observers[key] = False

