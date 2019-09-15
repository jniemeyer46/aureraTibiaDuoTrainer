from pyautogui import click, typewrite, press
import time
import configs


def MultiLoginAndSetup():
    # Account 1 login
    click(x=102, y=833)

    typewrite(configs.accountName1)
    
    press('tab')
    
    typewrite(configs.password1)

    press('enter')
    time.sleep(1) 
    press('enter')
    time.sleep(1)

    click(button='right', x=947, y=369)
    time.sleep(1)
    click(button='right', x=1849, y=176)
    time.sleep(1)
    click(button='right', x=1766, y=536)

    # account 2 login
    click(x=2006, y=833)

    typewrite(configs.accountName2)
    
    press('tab')
    
    typewrite(configs.password2)

    press('enter')
    time.sleep(1) 
    press('enter')
    time.sleep(1)

    click(button='right', x=2868, y=369)
    time.sleep(1)
    click(button='right', x=3765, y=176)
    time.sleep(1)
    click(button='right', x=3693, y=536)


if __name__ == '__main__':
	MultiLoginAndSetup()