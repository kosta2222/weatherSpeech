import pyowm
owm=pyowm.OWM('bc4b0e40741c1b22706308dd5dedeefa')
print("""d={'whatweatherinthecity':0.1}""")
d={'whatweatherinthecity':0.1}
n=0
import speech_recognition as sr  
# get audio from the microphone                                                                       
r = sr.Recognizer() 
with sr.Microphone() as source: 
                                                                  
    print("Speak:")                                                                                   
    audio = r.listen(source) 
    try:
      s=r.recognize_google(audio)
      s=''.join(s.lower().split())
      n=d[s]	
      print("You said :" + s )
    except sr.UnknownValueError:
     	
      print("Could not understand audio")
    except sr.RequestError as e:
      	
      print("Could not request results; {0}".format(e))  
 	
if n==0.1:
 city='Saransk'
 observation=owm.weather_at_place(city)
 w=observation.get_weather()
 temperature=w.get_temperature('celsius')['temp']
 wind=w.get_wind()['speed']
 vlajnost=w.get_humidity()
 print('В городе '+city+' сейчас:'+str(temperature)+' градуса цельсия скорость ветра:'+\
 str(wind)+' влажность:'+str(vlajnost)+\
 ",в городе:"+w.get_detailed_status())
