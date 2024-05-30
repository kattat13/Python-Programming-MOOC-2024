class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

    def tick(self):
        if self.minutes == 59 and self.seconds == 59:
            self.minutes = 0
            self.seconds = 0
        else:
            if self.seconds == 59:
                self.minutes += 1
                self.seconds = 0
            else:
                self.seconds += 1
    

if __name__ == '__main__':
    watch = Stopwatch()
    for i in range(61):
        print(watch)
        watch.tick()