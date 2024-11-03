import random

def main():
    random.seed(123)
    generate_fractal()




def generate_fractal(n=1e5):

    losowe=random.uniform(0,1)
    poprz_x=0
    poprz_y=0
    if losowe<0.32:
        poprz_x = -0.67 * poprz_x - 0.02 * poprz_y
        poprz_y = -0.18 * poprz_x + 0.81 * poprz_y + 10
    elif losowe<0.64:
        poprz_x = 0.4 * poprz_x + 0.4 * poprz_y
        poprz_y = -0.1 * poprz_x + 0.4 * poprz_y
    elif losowe < 0.96:
        poprz_x = -0.4 * poprz_x - 0.4 * poprz_y
        poprz_y = -0.1 * poprz_x + 0.4 * poprz_y
    else:
        poprz_x = -0.1 * poprz_x
        poprz_y = 0.44 * poprz_x + 0.44 * poprz_y - 2






if __name__ == '__main__':
        main()