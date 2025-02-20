from flask import Flask, render_template, url_for
import pyautogui
import time



app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/autoclick')
def autoclick():
    time.sleep(5)
    try:
        while True:
            pyautogui.click()
    except pyautogui.FailSafeException:
        return('Autoclicker stopped :/')


if __name__ == "__main__":
    app.run(debug=True)