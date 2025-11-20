from chess import *

BOT = False   # True for 1P mode

SLEEP1 = 2
SLEEP2 = 1


def main():
    player1, player2 = Player(), Player(BOT)
    chess = ChessBoard(player1, player2)
    chess.init_board()
    player = player2
    pieces_names = ['Pawn', 'King', 'Queen', 'Tower', 'Knight', 'Bishop']

    while True:

        if player == player1:
            player = player2
        else:
            player = player1
        chess.reset_en_passant(player)

        ckmate = check_checkmate(chess, player.is_black)
        if ckmate == 1:
            chess.print_c_board()
            if player == player1:
                print("\n              'CHECKMATE'")
                print("     -->  BLACK PLAYER WINS !!!  <--\n\n")
            else:
                print("\n              'CHECKMATE'")
                print("\n    -->  WHITE PLAYER WINS !!!  <--\n\n")
            break
        elif ckmate == 2:
            chess.print_c_board()
            print("\n         'STALEMATE'")
            print("     -->  NO-ONE WINS !!!  <--\n\n")
            break

        chess.print_eaten()
        if check_check(chess, player.is_black):
            print("\n   'CHECK!'  <--")
            if player.bot:
                sleep(SLEEP2/2)
            else:
                sleep(SLEEP1/2)
        else:
            print("\n")
        if player == player1:
            print("         -->  White turn  <--")
        else:
            print("         -->  Black turn  <--")
        chess.print_c_board()
        if player.bot:
            sleep(SLEEP2/4)
            make_rand_move(chess, player)
            sleep(SLEEP2)
            continue
        while True:
            move_from, move_to = get_move_player(chess, player)
            action, piece = get_action(chess, move_from, move_to)
            if castling(chess, move_from, move_to, player):
                print(f"\nCastling from {move_from} to {move_to} ...\n\n...\n")
                sleep(SLEEP1)
                break
            elif en_passant(chess, move_from, move_to, player):
                print(f"\nEn passant from {move_from} to {move_to} ...\n\n...\n")
                sleep(SLEEP1)
                break
            elif chess.move(move_from, move_to):
                pawn_transformation(chess, move_to, player)
                print(f"\n{pieces_names[piece]} {action}from {move_from} to {move_to} ...\n\n...\n")
                check_en_passant(chess, move_from, move_to, player)
                check_castling(move_from, player)
                sleep(SLEEP1)
                break
            else:
                print("Move is not legal...Try again\n")
                sleep(1)
                if check_check(chess, player.is_black):
                    print("   'CHECK!'")
                else:
                    print("\n")
                if player == player1:
                    print("         -->  White turn  <--")
                else:
                    print("         -->  Black turn  <--")
                chess.print_c_board()
    return 0


if __name__ == '__main__':
    main()
