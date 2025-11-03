# 👋🏻 Leonardo de Moura Fuseti

Estudante de Defesa Cibernetica no Polo Estacio Piumhi MG . Formação tecnica em Tecnico em Redes de Computadores no IFMG Bambui MG , intusiasta na programação gostando muito de Python e evoluindo dia a dia .

### Conecte-se comigo

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://www.dio.me/users/mourafuseti)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:mourafuseti@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/leonardo-moura-fuseti-4052b0359/)

### Habilidades

![HTML](https://img.shields.io/badge/HTML-000?style=for-the-badge&logo=html5&logoColor=30A3DC)
![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=E94D5F)
![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript&logoColor=F0DB4F)
![Sass](https://img.shields.io/badge/SASS-000?style=for-the-badge&logo=sass&logoColor=CD6799)
![Bootstrap](https://img.shields.io/badge/bootstrap-000?style=for-the-badge&logo=bootstrap&logoColor=553C7B)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)

### GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=mourafuseti&theme=transparent&bg_color=000&border_color=30A3DC&show_icons=true&icon_color=30A3DC&title_color=E94D5F&text_color=FFF)

![Cobrinha](https://img.shields.io/badge/Jogo-Cobrinha-green?style=for-the-badge&logo=python) 

# Jogo da Cobrinha

 
**Aplicação em Python + Pygame**  
**Criado por: Leonardo de Moura Fuseti**  
**Copyright 2025 - All Rights Reserved**

---

## Descrição

Um clássico **Jogo da Cobrinha** com recursos modernos:
- Tela cheia
- Música de fundo (volume baixo)
- Sons ao comer e Game Over
- Velocidade aumenta a cada **40 pontos**
- **TOP 5 recordes** com nome do jogador
- Salva recordes em `recorde.txt`
- Executável `.exe` incluso (roda sem Python!)

---

## Como Jogar

| Ação | Tecla |
|------|-------|
| Mover | Setas do teclado |
| Reiniciar | `R` |
| Sair | `ESC` |

> **Objetivo:** Coma a comida vermelha (+10 pontos) e evite bater!

---

## Arquivos Incluídos

```
jogo/
├── cobrinha.exe          ← Executável (roda sem Python)
├── cobrinha.py           ← Código-fonte (opcional)
├── comer.wav             ← Som ao comer
├── gameover.wav          ← Som de Game Over
├── musica.wav            ← Música de fundo
├── recorde.txt           ← Salva os TOP 5 recordes
└── README.md             ← Este arquivo
```

---

## Como Executar

### Opção 1: Usar o `.exe` (recomendado)
1. Dê **dois cliques em `cobrinha.exe`**
2. Jogue em tela cheia!

> Funciona em qualquer PC com Windows (sem instalar nada)

---

### Opção 2: Rodar com Python (desenvolvedores)

```powershell
# Instalar dependências
pip install pygame

# Executar
python cobrinha.py
```

---

## Recorde

- O jogo salva os **5 melhores jogadores** em `recorde.txt`
- Ao bater um recorde, digite seu nome (máx 12 letras)
- O ranking aparece na tela inicial e no Game Over

---

## Créditos

- **Desenvolvedor:** Leonardo de Moura Fuseti
- **Linguagem:** Python 3.13
- **Biblioteca:** Pygame
- **Sons:** [Freesound.org](https://freesound.org) (CC0)
- **Música:** Loop de fundo (CC0)

---

## Compilação (para desenvolvedores)

```powershell
pyinstaller --onefile --windowed ^
  --add-data "comer.wav;." ^
  --add-data "gameover.wav;." ^
  --add-data "musica.wav;." ^
  cobrinha.py
```

---

## Distribuição

Você pode copiar a pasta inteira ou apenas:
```
cobrinha.exe
comer.wav
gameover.wav
musica.wav
```
→ O jogo funcionará em qualquer PC!

---

## Licença

**Todos os direitos reservados © 2025 Leonardo de Moura Fuseti**  
Uso pessoal e educacional permitido.  
Proibida a comercialização ou redistribuição sem permissão.

---

> **Divirta-se e bata o recorde!**
```


