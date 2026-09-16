import pyautogui
import time
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('Google Chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://olist.com/')
pyautogui.press('enter')
pyautogui.click(x=1444, y=129)
pyautogui.click(x=1391, y=248)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('login fábio') #login_tiny
pyautogui.press('tab')
pyautogui.write('senha do fábio') #senha_tiny
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=129, y=316) #cadastros
pyautogui.keyDown('ctrl')
pyautogui.click(x=397, y=216) #produtos
pyautogui.keyUp('ctrl')
pyautogui.click(x=190, y=367) #suprimentos
pyautogui.keyDown('ctrl')
pyautogui.click(x=432, y=211) #ordem_de_compra
pyautogui.click(x=415, y=274) #nota_de_entrada
pyautogui.keyUp('ctrl')
pyautogui.click(x=1003, y=19) #nova_guia
pyautogui.write('https://qive.com.br/') #qive
time.sleep(3)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=1606, y=103) #login
time.sleep(1)
pyautogui.click(x=504, y=293) #email
time.sleep(1)
pyautogui.write('login qive da empresa')
pyautogui.press('tab')
pyautogui.write('senha qive da empresa')
pyautogui.press('enter')
pyautogui.click(x=1205, y=18) #fechar
pyautogui.click(x=1245, y=17) #nova_guia
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
pyautogui.click(x=255, y=18) #fechar_aba_d
pyautogui.click(x=144, y=15)
