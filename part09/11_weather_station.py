class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = []

    def __str__(self):
        return f'{self.__name}, {len(self.__observations)} observations'
    
    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        if len(self.__observations) == 0:
            return ''
        return self.__observations[-1]
    
    def number_of_observations(self):
        return len(self.__observations)


