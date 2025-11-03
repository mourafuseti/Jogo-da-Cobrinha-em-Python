import pygame
import random
import time
import os

# ===========================================
# INICIALIZAÇÃO
# ===========================================
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# --- TELA CHEIA ---
INFO = pygame.display.Info()
LARGURA = INFO.current_w
ALTURA = INFO.current_h
tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo da Cobrinha - MÚSICA DE FUNDO")

# --- CORES ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
AZUL = (0, 0, 200)
CINZA = (100, 100, 100)
AMARELO = (255, 215, 0)
DOURADO = (255, 215, 0)
PRATA = (192, 192, 192)
BRONZE = (205, 127, 50)

# --- FONTES ---
fonte_tamanho = max(20, LARGURA // 60)
fonte = pygame.font.SysFont("consolas", fonte_tamanho, bold=True)
fonte_pequena = pygame.font.SysFont("consolas", int(fonte_tamanho * 0.7))
fonte_gameover = pygame.font.SysFont("consolas", int(fonte_tamanho * 1.8), bold=True)
fonte_input = pygame.font.SysFont("consolas", int(fonte_tamanho * 1.2))
fonte_ranking = pygame.font.SysFont("consolas", int(fonte_tamanho * 1.1), bold=True)

# --- CONFIGURAÇÕES ---
TAMANHO_BLOCO = max(10, LARGURA // 80)
FPS_INICIAL = 10
AUMENTO_POR_NIVEL = 40
ARQUIVO_RECORDE = "recorde.txt"
TOP_N = 5
ARQUIVO_MUSICA = "musica.wav"  # ou .mp3

# ===========================================
# SONS E MÚSICA
# ===========================================
def carregar_som(caminho, volume=0.6):
    if os.path.exists(caminho):
        try:
            som = pygame.mixer.Sound(caminho)
            som.set_volume(volume)
            return som
        except Exception as e:
            print(f"Erro ao carregar som {caminho}: {e}")
    return None

som_comer = carregar_som("comer.wav", 0.6)
som_gameover = carregar_som("gameover.wav", 0.7)

# --- MÚSICA DE FUNDO ---
musica_carregada = False
if os.path.exists(ARQUIVO_MUSICA):
    try:
        pygame.mixer.music.load(ARQUIVO_MUSICA)
        pygame.mixer.music.set_volume(0.2)  # VOLUME BAIXO
        pygame.mixer.music.play(-1)  # LOOP INFINITO
        musica_carregada = True
        print("Música de fundo carregada e tocando!")
    except Exception as e:
        print(f"Erro ao carregar música: {e}")
else:
    print(f"{ARQUIVO_MUSICA} não encontrado! Jogo roda sem música.")

# ===========================================
# RECORDE - TOP 5
# ===========================================
def carregar_top5():
    top5 = []
    if os.path.exists(ARQUIVO_RECORDE):
        try:
            with open(ARQUIVO_RECORDE, "r", encoding="utf-8") as f:
                for linha in f.readlines():
                    linha = linha.strip()
                    if linha and ":" in linha:
                        nome, pontos = linha.split(":", 1)
                        try:
                            top5.append((nome.strip(), int(pontos)))
                        except:
                            pass
            top5.sort(key=lambda x: x[1], reverse=True)
            top5 = top5[:TOP_N]
        except:
            pass
    return top5

def salvar_top5(top5):
    with open(ARQUIVO_RECORDE, "w", encoding="utf-8") as f:
        for nome, pontos in top5:
            f.write(f"{nome}:{pontos}\n")

def adicionar_recorde(nome, pontos):
    top5 = carregar_top5()
    top5.append((nome, pontos))
    top5.sort(key=lambda x: x[1], reverse=True)
    top5 = top5[:TOP_N]
    salvar_top5(top5)
    return top5

top5_recordes = carregar_top5()

# ===========================================
# BANNER ASCII
# ===========================================
BANNER = [
    "╔═══════════════════════════════════════════════════════════════════════════════╗",
    "║                                  Jogo da cobrinha                             ║",
    "║                             Aplicação  Python   Pygame                        ║",
    "║                       Criado por Leonardo de Moura Fuseti                     ║",
    "║                      Copyright 2025 - All Rights Reserved                     ║",
    "╚═══════════════════════════════════════════════════════════════════════════════╝"
]

# ===========================================
# FUNÇÕES DO JOGO
# ===========================================
def resetar_jogo():
    global cobra, direcao, comida, pontuacao, nivel, velocidade, tempo_inicio, game_over
    centro_x = (LARGURA // 2) // TAMANHO_BLOCO * TAMANHO_BLOCO
    centro_y = (ALTURA // 2) // TAMANHO_BLOCO * TAMANHO_BLOCO
    cobra = [(centro_x, centro_y)]
    direcao = (TAMANHO_BLOCO, 0)
    comida = gerar_comida()
    pontuacao = 0
    nivel = 1
    velocidade = FPS_INICIAL
    tempo_inicio = time.time()
    game_over = False

def gerar_comida():
    while True:
        x = random.randrange(0, LARGURA, TAMANHO_BLOCO)
        y = random.randrange(0, ALTURA, TAMANHO_BLOCO)
        nova = (x, y)
        if nova not in cobra:
            return nova

def desenhar_cobra(cobra):
    for i, bloco in enumerate(cobra):
        intensidade = max(50, 180 - i * 8)
        cor = (0, intensidade, 0) if i == 0 else (0, intensidade - 40, 0)
        pygame.draw.rect(tela, cor, (*bloco, TAMANHO_BLOCO, TAMANHO_BLOCO))
        pygame.draw.rect(tela, (0, 80, 0), (*bloco, TAMANHO_BLOCO, TAMANHO_BLOCO), 1)

def exibir_texto(texto, fonte, cor, x, y, centralizado=False):
    img = fonte.render(texto, True, cor)
    rect = img.get_rect()
    if centralizado:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    tela.blit(img, rect)

# ===========================================
# TELA DE INÍCIO COM TOP 5
# ===========================================
def tela_inicio():
    global top5_recordes
    top5_recordes = carregar_top5()

    tela.fill(PRETO)
    largura_banner = max(len(linha) for linha in BANNER) * fonte_tamanho * 0.6
    x_inicio = (LARGURA - largura_banner) // 2
    y_inicio = ALTURA // 2 - len(BANNER) * fonte_tamanho - 100

    for i, linha in enumerate(BANNER):
        exibir_texto(linha, fonte, VERDE, x_inicio, y_inicio + i * fonte_tamanho)

    exibir_texto("PRESSIONE QUALQUER TECLA PARA INICIAR", fonte_pequena, BRANCO,
                 LARGURA//2, y_inicio + len(BANNER) * fonte_tamanho + 60, centralizado=True)
    exibir_texto("Use as setas • R = Reiniciar • ESC = Sair", fonte_pequena, CINZA,
                 LARGURA//2, y_inicio + len(BANNER) * fonte_tamanho + 90, centralizado=True)

    # TOP 5
    exibir_texto("TOP 5 RECORDES", fonte_ranking, AMARELO, LARGURA//2, y_inicio + len(BANNER) * fonte_tamanho + 150, centralizado=True)
    y_top = y_inicio + len(BANNER) * fonte_tamanho + 200
    for i, (nome, pontos) in enumerate(top5_recordes):
        cor = DOURADO if i == 0 else PRATA if i == 1 else BRONZE if i == 2 else BRANCO
        medalha = "1st" if i == 0 else "2nd" if i == 1 else "3rd" if i == 2 else f"{i+1}th"
        texto = f"{medalha} {nome} - {pontos} pts"
        exibir_texto(texto, fonte_pequena, cor, LARGURA//2, y_top + i * 35, centralizado=True)

    if not top5_recordes:
        exibir_texto("Nenhum recorde ainda!", fonte_pequena, CINZA, LARGURA//2, y_top, centralizado=True)

    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                esperando = False

# ===========================================
# TELA DE NOVO RECORDE
# ===========================================
def tela_novo_recorde(pontos):
    nome = ""
    input_ativo = True

    while input_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome.strip():
                    input_ativo = False
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif len(nome) < 12 and evento.unicode.isalnum():
                    nome += evento.unicode.upper()

        tela.fill(PRETO)
        exibir_texto("NOVO RECORDE!", fonte_gameover, DOURADO, LARGURA//2, ALTURA//3, centralizado=True)
        exibir_texto(f"Pontuação: {pontos}", fonte, BRANCO, LARGURA//2, ALTURA//3 + 80, centralizado=True)
        exibir_texto("Digite seu nome:", fonte, BRANCO, LARGURA//2, ALTURA//2, centralizado=True)
        exibir_texto(nome + "_", fonte_input, VERDE, LARGURA//2, ALTURA//2 + 60, centralizado=True)
        exibir_texto("ENTER = Confirmar • ESC = Sair", fonte_pequena, CINZA, LARGURA//2, ALTURA//2 + 120, centralizado=True)

        pygame.display.flip()
        relogio.tick(30)

    nome = nome.strip() or "ANÔNIMO"
    global top5_recordes
    top5_recordes = adicionar_recorde(nome, pontos)
    return nome

# ===========================================
# INICIAR
# ===========================================
tela_inicio()
resetar_jogo()
relogio = pygame.time.Clock()

# ===========================================
# LOOP PRINCIPAL
# ===========================================
rodando = True
game_over_som_tocou = False
novo_recorde = False

while rodando:
    tempo_atual = time.time()
    tempo_jogo = int(tempo_atual - tempo_inicio)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
            if evento.key == pygame.K_r and game_over:
                resetar_jogo()
                game_over_som_tocou = False
                novo_recorde = False
                # Reinicia música se pausou
                if musica_carregada and not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play(-1)
                continue
            if not game_over:
                if evento.key == pygame.K_UP and direcao != (0, TAMANHO_BLOCO):
                    direcao = (0, -TAMANHO_BLOCO)
                elif evento.key == pygame.K_DOWN and direcao != (0, -TAMANHO_BLOCO):
                    direcao = (0, TAMANHO_BLOCO)
                elif evento.key == pygame.K_LEFT and direcao != (TAMANHO_BLOCO, 0):
                    direcao = (-TAMANHO_BLOCO, 0)
                elif evento.key == pygame.K_RIGHT and direcao != (-TAMANHO_BLOCO, 0):
                    direcao = (TAMANHO_BLOCO, 0)

    # --- GAME OVER ---
    if game_over:
        if not game_over_som_tocou and som_gameover:
            som_gameover.play()
            game_over_som_tocou = True

        if pontuacao > (top5_recordes[-1][1] if len(top5_recordes) >= TOP_N else -1) and not novo_recorde:
            tela_novo_recorde(pontuacao)
            novo_recorde = True

        tela.fill(PRETO)
        exibir_texto("GAME OVER", fonte_gameover, VERMELHO, LARGURA//2, ALTURA//2 - 120, centralizado=True)
        exibir_texto(f"Pontuação: {pontuacao}", fonte, BRANCO, LARGURA//2, ALTURA//2 - 60, centralizado=True)
        exibir_texto(f"Tempo: {tempo_jogo}s", fonte, BRANCO, LARGURA//2, ALTURA//2 - 30, centralizado=True)

        # TOP 5
        exibir_texto("TOP 5 RECORDES", fonte_pequena, AMARELO, LARGURA//2, ALTURA//2 + 10, centralizado=True)
        y_top = ALTURA//2 + 50
        for i, (nome, pontos) in enumerate(top5_recordes):
            cor = DOURADO if i == 0 else PRATA if i == 1 else BRONZE if i == 2 else BRANCO
            texto = f"{i+1}. {nome} - {pontos} pts"
            exibir_texto(texto, fonte_pequena, cor, LARGURA//2, y_top + i * 30, centralizado=True)

        exibir_texto("R = Jogar Novamente", fonte, AZUL, LARGURA//2, ALTURA//2 + 180, centralizado=True)
        exibir_texto("ESC = Sair", fonte, CINZA, LARGURA//2, ALTURA//2 + 210, centralizado=True)
        pygame.display.flip()
        relogio.tick(10)
        continue

    # --- MOVIMENTO ---
    cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
    cobra.insert(0, cabeca)

    # --- COMER + SOM + VELOCIDADE ---
    if cabeca == comida:
        comida = gerar_comida()
        pontuacao += 10
        if som_comer:
            som_comer.play()
        if pontuacao % AUMENTO_POR_NIVEL == 0:
            nivel += 1
            velocidade += 2
    else:
        cobra.pop()

    # --- COLISÃO ---
    if (cabeca[0] < 0 or cabeca[0] >= LARGURA or
        cabeca[1] < 0 or cabeca[1] >= ALTURA or
        cabeca in cobra[1:]):
        game_over = True

    # --- DESENHAR ---
    tela.fill(PRETO)
    pygame.draw.rect(tela, VERMELHO, (*comida, TAMANHO_BLOCO, TAMANHO_BLOCO))
    pygame.draw.rect(tela, (255, 100, 100), (*comida, TAMANHO_BLOCO, TAMANHO_BLOCO), 2)
    desenhar_cobra(cobra)

    # HUD
    margem = 20
    exibir_texto(f"Pontos: {pontuacao}", fonte, BRANCO, margem, margem)
    exibir_texto(f"Tempo: {tempo_jogo}s", fonte, BRANCO, margem, margem + fonte_tamanho + 10)
    exibir_texto(f"Nível: {nivel}", fonte, BRANCO, LARGURA - 140, margem)
    if top5_recordes:
        exibir_texto(f"1st {top5_recordes[0][0]} - {top5_recordes[0][1]}", fonte_pequena, DOURADO, LARGURA//2, 20, centralizado=True)
    exibir_texto("© 2025 Leonardo de Moura Fuseti", fonte_pequena, CINZA, LARGURA//2, ALTURA - 40, centralizado=True)

    pygame.display.flip()
    relogio.tick(velocidade)

# ===========================================
# FINALIZAR
# ===========================================
if musica_carregada:
    pygame.mixer.music.stop()
pygame.quit()