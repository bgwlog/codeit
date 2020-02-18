class Clock:
    def __init__(self, hour, minute, sec):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def tick(self):
        if self.sec == 59:
            if self.minute == 59:
                if self.hour == 23:
                    self.hour = 0
                else:
                    self.hour += 1
                self.minute = 0
            else:
                self.minute += 1
            self.sec = 0
        else:
            self.sec += 1

    def set(self, hour, minute, sec):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def __str__(self):
        return "{}:{}:{}".format(str(self.hour).zfill(2), str(self.minute).zfill(2), str(self.sec).zfill(2))


# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)

# 13초를 늘린다
for i in range(13):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 23시 59분 57초로 세팅
clock.set(23, 59, 57)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)
