import tkinter as tk

        

            
    
class CFG:
    #inputlari list turune donusturuyor
    def stringtolist(self,text):
        lists=[]
        start=0
        for i in range(0,len(text)):
            if(text[i]=='|'):
                lists.append(text[start:i])
                start=i+1;
        lists.append(text[start:len(text)])
        return lists
    #list degisken türü ile bir agac yapisi olurturuyor
    def creatertree(self,listx,listy):
        temp=""
        templist=[]
        for i in listy:
            if(i.count('X')>0):
                
                for j in range(0,len(listx)):
                    
                  temp=i.replace('X',listx[j],1)
                  templist.append(temp)
                  
                print(templist)
                self.listree.append(templist)
                self.creatertree(listx,templist)
                templist=[]
                
            
                 
                 
    def __init__(self):
        self.listree=[]
        self.root=tk.Tk()
        self.root.wm_title("context free grammar")
        self.root.geometry('{}x{}'.format(450, 350))
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        #penceyi iki frame boluyoruz
        self.Topframe=tk.Frame(self.root, bg='lavender', width=450, height=200, pady=3)
        self.Botframe=tk.Frame(self.root, bg='lavender', width=450, height=150,)
        self.Botframe.grid(row=1 ,sticky="ew")
        self.Topframe.grid(row=0, sticky="ew")
        self.lbls=tk.Label(self.Topframe,text="S=" ,fg="blue",font=("Helvetica",16)).grid(row=0,column=0)
        self.lblx=tk.Label(self.Topframe,text="X=",fg="blue",font=("Helvetica",16)).grid(row=1,column=0)
        
        self.entitys=tk.Entry(self.Topframe)
        self.entitys.grid(row=0,column=1)
        self.entityx=tk.Entry(self.Topframe)
        self.entityx.grid(row=1,column=1,sticky='W')
        
        self.lblhata=tk.Label(self.Topframe,text="")
        self.lblhata.grid(row=2,column=0)
       
        #tablo olusturmak icin button
        self.btnshow=tk.Button(self.Topframe,text='Devamet',command=self.cfg).grid(row=2,column=3)
    def cfg(self):
        self.listree=[]
        self.stringS=self.entitys.get()
        self.stringX=self.entityx.get()
 
        self.listx=self.stringtolist(self.stringX)
        self.listy=self.stringtolist(self.stringS)
        self.listree.append(self.listy)
        self.creatertree(self.listx,self.listy)
        
        self.sonuc=""
        self.tekrar=""
        counter=0
        kontrol=False
        #agac yapisindan olusan kelimeleri ekrana yazmamizi sagliyor
        for i in self.listree:
            
            for j in i:
               
                if(j.count('X')==0):
                    
                    self.sonuc+=" "+j
                    
                elif(j.count('X')==2):
                    kontrol=True
                    counter=2
                    self.tekrar=""
            if(kontrol==True and counter==0):
                
                for k in i:
                    if(k.count('X')==0):
                      self.tekrar+=" "+k
            elif(kontrol==True and counter!=0):
                counter=counter-1
            elif(kontrol==False):
                self.tekrar="Tetrarlanan kelime bulunamadi"
                    

            
                
            
                   
        self.lblsonuc=tk.Label(self.Botframe,text="Verilen CFG için üretilen kelimeler:" ,fg="blue",font=("Helvetica",16)).grid(row=0,column=0)
        self.lblss=tk.Label(self.Botframe,text=self.sonuc,fg="red",font=("Helvetica",12)).grid(row=1,column=0)
        self.lbltekrar=tk.Label(self.Botframe,text="Tekrarlanan kelimeler: " ,fg="blue",font=("Helvetica",16)).grid(row=2,column=0)
        self.lblt=tk.Label(self.Botframe,text=self.tekrar,fg="red",font=("Helvetica",12)).grid(row=3,column=0)
        
        
        
a=CFG();
a.root.mainloop()
