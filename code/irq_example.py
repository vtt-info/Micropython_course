##example of using irq and callback
import machine

interruptCounter = 0
totalInterruptsCounter = 0

timer = machine.Timer(0)

def handleInterrupt(timer):
  global interruptCounter
  interruptCounter = interruptCounter+1

timer.init(period=10000, mode=machine.Timer.PERIODIC, callback=handleInterrupt)

while True:
  if interruptCounter>0:
    state = machine.disable_irq()
    interruptCounter = interruptCounter-1
    machine.enable_irq(state)

    #do something here

    totalInterruptsCounter = totalInterruptsCounter+1
    print("Interrupt has occurred: " + str(totalInterruptsCounter))
    machine.idle()
