from time import sleep
import random

WHITE_SHAPE = ['♟', '♚', '♛', '♜', '♞', '♝']  # change here to change shape
BLACK_SHAPE = ['♙', '♔', '♕', '♖', '♘', '♗']


class Player:
    def __init__(self, bot=0):
        self.is_black = False
        self.bot = bot
        self.can_short_castling = True
        self.can_long_castling = True


class Piece:
    def __init__(self, type, is_black=False):
        self.type = type    # 0.pawn 1.king 2.queen 3.tower 4.knight 5.bishop
        self.black = is_black
        self.en_passant = False


class ChessBoard:
    def __init__(self, white_player, black_player):
        self.board = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
        ]
        self.board2 = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
        ]
        self.white_player = white_player
        self.black_player = black_player
        self.black_player.is_black = True

    def init_board(self):
        for l in range(8):
            for n in range(8):

                if n == 1:  #2
                    self.board[l][n] = Piece(0)
                    # self.board[l][n].spot[0] = l
                    # self.board[l][n].spot[1] = n

                if n == 6:  #7
                    self.board[l][n] = Piece(0, True)
                    # self.board[l][n].spot[0] = l
                    # self.board[l][n].spot[1] = n

                if l == 0:  #A
                    if n == 0:  #1
                        self.board[l][n] = Piece(3)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(3, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                if l == 1:  #B
                    if n == 0:  #1
                        self.board[l][n] = Piece(4)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(4, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n

                if l == 2:  #C
                    if n == 0:  #1
                        self.board[l][n] = Piece(5)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(5, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n

                if l == 3:  #D
                    if n == 0:  #1
                        self.board[l][n] = Piece(2)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(2, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n

                if l == 4:  #E
                    if n == 0:  #1
                        self.board[l][n] = Piece(1)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(1, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n

                if l == 5:  #F
                    if n == 0:  #1
                        self.board[l][n] = Piece(5)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(5, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n

                if l == 6:  #G
                    if n == 0:  #1
                        self.board[l][n] = Piece(4)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(4, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n

                if l == 7:  #H
                    if n == 0:  #1
                        self.board[l][n] = Piece(3)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n
                    if n == 7:  #8
                        self.board[l][n] = Piece(3, True)
                        # self.board[l][n].spot[0] = l
                        # self.board[l][n].spot[1] = n

        self.reset2()

    def reset2(self):
        for l in range(8):
            for n in range(8):
                self.board2[l][n] = self.board[l][n]

    def reset(self, white_player, black_player):
        self.white_player = white_player
        self.black_player = black_player
        self.init_board()

    def reset_en_passant(self, player):
        for l in range(8):
            for n in range(8):
                piece = self.board[l][n]
                if isinstance(piece, Piece):
                    if piece.black == player.is_black and piece.type == 0:
                        print(piece.en_passant, end=' ')
                        piece.en_passant = False
        print("\n")

    def print_c_board(self):

        front_board =[
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
        ]

        for l in range(8):
            for n in range(8):
                if isinstance(self.board[l][n], Piece):

                    if self.board[l][n].type == 0:
                        if self.board[l][n].black:
                            front_board[l][n] = BLACK_SHAPE[self.board[l][n].type]
                        else:
                            front_board[l][n] = WHITE_SHAPE[self.board[l][n].type]
                    elif self.board[l][n].type == 1:
                        if self.board[l][n].black:
                            front_board[l][n] = BLACK_SHAPE[self.board[l][n].type]
                        else:
                            front_board[l][n] = WHITE_SHAPE[self.board[l][n].type]
                    if self.board[l][n].type == 2:
                        if self.board[l][n].black:
                            front_board[l][n] = BLACK_SHAPE[self.board[l][n].type]
                        else:
                            front_board[l][n] = WHITE_SHAPE[self.board[l][n].type]
                    elif self.board[l][n].type == 3:
                        if self.board[l][n].black:
                            front_board[l][n] = BLACK_SHAPE[self.board[l][n].type]
                        else:
                            front_board[l][n] = WHITE_SHAPE[self.board[l][n].type]
                    elif self.board[l][n].type == 4:
                        if self.board[l][n].black:
                            front_board[l][n] = BLACK_SHAPE[self.board[l][n].type]
                        else:
                            front_board[l][n] = WHITE_SHAPE[self.board[l][n].type]
                    elif self.board[l][n].type == 5:
                        if self.board[l][n].black:
                            front_board[l][n] = BLACK_SHAPE[self.board[l][n].type]
                        else:
                            front_board[l][n] = WHITE_SHAPE[self.board[l][n].type]
                else:
                    front_board[l][n] = '_'

        fb = front_board
        print(f"    _______________________________\n"
 f"  8|_{fb[0][7]}_| {fb[1][7]} |_{fb[2][7]}_| {fb[3][7]} |_{fb[4][7]}_| {fb[5][7]} |_{fb[6][7]}_| {fb[7][7]} |\n"
 f"  7| {fb[0][6]} |_{fb[1][6]}_| {fb[2][6]} |_{fb[3][6]}_| {fb[4][6]} |_{fb[5][6]}_| {fb[6][6]} |_{fb[7][6]}_|\n"
 f"  6|_{fb[0][5]}_| {fb[1][5]} |_{fb[2][5]}_| {fb[3][5]} |_{fb[4][5]}_| {fb[5][5]} |_{fb[6][5]}_| {fb[7][5]} |\n"
 f"  5| {fb[0][4]} |_{fb[1][4]}_| {fb[2][4]} |_{fb[3][4]}_| {fb[4][4]} |_{fb[5][4]}_| {fb[6][4]} |_{fb[7][4]}_|\n"
 f"  4|_{fb[0][3]}_| {fb[1][3]} |_{fb[2][3]}_| {fb[3][3]} |_{fb[4][3]}_| {fb[5][3]} |_{fb[6][3]}_| {fb[7][3]} |\n"
 f"  3| {fb[0][2]} |_{fb[1][2]}_| {fb[2][2]} |_{fb[3][2]}_| {fb[4][2]} |_{fb[5][2]}_| {fb[6][2]} |_{fb[7][2]}_|\n"
 f"  2|_{fb[0][1]}_| {fb[1][1]} |_{fb[2][1]}_| {fb[3][1]} |_{fb[4][1]}_| {fb[5][1]} |_{fb[6][1]}_| {fb[7][1]} |\n"
 f"  1| {fb[0][0]} |_{fb[1][0]}_| {fb[2][0]} |_{fb[3][0]}_| {fb[4][0]} |_{fb[5][0]}_| {fb[6][0]} |_{fb[7][0]}_|\n"
  "     A   B   C   D   E   F   G   H")

    def print_eaten(self):
        white_eaten, black_eaten = [], []

        white_eaten.append(WHITE_SHAPE[2])
        black_eaten.append(BLACK_SHAPE[2])

        for i in range(2):
            white_eaten.append(WHITE_SHAPE[3])
            black_eaten.append(BLACK_SHAPE[3])

        for i in range(2):
            white_eaten.append(WHITE_SHAPE[4])
            black_eaten.append(BLACK_SHAPE[4])

        for i in range(2):
            white_eaten.append(WHITE_SHAPE[5])
            black_eaten.append(BLACK_SHAPE[5])

        for i in range(8):
            white_eaten.append(WHITE_SHAPE[0])
            black_eaten.append(BLACK_SHAPE[0])

        for l in range(8):
            for n in range(8):
                # piece =
                if isinstance(self.board[l][n], Piece):
                    if self.board[l][n].type != 1:
                        if self.board[l][n].black:
                            black_eaten.remove(BLACK_SHAPE[self.board[l][n].type])
                            ...
                        else:
                            bo = self.board[l][n].type
                            white_eaten.remove(WHITE_SHAPE[self.board[l][n].type])
        if len(white_eaten) == 0 and len(black_eaten) == 0:
            return 0

        print(" -------------------------------------------------------------------\n  ", end='')
        for p in white_eaten:
            print(p, end=' ')
        print("\n  ", end='')
        for p in black_eaten:
            print(p, end=' ')
        print("")
        print(" -------------------------------------------------------------------  ")
        return 1

    def move(self, spot_from, spot_to):  # >0 success, <= 0 not success

        possible_moves = av_moves(self, spot_from)
        legal_moves = check_legal(self, spot_from, possible_moves)

        for spot in legal_moves:
            if spot.strip().capitalize() == spot_to.strip().capitalize():
                lf = letter_to_number(spot_from[0])
                nf = int(spot_from[1]) - 1
                lt = letter_to_number(spot_to[0])
                nt = int(spot_to[1]) - 1
                self.board[lt][nt] = self.board[lf][nf]
                self.board[lf][nf] = ''
                return 1
        print("Move error...\n")
        return 0


# ----------> Stand-alone functions <----------


def letter_to_number(letter):
    if letter == 'a' or letter == 'A':
        return 0
    elif letter == 'b' or letter == 'B':
        return 1
    elif letter == 'c' or letter == 'C':
        return 2
    elif letter == 'd' or letter == 'D':
        return 3
    elif letter == 'e' or letter == 'E':
        return 4
    elif letter == 'f' or letter == 'F':
        return 5
    elif letter == 'g' or letter == 'G':
        return 6
    elif letter == 'h' or letter == 'H':
        return 7
    else:
        return -1


def number_to_letter(number):
    if number == 0:
        return 'A'
    elif number == 1:
        return 'B'
    elif number == 2:
        return 'C'
    elif number == 3:
        return 'D'
    elif number == 4:
        return 'E'
    elif number == 5:
        return 'F'
    elif number == 6:
        return 'G'
    elif number == 7:
        return 'H'
    else:
        return 'error'


def get_move_player(chess, player):
    Keep = True
    while Keep:
        move = input("\n(ES.'A1 in B2')\nInsert move --> ")
        keep = False
        move_from, move_to = '', ''
        try:
            move_from, move_to = move.split(" in ", 1)
        except ValueError:
            keep = True
            print("\nFormat is not correct.\nNeeds to be like this: ES.'A1 in B2'\nTry again...")
            sleep(1)
            chess.print_c_board()
            continue
        if not keep:
            if not isinstance(move_from, str) or not isinstance(move_to, str):
                print("\nFormat is not correct.\nNeeds to be like this: ES.'A1 in B2'\nTry again...")
                keep = True  # wrong spot format
                sleep(1)
                chess.print_c_board()
            else:
                if len(move_from) > 2 or len(move_to) > 2 or len(move_from) < 2 or len(move_to) < 2:
                    print("\nFormat is not correct.\nNeeds to be like this: ES.'A1 in B2'\nTry again...")
                    keep = True  # wrong spot format
                    sleep(1)
                    chess.print_c_board()

            if check_from_spot(chess, move_from, player.is_black):
                keep = True  # starting spot is not legal
                print("\nMove is not legal...Try again\n")
                sleep(1)
                chess.print_c_board()
                continue

            if check_to_spot(chess, move_to, player.is_black):
                keep = True  # destination spot is not legal
                print("\nMove is not legal...Try again\n")

                sleep(1)
                chess.print_c_board()
                continue
        if not keep:
            break
    return move_from.capitalize(), move_to.capitalize()


def check_from_spot(chess, spot, black):
    l = letter_to_number(spot[0])
    if l < 0:
        return 5
    try:
        n = int(spot[1]) - 1
    except ValueError:
        return 5
    if l < 0 or l > 7:
        return 1    # letter is wrong
    if n < 0 or n > 7:
        return 2    # number is wrong
    if not isinstance(chess.board[l][n], Piece):
        return 3   # empty space
    if chess.board[l][n].black != black:
        return 4    # piece is of different color
    return 0


def check_to_spot(chess, spot, black):
    l = letter_to_number(spot[0])
    if l < 0:
        return 5
    try:
        n = int(spot[1]) - 1
    except ValueError:
        return 5
    if l < 0 or l > 7:
        return 1    # letter is wrong
    if n < 0 or n > 7:
        return 2    # number is wrong
    if isinstance(chess.board[l][n], Piece) and chess.board[l][n].black == black:
        return 4    # piece is the same color
    return 0


def check_legal(chess, spot_from,  po_moves):
    available_moves = po_moves.copy()
    no_moves = set()
    fl, fn = letter_to_number(spot_from[0]), int(spot_from[1]) - 1
    color = chess.board[fl][fn].black

    for move in available_moves:
        l = letter_to_number(move[0])
        n = int(move[1]) - 1
        chess.reset2()
        chess.board2[l][n] = chess.board2[fl][fn]
        chess.board2[fl][fn] = ''

        for lk in range(8):  # find own king
            for nk in range(8):
                if isinstance(chess.board2[lk][nk], Piece):
                    if chess.board2[lk][nk].type == 1 and chess.board2[lk][nk].black == color:
                        king_spot = number_to_letter(lk) + str(nk + 1)

        # check among all the other player legal moves in board2, if there is the same one as the king is at
        for lt in range(8):
            for nt in range(8):
                if isinstance(chess.board2[lt][nt], Piece):
                    if chess.board2[lt][nt].black != color:
                        moves2 = av_moves(chess, number_to_letter(lt) + str(nt+1), True)
                        for m2 in moves2:
                            if king_spot == m2:
                                no_moves.add(move)
    for m in no_moves:
        available_moves.remove(m)
    return available_moves


def av_moves(chess, spot_from, test=False):
    l_from = letter_to_number(spot_from[0])
    n_from = int(spot_from[1]) - 1
    if test:
        type = chess.board2[l_from][n_from].type
    else:
        type = chess.board[l_from][n_from].type
    av_moves = []
    if type == 0:
        av_moves = pawn_av_move(chess, l_from, n_from, test)
    elif type == 1:
        av_moves = king_av_move(chess, l_from, n_from, test)
    elif type == 2:
        av_moves = queen_av_move(chess, l_from, n_from, test)
    elif type == 3:
        av_moves = tower_av_move(chess, l_from, n_from, test)
    elif type == 4:
        av_moves = knight_av_move(chess, l_from, n_from, test)
    elif type == 5:
        av_moves = bishop_av_move(chess, l_from, n_from, test)

    return av_moves


def check_checkmate(chess, turn_color):  # 1 -> checkmate | 2 -> stallo
    legal_moves = []
    pos_moves = []
    for l, x in enumerate(chess.board):
        for n, spot in enumerate(x):
            if isinstance(spot, Piece):
                if spot.black == turn_color:
                    i_pos_moves = av_moves(chess, number_to_letter(l) + str(n+1))
                    pos_moves = pos_moves + i_pos_moves
                    legal_moves = legal_moves + check_legal(chess, number_to_letter(l) + str(n+1), i_pos_moves)
    if len(pos_moves) == 0:
        return 2
    if len(legal_moves) == 0:
        return 1
    return 0


def check_check(chess, turn_color):
    king_spot = '..'
    for l in range(8):
        if king_spot != '..':
            break
        for n in range(8):
            piece = chess.board[l][n]
            if isinstance(piece, Piece):
                if piece.black == turn_color and piece.type == 1:
                    king_spot = number_to_letter(l) + str(n+1)
                    break

    for l in range(8):
        for n in range(8):
            piece = chess.board[l][n]
            spot = number_to_letter(l) + str(n+1)
            if isinstance(piece, Piece):
                if piece.black != turn_color:
                    po_moves = av_moves(chess, spot)
                    for m in po_moves:
                        if m == king_spot:
                            return 1
    return 0


def choose_transf_option():
    t = -1
    while True:
        print(" What do you wanna transform your pawn into? ")
        print("\n Options:\n 0 - Leave it as pawn \n 1 - Queen \n 2 - Tower \n 3 - Knight \n 4 - Bishop")
        choise = input("Insert a number from 0 to 4 --> ")
        try:
            t = int(choise)
        except ValueError:
            print("Wrong input, only insert a number from 0 to 4.\nTry again...\n\n")
            continue
        if t > 0:
            t = t + 1
        if 0 <= t <= 5:
            break
        print("Wrong input, only insert a number from 0 to 4.\nTry again...\n\n")
    return t


def check_castling(move_from, player):
    if player.is_black:
        if move_from == 'E8' or move_from == 'H8':
            player.can_short_castling = False
        if move_from == 'E8' or move_from == 'A8':
            player.can_long_castling = False
    else:
        if move_from == 'E1' or move_from == 'H1':
            player.can_short_castling = False
        if move_from == 'E1' or move_from == 'A1':
            player.can_long_castling = False


def castling(chess, move_from, move_to, player):
    if not isinstance(move_from, str) or not isinstance(move_to, str):
        return 0
    else:
        if len(move_from) > 2 or len(move_to) > 2 or len(move_from) < 2 or len(move_to) < 2:
            return 0

    if check_from_spot(chess, move_from, player.is_black):
        return 0

    if check_to_spot(chess, move_to, player.is_black):
        return 0

    if player.is_black:
        if move_from == "E8" and move_to == "C8":
            if player.can_long_castling:
                if long_castling(chess, player):
                    player.can_short_castling = False
                    player.can_long_castling = False
                    return 1
            return 0
        elif move_from == "E8" and move_to == "G8":
            if player.can_long_castling:
                if short_castling(chess, player):
                    player.can_short_castling = False
                    player.can_long_castling = False
                    return 1
            return 0
    else:
        if move_from == "E1" and move_to == "C1":
            if player.can_long_castling:
                if long_castling(chess, player):
                    player.can_short_castling = False
                    player.can_long_castling = False
                    return 1
            return 0
        elif move_from == "E1" and move_to == "G1":
            if player.can_long_castling:
                if short_castling(chess, player):
                    player.can_short_castling = False
                    player.can_long_castling = False
                    return 1
            return 0
    return 0


def long_castling(chess, player):
    if player.is_black:
        n = 7
    else:
        n = 0
    if isinstance(chess.board[4][n], Piece) and isinstance(chess.board[0][n], Piece):
        if chess.board[4][n].type == 1 and chess.board[0][n].type == 3:
            if isinstance(chess.board[1][n], str) and isinstance(chess.board[2][n], str):
                if isinstance(chess.board[3][n], str):
                    if not check_check(chess, player.is_black):
                        chess.board[2][n] = chess.board[4][n]
                        chess.board[4][n] = ''
                        if not check_check(chess, player.is_black):
                            chess.board[3][n] = chess.board[0][n]
                            chess.board[0][n] = ''
                            return 1
                        else:
                            chess.board[4][n] = chess.board[2][n]
                            chess.board[2][n] = ''
    return 0


def short_castling(chess, player):
    if player.is_black:
        n = 7
    else:
        n = 0
    if isinstance(chess.board[4][n], Piece) and isinstance(chess.board[7][n], Piece):
        if chess.board[4][n].type == 1 and chess.board[7][n].type == 3:
            if isinstance(chess.board[5][n], str) and isinstance(chess.board[6][n], str):
                if not check_check(chess, player.is_black):
                    chess.board[6][n] = chess.board[4][n]
                    chess.board[4][n] = ''
                    if not check_check(chess, player.is_black):
                        chess.board[5][n] = chess.board[7][n]
                        chess.board[7][n] = ''
                        return 1
                    else:
                        chess.board[4][n] = chess.board[6][n]
                        chess.board[6][n] = ''
    return 0


def check_en_passant(chess, move_from, move_to, player):
    if chess.board[letter_to_number(move_to[0])][int(move_to[1]) -1].type == 0:
        if player.is_black:
            if move_from[1] == '7' and move_to[1] == '5':
                chess.board[letter_to_number(move_to[0])][int(move_to[1]) -1].en_passant = True
        else:
            if move_from[1] == '2' and move_to[1] == '4':
                chess.board[letter_to_number(move_to[0])][int(move_to[1]) -1].en_passant = True


def en_passant(chess, move_from, move_to, player):
    if not isinstance(move_from, str) or not isinstance(move_to, str):
        return 0
    else:
        if len(move_from) > 2 or len(move_to) > 2 or len(move_from) < 2 or len(move_to) < 2:
            return 0

    if check_from_spot(chess, move_from, player.is_black):
        return 0

    if check_to_spot(chess, move_to, player.is_black):
        return 0

    lt, nt = letter_to_number(move_to[0]), int(move_to[1]) - 1
    lf, nf = letter_to_number(move_from[0]), int(move_from[1]) - 1
    piece_from = chess.board[lf][nf]
    if player.is_black:
        if isinstance(piece_from, Piece) and nf == 4 and nt == 3:
            if player.is_black == piece_from.black and piece_from.type == 0:
                if isinstance(chess.board[lt][nt], str):
                    if lt + 1 <= 7:
                        if isinstance(chess.board[lt + 1][nt], Piece):
                            if chess.board[lt + 1][nt].type == 0 and chess.board[lt + 1][nt].en_passant:
                                chess.board[lt + 1][nt] = ''
                                chess.board[lt][nt] = chess.board[lf][nf]
                                chess.board[lf][nf] = ''
                                return 1
                    if lt - 1 >= 0:
                        if isinstance(chess.board[lt - 1][nt], Piece):
                            if chess.board[lt - 1][nt].type == 0 and chess.board[lt - 1][nt].en_passant:
                                chess.board[lt - 1][nt] = ''
                                chess.board[lt][nt] = chess.board[lf][nf]
                                chess.board[lf][nf] = ''
                                return 1
    else:
        if isinstance(piece_from, Piece) and nf == 3 and nt == 4:
            if player.is_black == piece_from.black and piece_from.type == 0:
                if isinstance(chess.board[lt][nt], str):
                    if lt + 1 <= 7:
                        if isinstance(chess.board[lt + 1][nt], Piece):
                            if chess.board[lt + 1][nt].type == 0 and chess.board[lt + 1][nt].en_passant:
                                chess.board[lt + 1][nt] = ''
                                chess.board[lt][nt] = chess.board[lf][nf]
                                chess.board[lf][nf] = ''
                                return 1
                    if lt - 1 >= 0:
                        if isinstance(chess.board[lt - 1][nt], Piece):
                            if chess.board[lt - 1][nt].type == 0 and chess.board[lt - 1][nt].en_passant:
                                chess.board[lt - 1][nt] = ''
                                chess.board[lt][nt] = chess.board[lf][nf]
                                chess.board[lf][nf] = ''
                                return 1
    return 0


# ----------> Pieces Logic <----------

def pawn_transformation(chess, move_to):
    lt, nt = letter_to_number(move_to[0]), int(move_to[1])-1
    black = chess.board[lt][nt].black
    if chess.board[lt][nt].type == 0:
        if black:
            if lt == 0:
                n = choose_transf_option()
                chess.board[lt][nt].type = n
                return 1
        else:
            if lt == 7:
                n = choose_transf_option()
                chess.board[lt][nt].type = n
                return 1
    return 0


def pawn_av_move(chess, l, n, test=False):
    av_moves = []
    if test:
        board = chess.board2
    else:
        board = chess.board
    if board[l][n].black:
        if (n - 1) > -1:
            if not isinstance(board[l][(n - 1)], Piece):
                av_moves.append(number_to_letter(l) + str(n))
            if l < 7:
                if isinstance(board[(l + 1)][(n - 1)], Piece):
                    if board[(l + 1)][(n - 1)].black != board[l][n].black:
                        av_moves.append(number_to_letter(l+1) + str(n))
            if l > 0:
                if isinstance(board[(l - 1)][(n - 1)], Piece):
                    if board[(l - 1)][(n - 1)].black != board[l][n].black:
                        av_moves.append(number_to_letter(l-1) + str(n))
        if n == 6:
            if not isinstance(board[l][(n - 2)], Piece) and not isinstance(board[l][(n-1)], Piece):
                av_moves.append(number_to_letter(l) + str(n - 1))

    else:
        if (n + 1) < 8:
            if not isinstance(board[l][(n + 1)], Piece):
                av_moves.append(number_to_letter(l) + str(n+2))

            if l < 7:
                if isinstance(board[(l + 1)][(n + 1)], Piece):
                    if board[(l + 1)][(n + 1)].black != board[l][n].black:
                        av_moves.append(number_to_letter(l+1) + str(n+2))
            if l > 0:
                if isinstance(board[(l - 1)][(n + 1)], Piece):
                    if board[(l - 1)][(n + 1)].black != board[l][n].black:
                        av_moves.append(number_to_letter(l-1) + str(n+2))

        if n == 1:
            if not isinstance(board[l][(n + 2)], Piece) and not isinstance(board[l][(n+1)], Piece):
                av_moves.append(number_to_letter(l) + str(n + 3))
    return av_moves


def king_av_move(chess, l, n, test=False):
    av_moves = []
    l_step = -1
    if test:
        board = chess.board2
    else:
        board = chess.board
    while l_step <= 1:
        n_step = -1
        while n_step <= 1:
            xl = l_step + l
            xn = n_step + n
            if xl <= 7 and xl >= 0 and xn <= 7 and xn >= 0:
                if isinstance(board[xl][xn], Piece):
                    if board[xl][xn].black != board[l][n].black:
                        av_moves.append(number_to_letter(xl) + str(xn + 1))
                else:
                    av_moves.append(number_to_letter(xl) + str(xn + 1))
            n_step = n_step + 1
        l_step = l_step + 1

    return av_moves


def queen_av_move(chess, l, n, test=False):
    av_moves1 = tower_av_move(chess, l, n, test)
    av_moves2 = bishop_av_move(chess, l, n, test)
    av_moves = av_moves1 + av_moves2
    return av_moves


def tower_av_move(chess, l, n, test=False):
    av_moves = []
    if test:
        board = chess.board2
    else:
        board = chess.board
    go = True
    x = l
    # right side
    while go:
        if x < 7:
            x = x + 1
        else:
            break
        if isinstance(board[x][n], Piece):
            if board[x][n].black == board[l][n].black:
                go = False
            else:
                av_moves.append(number_to_letter(x) + str(n+1))
                go = False
        else:
            av_moves.append(number_to_letter(x) + str(n + 1))
    go = True
    x = l
    # left side
    while go:
        if x > 0:
            x = x - 1
        else:
            break
        if isinstance(board[x][n], Piece):
            if board[x][n].black == board[l][n].black:
                go = False
            else:
                av_moves.append(number_to_letter(x) + str(n+1))
                go = False
        else:
            av_moves.append(number_to_letter(x) + str(n + 1))
    go = True
    x = n
    # upside
    while go:
        if x < 7:
            x = x + 1
        else:
            break
        if isinstance(board[l][x], Piece):
            if board[l][x].black == board[l][n].black:
                go = False
            else:
                av_moves.append(number_to_letter(l) + str(x + 1))
                go = False
        else:
            av_moves.append(number_to_letter(l) + str(x + 1))
    go = True
    x = n
    # downside
    while go:
        if x > 0:
            x = x - 1
        else:
            break
        if isinstance(board[l][x], Piece):
            if board[l][x].black == board[l][n].black:
                go = False
            else:
                av_moves.append(number_to_letter(l) + str(x + 1))
                go = False
        else:
            av_moves.append(number_to_letter(l) + str(x + 1))

    return av_moves


def knight_av_move(chess, l, n, test=False):
    av_moves = []
    if test:
        board = chess.board2
    else:
        board = chess.board
    step_l = [1, 2, -1, -2, 1, 2, -1, -2]
    step_n = [2, 1, -2, -1, -2, -1, 2, 1]
    for i in range(8):
        xl = l + step_l[i]
        xn = n + step_n[i]
        if xl<=7 and xl>=0 and xn<=7 and xn>=0:
            if isinstance(board[xl][xn], Piece):
                if board[xl][xn].black != board[l][n].black:
                    av_moves.append(number_to_letter(xl) + str(xn+1))
            else:
                av_moves.append(number_to_letter(xl) + str(xn + 1))
    return av_moves


def bishop_av_move(chess, l, n, test=False):
    av_moves = []
    if test:
        board = chess.board2
    else:
        board = chess.board

    # right-up
    lx, nx = l, n
    while lx < 7 and nx < 7:
        lx = lx + 1
        nx = nx + 1
        if isinstance(board[lx][nx], Piece):
            if board[lx][nx].black == board[l][n].black:
                break
            else:
                av_moves.append(number_to_letter(lx) + str(nx + 1))
                break
        else:
            av_moves.append(number_to_letter(lx) + str(nx + 1))
    # right-left
    lx, nx = l, n
    while lx > 0 and nx < 7:
        lx = lx - 1
        nx = nx + 1
        if isinstance(board[lx][nx], Piece):
            if board[lx][nx].black == board[l][n].black:
                break
            else:
                av_moves.append(number_to_letter(lx) + str(nx + 1))
                break
        else:
            av_moves.append(number_to_letter(lx) + str(nx + 1))
    # right-down
    lx, nx = l, n
    while lx < 7 and nx > 0:
        lx = lx + 1
        nx = nx - 1
        if isinstance(board[lx][nx], Piece):
            if board[lx][nx].black == board[l][n].black:
                break
            else:
                av_moves.append(number_to_letter(lx) + str(nx + 1))
                break
        else:
            av_moves.append(number_to_letter(lx) + str(nx + 1))
    # right-up
    lx, nx = l, n
    while lx > 0 and nx > 0:
        lx = lx - 1
        nx = nx - 1
        if isinstance(board[lx][nx], Piece):
            if board[lx][nx].black == board[l][n].black:
                break
            else:
                av_moves.append(number_to_letter(lx) + str(nx + 1))
                break
        else:
            av_moves.append(number_to_letter(lx) + str(nx + 1))

    return av_moves


# ----------> Bot Logic <----------

def make_rand_move(chess, player):
    i = 0
    spots_from = []
    for l, x in enumerate(chess.board):
        for n, piece in enumerate(x):
            if isinstance(piece, Piece):
                if piece.black == player.is_black:
                    spot_from = number_to_letter(l) + str(n + 1)
                    if len(check_legal(chess, spot_from, av_moves(chess, spot_from))) > 0:
                        spots_from.append(spot_from)
                        i = i + 1

    r = random.randint(0, i-1)
    spot_from = spots_from[r]
    moves = check_legal(chess, spot_from, av_moves(chess, spot_from))
    spot_to = random.choice(moves)
    chess.move(spot_from, spot_to)
    print(f"\nMoving from {spot_from} to {spot_to} ...\n\n...\n")
