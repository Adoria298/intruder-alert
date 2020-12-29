import random, os

def play_mp3(path_to_mp3):
    os.system("mplayer " + path_to_mp3)
    print("Player sound: " + str(path_to_mp3))

def choose_random_alert():
    alerts = [alert for alert in os.listdir(os.path.abspath("./alerts")) if str(alert).endswith(".mp3")]
    alert = random.choice(alerts)
    return os.path.abspath("./alerts/" + alert)

if __name__ == "__main__":
    play_mp3(choose_random_alert())