#Maggie Zhao
#SoftDev1 pd7
#K08: Fill Yer Flask
#2018-09-18

from flask import Flask
app = Flask(__name__) #create instance of class flask

@app.route("/")
def hello_world():
    print("Now printing __name__:")
    print(__name__)
    return "No hablo queso!"

@app.route("/pi")
def pi_main():
    return "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337"

@app.route("/bee")
def bee_main():
    return "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little."

@app.route("/trump")
def trump_main():
    return "covfefe"

if __name__ == "__main__":
    app.debug = True
    app.run()
