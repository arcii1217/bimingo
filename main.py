from game.game import Game


def main():
  game = Game()
  print("🎮 양면 빙고 시작")
  for p in game.players:
    print(f"{p.name} 지정색: {p.secret_color}")
    
  while True:
    player = game.state.current_player()
    board = game.state.board
    print(f"\n[{player.name} 턴 | 지정색 {player.secret_color}]")
    
    # (터미널 입력 루프는 이전 버전과 동일하게 구현 가능)
    # 여기서는 구조 예시만 제시

    break


if __name__ == "__main__":
  main()
