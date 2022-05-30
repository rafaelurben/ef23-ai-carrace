from pyworld.Car import Car
from pyworld.Monaco import setupMonaco
from pyworld.Traces import clearTraces, saveTraces

from neural_network import loader, training

import os.path

name = "carai_v5"
folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "networks", name, "")

class CarGenome(training.Genome):
    def setup(self, track):
        self.obj = Car(track)

    def step(self):
        car = self.obj

        scans = car.getScans()
        acc, steer = self.feed_forward([*scans, car.v])
        car.acc = -1 + 2 * acc
        car.steer = -1 + 2 * steer
        car.move()
        car.updateScore()

        if car.checkCollision():
            return False
        return True

    def run_evaluation(self, timestepamount=5000):
        for _ in range(timestepamount):
            if not self.step():
                break

        return self.obj.score


track_monaco = setupMonaco()

clearTraces()

myloader = loader.NeuroLoader(name=name, folder=folder)
carai = myloader.get_genome(CarGenome, track=track_monaco)
carai.run_evaluation(5000)
print(carai.score)

saveTraces([carai.obj])
