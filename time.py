import time

def pomodoro_clock():
    # 设置每个时间段的长度（以秒为单位）
    work_time = 25*60
    short_break = 5*60
    long_break = 15*60
    rounds = 0
    
    # 通过循环来控制四个时间段的交替
    while True:
        rounds += 1
        print(f"Round {rounds}: Work Time")
        time.sleep(work_time)
        
        if rounds % 4 == 0:
            print("Long Break")
            time.sleep(long_break)
        else:
            print("Short Break")
            time.sleep(short_break)

if __name__ == "__main__":
    pomodoro_clock()
