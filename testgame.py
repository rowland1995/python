import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
test_fontend = pygame.font.Font('font/Pixeltype.ttf',100)
game_active = True

#variables
start_score = 0

sky_surface = pygame.image.load('graphics/sky.png').convert() #convert makes pygame run better
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('Score ='+ str(start_score), False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #turns player_surf into rectangle and defines positon
player_gravity = 0

end_title = test_fontend.render('YOU DIED', False, ('White')) 
end_rect = end_title.get_rect(center = (400,200))


#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: #if player clicks, jump
                player_gravity = -20

        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300: #space to jump, checks if player on ground
                player_gravity = -20
        
    if game_active:
        # places surfaces on display
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen,'#c0e8ec',score_rect)
        pygame.draw.rect(screen,'#c0e8ec',score_rect,10) 
        # draws updated score
        score_surf = test_font.render('Score = '+ str(start_score), False, (64,64,64))
        screen.blit(score_surf,(score_rect))
        
        
        snail_rect.x -= 10 #moves snail to left
        if snail_rect.right <= 0: start_score += 1  #adds points to score
        print (start_score)
        if snail_rect.right <= 0: snail_rect.left = 800 #loops snail if x position falls below or equal to 0
        screen.blit(snail_surf,(snail_rect)) #places snail surf at postition of snail_rect
        
        # Player
        player_gravity += 1 
        player_rect.y += player_gravity #add gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300 #sets ground level
        if player_rect.bottom <= 0 : player_rect.bottom = 10 #adds ceiling (not needed for single jump)
        screen.blit(player_surf,(player_rect)) #places player surf at position of player_rect
        
        # Collision
        if snail_rect.colliderect(player_rect): #detects collision and ends game
            snail_rect.left = 800 #resets snail to original x position
            start_score = 0
            game_active = False
    else:
        screen.fill('Red')
        screen.blit(end_title,(end_rect))
        if event.type == pygame.TEXTINPUT: 
            game_active = True

    
    #sets fps
    pygame.display.update()
    clock.tick(60)
