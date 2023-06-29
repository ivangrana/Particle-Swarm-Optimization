import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2


class particula:
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = np.zeros_like(posicao)
        self.melhor_posicao = posicao
        self.best_fitness = float('inf')


class PSO:
    def __init__(self, tamanho_enxame, limites, c1, c2, inercia):
        self.tamanho_enxame = tamanho_enxame
        self.limites = limites
        self.c1 = c1
        self.c2 = c2
        self.inercia = inercia

        self.particulas = []

        for _ in range(tamanho_enxame):
            posicao = np.random.uniform(limites[0], limites[1], size=2)
            particula = particula(posicao)
            self.particulas.append(particula)

        self.melhor_pos_global = None
        self.global_best_fitness = float('inf')

    def otimizacao(self, num_iteracoes):
        fig, ax = plt.subplots()
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)

        x = np.linspace(-3, 3, 100)
        y = np.linspace(-3, 3, 100)
        X, Y = np.meshgrid(x, y)
        Z = rosenbrock(X, Y)

        contour = ax.contour(X, Y, Z, levels=50, cmap='jet')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        scatter = ax.scatter([], [], c='red')

        def atualizar(frame):
            for particula in self.particulas:
                fitness = rosenbrock(particula.posicao[0], particula.posicao[1])
                if fitness < particula.best_fitness:
                    particula.best_fitness = fitness
                    particula.melhor_posicao = particula.posicao

                if fitness < self.global_best_fitness:
                    self.global_best_fitness = fitness
                    self.melhor_pos_global = particula.posicao

                velocidade = (particula.velocidade * self.inercia +
                            self.c1 * np.random.rand() * (particula.melhor_posicao - particula.posicao) +
                            self.c2 * np.random.rand() * (self.melhor_pos_global - particula.posicao))
                particula.velocidade = velocidade
                particula.posicao += velocidade

            scatter.set_offsets(np.array([particula.posicao for particula in self.particulas]))

            return scatter,

        ani = animation.FuncAnimation(fig, atualizar, frames=num_iteracoes, interval=100, blit=True)
        plt.show()

        return self.melhor_pos_global


if __name__ == '__main__':
    tamanho_enxame = 60
    limites = (-2, 2)
    c1 = 0.5
    c2 = 0.1
    inercia = 0.1
    num_iteracoes = 100

    pso = PSO(tamanho_enxame, limites, c1, c2, inercia)
    melhor_pos_global = pso.otimizacao(num_iteracoes)

    print("Minimo Global x =", melhor_pos_global[0], ", y =", melhor_pos_global[1])
    print("Valor da função no minimo global:", rosenbrock(*melhor_pos_global))
