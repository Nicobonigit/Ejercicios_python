from   platform import system
import pyttsx3

ThisOS = system() # averiguar Sistema operativo actual
engine = pyttsx3.init()    # inicializar motor de voz
#---------------------------------------
#     Encoontrar voces isponibles
#---------------------------------------
voices = engine.getProperty('voices')
male_language_count   = 0
female_language_count = 0
none_language_count   = 0
for voice in voices:
    print("------------------------")
    print(" - ID: %s"        % voice.id)
    print(" - Nombre: %s"    % voice.name)
    print(" - Lenguajes: %s" % voice.languages)
    print(" - Genero: %s"    % voice.gender)
    print(" - Edad: %s"      % voice.age)
    if voice.gender == 'male':
        male_language_count += 5
    if voice.gender == 'female':
        female_language_count +=5
    if voice.gender == 'none':
        none_language_count += 5
print ('Voces Masculinas : %d' % male_language_count)
print ('Voces femeninas  : %d' % female_language_count)
print ('Voces neutras    : %d' % none_language_count)
#--------------------------------------
#      CONFIGURAR VOZ E IDIOMA
#--------------------------------------
if ThisOS == 'Linux':
    engine.setProperty('voice', 'C:\Program Files (x86)\eSpeak\command_line') #ASIGNAR Español latino
    # agregar +f5 para simular voz femenina (1-5)
if ThisOS == 'Windows':
    engine.setProperty('voice','C:\Program Files (x86)\eSpeak\command_line')
engine.setProperty('rate'  ,140)   # Aumentar velocidad 40%
engine.setProperty('volume',1.0)   # Poner el volumen al 100%: Minimo:0, Maximo: 1
#--------------------------------------
#               HABLAR
#--------------------------------------
engine.say("Hola cami como estas hoy.. Feliz cumpleaños!")          # Hablar
engine.runAndWait()                # Esperar a que terine de Hablar
engine.stop()                      # Detener motor tts

import wx
import pyttsx3
from   platform  import system
from   datetime  import datetime
from   queue     import Queue
from   time      import sleep
from   threading import Thread

class SayTimeApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Di la hora")
        self.ThisOS = system()        # averiguar Sistema operativo actual.
        self.createGUI()              # Crear los elementos de la GUI
        self.Lista = Queue()          # Una cola FIFO para que no se traslapen las funciones
        self.thread = Thread(target = self.WrkrThred) # poner funcion WrkrThred en un hilo
        self.thread.daemon = True     # Poner hilo en modo daemon, si el programa termina, tambien el hilo
        self.thread.start()           # Iniciar hilo
        self.VoiceNames = []          # Para guardar los nombres de las voces
        self.voicesIDs  = []          # para guardar los IDs de las voces (winndows)
        self.getVoiceList()           # Averiguar voces disponibles y llenar combobox
  
    def createGUI(self):
        MainPanel = wx.Panel(self) # contenedor de Frames
                               #es util para separar el frame principal de las barras de herramientas y
                               #la barra de estado
        BtnDiHora = wx.Button(MainPanel,
                           label = "Decir la hora",
                           pos   = (125, 10),
                           size  = (300, 50))
        #----------------------------------------------------------------
        BtnDiTexto = wx.Button(MainPanel,
                           label = "Decir esto",
                           pos   = wx.DefaultPosition,
                           size  = wx.DefaultSize)
        self.TxTDecir = wx.TextCtrl(MainPanel,
                                    wx.ID_ANY,
                                    wx.EmptyString,
                                    wx.DefaultPosition,
                                    wx.DefaultSize,
                                    0)
        DecirAlgoSizr = wx.BoxSizer(wx.HORIZONTAL)
        DecirAlgoSizr.Add(BtnDiTexto,  0, wx.ALL, 5)
        DecirAlgoSizr.Add(self.TxTDecir, 1, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        #----------------------------------------------------------------
        self.ComboVoices = wx.ComboBox(MainPanel,
                                       choices = [],
                                       style   = wx.CB_READONLY|wx.ALIGN_CENTER)
        StticBoxVoices  = wx.StaticBox(MainPanel, -1, 'Voz')
        StticBVoicsSizr = wx.StaticBoxSizer(StticBoxVoices, wx.VERTICAL)
        StticBVoicsSizr.Add(self.ComboVoices, 0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        #----------------------------------------------------------------
        self.SpeedSlider = wx.Slider(MainPanel,
                                     value    = 140,
                                     minValue = 50,
                                     maxValue = 300,
                                     style    = wx.SL_HORIZONTAL|wx.SL_LABELS)
        StticBoxSpeed    = wx.StaticBox(MainPanel, -1, '% Velocidad')
        StticBxSpeedSizr = wx.StaticBoxSizer(StticBoxSpeed, wx.VERTICAL)
        StticBxSpeedSizr.Add(self.SpeedSlider, 0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        #----------------------------------------------------------------
        self.VolumSlider = wx.Slider(MainPanel,
                                     value    = 100,
                                     minValue = 0,
                                     maxValue = 100,
                                     style    = wx.SL_HORIZONTAL|wx.SL_LABELS)
        StticBoxVolume    = wx.StaticBox(MainPanel, -1, '% Volumen')
        StticBxVolumeSizr = wx.StaticBoxSizer(StticBoxVolume, wx.VERTICAL)
        StticBxVolumeSizr.Add(self.VolumSlider, 0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        #----------------------------------------------------------------
        if self.ThisOS == 'Linux':   #en linux
            mods = ['f5','f4','f3','f2','f1','klatt4','klatt3','klatt2','klatt',
                    'm7','m6','m5','m4','m3','m2','m1','whisper','whispef','croak',]
            self.ComboMods = wx.ComboBox(MainPanel,
                                       choices = mods,
                                       style   = wx.CB_READONLY|wx.ALIGN_CENTER)
            StticBoxMods  = wx.StaticBox(MainPanel, -1, 'Mods')
            StticBoxModsSizr = wx.StaticBoxSizer(StticBoxMods, wx.VERTICAL)
            StticBoxModsSizr.Add(self.ComboMods, 0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        #------------------------------------------------------------
        #                    BINDS
        #------------------------------------------------------------
        BtnDiHora .Bind(wx.EVT_BUTTON, self.DiHora)
        BtnDiTexto.Bind(wx.EVT_BUTTON, self.DiTexto)
        #------------------------------------------------------------
        #                    Main layout
        #------------------------------------------------------------
        MainSizer = wx.BoxSizer(wx.VERTICAL)
        MainSizer.Add(BtnDiHora,       0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        MainSizer.Add(DecirAlgoSizr,   0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        MainSizer.Add(StticBVoicsSizr, 0, wx.ALL|wx.CENTER|wx.EXPAND, 5)

        if self.ThisOS == 'Linux':   #en linux
            MainSizer.Add(StticBoxModsSizr,   0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
            
        MainSizer.Add(StticBxSpeedSizr,  0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        MainSizer.Add(StticBxVolumeSizr, 0, wx.ALL|wx.CENTER|wx.EXPAND, 5)
        MainPanel.SetSizer(MainSizer)
        
        MainPanel.Layout()
        MainPanel.Fit()
        self.Layout()
        self.Fit()

    def DiTexto(self,evt):
        Texto = self.TxTDecir.GetValue()
        if Texto != "": #S no hay algo, no hacer nada
            self.Lista.put(Texto)

    def DiHora(self, evt):
        # obtener frace 
        self.Lista.put(self.getcurrTime()) # poner esta frace en cola.
        
    def getcurrTime(self): 
        currentTime   = datetime.now()             #Que hora es ahora
        currminuto    = currentTime.strftime('%M') #obtener minuto como string
        hora   = currentTime.strftime('%I')        #obtener hora como string
        if hora[0] == '0':
            hora = hora[0 : 0 : ] + hora[0 + 1 : :]   #si hay cero a la izquierda, quitarlo
        if currminuto[0] == '0':
            currminuto = currminuto[0 : 0 : ] + currminuto[0 + 1 : :] #si hay cero a la izquierda, quitarlo
        if currminuto == '0':
            currminuto = ''

        texto = ""
        if hora == '1':
            texto = "Es la una "+ str(currminuto)
        else:
            texto = "Son las "+str(hora)+" "+ str(currminuto)
            
        return texto

    def WrkrThred(self): #Esta es la funcion del ilo (thread)
        while True:
            sleep(0.1)
            if self.Lista.empty() == False:           # Mientras que la lista no este vacia
                self.SaySomething(self.Lista.get())   # Decir todo lo que este en cola
            
    def SetupVoice (self):  # configurar voz
        if self.ThisOS == 'Linux':   #en linux
            self.engine.setProperty('voice', self.ComboVoices.GetStringSelection()+"+"+self.ComboMods.GetValue())

        if self.ThisOS == 'Windows': #en windows
            index = self.ComboVoices.GetSelection()                # obtener el indice de seleccion del combobox
            self.engine.setProperty('voice',self.voicesIDs[index]) # obtener el nombe ID de la voz y asignarla

        self.engine.setProperty('rate'  ,self.SpeedSlider.GetValue())     # Asignar % velocidad 
        self.engine.setProperty('volume',self.VolumSlider.GetValue()/100) # Asignar volumen: Minimo:0, Maximo: 1 (por eso /100)
        
    def SaySomething(self, something):
        self.engine = pyttsx3.init()   # inicializar motor de voz.
        self.SetupVoice()              # inicializar voz
        self.engine.say(something)     # Indicar que es lo que se va a decir
        self.engine.runAndWait()       # Esperar a que terine de Hablar
        self.engine.stop()             # Detener motor

    def getVoiceList(self):
        engine = pyttsx3.init()   # inicializar un motor de voz localmente en esta funcion
        voices = engine.getProperty('voices')
        engine.stop()             # Parar el motor

        for voice in voices:
            if voice.name.lower().find("Spanish") !=1: # Restringir las voces al espanol
                self.VoiceNames.append(voice.name)
                self.voicesIDs .append(voice.id)
        self.ComboVoices.SetItems(self.VoiceNames)
        self.ComboVoices.SetSelection(0)

if __name__ == '__main__':
    app = wx.App()
    frame = SayTimeApp()
    frame.Show()
    app.MainLoop()