import wx
import analyse #soundanalyse
import Layout as ly  # Layout code generated by wxGlade
import gettext # for localisation shit required by wxGlade
import numpy,time ,math
import alsaaudio 
import threading 
from multi_key_dict import multi_key_dict #this lib allow to point multiple keys to a value which is not realized in standart dictionary lib

#note_dict is a dictionary of midi key values which point to a note
note_dict = multi_key_dict()
note_dict[0,12,24,36,48,60,72,84,96,108,120] = "C"
note_dict[1,13,25,37,49,61,73,85,97,109,121] = "C#"
note_dict[2,14,26,38,50,62,74,86,98,110,122] = "D"
note_dict[3,15,27,39,51,63,75,87,99,111,123] = "D#"
note_dict[4,16,28,40,52,64,76,88,100,112,124]= "E"
note_dict[5,17,29,41,53,65,77,89,101,113,125]= "F"
note_dict[6,18,30,42,54,66,78,90,102,114,126]= "F#"
note_dict[7,19,31,43,55,67,79,91,103,115,127]= "G"
note_dict[8,20,32,44,56,68,80,92,104,116] =    "G#"
note_dict[9,21,33,45,57,69,81,93,105,117] =    "A"
note_dict[10,22,34,46,58,70,82,94,106,118]=    "A#"
note_dict[11,23,35,47,59,71,83,95,107,119]=    "B"



def set_input_list():
    input_devices_list = get_input_devices()
    for i in input_devices_list :
        frame.input_list.Append(i)
        
    frame.input_list.SetSelection(0)
    #print frame.input_list.GetSelection()
    
def get_input_devices ():
        return alsaaudio.pcms(alsaaudio.PCM_CAPTURE) 
        # TODO  too many devices are being shown

def show_derivation(pitch):
    """ Show first 2 decimal numbers as derivation """
    if pitch is None:
        frame.derivation.SetLabel("0")
    else:
        frac,whole = math.modf(pitch)

        deriv = ""
        for i in range(2,4) :
            str_frac = str(frac)
            deriv +=str_frac[i]
        
        frame.derivation.SetLabel(deriv)


   
def get_midi_note(pitch):
    """From float pitch this func is  returning  int midi note or None if the pitch is also None"""
    
    if pitch != None:
        frac,whole = math.modf(pitch)
         
        if frac <= 0.5 :
            note = int(whole)
        else :
            note = int(whole) +1
         
    else:
        note = None
    return note
 

def show_note(pitch):
    midi_note = get_midi_note(pitch)
    try:
          
        frame.note.SetLabel(str(note_dict[midi_note])) #this part will throw an exception if midi_note is None
        frame.midi_note.SetLabel(str(midi_note)) #Should be placed bellow note.SetLabel 
    except:
        global count_none
        count_none +=1
        if count_none >= 100 :
            count_none = 0
            frame.note.SetLabel("None")
            frame.midi_note.SetLabel("None") 



def start_stream ():
    """This function should be executed in a separated thread because of infinite loop"""
    inp = alsaaudio.PCM(type= alsaaudio.PCM_CAPTURE, mode=alsaaudio.PCM_NORMAL,device='default')
    inp.setchannels(1)
    inp.setrate(44100)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(1024)
     
    while True:
            length, data = inp.read()
            samps = numpy.fromstring(data, dtype='int16') 

            pitch = analyse.musical_detect_pitch(samps)          
            wx.CallAfter(show_derivation,pitch )  #CallAfter is necessary for making GUI method calls from non-GUI threads    
            wx.CallAfter(show_note,pitch) # pitch is passed as an argument
            


count_none= 0

if __name__ == "__main__":
    gettext.install("app") 
    
    app = wx.App()
    frame = ly.MainFrame(None, wx.ID_ANY )
    #####start code inserting #####

    
    

    set_input_list()
    detect_pitch_thread = threading.Thread(target=start_stream )
    detect_pitch_thread.start()

    #####end code inserting #####
    #app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()
    #after app.MainLoop() no code will be executed
    

    

        
    
        


    
    