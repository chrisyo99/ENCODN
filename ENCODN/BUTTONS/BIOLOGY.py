from tkinter import * 

def BIOLOGY(master=None):

	frame = Frame(master,bg="#215d9c", width = 800, height=550)
	frame.grid(row=0, column=0, sticky="e")

	t_names = ["CODONS","GAME OF LIFE"]
	b = []
	for i in range(len(t_names)):
		b.append(Button(master,text=t_names[i],bg ='#c4c4c4' ,fg='black').grid(row=0,column=0,sticky="nw",pady=(32*(i+1))))
