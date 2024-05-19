import time

from uiautomator import Device

device = Device()
device.wakeup()

device(text='微信').click()

# device(scrollable=True).scroll.vert.toBeginning()
print(device.dump())
time.sleep(1)
while True:
    yue = device(index='23')
    if yue.exists:
        yue.click()
        break
    else:
        device(scrollable=True).scroll.vert.forward()
print(device.dump())
time.sleep(1)
while True:
    msgInput = device(resourceId='com.tencent.mm:id/bkk')
    if msgInput.exists:
        time.sleep(1)
        msgInput.set_text('晚安')
        time.sleep(1)
        device(text='发送').click()
    time.sleep(5)


