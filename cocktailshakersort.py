from random import randint
import pygame
screen = pygame.display.set_mode((700, 500))
import time

def random(arr, length):
    n = randint(1, length) * 1.5
    if n in arr:
        return random(arr, length)
    else:
        return n

def Randomise(length):
    len = length
    result = []
    for i in range(length):
        result.append(random(result,length))
    return result


array = []
array = Randomise(200)

def Reverse(length):
    result = []
    for i in range(length):
        result.append(length-i)
    return result




def is_sorted(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))

def cocktailShakerSort(arr, running=None):
    i = 0
    dir = 1
    close = False
    array = arr.copy()  
    steps = 0
    while is_sorted(array) == False:
        
        if dir == 1 and  i < len(array) - 1:
            screen.fill((0,0,0))
            if array[i] > array[i+1]:
                

                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp    
            for n in range(len(array)):
                if n != i+1:
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(n * 2.96 + 50, 400  - array[n], 2.94, array[n]))
                else:
                    pygame.draw.rect(screen, (255,0,0), pygame.Rect(n * 2.96 + 50, 400  - array[n], 2.94, array[n]))
            #\time.sleep(0.01)
            pygame.display.flip()
            i += 1
            #time.sleep(0.0000000001)
        else: 
            dir = 0
        if dir == 0 and  i > 0:
            screen.fill((0,0,0))
            if array[i-1] > array[i]:
                

                tmp = array[i]
                array[i] = array[i-1]
                array[i-1] = tmp    
            for n in range(len(array)):
                if n != i-1:
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(n * 2.96 + 50, 400  - array[n], 2.94, array[n]))
                else:
                    pygame.draw.rect(screen, (255,0,0), pygame.Rect(n * 2.96 + 50, 400  - array[n], 2.94, array[n]))
            #\time.sleep(0.01)
            pygame.display.flip()
            i -= 1
            #time.sleep(0.0000000001)
        else: 
            dir = 1    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        steps+=1
    print(steps)
    return array

running = True
while running:
    screen.fill((0,0,0))
    array = Randomise(200)
    time.sleep(0.5)
    cocktailShakerSort(array)
    #array = []
    
