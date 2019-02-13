from os import path

# 系统设置 其他地方都会用到这里的配置

# 全塔属性设置
TOWER_NAME = "Magic Tower"
FONT_NAME = "arial"
# --- 勇士数据设置 START ---
# 玩家初始坐标以及楼层
# face[0]调用勇士朝向 0=下，1=左，2=右，3=上
X_COORDINATE = 6
Y_COORDINATE = 10
PLAYER_FLOOR = 1
# 玩家初始属性
PLAYER_HP = 100
PLAYER_ATK = 1
PLAYER_DEF = 0
PLAYER_MDEF = 0
PLAYER_GOLD = 0
PLAYER_EXP = 0
PLAYER_YELLOWKEY = 0
PLAYER_BLUEKEY = 0
PLAYER_REDKEY = 0
PLAYER_GREENKEY = 0
PLAYER_STEELKEY = 0
PLAYER_ITEM = {}
# --- 勇士数据设置 END ---

# --- 物品/道具数据设置 START ---
# 宝石
RED_JEWEL = 1
BLUE_JEWEL = 1
GREEN_JEWEL = 4
YELLOW_JEWEL = 1
# 血瓶
RED_POTION = 40
BLUE_POTION = 80
GREEN_POTION = 400
YELLOW_POTION = 800
# 装备
SWORD_1 = 10
SHIELD_1 = 10
SWORD_2 = 20
SHIELD_2 = 20
SWORD_3 = 40
SHIELD_3 = 40
SWORD_4 = 80
SHIELD_4 = 80
SWORD_5 = 160
SHIELD_5 = 160

# 【可选】设置
STEEL_DOOR_NEEDS_KEY = True
BIG_KEY_OPEN_YELLOW_DOORS = False
# --- 道具数据设置 END ---


# --- Basic Constants START ---
# Define some properties of the game
WIDTH = (13 + 4) * 64  # 1088  # (13 + 4) * 64
HEIGHT = 13 * 64  # 832  # 13 * 64
# BLOCK_UNIT is used to create "invisible tiles" later. In this case the size of a block is 64 * 64 instead of 32 * 32
BLOCK_UNIT = HEIGHT / 13  # BLOCK_UNIT = 64
FPS = 120  # 每秒帧数
MSPF = int(1000 / FPS)  # 每一帧毫秒数
DEFAULT_SPEED = 500  # 默认动画速度(周期)

RESOURCE_SCALE = BLOCK_UNIT / 32

true = True
false = False
null = None

# Define directories for images and sounds
img_dir = path.join(path.dirname(__file__), "img")
snd_dir = path.join(path.dirname(__file__), "sound")

## Define Colors
# RED COLORS
RED = (255, 0, 0)
DARKRED = (139, 0, 0)
# ORANGE COLORS
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
DARKORANGE = (255, 140, 0)
# YELLOW COLORS
LIGHTYELLOW = (255, 255, 224)
YELLOW = (255, 255, 0)
# GREEN COLORS
LIME = (0, 255, 0)
LIMEGREEN = (50, 205, 50)
GREEN = (0, 128, 0)
SPRINGGREEN = (0, 255, 127)
SEAGREEN = (46, 139, 87)
OLIVE = (128, 128, 0)
# CYAN COLORS
CYAN = (0, 255, 255)
DARKCYAN = (0, 139, 139)
# BLUE COLORS
LIGHTSKYBLUE = (135, 206, 250)
SKYBLUE = (135, 206, 235)
DEEPSKYBLUE = (0, 191, 255)
LIGHTSTEELBLUE = (176, 196, 222)
BLUE = (0, 0, 255)
MEDIUMBLUE = (0, 0, 205)
DARKBLUE = (0, 0, 139)
# PURPLE COLORS
VIOLET = (238, 130, 238)
FUCHSIA = (255, 0, 255)
PURPLE = (128, 0, 128)
INDIGO = (75, 0, 130)
# PINK COLORS
PINK = (255, 192, 203)
LIGHTPINK = (255, 182, 193)
DEEPPINK = (255, 20, 147)
# WHITE COLORS
WHITE = (255, 255, 255)
SNOW = (255, 250, 250)
AZURE = (240, 255, 255)
# GRAY COLORS
LIGHTGRAY = (211, 211, 211)
SILVER = (192, 192, 192)
DARKGRAY = (169, 169, 169)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
# BROWN COLORS
WHEAT = (245, 222, 179)
CHOCOLATE = (210, 105, 30)
BROWN = (165, 42, 42)
# --- Basic Constants END ---
