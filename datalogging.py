from microbit import *
# write to a csv file(create a new one if not existed).
# every 10 seconds write compass heading and temperature to the file.
# press a to display the latest record
def wd():
    with open('data.csv', 'w') as f:
        temp = temperature()
        comp = compass.heading()
        # this sentence below is used to test if the data keeps refreshing.
        print(comp, temp, sep=',')
        dat = (str(comp) + ',' + str(temp))
        f.write(dat)
        display.scroll(dat)

while True:
    wd()
    sleep(7000)
# :/ i haven't figured out how to stop sleeping by pressing a button.