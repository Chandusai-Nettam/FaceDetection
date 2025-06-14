import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox

class face_Detector:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1200+0+0")
        self.root.title("Face Detector")
        self.root.config(bg="BLACK")
        self.root.wm_iconbitmap(r"D:\projects\sahithi\face.ico")

        title_lbl=Label(text="FACE DETECTOR",font=("Bold",45 ,"bold"),bg="black",fg="gold") 
        title_lbl.place(x=-100,y=0,width=1730,height=50)
        
        img=Image.open(r"D:\projects\sahithi\krishna.PNG")
        img=img.resize((1700,900),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=50,width=1700,height=900)
        
        
        
        b1=Button(f_lbl,text="FACE DETECTION WITH WEBCAM",command=self.face_recog,font=("Dancing Script",13 ,"bold"),bg="dark green",fg="white",cursor="hand2")
        b1.place(x=150,y=470,width=350,height=30)

        b2=Button(f_lbl,text="FACE DETECTION WITH LOCAL IMAGE",command=self.face_img,font=("Dancing Script",13 ,"bold"),bg="dark green",fg="white",cursor="hand2")
        b2.place(x=550,y=470,width=350,height=30)

        b2=Button(f_lbl,text="ABOUT",command=self.about,font=("Dancing Script",13 ,"bold"),bg="dark green",fg="white",cursor="hand2")
        b2.place(x=470,y=570,width=100,height=30)

        b1=Button(f_lbl,text="WELCOME TO FACE DETECTION!!!",font=("Dancing Script",20 ,"bold"),bg="WHITE",fg="BLACK")
        b1.place(x=300,y=100,width=490,height=40)
    def face_recog(self):

        faceCascade = cv2.CascadeClassifier(r"D:\projects\sahithi\haarcascade_frontalface_default.XML")
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
        
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )  
            for (x, y, h) in faces:
                cv2.rectangle(frame, (x, y), (x, y+h), (0, 255, 0), 2)
            cv2.imshow('FACE__DETECTION', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        video_capture.release()
        cv2.destroyAllWindows()
        
        print(f"{len(faces)} faces detected in the image")
        messagebox.showinfo("RESULT",f"FACES FOUND:{len(faces)}") 
    def face_img(self):  
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select image to detect",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print (root.filename)
        faceCascade = cv2.CascadeClassifier(r"D:\projects\sahithi\haarcascade_frontalface_default.XML")
        image = cv2.imread(root.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        print(f"{len(faces)} faces detected in the image")
        messagebox.showinfo("RESULT",f"FACES found:{len(faces)}")

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:

            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Faces found", image)
        cv2.waitKey(1) & 0xFF == ord('s')

    def about(self): 
        im = Image.open(r"C:\Users\sahit\OneDrive\Pictures\Screenshots\2023-01-24 (1).png") 
        im.show()
          
    
if __name__ == "__main__":
    root=Tk()
    obj=face_Detector(root)
    root.mainloop()  
