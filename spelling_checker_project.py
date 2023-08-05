#Python program to create a Spell Corrector GUI using Tkinter     
from tkinter import *  
from textblob import TextBlob  
  
def clrAll() :  
   
    word1_place.delete(0, END)  
    word2_place.delete(0, END)  
  
def crction() :  
  
    input_wrd = word1_place.get()  
  
    blob_objct = TextBlob(input_wrd)  
  
    crctd_word = str(blob_objct.correct())  
  
    word2_place.insert(10, crctd_word)  
  
  
# Main code  
if __name__ == "__main__" :  

    base = Tk()  

    base.configure(background = 'light green')  

    base.geometry("400x150")  
  
    base.title("Spell Corrector")  
 
    headlbl = Label(base , text = 'Welcome to Spell Corrector Application' ,  
        fg = 'black' , bg = "red")  

    lbl1 = Label(base , text = "Input Word" ,  
        fg = 'black' , bg = 'dark green')  
 
    lbl2 = Label(base , text = "Corrected Word" ,  
        fg = 'black' , bg = 'dark green')  
     
    headlbl.grid(row = 0 , column = 1)  
    lbl1.grid(row = 1 , column = 0)  
    lbl2.grid(row = 3 , column = 0 , padx = 10)  
 
    word1_place = Entry()  
    word2_place = Entry()  
  
    word1_place.grid(row = 1, column = 1, padx = 10, pady = 10)  
    word2_place.grid(row = 3, column = 1, padx = 10, pady = 10)  
  
    
    btn1 = Button(base , text = "Correction" , bg = "red" , fg = "black" ,  
        command = crction)  
    
    btn1.grid(row = 2 , column = 1)  

    btn2 = Button(base , text = "Clear" , bg = "red" ,  
        fg = "black" , command = clrAll)  
   
    btn2.grid(row = 4 , column = 1)  
   
    base.mainloop()