from game import Game

def main():
    print("=== Ignes Development Center ===")

    name = input("名前入力:")
    if not name:
        name = "管理人"

    game = Game(name)
    game.start()

if __name__ == "__main__":
    main()
