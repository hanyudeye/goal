import random
from time import sleep

# 初始化一副扑克牌 (1-11点)
扑克牌 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def 显示游戏开始():
    print(f"{'*'*58}\n 欢迎来到21点扑克游戏!\n{'*'*58}")
    sleep(1)
    print("让我们开始游戏吧...")
    sleep(1)

def 发牌():
    # 初始化庄家和玩家的牌
    庄家牌组 = []
    玩家牌组 = []
    
    # 给庄家发两张牌
    while len(庄家牌组) != 2:
        random.shuffle(扑克牌)
        庄家牌组.append(扑克牌.pop())
        if len(庄家牌组) == 2:
            print(f"庄家的牌是: X {庄家牌组[1]}")  # 第一张牌保密
            
    # 给玩家发两张牌
    while len(玩家牌组) != 2:
        random.shuffle(扑克牌)
        玩家牌组.append(扑克牌.pop())
        if len(玩家牌组) == 2:
            print(f"您的总点数是: {sum(玩家牌组)}")
            print(f"您的牌是: {玩家牌组}")
            
    return 庄家牌组, 玩家牌组

def 庄家行动(庄家牌组):
    # 庄家必须要牌直到17点以上
    while sum(庄家牌组) < 17:
        random.shuffle(扑克牌)
        庄家牌组.append(扑克牌.pop())
    print(f"\n庄家的总点数是: {sum(庄家牌组)}")
    print(f"庄家的牌是: {庄家牌组}")
    return 庄家牌组

def 游戏主循环():
    显示游戏开始()
    庄家牌组, 玩家牌组 = 发牌()

    while sum(玩家牌组) < 21:
        选择 = input("\n是否要牌? (y/n): ")
        
        if 选择.lower() == 'y':
            random.shuffle(扑克牌)
            玩家牌组.append(扑克牌.pop())
            print(f"\n您的总点数是: {sum(玩家牌组)}")
            print(f"您的牌是: {玩家牌组}")
            
            if sum(玩家牌组) > 21:
                print(f"\n{'*'*13}爆牌了!{'*'*13}\n庄家赢!")
                return
                
        elif 选择.lower() == 'n':
            庄家牌组 = 庄家行动(庄家牌组)
            
            # 判定胜负
            庄家点数 = sum(庄家牌组)
            玩家点数 = sum(玩家牌组)
            
            if 庄家点数 > 21:
                print(f"\n{'*'*13}庄家爆牌!{'*'*13}\n您赢了!")
            elif 庄家点数 > 玩家点数:
                print(f"\n{'*'*13}庄家赢了!{'*'*13}")
            elif 庄家点数 < 玩家点数:
                print(f"\n{'*'*13}恭喜您赢了!{'*'*13}")
            else:
                print(f"\n{'*'*13}平局!{'*'*13}")
            return

if __name__ == "__main__":
    游戏主循环()