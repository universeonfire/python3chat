import socket
from tkinter import *
import tkinter
from threading import Thread

def receive():
	while True:
		try:
			mess = clientSocket.recv(1024)
			messageList.insert(tkinter.END,mess)
		except:
			print("bir hata oluştu!")
			break	

def send_message():
	my_msg = messages.get()
	messages.set("")
	clientSocket.send(my_msg.encode())
	if my_msg=="#quit":
		clientSocket.close()
		window.quit()

def on_closing():
	messages.set("#quit")
	send_message()


window = Tk()

window.title("Sohbet Odası")
window.configure(bg="blue")
messageFrame = Frame(window,height=200,width=200,bg="yellow")
messages = StringVar()
messages.set("")
scrollBar=Scrollbar(messageFrame)
messageList = Listbox(messageFrame, height= 30, width=100, bg="white",yscrollcommand=scrollBar.set)
scrollBar.pack(side=RIGHT,fill=Y)
messageList.pack(side=LEFT,fill=BOTH)
messageFrame.pack()
buttonLabel = Label(window,text="Mesajını Yaz",fg="blue",font="Aerial",bg="red")
buttonLabel.pack()
entryField = Entry(window,textvariable=messages,fg="red",width=50)
entryField.pack()
sendButton = Button(window,text="Yolla",bg="green",font="Aerial",fg="white", command=send_message)
sendButton.pack()
quitButton = Button(window,text="Çıkış",bg="green", font="Aerial",fg="white", command=on_closing)
quitButton.pack()
window.protocol("WM_DELETE_WINDOW",on_closing)

host = "localhost"
port = 8080
clientSocket = socket.socket()

clientSocket.connect((host,port))

receive_thread=Thread(target=receive)
receive_thread.start()



mainloop()