import os
import multiprocessing
import time

Process = multiprocessing.Process

def func(cmd):
    os.system(cmd)

if __name__ == "__main__":
    cmd1 = '''java `cat conf-quickstart/druid/historical/jvm.config | xargs` -cp "conf-quickstart/druid/_common:conf-quickstart/druid/historical:lib/*" io.druid.cli.Main server historical'''
    cmd2 = '''java `cat conf-quickstart/druid/broker/jvm.config | xargs` -cp "conf-quickstart/druid/_common:conf-quickstart/druid/broker:lib/*" io.druid.cli.Main server broker'''
    cmd3 = '''java `cat conf-quickstart/druid/coordinator/jvm.config | xargs` -cp "conf-quickstart/druid/_common:conf-quickstart/druid/coordinator:lib/*" io.druid.cli.Main server coordinator'''
    cmd4 = '''java `cat conf-quickstart/druid/overlord/jvm.config | xargs` -cp "conf-quickstart/druid/_common:conf-quickstart/druid/overlord:lib/*" io.druid.cli.Main server overlord'''
    cmd5 = '''java `cat conf-quickstart/druid/middleManager/jvm.config | xargs` -cp "conf-quickstart/druid/_common:conf-quickstart/druid/middleManager:lib/*" io.druid.cli.Main server middleManager'''

    os.chdir('/Users/astrozhou/testspace/druid/druid-0.11.0')
    p1 = Process(target=func, args=(cmd1,))
    p1.daemon = True
    p1.start()
    p2 = Process(target=func, args=(cmd2,))
    p2.daemon = True
    p2.start()
    p3 = Process(target=func, args=(cmd3,))
    p3.daemon = True
    p3.start()
    p4 = Process(target=func, args=(cmd4,))
    p4.daemon = True
    p4.start()
    p5 = Process(target=func, args=(cmd5,))
    p5.daemon = True
    p5.start()
    while(1):
        cmd = raw_input()
        if cmd=='stop':
            break
        else:
            print 'input stop to endup'
    print 'run end'

