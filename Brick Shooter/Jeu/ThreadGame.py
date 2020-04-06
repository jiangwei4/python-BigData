import threading 
import time;

class ThreadGame(threading.Thread):

    def __init__(self, *args, **kwargs): 
        super(ThreadGame, self).__init__(*args, **kwargs) 
        self._stop = threading.Event()
    
    def setInformations(self,vaisseau, affichage):
        self.vaisseau = vaisseau
        self.affichage = affichage

    def setxy(self,x,y,surfaceH,surfaceW):
        self.vaisseau.setx(x,surfaceW,0)
        self.vaisseau.sety(y,surfaceH,0)
        
    def stop(self): 
        self._stop.set() 
  
    def stopped(self): 
        return self._stop.isSet() 
  
    def run(self): 
        while True:
            if self.stopped(): 
                return
            time.sleep(self.vaisseau.getMouvementSpeed())
            self.affichage.update()

        
        #self.stop()

   