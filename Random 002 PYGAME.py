import pygame, sys, random


pygame.init()
screen =  pygame.display.set_mode((700,480))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont("arial", 40)

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (350,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (350,50))
        screen.blit(score_surface,score_rect)
        
        highscore_surface = game_font.render(f'High Score: {int(highscore)}',True,(255,255,255))
        highscore_rect = highscore_surface.get_rect(center = (350,100))
        screen.blit(highscore_surface,highscore_rect)

def update_score(score, highscore):
    if score > highscore:
        highscore = score
    return highscore

bg_surface = pygame.image.load('new/Desert.JPG').convert()

floor_surface = pygame.image.load('new/Chrysanthemum.JPG').convert()
floor_x_pos = 0

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,411))
    screen.blit(floor_surface,(floor_x_pos + 700,411))

box = pygame.image.load('new/Triangle.PNG').convert_alpha()
box_rect = box.get_rect(center = (120,130))

pipe_surf = pygame.image.load('new/pipe.PNG').convert()
pipe_surf = pygame.transform.scale2x(pipe_surf)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1000)
pipe_height = [200,250,300,350]

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bot_new_pipe = pipe_surf.get_rect(midtop = (700,random_pipe_pos))
    top_new_pipe = pipe_surf.get_rect(midtop = (700,random_pipe_pos-1080))
    return bot_new_pipe, top_new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 200:
            screen.blit(pipe_surf,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surf, False, True)
            screen.blit(flip_pipe,pipe)
            
def check_collision(pipes):
    for pipe in pipes:
        if box_rect.colliderect(pipe):
            go_sound.play()
            return False
    if box_rect.top <= -100 or box_rect.bottom >= 420:
        return False    
    return True

def box_animation():
    new_box = box_frames[box_index]
    new_box_rect = new_box.get_rect(center = (120,box_rect.centery))
    return new_box, new_box_rect

#game variables
gravity = 0.10
box_movement = 0
game_active = True

box_up = pygame.image.load('new/Triangle-up.png').convert()
box_mid = pygame.image.load('new/Triangle-mid.png').convert()
box_down = pygame.image.load('new/Triangle-down.png').convert()
box_frames = [box_up, box_mid, box_down]
box_index = 0
box = box_frames[box_index]
box_rect = box.get_rect(center = (120,130))

BOXFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BOXFLAP,200)

game_over_surface = pygame.image.load('new/gameover.JPG').convert()
game_over_rect = game_over_surface.get_rect(center = (350,240))

score = 0
highscore = 0

flap_sound = pygame.mixer.Sound('new/flap.MP3')
go_sound = pygame.mixer.Sound('new/death.MP3')
score_sound = pygame.mixer.Sound('new/score-sound.MP3')
score_sound_countdown = 125

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                box_movement = 0
                box_movement -= 4
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                box_rect.center = (120,130)
                score = 0
                
                
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        
        if event.type == BOXFLAP:
            if box_index < 2:
                box_index += 1
            else:
                box_index = 0
            box,box_rect = box_animation()
    
    screen.blit(bg_surface,(0,0))
    
    if game_active:
        # Box 
        box_movement += gravity
        box_rect.centery += box_movement
        screen.blit(box,box_rect)
        check_collision(pipe_list)
        
        game_active = check_collision(pipe_list)
        
        # Pipe 
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
    
        score+=0.008
        score_display('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 120
        
    else:
        screen.blit(game_over_surface,game_over_rect)
        highscore = update_score(score,highscore)
        score_display('game_over')
    
    # Floor
    floor_x_pos-=1
    draw_floor()
    if floor_x_pos < -700:
        floor_x_pos = 0
    
    
    
    pygame.display.update()
    clock.tick(120)