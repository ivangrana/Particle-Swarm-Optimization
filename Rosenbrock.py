import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Função de Rosenbrock em 3D
def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

# Implementação do PSO
def PSO(cost_function, num_particulas, num_iterations):
    # Limites do espaço 
    x_min, x_max = -2, 2
    y_min, y_max = -1, 3
    
    # Inicialização dos enxames de partículas
    particulas_X = np.random.uniform(x_min, x_max, num_particulas)
    particulas_Y = np.random.uniform(y_min, y_max, num_particulas)
    particulas = np.array(list(zip(particulas_X, particulas_Y)))
    
    # Inicialização das melhores posições
    melhores_pos = particulas.copy()
    
    # Inicialização das melhores pontuações
    melhores_pts = np.full(num_particulas, np.inf)
    
    # Inicialização da melhor posição global
    melhor_pos_global = None
    
    # Inicialização da melhor pontuação global
    melhor_pts_global = np.inf
    
    # Loop principal do PSO
    for _ in range(num_iterations):
        for i in range(num_particulas):
            x, y = particulas[i]
            score = cost_function(x, y)
            
            # Atualização da melhor posição da partícula
            if score < melhores_pts[i]:
                melhores_pos[i] = (x, y)
                melhores_pts[i] = score
            
            # Atualização da melhor posição global
            if score < melhor_pts_global:
                melhor_pos_global = (x, y)
                melhor_pts_global = score
            
            # Atualização da velocidade e posição da partícula
            velocidade = np.random.random() * (melhores_pos[i] - particulas[i]) + \
                       np.random.random() * (melhor_pos_global - particulas[i])
            particulas[i] += velocidade
        
    return melhor_pos_global, melhor_pts_global

# Configuração do espaço de busca
x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 3, 100)
X, Y = np.meshgrid(x, y)
Z = rosenbrock(X, Y)

# Execução do PSO
melhor_pos, melhor_pontuacao = PSO(rosenbrock, num_particulas=20, num_iterations=100)

# Plotagem da superfície de Rosenbrock
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Plotagem do ponto de mínimo encontrado pelo PSO
ax.scatter(melhor_pos[0], melhor_pos[1], melhor_pontuacao, color='r', s=100)

# Configuração do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Otimização da função de Rosenbrock por Enxame de Partículas (PSO)')

# Exibição do gráfico
plt.show()
