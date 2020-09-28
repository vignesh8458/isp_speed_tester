import speedtest
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():
    # write to csv
    with open('file.csv', 'a+') as f:
        #f.write('Date,Time,download,upload,ping\n')
        for i in range(1):
            print('Making test #{}'.format(i+1))
            d, u, p = test()
            f.write('{},{},{},{},{}\r'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'),d / 1024000, u / 1024000, p))
    # pretty write to txt file
    #with open('file.txt', 'w') as f:
      #  for i in range(3):
      #      print('Making test #{}'.format(i+1))
      #      d, u, p = test()
       #     f.write('Test #{}\n'.format(i+1))
        #    f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
        #    f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
         #   f.write('Ping: {}\n'.format(p))
    # simply print in needed format if you want to use pipe-style: python script.py > file
   # for i in range(3):
      #  d, u, p = test()
      #  print('Test #{}\n'.format(i+1))
       # print('Download: {:.2f} Kb/s\n'.format(d / 1024))
       # print('Upload: {:.2f} Kb/s\n'.format(u / 1024))
       # print('Ping: {}\n'.format(p))

scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', hours=0.0833333)
scheduler.start()


if __name__ == '__main__':
    main()
