def speakfemale(str):
    import win32com.client as wincl
    speaker_number = 1
    spk = wincl.Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    spk.Voice
    spk.SetVoice(vcs.Item(speaker_number))
    spk.Speak(str)

def speakmale(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    gender=str(input("Your Gender?M/F: "))
    import requests
    import json

    url = ('http://newsapi.org/v2/top-headlines?'
           'sources=bbc-news&'
           'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
    response = requests.get(url)
    text = response.text
    news = json.loads(text)
    greet="Today's Top 10 News headlines are"
    bye="thank you"
    run=True
    while(run):
        if gender.upper()=='M':
            speakfemale(greet)
            for i in range(10):
                speakfemale(news['articles'][i]['title'])
                run=False
            speakfemale(bye)
        elif gender.upper()=='F':
            speakmale(greet)
            for i in range(10):
                speakmale(news['articles'][i]['title'])
                run=False
            speakmale(bye)