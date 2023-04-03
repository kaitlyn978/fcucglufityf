from tkinter import*
root = Tk()
root.title("Dictionary")
root.geometry("600x600")
colors=["aquamarine","plum","moccasin","medium spring green","tomato","light salmon","medium purple","light sea green","light pink","khaki"]
def p():
    r=random.randint(0,9)
    rd=dictionary(["colors"][rd])
b=Button(root,text="color",command=p)
b.pack()
root.configure("rd")
root.mainloop()