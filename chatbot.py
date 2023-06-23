import aiml
import requests
import pyttsx3
import json
import wikipedia
import speech_recognition as sr

def getWeather(city):
    apikey = "1f5666d3683bd6d01774bb988d857db5"  # Replace with your OpenWeatherMap API key
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?appid=" + apikey + "&q=" + city
    )
    jsonResponse = response.json()
    return jsonResponse


def getJoke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    return json.loads(response.text)

def getWiki(search):
    return wikipedia.summary(search, sentences=2)

speechEngine = pyttsx3.init()
kernel = aiml.Kernel()
kernel.learn("brain.json")

print("WORKING OF MICROPHONE")
c = "y"
ctr = 0

while c == "y":
    # obtain audio from the microphone
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Talk!")
        audio = r.listen(source, phrase_time_limit=5)

    # recognize speech using Google
    try:
        response = r.recognize_google(audio)
        print(response)
        responseParts = response.split()
        for part in responseParts:
            if part.lower() == "weather":
                speechEngine.say("Please provide a city name.")
                speechEngine.runAndWait()
                city = input("Enter city name: ")
                weatherData = getWeather(city)
                if weatherData["cod"] != 404:
                    print(weatherData)  # Print the weather data dictionary
                    temp = weatherData["main"]["temp"]
                    fahrenheit = ((temp - 273.15) * 9 / 5) + 32
                    print(fahrenheit)
                    speechEngine.say(fahrenheit)
                    speechEngine.say("degrees Fahrenheit")
                    speechEngine.runAndWait()
                else:
                    print("Weather data not available for the provided city.")

            elif part.lower() == "joke":
                jokeData = getJoke()
                if jokeData["status"] != 404:
                    speechEngine.say(jokeData["joke"])
                    speechEngine.runAndWait()

            elif part.lower() == "wiki":
                speechEngine.say("Please provide a search term.")
                speechEngine.runAndWait()
                search = input("Enter search term: ")
                wikiSummary = getWiki(search)
                speechEngine.say(wikiSummary)
                speechEngine.runAndWait()

            else:
                response2 = kernel.respond(str(response))
                print(response2)
                speechEngine.say(response2)
                speechEngine.runAndWait()
        ctr += 1

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print("Keep Listening? (Y/N)")
    c = input()
