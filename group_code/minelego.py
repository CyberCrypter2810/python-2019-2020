# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import random

def init():
    ip = "192.168.7.226"
    #ip = "127.0.0.1"
    mc = Minecraft.create(ip, 4711)
    #mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def clearAir(mc,x,y,z):
    mc.setBlocks(x-10,y-5,z-20,x+10,y+20,z+20,0)
    #mc.setBlocks(x-10,y-5,z-20,x+10,y,z+20,3)
    
def output2d(mc,mList,x,y,z):
     for k in range (0,11):
        for l  in range (0,10):
            #print(mList[k][l],end="")
            theBlock = mList[k][l]
            if (theBlock == "1"):
                theBlock = 14
            if (theBlock == "0"):
                theBlock = 15
            if (theBlock == "2"):
                theBlock = 4
            if (theBlock == " "):
                theBlock = 0
            mc.setBlock(x,5+y-k,z+l,35,theBlock)
    #print()

def output2de(mc,mList,x,y,z):
     for k in range (0,11):
        for l  in range (0,3):
            #print(mList[k][l],end="")
            theBlock = mList[k][l]
            if (theBlock == "1"):
                theBlock = 14
            if (theBlock == "0"):
                theBlock = 15
            if (theBlock == "2"):
                theBlock = 4
            if (theBlock == " "):
                theBlock = 0
            mc.setBlock(x,5+y-k,z+l,35,theBlock)
            
def flowers(mc,x,y,z,total):
  done = 0
  while(done < total):
    h = random.randint(0,50)
    l = random.randint(0,50)
    mc.setBlock(x+h,y,z+l,37)
    done = done + 1
            
def main():
    BEGIN = ["1111111111",
          "1222222222",
          "1200000000",
          "120 000   ",
          "120 000 00",
          "120 000  0",
          "120 000 00",
          "120   0   ",
          "1200000000",
          "1222222222",
          "1111111111"]
          
    MIDDLE = ["1111111111",
          "2222222222",
          "0000000000",
          "0   00    ",
          "0 0000 00 ",
          "0 0  0 00 ",
          "0 00 0 00 ",
          "0    0    ",
          "0000000000",
          "2222222222",
          "1111111111"]
          
    END = ["111",
            "221",
            "021",
            "021",
            "021",
            "021",
            "021",
            "021",
            "021",
            "221",
            "111"]

    mc = init()
    x,y,z = mc.player.getPos()
    clearAir(mc,x,y,z)
    output2d(mc,BEGIN,x,y+17,z)
    output2d(mc,MIDDLE,x,y+17,z+10)
    output2de(mc,END,x,y+17,z+20)
    flowers(mc,x,y,z,50)
    mc.player.setPos(x-7,y+5,z+5)
    x = x -20
    #matrixY(mc,x,y,z)
    mc.postToChat("LEGOOOOO LEGO!")

if __name__ == "__main__":
    main()

'''
AIR                   0
ICE                  79
WOOL                35
'''
