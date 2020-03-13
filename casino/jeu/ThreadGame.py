import threading 
import time;

class ThreadGame(threading.Thread):

    def __init__(self, *args, **kwargs): 
        super(ThreadGame, self).__init__(*args, **kwargs) 
        self._stop = threading.Event()
    
    def setInformations(self,essai, perso):
        self.essai = essai
        self.temps = 5
        self.perso = perso
        
    def stop(self): 
        self._stop.set() 
  
    def stopped(self): 
        return self._stop.isSet() 
  
    def run(self): 
        t=self.temps
        while t:
            if self.stopped(): 
                return
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            t -= 1
        self.perso.setEssai(self.perso.getEssai()+1)
        print('Vous avez dépassé le délai de 5 secondes" ! Vous perdez l\'essai courantet il vous reste "',self.perso.getEssai() - self.essai,'" essai(s) !')

   