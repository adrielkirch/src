
import dateUtil
import time
import pyautoguiUtil
import pyautogui
import pyperclip
import tkinter as tk
tinker = tk.Tk()
pyautogui.PAUSE = 0.5



def openChrome():
    pyautogui.press('win')
    pyautogui.write('Chrome')
    pyautogui.press('enter')
    time.sleep(2)


def publishPrinterest(publication,altTab = False):
    if altTab:
        pyautogui.hotkey('alt', 'tab')

    pyautogui.write('https://br.pinterest.com/pin-builder/')
    pyautogui.press('enter')
    time.sleep(3)

    for i in range (0,17):
        pyautogui.press('tab')

    pyautogui.PAUSE = 1
    pyautoguiUtil.copyAndPaste(publication['title'],2)
    pyautogui.press('tab')

    # pyperclip.copy(publication['descrição'])
    # time.sleep(1)
    # pyautogui.hotkey('ctrl','v')
    # time.sleep(1)
    # pyautogui.press('tab')
    # pyautogui.press('tab')
    # pyautogui.press('enter')

    # pyperclip.copy(publication['descrição2'])
    # time.sleep(1)
    # pyautogui.hotkey('ctrl','v')
    # time.sleep(1)
    # pyautogui.press('tab')


    # pyperclip.copy(publication['url'])
    # time.sleep(1)
    # pyautogui.hotkey('ctrl','v')
    # time.sleep(1)

    # pyautogui.hotkey('ctrl','f')
    # pyautogui.write('arraste e solte ou clique')
    # pyautogui.click(x=618, y=545)
    # time.sleep(1)
    # pyperclip.copy(dateUtil.today())
    # time.sleep(1)
    # pyautogui.hotkey('ctrl','v')
    # time.sleep(1)
    # pyautogui.press('down')
    # time.sleep(1)
    # pyautogui.press('enter')

    # pyautogui.hotkey('ctrl','f')
    # pyautogui.write('Publicar')
    # pyautogui.press('enter')
    # pyautogui.press('enter')
    # pyautogui.click(x=1468, y=528)

publication = {
    "title": "Por que criar um site?",
    "descrição": "O InternetLiveStats estima que mais de 4 bilhões de pessoas pesquisam na web todos os dias . Isso é mais da metade da população global. Assim, possuir um site ou uma página web é fundamental para qualquer negócio, independente da natureza da organização. 🐵🚀 A criação de um webSite talvez seja a forma mais indicada e com melhor custo benefício para iniciar um projeto digital, não importa qual o tamanho da empresa, ou a segmentação. Saiba mais: https://gorilafreela.com.br",
    "descrição2": "A importância de um site para sua empresa.",
    "url":"https://gorilafreela.com.br",
    "type": "jpg"
}

openChrome()
publishPrinterest(publication)
