import cv2
import mediapipe as mp
import pygame
import chess
from groq import Groq
import random
import math

# ======================
# GROQ API
# ======================
GROQ_API_KEY = "PASTE_YOUR_GROQ_KEY"
client = Groq(api_key=GROQ_API_KEY)

# ======================
# PYGAME FULLSCREEN
# ======================
pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

BOARD_SIZE = WIDTH//2
CAM_SIZE = WIDTH//2
SQUARE = BOARD_SIZE//8

font = pygame.font.SysFont("Segoe UI Symbol",48)
small_font = pygame.font.SysFont("Arial",28)
big_font = pygame.font.SysFont("Arial",70)

# ======================
# CHESS
# ======================
board = chess.Board()

selected_square=None
possible_moves=[]

captured_white=[]
captured_black=[]

game_over=False
winner_text=""

# ======================
# CURSOR
# ======================
cursor_x=0
cursor_y=0

prev_x=0
prev_y=0

alpha=0.20
deadzone=3

pinch_state=False
pinch_cooldown=0

# ======================
# CAMERA
# ======================
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

cap=cv2.VideoCapture(0)

# ======================
# PIECE SYMBOLS
# ======================
symbols={
"P":"♙","R":"♖","N":"♘","B":"♗","Q":"♕","K":"♔",
"p":"♟","r":"♜","n":"♞","b":"♝","q":"♛","k":"♚"
}

# ======================
# DRAW BOARD
# ======================
def draw_board():

    colors=[(240,217,181),(181,136,99)]

    for r in range(8):
        for c in range(8):

            pygame.draw.rect(
                screen,
                colors[(r+c)%2],
                (c*SQUARE,r*SQUARE,SQUARE,SQUARE)
            )

    if selected_square:

        r=7-chess.square_rank(selected_square)
        c=chess.square_file(selected_square)

        pygame.draw.rect(screen,(0,255,0),
                         (c*SQUARE,r*SQUARE,SQUARE,SQUARE),4)

    for m in possible_moves:

        sq=m.to_square

        r=7-chess.square_rank(sq)
        c=chess.square_file(sq)

        pygame.draw.rect(screen,(255,0,0),
                         (c*SQUARE,r*SQUARE,SQUARE,SQUARE),3)

# ======================
# DRAW PIECES
# ======================
def draw_pieces():

    for sq in chess.SQUARES:

        piece=board.piece_at(sq)

        if piece:

            sym=symbols[piece.symbol()]

            r=7-chess.square_rank(sq)
            c=chess.square_file(sq)

            text=font.render(sym,True,(0,0,0))

            screen.blit(text,(c*SQUARE+18,r*SQUARE+10))

# ======================
# DRAW CAPTURED
# ======================
def draw_captured():

    y1=BOARD_SIZE+10
    y2=BOARD_SIZE+70

    label_user=small_font.render("USER",True,(255,255,255))
    label_ai=small_font.render("AI",True,(255,255,255))

    screen.blit(label_user,(20,y1))
    screen.blit(label_ai,(20,y2))

    x=140
    for p in captured_white:

        text=font.render(symbols[p],True,(255,255,255))
        screen.blit(text,(x,y1-10))
        x+=40

    x=140
    for p in captured_black:

        text=font.render(symbols[p],True,(255,255,255))
        screen.blit(text,(x,y2-10))
        x+=40

# ======================
# CURSOR TO BOARD
# ======================
def cursor_to_square(x,y):

    col=int(x//SQUARE)
    row=int(y//SQUARE)

    row=7-row

    if col<0 or col>7 or row<0 or row>7:
        return None

    return chess.square(col,row)

# ======================
# PINCH DETECTION
# ======================
def detect_pinch(ix,iy,tx,ty):

    dist=math.hypot(ix-tx,iy-ty)

    return dist<40

# ======================
# AI MOVE
# ======================
def ai_move():

    global board

    legal=[m.uci() for m in board.legal_moves]
    fen=board.fen()

    prompt=f"""
You are a strong chess engine.

Board position:
{fen}

Legal moves:
{legal}

Return only the best move.
"""

    try:

        res=client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role":"user","content":prompt}]
        )

        txt=res.choices[0].message.content.strip()
        move=txt.split()[0]

        if move in legal:

            move_obj=chess.Move.from_uci(move)

            captured=board.piece_at(move_obj.to_square)

            if captured:
                captured_black.append(captured.symbol())

            board.push(move_obj)
            return

    except:
        pass

    capture_moves=[]
    normal_moves=[]

    for m in board.legal_moves:

        if board.is_capture(m):
            capture_moves.append(m)
        else:
            normal_moves.append(m)

    if capture_moves:
        move=random.choice(capture_moves)
    else:
        move=random.choice(normal_moves)

    captured=board.piece_at(move.to_square)

    if captured:
        captured_black.append(captured.symbol())

    board.push(move)

# ======================
# CHECK GAME
# ======================
def check_game():

    global game_over,winner_text

    if board.is_checkmate():

        game_over=True

        if board.turn:
            winner_text="BLACK WINS"
        else:
            winner_text="WHITE WINS"

# ======================
# RESET GAME
# ======================
def reset_game():

    global board,selected_square,possible_moves
    global captured_white,captured_black
    global game_over,winner_text

    board=chess.Board()

    selected_square=None
    possible_moves=[]

    captured_white=[]
    captured_black=[]

    game_over=False
    winner_text=""

# ======================
# MAIN LOOP
# ======================
running=True

while running:

    ret,frame=cap.read()

    frame=cv2.flip(frame,1)

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    res=hands.process(rgb)

    h,w,_=frame.shape

    pinch=False

    if res.multi_hand_landmarks:

        for hand in res.multi_hand_landmarks:

            lm=hand.landmark

            thumb=lm[4]
            index=lm[8]

            tx,ty=int(thumb.x*w),int(thumb.y*h)
            ix,iy=int(index.x*w),int(index.y*h)

            cv2.circle(frame,(tx,ty),8,(0,0,255),-1)
            cv2.circle(frame,(ix,iy),8,(0,0,255),-1)

            # FULL FRAME MAPPING
            cursor_x=int(index.x*BOARD_SIZE)
            cursor_y=int(index.y*BOARD_SIZE)

            pinch=detect_pinch(ix,iy,tx,ty)

    # SMOOTH CURSOR
    smooth_x=int(prev_x+alpha*(cursor_x-prev_x))
    smooth_y=int(prev_y+alpha*(cursor_y-prev_y))

    if abs(smooth_x-prev_x)<deadzone:
        smooth_x=prev_x

    if abs(smooth_y-prev_y)<deadzone:
        smooth_y=prev_y

    prev_x=smooth_x
    prev_y=smooth_y

    if pinch_cooldown>0:
        pinch_cooldown-=1

    if pinch and not pinch_state and pinch_cooldown==0 and not game_over:

        pinch_state=True
        pinch_cooldown=8

        sq=cursor_to_square(smooth_x,smooth_y)

        if sq:

            if selected_square is None:

                piece=board.piece_at(sq)

                if piece and piece.color==chess.WHITE:

                    selected_square=sq

                    possible_moves=[
                        m for m in board.legal_moves
                        if m.from_square==sq
                    ]

            else:

                move=None

                for m in possible_moves:

                    if m.to_square==sq:
                        move=m

                if move:

                    captured=board.piece_at(move.to_square)

                    if captured:
                        captured_white.append(captured.symbol())

                    board.push(move)

                    selected_square=None
                    possible_moves=[]

                    check_game()

                    if not game_over:
                        ai_move()

                else:

                    selected_square=None
                    possible_moves=[]

    if not pinch:
        pinch_state=False

    screen.fill((0,0,0))

    draw_board()
    draw_pieces()
    draw_captured()

    pygame.draw.circle(screen,(0,0,255),(smooth_x,smooth_y),8)

    cam=cv2.resize(frame,(CAM_SIZE,HEIGHT))
    cam=cv2.cvtColor(cam,cv2.COLOR_BGR2RGB)
    cam=pygame.surfarray.make_surface(cam.swapaxes(0,1))

    screen.blit(cam,(BOARD_SIZE,0))

    if game_over:

        txt=big_font.render(winner_text,True,(255,0,0))
        screen.blit(txt,(BOARD_SIZE//2-200,HEIGHT//2-40))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_RETURN:
                running=False

            if event.key==pygame.K_SPACE:
                reset_game()

cap.release()
pygame.quit()
