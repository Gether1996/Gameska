from enum import Enum
import random

# you can change number of actions, doesnt matter how many are inside of Schedule or Schedule2
class Schedule(Enum):
    freeday = 0
    recruitment = 1
    teamgame = 2
    duel = 3
    freeforall = 4
    none = 5


class Schedule2(Enum):
    deathmatch = 0
    peace = 1
    brawl = 2
    raidboss = 3
    training = 4
    none = 5


class Arena():

    # counter for lenght of schedule
    index_of_arena = 0


    def __init__(self, m_arenaName:str, m_arenaSchedule):
        self.m_arenaName = m_arenaName
        self.m_arenaSchedule = m_arenaSchedule

    def fill_schedule(self):
        if self.index_of_arena < len(self.m_arenaSchedule)-1:
            self.index_of_arena += 1
            return self.m_arenaSchedule(self.index_of_arena -1).name
        else:
            copy_of_index = self.index_of_arena
            self.index_of_arena = 0
            return self.m_arenaSchedule(copy_of_index).name


    def progress_day(self):
        print(f"Todays plan of arena {self.m_arenaName} is {self.fill_schedule()}.")

    def __str__(self):
        return f"Name of this arena: {self.m_arenaName}"


class World():

    m_arenaDay = 0
    m_max_days = 500


    def __init__(self, m_arenas:list):
        self.m_arenas = m_arenas


    def simulate_day(self):
        self.m_arenaDay += 1
        if self.m_arenaDay == self.m_max_days:
            print(f"Day: {self.m_arenaDay} - maximum days count reached.\n"
                  f"Finishing process...")
            quit()
        else:
            print(f"Day: {self.m_arenaDay}")
            for x in self.m_arenas:
                x.progress_day()



arena1 = Arena("Kako", Schedule)
arena2 = Arena("Hell", Schedule2)
myWorld = World([arena1, arena2])

while True:
    myWorld.simulate_day()




