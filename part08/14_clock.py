class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0


    def set(self, new_hours, new_minutes):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = 0


if __name__ == '__main__':
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.set(12, 5)
    print(clock)