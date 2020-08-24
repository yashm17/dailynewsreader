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
def newsreader(link):
    import requests
    import json
    url = link
    response = requests.get(url)
    text = response.text
    news = json.loads(text)
    greet = "Today's Top 10 News headlines are"
    bye = "thank you"
    run = True
    while (run):
        print('Listen your News.......')
        if gender.upper() == 'M':
            speakfemale(greet)
            for i in range(10):
                speakfemale(news['articles'][i]['title'])
                run = False
            speakfemale(bye)
        elif gender.upper() == 'F':
            speakmale(greet)
            for i in range(10):
                speakmale(news['articles'][i]['title'])
                run = False
            speakmale(bye)
        print('News are over')

gender = str(input("Your Gender?M/F: "))
while(True):
    if __name__=='__main__':
            moment = input('Continue/Quit? ')
            if moment=='quit':
                break
            region=int(input('1-International news\n2-India news\nChoose your options: '))
            topic=int(input('1.All\n2.Business\n3.Tech\n4.Sports\n5.Entertainment\nChoose your option: '))

            if region==1 and topic==1:
                url=('http://newsapi.org/v2/top-headlines?'
                       'sources=bbc-news&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==1 and topic==2:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=us&category=business&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==1 and topic==3:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'sources=techcrunch&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==1 and topic==4:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=us&category=sports&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==1 and topic==5:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=us&category=entertainment&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==2 and topic==1:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=in&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==2 and topic==2:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=in&category=business&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==2 and topic==3:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=in&category=technology&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==2 and topic==4:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=in&category=sports&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            elif region==2 and topic==5:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=in&category=entertainment&'
                       'apiKey=87c6c953e7b04d6c8450287cb9cbfa48')
                newsreader(url)
            else:
                print('Invalid input')