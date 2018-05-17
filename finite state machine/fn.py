import tkinter as tk
import state
import pygame
#arayuz ve bazı ilskilerin tanımlandıgı class
class fn:
    def __init__(self):
       #pencere olusturdugu bolum
       self.root=tk.Tk()
       self.root.wm_title("finite state machine App")

       self.root.geometry('{}x{}'.format(450, 350))

       self.root.grid_rowconfigure(1, weight=1)
       self.root.grid_columnconfigure(0, weight=1)
       #penceyi iki frame boluyoruz
       self.Topframe=tk.Frame(self.root, bg='lavender', width=450, height=200, pady=3)
       self.Botframe=tk.Frame(self.root, bg='lavender', width=450, height=150,)
       self.Botframe.grid(row=1 ,sticky="ew")
       self.Topframe.grid(row=0, sticky="ew")
       #alfabe,durumlar icin label ve entity
       
       self.lblAlfabe=tk.Label(self.Topframe,text="Alfabeyi giriniz:",fg="red",font=("Helvetica",14)).grid(row=0,column=0)
       self.lblgecisler=tk.Label(self.Topframe,text="Durumlar kümesini giriniz:",fg="red",font=("Helvetica",14)).grid(row=1,column=0)
       self.lblbaslangic=tk.Label(self.Topframe,text="Başlangıç durumunu giriniz:",fg="red",font=("Helvetica",14)).grid(row=2,column=0)
       self.lblbitis=tk.Label(self.Topframe,text="Bitiş durumunu giriniz:",fg="red",font=("Sunflowers",14)).grid(row=3,column=0)
       self.entityalfabe=tk.Entry(self.Topframe)
       self.entityalfabe.grid(row=0,column=1)
       self.entitydurum=tk.Entry(self.Topframe)
       self.entitydurum.grid(row=1,column=1,sticky='W')
       self.entitybaslangic=tk.Entry(self.Topframe)
       self.entitybaslangic.grid(row=2,column=1)
       self.entitybitis=tk.Entry(self.Topframe)
       self.entitybitis.grid(row=3,column=1)
       self.lblhata=tk.Label(self.Topframe,text="")
       self.lblhata.grid(row=4,column=0)
       
       #tablo olusturmak icin button
       self.btnshow=tk.Button(self.Topframe,text='Devamet',command=self.tablo).grid(row=4,column=3)
       
       self.root.mainloop()
       #tablonun olusturdugu fonksiyon
    def tablo(self):
        self.dil=[]
        self.baslangic=self.entitybaslangic.get()
        self.bitis=self.entitybitis.get()
        durum=self.entitydurum.get()
        s=0
        alfabe=self.entityalfabe.get()
        if(self.baslangic=="" or self.bitis=="" or alfabe=="" or durum==""):
            self.lblhata["text"]="tüm alanları doldulun";
        else:   
         for i in range(0,len(alfabe)):
          if(alfabe[i]==','):
              self.dil.append(alfabe[s:i])
              s=i+1
         self.dil.append(alfabe[s:])
         print("Dil:")
         print(self.dil)
         self.durum=[]
        
        
         s=0;
         for i in range(0,len(durum)):
          if(durum[i]==','):
              self.durum.append(durum[s:i])
              s=i+1
         self.durum.append(durum[s:])    
         print("Durumlar:")
         print( self.durum)
         self.tablo=[]
        
         lbltble=tk.Label(self.Botframe,text="Durumlar arası geçişleri giriniz:")
         lbltble.grid(row=0,column=1)
         lblstate=tk.Label(self.Botframe,text="state")
         lblstate.grid(row=1,column=0)
         lbla=tk.Label(self.Botframe,text=self.dil[0]+"'okunduktan sonra")
      
         lbla.grid(row=1,column=1)
         lblb=tk.Label(self.Botframe,text=self.dil[1]+"' okunduktan sonra")
      
         lblb.grid(row=1,column=2)
         for item in range(0,len(self.durum)):
           if(self.durum[item]==self.baslangic):
              lbl=tk.Label(self.Botframe,text="->"+self.durum[item])
           elif(self.durum[item]==self.bitis):
               lbl=tk.Label(self.Botframe,text="*"+self.durum[item])
           else:
            lbl=tk.Label(self.Botframe,text=self.durum[item])
            
           lbl.grid(row=item+2,column=0)
           lbl.attr=item
           entity=tk.Entry(self.Botframe)
           entity.grid(row=item+2,column=1)
           entity.attr=str(item)+"a"
          
           self.tablo.append(entity)
           entity=tk.Entry(self.Botframe)
           entity.grid(row=item+2,column=2)
           entity.attr=(str(item))+"b"
           self.tablo.append(entity)
            
        self.btncreat=tk.Button(self.Botframe,text='Devamet',command=self.fncreater).grid(row=len(self.durum)+2,column=4)
        #statelerin  olusturdugu fonksiyon
    def fncreater(self):
        pygame.init()
        textcolor =   (255, 0,  0)
        color =  (0,   0, 0)
        WHITE = (255, 255, 255)
        screen=pygame.display.set_mode((640,480))
        self.state=[]
        screen.fill(WHITE)
        q=None
        for i in range(0,len(self.durum)):
            if(self.durum[i]==self.baslangic):
                
                q=state.state(self.durum[i],100+50*i*2,250,True,False,screen,color, textcolor)
            elif(self.durum[i]==self.bitis):
                
                q=state.state(self.durum[i],100+50*i*2,250,False,True,screen,color, textcolor)
            else:
                 q=state.state(self.durum[i],100+50*i*2,250,False,False,screen,color, textcolor)
            q.attr=i
            #statelerin tutuldugu liste
            self.state.append(q)
            
       
        count=0
        self.geciskümeleri=[]
        self.stategecis=[]
        for c in range(0,len(self.durum)):
                
                x=[self.durum[c],self.dil[0],self.tablo[count].get()]
                self.stategecis.append(x)
                x=None
                x=[self.durum[c],self.dil[1],self.tablo[count+1].get()]
                self.stategecis.append(x)
                count=count+2
                self.geciskümeleri.append(self.stategecis)
                #geçislerin tutuldugu liste
                self.stategecis=[]
                
        print("gecisler:")
        print(self.geciskümeleri)
        
        for i in range(0,len(self.geciskümeleri)):
         if(self.geciskümeleri[i][0][2]==self.geciskümeleri[i][1][2]):
                       for item in self.state:
                          if(item.title==self.geciskümeleri[i][0][2]):
                            state.draw(screen,[self.state[i].x,self.state[i].y],[item.x,item.y],self.dil[0]+" ,"+self.dil[1])
                            
         else:
             for j in self.geciskümeleri[i]:   
                         for item in self.state:
                            if(item.title==j[2]):
                              state.draw(screen,[self.state[i].x,self.state[i].y],[item.x,item.y],"  "+j[1]+"  ")
        
        self.Botframe.destroy()                  
        self.Botframe=tk.Frame(self.root, bg='lavender', width=450, height=150,)
        self.Botframe.grid(row=1 ,sticky="ew")
        
        
        
        lbl=tk.Label(self.Botframe,text="Test kelimesi:")
            
        lbl.grid(row=5,column=0)
        self.test=tk.Entry(self.Botframe)
        self.test.grid(row=5,column=2)
        
        self.btntest=tk.Button(self.Botframe,text='Devam',command=self.teststring).grid(row=5,column=3)
        #Test kısmı kullanıcıdan alınan degerlerin denendiği kısım
    def teststring(self):
       test=self.test.get()
       
       sonuc=""
       item=None
       msj=""
       for i in self.state:
          
           if(i.start==True):
              
               item=i.title
       sonuc=item
       for j in test:
          
        for c in self.geciskümeleri:
            
            if(c[0][0]==item):
               if(c[0][1]==j):
                sonuc=sonuc +  "->"+c[0][2]
                item=c[0][2]
                
                break
               elif(c[1][1]==j):
                   sonuc=sonuc +  "->"+c[1][2]
                   item=c[1][2]
                   
                   break
          
       if(item==self.bitis) :
            msj="Bitiş durumuna ulaşıldı FA kelimeyi kabul eder"
       else:
        msj="Bitiş durumuna ulaşılmadı FA kelimeyi kabul etmez"
        
       sc=tk.Tk()
       sc.wm_title("FN-Sonuc")
       self.root.grid_rowconfigure(1, weight=1)
       self.root.grid_columnconfigure(0, weight=1)
       lbl= lbl=tk.Label(sc,text="Geçisler:"+sonuc)
            
       lbl.grid(row=1,column=0)
       lbl=tk.Label(sc,text=msj)
            
       lbl.grid(row=2,column=0)    
       sc.mainloop()   
                    
                    
        
a=fn()
a.root.mainloop()


        
    
    
