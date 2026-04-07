class WiFiDevice:
    def wifi_connect(self):
        print("Connected to WiFi")

class VoiceAssistant:
    def voice_control(self):
        print("Voice control activated")

class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker is ready")
s = SmartSpeaker()
s.wifi_connect()
s.voice_control()
s.display()
