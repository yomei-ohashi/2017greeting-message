from datetime import datetime

def greet(name):
    # シンプルなあいさつ
    simple_message = "Hello, " + name + "-san!"
    print(simple_message)

    # 時間帯によるあいさつ
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    print(message + "," + name +  "-san!")

greet("Inoue")
print("INIAD")

