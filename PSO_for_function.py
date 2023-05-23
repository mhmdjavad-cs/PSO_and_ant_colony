import math
import random

#costants:
y_range = 10
x_range = 10
initial_velocity_range = 0.1
number_of_particles = 3000
number_of_iterations = 500
inertia = 0.1
c1 = 0.1
c2 = 0.1

class Particle:
    def __int__(self):
        pass

    def random_initial(self):
        self.x_position = random.uniform(-x_range, x_range)
        self.y_position = random.uniform(-y_range, y_range)
        self.x_velocity = random.uniform(-initial_velocity_range, initial_velocity_range)
        self.y_velocity = random.uniform(-initial_velocity_range, initial_velocity_range)
        self.x_global = 0
        self.y_global = 0
        self.x_local = 0
        self.y_local = 0
        self.local_best = 0
        self.value = 0

    def computing_value(self):
        # the main function should be defined here:
        self.value = abs(math.sin(self.x_position) * math.cos(self.y_position) * \
                         math.exp(abs(1 - (math.sqrt(self.x_position**2 + self.y_position**2))/math.pi)))

    def update_local(self):
        if self.value >= self.local_best:
            self.local_best = self.value
            self.x_local = self.x_position
            self.y_local = self.y_position

    def update_global(self, x, y):
        self.x_global = x
        self.y_global = y

    def update_velocity(self):
        self.x_velocity = inertia * self.x_velocity + c1 * (self.x_local - self.x_position) + c2 * (
                    self.x_global - self.x_position)
        self.y_velocity = inertia * self.y_velocity + c1 * (self.y_local - self.y_position) + c2 * (
                    self.y_global - self.y_position)

    def update_position(self):
        self.x_position = self.x_position + self.x_velocity
        self.y_position = self.y_position + self.y_velocity
        if self.x_position > 10:
            self.x_position = 10
        if self.x_position < -10:
            self.x_position = -10
        if self.y_position > 10:
            self.y_position = 10
        if self.y_position < -10:
            self.y_position = -10


def main():
    particles_list = []
    for i in range(0, number_of_particles):
        particle = Particle()
        particle.random_initial()
        particles_list.append(particle)

    for t in range(0, number_of_iterations):
        for particle in particles_list:
            particle.computing_value()

        particles_list.sort(key=lambda particle: particle.value, reverse=True)
        print(" best_value: ", particles_list[0].value)
        #print("x: ", particles_list[0].x_position, " y: ", particles_list[0].y_position\
        #      , " global: ", particles_list[0].x_global, " ", particles_list[0].y_global\
        #      , " local: ", particles_list[0].x_local, " ", particles_list[0].y_local\
        #      , " value: ", particles_list[0].value)


        for particle in particles_list:
            particle.update_local()
            particle.update_global(particles_list[0].x_position,particles_list[0].y_position)
            #print("x: ",particle.x_position," y: ",particle.y_position\
            #      ," global: ",particle.x_global," ",particle.y_global\
            #      ," local: ",particle.x_local," ",particle.y_local\
            #      ," value: ",particle.value)

        for particle in particles_list:
            particle.update_velocity()
            particle.update_position()

    print("x: ", particles_list[0].x_position, " y: ", particles_list[0].y_position\
          , " global: ", particles_list[0].x_global, " ", particles_list[0].y_global\
          , " local: ", particles_list[0].x_local, " ", particles_list[0].y_local\
          , " value: ", particles_list[0].value)


if __name__ == '__main__':
    main()