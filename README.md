# Voice-Activated Chatbot

## Overview
This is a voice-activated chatbot implemented in Python. The chatbot utilizes speech recognition to listen to user input, processes the input using AIML (Artificial Intelligence Markup Language), and provides appropriate responses. The chatbot can fetch weather information, tell jokes, provide Wikipedia summaries, and handle general conversation.

## Features
- Voice-activated interaction with the chatbot using speech recognition
- AIML-based conversation processing for general queries and responses
- Fetching weather information for a given city using the OpenWeatherMap API
- Retrieving jokes from the icanhazdadjoke API
- Displaying Wikipedia summaries based on user-provided search terms

## Limitations
- The weather functionality relies on the OpenWeatherMap API. However, the free tier of the API has limitations, such as:
    - Limited number of requests per minute and per day
    - Limited availability of weather data for certain locations
    - Weather data may not always be up to date or accurate
- Please note that the weather functionality may not work as expected due to these limitations.

## Requirements
- Python 3.x
- aiml
- requests
- pyttsx3
- wikipedia
- SpeechRecognition

## Installation
1. Clone the repository or download the code files.
2. Install the required packages using the following command:
   ```
   pip install aiml requests pyttsx3 wikipedia SpeechRecognition
   ```
3. Obtain an API key from OpenWeatherMap by signing up at https://openweathermap.org/ and create a free account.
4. Replace `"YOUR_API_KEY"` in the code with your actual OpenWeatherMap API key.

## Usage
1. Run the script `chatbot.py` using the following command:
   ```
   python chatbot.py
   ```
2. The chatbot will prompt you to speak. Start speaking to interact with the chatbot.
3. You can ask questions, request weather information, tell the chatbot to fetch jokes, or ask for Wikipedia summaries.
4. The chatbot will respond accordingly using speech synthesis.

## License
This project is licensed under the [MIT License](LICENSE).
