import pygame

pygame.init()
#screen = pygame.display.set_mode((640, 840))
clock = pygame.time.Clock()
pygame.display.set_caption("Imagem de Fundo no Pygame")
running = True
info = pygame.display.Info()
largura_tela = info.current_w - 960
altura_tela = info.current_h - 150

screen = pygame.display.set_mode((largura_tela, altura_tela))

# def events():
#   for event in pygame.event.get():

#     t = event.type
#     if event.type == pygame.QUIT:
#       running = False
#     if event.type == pygame.K_UP:     
#       running = False
        # loop()
        # figura = pygame.Surface([245, 70]) # cria uma superfície quadrada com 30 pixels de lado
        # figura.fill((0, 0, 0)) # preenche a superfície com cor preta
        # screen.blit(figura, (197, 467))

def inicio(running_inicio,running_jogo):
    
    
    imagem_fundo = pygame.image.load('fundo/iniciar(3).png')
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela+99))#640, 889
 # iniciar = pygame.image.load('fundo/INICIAR.png')
  #iniciar = pygame.transform.scale(iniciar, (245, 70))
  #screen.blit(iniciar, (197, 413))
    while running_inicio:
      screen.blit(imagem_fundo, (0, 0))
      for event in pygame.event.get():
        #print(event, "outronome")
        if event.type == pygame.QUIT:
          running_inicio = False
          return running_inicio, running_jogo, False
      
      
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w]:
        running_inicio = False
      if keys[pygame.K_SPACE]:
        running_jogo = True
        running_inicio = False

      pygame.display.flip() # Desenha o quadro atual na tela
      clock.tick(60)
    return running_inicio, running_jogo, True


def loop(running_jogo):
  vivo = True
  while running_jogo:
    while vivo:
      #jogo(por enquanto vai direto pra tela de morte)
      
      vivo = False
      pygame.display.flip() # Desenha o quadro atual na tela
      clock.tick(60)
    while not vivo:
      for event in pygame.event.get():
        # print(event, "mais um nome")
        if event.type == pygame.QUIT:
          return running_jogo, False
      imagem_morte = pygame.image.load('fundo/morte.png')
      imagem_morte = pygame.transform.scale(imagem_morte, (largura_tela, altura_tela+99))#640, 889
      screen.blit(imagem_morte, (0, 0))
      # tela morte
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        vivo = True
      pygame.display.flip() # Desenha o quadro atual na tela
      clock.tick(60)
    
    pygame.display.flip() # Desenha o quadro atual na tela
    clock.tick(60)
  return running_jogo, True
  
  

  
def main(running_inicio,running_jogo):
  
  running_inicial = inicio(running_inicio,running_jogo)
  running_inicio = running_inicial[0]
  running_jogo = running_inicial[1]
  lop = loop(running_jogo)
  running_jogo = lop[0]
  if running_inicial[2] == False or lop[1] == False:
    running = False
  else:
    running = True
  return running_inicio, running_jogo, running

running_inicio = True
running_jogo = False

while running:
  
  for event in pygame.event.get():
    # print(event, "nome")
    if event.type == pygame.QUIT:
      running = False
    
  screen.fill((255,255,255)) # apaga o quadro atual
  
  running2 = main(running_inicio,running_jogo)
  running_inicio= running2[0]
  running_jogo = running2[1]
  if running2[2] == False:
    running = running2[2]
  

  
  pygame.display.flip() # Desenha o quadro atual na tela
  clock.tick(60)
pygame.quit()



#43, 65, 87
#76 = "98"
#personagem = 43 
#personage = pygame.image.load(f'fundo/{personagem}.png')