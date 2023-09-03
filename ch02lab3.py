#ch02_lab3.py

class Tv:
    def __init__(self,p= False,c=0):
        self.power=p
        self.channel=c

    def status(self):
        if self.power:
            print(f'전원 ON')
        else:
            print(f'전원 OFF')

        print(f'채널은 {self.channel}')


    def power_click(self):
        self.power=not self.power

    def channel_up(self):
        self.channel +=1

    def channel_down(self):
        self.channel -=1
        if self.channel<0:
            self.channel=999;

        
tv1=Tv()
tv1.status()

tv2=Tv(True,10)
tv2.status()

tv1.power_click()
tv1.channel_up()
tv1.status()

print('tv3------')
tv3=Tv()
tv3.status()
tv3.channel_down()
tv3.status()
tv3.channel_down()
tv3.status()
