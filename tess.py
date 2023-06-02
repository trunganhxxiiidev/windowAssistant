import Speechtotext
import Texttospeech
import speech_recognition as sr
from PIL import ImageTk, Image
import time
import datetime
import wikipedia
from youtube_search import YoutubeSearch
import os
import string
import codecs
from tkinter import *
from gtts import gTTS
import playsound
import pathlib
import tkinter.messagebox
import webbrowser
wikipedia.set_lang('vi')
language = 'vi'

def Main_menu():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("800x650")
    main_screen.title("Menu")
    command=StringVar()
    main_screen.config(background="#A05120")
    Label(text="Select Your Choice", bg="orange", width="300", height="2", font=("Calibri", 16)).pack()
    Label(text="",bg="#A05120").pack()
    Label(text="",bg="#A05120").pack()
    Label(text="",bg="#A05120").pack()
    Button(text="Virtual assistant",bg="orange", height="3", width="40", command = Virtual_assistant,font=("Calibri", 13)).pack()
    Label(text="",bg="#A05120").pack()
    Label(text="",bg="#A05120").pack()
    Label(text="",bg="#A05120").pack()
    Button(text="Train Virutal assistant",bg="orange", height="3", width="40", command=Bot_User_Train,font=("Calibri", 13)).pack()
    Label(text="",bg="#A05120").pack()
    Label(text="",bg="#A05120").pack()
    Label(text="",bg="#A05120").pack()
    Button(text="Exit",bg="orange", height="3", width="40", command=Exit,font=("Calibri", 13)).pack()
    main_screen.mainloop()

def Exit():
 exit(0)

def Virtual_assistant():
    global top
    global listbox
    top= Tk()
    top.geometry("800x650")
    top.title("Virtual assistant")
    top.config(background="#A05120")
    Label(top,bg="orange",width=86,text = "Virtual Assistant").pack()
    listbox=Listbox(top,width=100,height=30)
    listbox.pack()
    Button(top,bg="orange", text="Click", width=10, height=2, command = click).pack()
    Button(top,bg="orange", text="Back", width=10, height=2, command = Back).pack()
    top.mainloop()

def click():
    text = Speechtotext.speech_text()
    listbox.insert(END,"Bạn: "+text)
    listbox.pack()
    if(text=='Wiki'):
        try:
            listbox.insert(END,"Máy: Bạn muốn nghe cái gì ")
            listbox.pack()
            Texttospeech.text_speech("Bạn muốn nghe cái gì ")
            text = Speechtotext.speech_text()
            listbox.insert(END,"Bạn: "+text)
            contents = wikipedia.summary(text).split('\n')
            listbox.insert(END,"Máy: "+contents[0])
            listbox.pack()
            Texttospeech.text_speech(contents[0])
            time.sleep(10)
            for content in contents[1:]:
                listbox.insert(END,"Máy: Bạn muốn nghe thêm không")
                listbox.pack()
                Texttospeech.text_speech("Bạn muốn nghe thêm không")
                ans = Speechtotext.speech_text()
                listbox.insert(END,"Bạn: "+ans)
                if "Có" not in ans:
                 break
                listbox.insert(END,"Máy: "+content)
                listbox.pack()  
                Texttospeech.text_speech(content)
                time.sleep(10)
            listbox.insert(END,"Máy: Cảm ơn bạn đã lắng nghe!!!")
            listbox.pack()
            Texttospeech.text_speech.text_speech('Cảm ơn bạn đã lắng nghe!!!')
        except:
            listbox.insert(END,"Máy: Xin lỗi thuật ngữ của bạn tôi không thể xác định")
            listbox.pack()
            Texttospeech.text_speech.text_speech("Xin lỗi thuật ngữ của bạn tôi không thể xác định")
    elif(text=="Mấy giờ rồi"):
            dt_o = datetime.datetime.today()
            tmp="Bây giờ là "+str(dt_o.hour)+" giờ "+ str(dt_o.minute)+" phút ngày "+str(dt_o.day)+" tháng "+str(dt_o.month)+" năm "+str(dt_o.year)
            listbox.insert(END,"Máy: " +tmp)
            listbox.pack()
            Texttospeech.text_speech(tmp)
    elif(text=="YouTube"):
        listbox.insert(END,"Máy: Bạn muốn tìm video gì?")
        listbox.pack()
        Texttospeech.text_speech("Bạn muốn tìm video gì?")
        text = Speechtotext.speech_text()
        listbox.insert(END,"Bạn: "+text)
        listbox.pack()
        while True:
            result = YoutubeSearch(text, max_results=10).to_dict()
            if result:
              break
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
        listbox.insert(END,"Máy: Tôi đã mở "+ str(text) +" theo yêu cầu của bạn")
        listbox.pack()
        Texttospeech.text_speech("Tôi đã mở "+ str(text) +" theo yêu cầu của bạn")
    elif(text=="tìm kiếm"):
        listbox.insert(END,"Máy: Bạn muốn tìm kiếm gì?")
        listbox.pack()
        Texttospeech.text_speech("Bạn muốn tìm kiếm gì?")
        time.sleep(7)
        text = Speechtotext.speech_text()
        listbox.insert(END,"Bạn: "+text)
        listbox.pack()
        print(text)
        url = 'https://www.google.com/search?q='+text
        driver=webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
        listbox.insert(END,"Máy: Tôi đã mở "+ str(text) +" theo yêu cầu của bạn")
        listbox.pack()
        Texttospeech.text_speech("Tôi đã mở "+ str(text) +" theo yêu cầu của bạn")
    else:
     with open("TiengViet.txt", 'r', encoding='utf8') as r:
        list_text=r.read().splitlines()
     temp=Low(list_text)
     if(text.lower() in temp and temp.index(text.lower())%2==0):
       listbox.insert(END,"Máy: "+list_text[temp.index(text.lower())+1])
       listbox.pack()
       Texttospeech.text_speech(list_text[temp.index(text.lower())+1])
       return
     listbox.insert(END,"Máy: Không hiểu")
     Texttospeech.text_speech("Không hiểu")
     listbox.pack()

def Low(list):
    return [x.lower() for x in list]    

def Bot_User_Train():
   # photo = ImageTk.PhotoImage(Image.open("micro.png"))
    global Train_screen
    Train_screen = Toplevel(main_screen)
    Train_screen.title("Train")
    Train_screen.geometry("500x250")
    Train_screen.config(background="#A05120")
    Label(Train_screen,bg="orange", text="Please Push to train bot").pack()
    Label(text="",bg="#A05120").pack()
    Button(Train_screen,bg="orange", text="User",width=20, height=10, command = User).place(x=40,y=35)
    Button(Train_screen,bg="orange", text="Bot", width=20, height=10, command = Bot).place(x=300,y=35)
    Label(text="",bg="#A05120").pack()
    Button(Train_screen,bg="orange",text="Back" ,width=10, height=1, command=Train_back).place(x=205,y=200)

def User():
    text=Speechtotext.speech_text()
    with open("TiengViet.txt", 'r', encoding='utf8') as r:
         list_text=r.read().splitlines()
    r.close()
    temp=Low(list_text)
    if(text.lower() in temp and temp.index(text.lower())%2==0):
        Found()
        return
    else:
       if(len(list_text)%2!=0):
        print(len(list_text))
        Texttospeech.text_speech("Không hợp lệ")
        return
       with open("TiengViet.txt", 'a', encoding='utf8') as w:
         w.write(text+"\n")
         w.close()
         return    

def Bot():
    text=Speechtotext.speech_text()
    with open("TiengViet.txt", 'r', encoding='utf8') as r:
        list_text=r.read().splitlines()
        if(len(list_text)%2==0):
            print(len(list_text))
            Texttospeech.text_speech("Không hợp lệ")
            return
    with open("TiengViet.txt", 'a', encoding='utf8') as w:
         w.write(text+"\n")
         w.close()
         Texttospeech.text_speech(text)
         return

def Found():
   global Show_found_success_screen
   Show_found_success_screen=Toplevel(Train_screen)
   Show_found_success_screen.title("Result")
   Show_found_success_screen.geometry("300x150")
   Label(Show_found_success_screen, text="Found Question!").pack()
   Button(Show_found_success_screen, text="OK", command=delete_found_success).pack()

def delete_found_success():
    Show_found_success_screen.destroy()

def Train_back():
    Train_screen.destroy()

def Back():
    top.destroy()
Main_menu()
