from subprocess import Popen, PIPE
from utils import getlogger
import tempfile

logger =getlogger(__name__, 'd:/test/exec.log')

class Exexutor:
    def run(self, script, timeout=None):
        """
        使用shell运行脚本
        :param script:
        :param timeout:
        :return:
        """

        with tempfile.TemporaryFile('w+b') as f:
            proc = Popen(script, shell=True, stdout=f, stderr=f)
            try:
                code = proc.wait(timeout)
                f.seek(0)
                if code == 0:
                    txt = f.read()
                else:
                    txt = f.read()
                logger.info('{} {}'.format(code, txt))
                return code,txt
            except Exception as e:
                logger.error(e)
                return (1, '')

if __name__ == '__main__':
    executor = Exexutor()
    print(executor.run('pause', 5))
