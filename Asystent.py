import speech_recognition as sr  # biblioteka odpowiedzialna za rozpoznawanie naszego głosu
import pyttsx3  # biblioteka odpowiedzialna za tworzenie głosu asystenta
import datetime  # pobieranie daty i godziny
import time  # obliczanie czasu
from tkinter import *  # do tworzenia interfejsu graficznego
import pyjokes  # biblioteka z żartami
from playsound import playsound  # odtwarzanie dzwięków
import webbrowser  # otwieranie stron
import wikipedia  # wyszkiwanie haseł na stronie wikipedia
import pyowm  # pokazywanie pogody
import sys

owm = pyowm.OWM('f58349d7f89f82766b104bc8b3f318b1')  # API komputera

name_file = open("Assistant_name", "r")
name_assistant = name_file.read()

engine = pyttsx3.init(
    'sapi5')  # uzywamy sapi5 w systemie windows, silnik zmiany tekstu na mowę, na tej zmiennej możemy operować i modyfikować możliwości głosowe naszego asystenta
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 odpowiada za głos damski


def speak(text):  # funkcja speak przyjmuje parametr text, (czyli to co nasz asystent będzie miał powiedzieć)
    engine.say(text)  # za pomocą engine.say(text) nasz asystent jest w stanie powiedzieć to co mu kazaliśmy
    print(name_assistant + " : " + text)  # pojawia się imię asystenta i tekst
    engine.runAndWait()  # funkcja ta powoduje, że mowa jest słyszalna


#  za pomocą engine.say(text) nasz bot jest w stanie powiedzieć to co mu kazaliśmy.

def wishMe():
    hour = datetime.datetime.now().hour  # pobieranie akutalnej godziny

    if 0 <= hour < 12:  # jezeli jest miedzy godzina 0 a godzina 12 asystent przedstawia sie i mowi Good morning
        speak("Hello, I am " + name_assistant + ". Good Morning")
    elif 12 <= hour < 18:  # miedzy 12 a 18 asystent przedstawia sie i mowi milego popoludnia
        speak("Hello, I am " + name_assistant + ". Good Afternoon")
    else:
        speak(
            "Hello, I am " + name_assistant + ". Good Evening")  # w pozostalych godzinach asystent przedstawia sie i mowi Good evening


def get_audio():
    r = sr.Recognizer()  # zmienna  r = sr.Recognizer() pozwala nam na wczytywanie naszego głosu
    audio = ''

    with sr.Microphone() as source:
        print("Listening")  # napis listening przy rozpoczeciu sluchania
        playsound(
            'C:/Users/W10Home/PycharmProjects/pythonProject/assistant_on.mp3')  # dzwiek, ktory informuje o poczatku sluchania polecen
        audio = r.listen(source,
                         phrase_time_limit=10)  # limit czasu na wypowiadanie polecen do asystenta wynosi 10 sekund
        playsound("assistant_off.mp3")  # dzwiek, ktory informuje o skonczonym procesie pobierania glosu
        print("Stop.")  # napis stop po zakonczonym procesie sluchania polecen
    try:
        text = r.recognize_google(audio, language='en-GB')  # język angielski, brytyjski
        print('You: ' + ': ' + text)
        return text
    except:
        return "None"


def date():
    now = datetime.datetime.now()  # dzisiejsza dokładna data
    month_name = now.month  # akutalny miesiąc
    day_name = now.day  # akutalny dzień
    month_names = (
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
        'December',)  # nazwy miesięcy
    ordinalnames = (
        '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th',
        '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th', '29th',
        '30th', '31st',)  # dni

    speak("Today is " + month_names[month_name - 1] + " " + ordinalnames[day_name - 1] + '.')


# asystent mówi jaki jest dziś miesiąc i dzień

# asystent mówi jaki jest dzis miesiac i dzien

wishMe()


def process_audio():
    if __name__ == '__main__':  # każdy moduł Pythona ma zdefiniowane __name__, jeśli jest to '__main__', oznacza to, że moduł jest uruchamiany samodzielnie przez użytkownika, a my możemy wykonać odpowiednie czynności
        while True:

            statement = get_audio().lower()

            if "hello" in statement or "hi" in statement:
                wishMe()
                time.sleep(5)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'joke' in statement:  # jezeli asystent uslyszy w zdaniu słowo joke, uslyszymy zart
                speak(pyjokes.get_joke())  # asystent opowie losowy zart z biblioteki pyjokes
                time.sleep(5)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'youtube' in statement:  # po powiedzeniu slowa youtube w zdaniu asystent otworzy w nowej karcie (new=2) strone youtube
                webbrowser.open("https://www.youtube.com", new=2)
                speak("youtube is open now")
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'google' in statement:  # po powiedzeniu slowa google w zdaniu asystent otworzy w nowej karcie (new=2) wyszukiwarke google
                webbrowser.open("https://www.google.com", new=2)
                speak("Google is open now")
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'gmail' in statement:  # po powiedzeniu slowa gmail w zdaniu asystent otworzy w nowej karcie (new=2) poczte Gmail
                webbrowser.open("mail.google.com", new=2)
                speak("Google Mail open now")
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'netflix' in statement:  # po powiedzeniu slowa netflix w zdaniu asystent otworzy w nowej karcie (new=2) strone Netflix
                webbrowser.open("netflix.com", new=2)
                speak("Netflix open now")
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'open prime video' in statement:  # po powiedzeniu slow prime vidwo w zdaniu asystent otworzy w nowej karcie (new=2) strone Amazon Prime Video
                webbrowser.open("primevideo.com", new=2)
                speak("Amazon Prime Video open now")
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'stackoverflow' in statement:
                speak('opening stackoverflow')
                webbrowser.open('stackoverflow.com')
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'news' in statement:  # po powiedzeniu slowa news w zdaniu asystent otworzy w nowej karcie (new=2) strone z najnowszymi wiadomosciami z Polski
                webbrowser.open("https://www.independent.co.uk/topic/poland", new=2)
                speak('Here are some headlines from the Times of Poland, Happy reading')
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'virus' in statement:  # po powiedzeniu slowa corona w zdaniu asystent otworzy w nowej karcie (new=2) strone z informacjami o covid
                webbrowser.open("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(10)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'time' in statement:  # jezeli w wypowiadanym zdaniu asystent uslyszy slowo time
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")  # czas godzina, minuta, sekunda
                time.sleep(5)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'date' in statement:  # jezeli asystent przetworzy slowo date powie dzisiejsza date
                date()
                time.sleep(5)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'who are you' in statement or 'what can you do' in statement:  # po pytaniu kim jestes, co robisz (w jezyku angielskim) asystnent odpowie
                speak(
                    'I am ' + name_assistant + ' your personal assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra')
                # asystent odpowie jak ma na imie i co jest w stanie zrobic
                time.sleep(5)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta
            if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:  # zapytanie o to kto stworzyl asystenta
                speak(
                    "I was built by Patrycja and Ola")  # po otrzymaniu jednego z trzech pytan asystent opowie kto byl jego tworcą
                time.sleep(5)  # odpowiada za czas oczekiwania na wywołanie uruchomionego asystenta

            if 'weather' in statement:  # jezeli asystent przetworzy slowo weather przytoczy dzisiejsza prognoze
                nameOFcity = statement.replace("weather", "")  # wyodrebnienie nazwy miasta

                mgr = owm.weather_manager()  # silnik prognozy pogody

                observation = mgr.weather_at_place(nameOFcity)
                w = observation.weather

                status = w.detailed_status  # pobiera informacje na temat ogolnego stanu pogody
                speak(f'Status is {status} ')

                temp = w.temperature(unit='celsius')  # temperatura w C
                a = temp['temp']  # a to temperatura
                b = temp['feels_like']  # bo to temperatura odczuwalna
                speak(f'Actual temperature is {a} celsius but it feels like {b} celsius')
                c = temp['temp_min']  # c to temperatura mininalna
                d = temp['temp_max']  # d to temperatura maksymalna
                speak(f'The highest temperature is {d} celsius and the lowest is {c} celsius')

                wind = w.wind()  # sila siatru w metrach na sekunde
                e = wind['speed']
                speak(f'Wind {e} meters per sec')

                sr = w.sunrise_time(timeformat='iso')  # czas wschodu slonca
                speak(f'SunRise time : {sr}')

                ss = w.sunset_time(timeformat='iso')  # czas zachodu slonca
                speak(f'SunSet time : {ss}')

                cloud = w.clouds  # zachmurzenie
                speak(f' The sky is in {cloud} percent covered by clouds')

                visibility = w.visibility_distance  # widocznosc
                speak(f' The visibility is {visibility} meters')

            if 'wikipedia' in statement:  # jezeli w zdaniu pojawi sie slowo wikipedia
                if 'open wikipedia' in statement:  # jezeli powie sie w zdaniu open wikipedia
                    webbrowser.open('wikipedia.com')  # otwieranie wikipedii w przeglądarce
                else:
                    try:
                        speak("Searching wikipedia")  # jeżeli powiemy frazę searching wikipedia
                        statement = statement.replace("wikipedia", "")
                        results = wikipedia.summary(statement,
                                                    sentences=2)  # znalezenie wyników wyszukiwania, 2 odnosi się do numerów wierszy/linii
                        speak("According to wikipedia")  # asystent powie "According to wikipedia"
                        wikipedia_screen(results)
                        speak(results)  # wypowiedziana zostanie definicja, o którą pytaliśmy asystent
                    except Exception:
                        speak(
                            'Sorry  could not find any results')  # jeżeli naszej frazy nie ma w wikipedii asystent odpowie, że nie może jej znaleźć

            if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
                speak('Your personal assistant ' + name_assistant + ' is shutting down, Good bye')
                screen.destroy()
                break
    sys.exit(0)  # oznacza czyste wyjście bez żadnych błędów / problemów, program się zamyka


# jeżeli w wypowiadanym zdaniu pojawi się jedno ze słów: ok bye, stop, goodbye
#  asystent powie: Your personal assistant + imię, które mu nadaliśmy + is shutting down, good bye, asystent pożegana się z nami

def change_name():  # zmiana imienia naszego asystenta
    name_info = name.get()

    with open("Assistant_name", "w") as file:
        file.write(name_info)

    settings_screen.destroy()
    screen.destroy()


def change_name_window():
    global settings_screen
    global name
    settings_screen = Toplevel(screen)  # tworzenie kolejnego okna
    settings_screen.title("Settings")  # tytul, wyswietlanie napisu settings
    settings_screen.geometry("300x300")  # wymiary okna
    settings_screen.iconbitmap('ludzik.ico')  # logo programu zrobione w inkscape

    name = StringVar()  # wprowadzanie nowej nazwy

    current_label = Label(settings_screen, text="Current name: " + name_assistant)  # nazwa asystenta obecnie
    current_label.pack()

    enter_label = Label(settings_screen, text="Please enter your Virtual Assistant's name below")  # etykieta z napisem, umieszczona w danym miejscu
    enter_label.pack(pady=10)

    Name_label = Label(settings_screen, text="Name")  #  etykieta Name
    Name_label.pack(pady=10)

    name_entry = Entry(settings_screen, textvariable=name)  # wprowadzenie nowego imienia
    name_entry.pack()

    change_name_button = Button(settings_screen, text="Ok", width=10, height=1,
                                command=change_name)  # przycisk zatwierdzajacy zmiane
    change_name_button.pack(pady=10)


def wikipedia_screen(text):
    wikipedia_screen = Toplevel(screen)  # te widżety działają jak okna, które są bezpośrednio zarządzane przez menedżera okien
    wikipedia_screen.geometry("400x400")  # rozmiar okna
    wikipedia_screen.title("Wikipedia")  # tytuł
    wikipedia_screen.iconbitmap('ludzik.ico')  # ustawienie ikony

    message = Message(wikipedia_screen, text=text)  # tekst - stosujemy aby wyświetlić jeden lub więcej wierszy tekstu w widżecie
    message.pack()

  # pack() służy do wypełniania widżetu w całej ramce

def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)  # nazwa asystenta
    screen.geometry("500x500")  # rozmiar okna programu
    screen.iconbitmap('ludzik.ico')  # ikona programu

    name_label = Label(text=name_assistant, width=300, bg="violet", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file="mikro.png")  # logo mikrofonu
    microphone_button = Button(image=microphone_photo, command=process_audio)
    microphone_button.pack(pady=10)

    settings_photo = PhotoImage(file="ustawienia.png")  # logo ustawien
    settings_button = Button(image=settings_photo, command=change_name_window)
    settings_button.pack(pady=10)

    screen.mainloop()


main_screen()
