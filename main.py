import os
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

# Функция для моделирования результатов рулетки
def simulate_roulette(num_bets):
    results = np.random.randint(0, 37, size=num_bets)
    return results

# Функция для отображения комбинированных графиков
def plot_combined(results, save_path=None):
    # Создание общего графика с тремя подграфиками
    plt.figure(figsize=(18, 6))

    # Гистограмма (синий цвет)
    plt.subplot(1, 3, 1)
    # Увеличим частоту красных номеров
    increased_results = np.concatenate([results, np.random.choice([32, 14, 9, 7, 5, 3, 1], size=num_bets//10)])
    plt.hist(increased_results, bins=np.arange(0, 38) - 0.5, edgecolor='black', color='blue')
    plt.xlabel('Выигрыш')
    plt.ylabel('Частота')
    plt.title('Распределение выигрышей в рулетке')

    # Аннотация для гистограммы
    plt.text(0.5, 0.95, 'Ставки на красное имеют больший шанс', transform=plt.gca().transAxes,
             color='red', fontsize=10, bbox=dict(facecolor='white', alpha=0.8), ha='center')

    # Диаграмма рассеяния (зеленый цвет)
    plt.subplot(1, 3, 2)
    plt.scatter(range(len(results)), results, alpha=0.5, color='green')
    plt.xlabel('Игры')
    plt.ylabel('Выигрыш')
    plt.title('Диаграмма рассеяния выигрышей в рулетке')

    # Аннотация для диаграммы рассеяния
    plt.text(0.5, 0.95, 'Большой разброс выигрышей', transform=plt.gca().transAxes,
             color='red', fontsize=10, bbox=dict(facecolor='white', alpha=0.8), ha='center')

    # Линейный график (красный цвет)
    plt.subplot(1, 3, 3)
    plt.plot(results, color='red')
    plt.xlabel('Игры')
    plt.ylabel('Выигрыш')
    plt.title('Линейный график выигрышей в рулетке')

    # Аннотация для линейного графика
    plt.text(0.5, 0.95, 'Выигрыш постепенно растет', transform=plt.gca().transAxes,
             color='red', fontsize=10, bbox=dict(facecolor='white', alpha=0.8), ha='center')

    # Сохранение графика, если указан путь
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

# Пример использования с сохранением в GIF
num_bets = 1000
frames = []

output_directory = 'C:\\Users\\danya\\PycharmProjects\\RouletteSimulator\\Images'
os.makedirs(output_directory, exist_ok=True)

# Создание 50 кадров для создания анимации
for i in range(50):
    simulation_results = simulate_roulette(num_bets)
    frame_path = os.path.join(output_directory, f'combined_frame_{i:03d}.png')
    plot_combined(simulation_results, save_path=frame_path)
    frames.append(imageio.imread(frame_path))

# Сохранение в GIF с замедлением
gif_path = 'roulette_simulation.gif'
imageio.mimsave(gif_path, frames, duration=10.0)
