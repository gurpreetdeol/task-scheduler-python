import time

from timeloop import Timeloop
from datetime import timedelta, datetime

tl = Timeloop()


@tl.job(interval=timedelta(seconds=5))
def sample_job_every_2s():
    """Running every 5 seconds"""
    msg = "5s job current time : {}".format(time.ctime())
    __write_log(msg)
    print(msg)


def __write_log(text):
    """Write log message to logs.txt file"""
    with open('logs.txt', 'a') as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {text}\n')


if __name__ == "__main__":
    """Main function"""
    __write_log('Application started')
    tl.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            tl.stop()
            break

    __write_log('Application stopped')
