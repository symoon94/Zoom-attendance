# Zoom-attendance

I'm too lazy to wake up early in the morning to attend online classes. This program can automatically start the zoom meeting at the specific time you set up, mute your mics, click any buttons popped up during the class, and leave the class when you want.

## Usage

To make a cookie that includes your login information such as id and password:

    $ python main.py --cookies=False 

When it stops at the ipdb line, you have to manually login through the created window. Then, type "c" on your terminal to continue the program. It 

To attend a class with the cookie file you saved:

    $ python main.py --cookies=True --url=ZOOM_URL --passcode=ZOOM_PASSCODE --start_time=06:00 --end_time=7:15

To see the argument options, run:

    $ python main.py --help

which will print:

    usage: main.py [-h] [--cookies COOKIES] [--url URL] [--passcode PASSCODE]
               [--start_time START_TIME] [--end_time END_TIME]

    optional arguments:
    -h, --help            show this help message and exit
    --cookies COOKIES
    --url URL
    --passcode PASSCODE
    --start_time START_TIME
    --end_time END_TIME


## Author

Sooyoung Moon / [@symoon94](https://www.facebook.com/msy0128) 