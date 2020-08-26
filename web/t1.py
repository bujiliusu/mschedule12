# from subprocess import Popen
# p = Popen('echo hello', shell=True)
# try:
#     print('world')
#     code = p.wait(5)
#     print(code)
# except Exception as e:
#     print(str(e))

import zerorpc
class MyRPC:
    def hello(self, text:str):
        return 'send back {}'.format(text)
s = zerorpc.Server(MyRPC())
s.bind('tcp://0.0.0.0:9000')
s.run()

#if __name__ == '__main__':

