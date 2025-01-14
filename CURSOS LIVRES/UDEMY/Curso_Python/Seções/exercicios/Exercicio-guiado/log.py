# Abstração
from pathlib import Path

log_file = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self,msg):
        raise NotImplementedError('Implente o método log')
    
    def log_error(self,msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self,msg):\
        return self._log(f'Sucess: {msg}')
        
    
class LogFileMixing(Log):
    
    def _log(self,msg):
        msgf = f'{msg}, em ({self.__class__.__name__})'
        print(f'Salvando no log: {msg}')
        with open(log_file, 'a') as arquivo:
            arquivo.write(msgf)
            arquivo.write('\n')

class LogPrintMixing(Log):
    def _log(self,msg):
        print(f'{msg}, em ({self.__class__.__name__})')
 
if __name__ == '__main__':
    lp = LogPrintMixing()
    lp.log_error('NOT OK')
    lp.log_sucess('OK')
    
    lf = LogFileMixing()
    lf.log_error('NOT OK')
    lf.log_sucess('OK')
