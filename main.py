import kivy
import random
import pyperclip as pc
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
import os
import sys

black = "#000000"
grey = "#adb4b4"
brighestGrn = "#04ca9f"

Window.clearcolor = black 
Window.size = (1150, 500)

keyDict = {
}

global keyStr
keyStr = 0

global message
message = 0

class loadUpWindow(Screen):

    def generateKey(self):

        tempDict = {
        }
 
        formattedChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
        possibleChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')' , ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        possibleCharsLen = len(possibleChars)


        random.shuffle(possibleChars)
        random.shuffle(formattedChars)

        for i in range (possibleCharsLen):
            randomLetter = possibleChars[0+i]
            formattedLetter = formattedChars[0+i]
    
            tempDict.update({formattedLetter: randomLetter})
            keyPC = list(tempDict.values())
            keyLen = len(keyPC)
            keyFC = list(tempDict.keys())

        keyFCStr = ''.join(keyFC) 
        keyPCStr = ''.join(keyPC) 


        fullKey = (keyFCStr + keyPCStr)
        global keyDict
        keyDict = tempDict

        global keyStr
        keyStr = fullKey
    
        sm.current = "mainMenu"
        self.ids.encryptionKeyLbl.text = keyStr
        self.manager.get_screen('mainMenu').labelText = keyStr
        self.manager.get_screen('encryptMesScr').labelText = keyStr
        self.manager.get_screen('decryptMesScr').labelText = keyStr
    
    def importKeyBtn(self):
        sm.current = "importKeyScr"
            
class mainMenuWindow(Screen):
    labelText = StringProperty('')

    def loadUpBtn(self):
        sm.current = "loadUp"

    def EncryptMesScrnBtn(self):
        sm.current = "encryptMesScr"

    def decryptMesScrBtn(self):
        sm.current = "decryptMesScr"

    def exportKeyBtn(self):
        if os.path.exists("exportedKey.txt"):
            os.remove("exportedKey.txt")
            f = open("exportedKey.txt", "a")
            f.write(keyStr)
            f.close()
            ExportKeyPopup().open() 
        else:
            f = open("exportedKey.txt", "a")
            f.write(keyStr)
            f.close() 

    def importGenerateBtn(self):
        sm.current = "loadUp"
    
    def importMessageFileBtn(self):
        sm.current="importFileScr"   

    def quitBtn(self):
        sys.exit()

    def copy2CB(self):
        pc.copy(keyStr)
        
class importKeyWindow(Screen):
    importKey = ObjectProperty(None)

    def importKeyBtn(self):
        importedKey = self.importKey.text.strip('\n')


        keyLen = len(importedKey)

        if keyLen != 144:
            self.importKey.text = ""
            self.importKey.hint_text = "Error: Please Check Your Key And Try Again"
        elif keyLen == 144:
            keyLists = [(importedKey[i:i+72]) for i in range(0, keyLen, 72)]
            formattedChars = keyLists[0]
            randomChars = keyLists[1]
            keyListsLen = 72
            for i in range (keyListsLen):
                randomLetter = randomChars[0+i]
                formattedLetter = formattedChars[0+i]
                keyDict.update({formattedLetter: randomLetter})
            keyExport = importedKey
            keyExportStr = keyExport

            global keyStr
            keyStr = keyExportStr

            self.manager.get_screen('mainMenu').labelText = keyStr
            self.manager.get_screen('encryptMesScr').labelText = keyStr
            self.manager.get_screen('decryptMesScr').labelText = keyStr
            sm.current ="mainMenu"

    def generateKey(self):

        tempDict = {

        }
 
        formattedChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
        possibleChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')' , ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        possibleCharsLen = len(possibleChars)

        random.shuffle(possibleChars)
        random.shuffle(formattedChars)

        for i in range (possibleCharsLen):
            randomLetter = possibleChars[0+i]
            formattedLetter = formattedChars[0+i]
    
            tempDict.update({formattedLetter: randomLetter})
            keyPC = list(tempDict.values())
            keyLen = len(keyPC)
            keyFC = list(tempDict.keys())

        keyFCStr = ''.join(keyFC) 
        keyPCStr = ''.join(keyPC) 


        fullKey = (keyFCStr + keyPCStr)
        global keyDict
        keyDict = tempDict

        global keyStr
        keyStr = fullKey
    
        sm.current = "mainMenu"
        self.manager.get_screen('mainMenu').labelText = keyStr
        self.manager.get_screen('encryptMesScr').labelText = keyStr
        self.manager.get_screen('decryptMesScr').labelText = keyStr

class encryptMessageWindow(Screen):
    
    encryptMesChangeTitle = StringProperty()
    labelText = StringProperty('')
    mes2Encrypt = ObjectProperty(None)

    class EncryptButton(Button):
        action = ObjectProperty()
        mes2encrypt = ObjectProperty(None)

        def encrypt(self, ti):
            self.action = self.export
            self.text = "Export"
            self.background_color = ("red")    
            message2En = ti.text
            def get_key(val):
                for key, value in keyDict.items():
                    if val == value:
                        return key
                return "key doesn't exist"
            tempArray = []
            wordCount = len(message2En)
            def wordChange (wordCount):
                for i in range(wordCount):
                    word = list(message2En[0+i])
                    wordLen = len(word)
                    for i in range (wordLen):
                        WordComplete = (keyDict[word[0 + i]])
                        tempArray.append(WordComplete)
                        encryptedMessage = ''.join(tempArray)
                global message
                message = encryptedMessage
                ti.text = ""
                ti.text = message
            wordChange(wordCount)

        def export(self, ti):

            self.action = self.encrypt
            self.text = "Encrypt"
            self.background_color = ("#04ca9fff")
            if os.path.exists("message.txt"):
                os.remove("message.txt")
                f = open("message.txt", "a")
                line1 = str((keyStr) + "\n")
                line3 = message
                f.writelines([line1, line3])
                f.close()
            else:
                f = open("message.txt", "a")
                line1 = str((keyStr) + "\n")
                line3 = message
                f.writelines([line1, line3])
                f.close()
            ti.text=""
            ExportedMessagePopup().open()
            sm.current = "mainMenu"

    def menuBtn(self):
        sm.current="mainMenu"
        self.mes2Encrypt.text = ""

    def copy2CB(self):
        pc.copy(keyStr)

class decryptMessageWindow(Screen):
    labelText = StringProperty('')
    mes2Decrypt = ObjectProperty(None)

    def decryptMesBtn(self):
        decryptMes = self.mes2Decrypt.text
        tempArray = []
        messageToDecrypt = decryptMes
        wordCount = len(messageToDecrypt)

        def find_key(v): 
            for k, val in keyDict.items(): 
                if v == val: 
                    return k 
            return "Key does not exist"

        for i in range (wordCount):
            newChar = str((messageToDecrypt[0+i]))
            result = find_key(newChar)
            tempArray.append(result)
            decryptedMes = ''.join(tempArray)
        self.manager.get_screen('decryptMesScr').resultTextDecrypt = decryptedMes
        self.mes2Decrypt.text = ""
        self.mes2Decrypt.text = decryptedMes
            

    def menuBtn(self):
        sm.current="mainMenu"
        self.mes2Decrypt.text = ""

    def copy2CB(self):
        pc.copy(keyStr)

class ExportKeyPopup(Popup):
    pass

class ExportedMessagePopup(Popup):
    pass

class ImportFileWindow(Screen):

    impFileKeyLbl = StringProperty("")
    impFileMesLbl = StringProperty("")

    def importBtn(self):
        if os.path.exists("message.txt"):
            with open('message.txt') as f:
                contents = f.readlines()
                importedKey = contents[0].strip('\n')
                global keyStr
                keyStr = importedKey
                importedMessage = contents[1]

                def importKey4Mes(self):
                    keyLen = len(importedKey)

                    if keyLen != 144:
                        self.manager.get_screen('importFileScr').impFileKeyLbl = "Error"

                    elif keyLen == 144:
                        keyLists = [(importedKey[i:i+72]) for i in range(0, keyLen, 72)]
                        formattedChars = keyLists[0]
                        randomChars = keyLists[1]
                        keyListsLen = 72
                        for i in range (keyListsLen):
                            randomLetter = randomChars[0+i]
                            formattedLetter = formattedChars[0+i]
                            keyDict.update({formattedLetter: randomLetter})
                        self.manager.get_screen('importFileScr').impFileKeyLbl = keyStr


                        self.manager.get_screen('mainMenu').labelText = keyStr
                        self.manager.get_screen('encryptMesScr').labelText = keyStr
                        self.manager.get_screen('decryptMesScr').labelText = keyStr

                importKey4Mes(self)

                def decryptMes4Mes(self):
                    tempArray = []
                    messageToDecrypt = importedMessage
                    wordCount = len(messageToDecrypt)

                    def find_key(v):
                        for k, val in keyDict.items():
                            if v == val:
                                return k
                        return "Key does not exist"

                    for i in range (wordCount):
                        newChar = str((messageToDecrypt[0+i]))
                        result = find_key(newChar)
                        tempArray.append(result)
                        decryptedMes = ''.join(tempArray)
                    self.manager.get_screen('importFileScr').impFileMesLbl = decryptedMes         
                decryptMes4Mes(self)


    def menuBtn(self):
        sm.current="mainMenu"
        self.manager.get_screen('importFileScr').impFileKeyLbl = ""
        self.manager.get_screen('importFileScr').impFileMesLbl = ""
     
class ImportedMessageFilePopup(Popup):
    messageLbl = StringProperty('')
    

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

sm = WindowManager()
sm.add_widget(loadUpWindow(name='loadUp'))
sm.add_widget(mainMenuWindow(name='mainMenu'))
sm.add_widget(importKeyWindow(name="importKeyScr"))
sm.add_widget(encryptMessageWindow(name="encryptMesScr"))
sm.add_widget(decryptMessageWindow(name="decryptMesScr"))
sm.add_widget(ImportFileWindow(name="importFileScr"))

class MyMainApp(App):

    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()