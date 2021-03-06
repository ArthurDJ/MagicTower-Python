"""

地图ground的demo：

建立需要知道地图逻辑大小w,h（如(13,13)），起始坐标默认0，0，
需要一个全局的资源访问接口，data_dict ，是id到Surface或者Sprite的映射

在地图ground范围内显示的有两类元素（暂不考虑动态图块 视为事件精灵）：
1. 静态图块： 典型元素如墙、道具、…… 直接使用Surface类素材
2. 动态事件： 如怪物、门…… 使用EventSprite(id,configure)生成，其中configure是对该事件动画的配置（素材形状）


TODO： 需要解决surface对底层不透明的问题，目前需要在地图层重绘地板

"""

from lib.ground import GroundSurface
from pygame import Rect, Surface
from .sprite import EventSprite
from lib.utools import *
from sysconf import *
from lib import global_var, WriteLog
import os
import json

class MapGround(GroundSurface):
    def __init__(self, w, h, block_size=32):
        self.block_size = block_size
        self.width = w
        self.height = h
        self.map_data = None
        self.event_data = None
        self.event_database = {}
        self.temp_srufcae = None
        self.map_database_init()
        self.event_database_init()
        self.FUNCTION = global_var.get_value("FUNCTION")
        self.show_damage_update = True
        self.damage_layer_cache = {}
        self.active = True
        super().__init__(mode="custom",x=0,y=0,w=w * block_size,h=h * block_size)

    def map_database_init(self):
        # 从/project/floors读取地图
        try:
            with open(os.path.join(os.getcwd(),"project", "floor_index.json")) as f:
                self.floor_index = json.load(f)
        except:
            WriteLog.critical(__name__, "读取地图index错误！")
        self.MAP_DATABASE = {}
        for floor in self.floor_index["index"]:
            try:
                with open(os.path.join(os.getcwd(),"project", "floors", f"{floor}.json")) as f:
                    self.MAP_DATABASE[f"{floor}"] = json.load(f)
            except:
                WriteLog.critical(__name__, f"读取{floor}错误!")

    def event_database_init(self):
        for floor in self.floor_index["index"]:
            self.event_database[floor] = []
            temp_event = self.MAP_DATABASE[floor]["events"]
            if temp_event != {}:
                for coordinate in temp_event:
                    result = coordinate.split(",")
                    result = [int(i) for i in result]
                    self.event_database[floor].append(result)
        WriteLog.debug(__name__, "初始化事件完成")

    def trans_locate(self, *args):
        """
        逻辑转物理，默认为top left
        :param args:
        :arg[3]: "up":top centerx "down": bottom centerx

        exmaple 1: map.trans_locate(12,12,'down') # 获取坐标 然后在该位置绘制敌人
        example 2: event.move(map.trans_locate(12,12,'down')) # 移动事件到12，12位置

        :return:
        """
        x, y = args[0], args[1]
        if len(args) > 2:
            if args[2] == "up":
                return int((x + 0.5) * self.block_size), y * self.block_size
            elif args[2] == "down":
                return int((x + 0.5) * self.block_size), (y + 1) * self.block_size

        return x * self.block_size, y * self.block_size

    def set_map(self, floor):
        self.clear_map()
        self.map_data = self.get_map(floor)
        self.event_data = self.get_event(floor)
        self.draw_map()

    def get_map(self, floor):
        data = self.MAP_DATABASE[self.floor_index["index"][floor]]["map"]
        return data

    def get_event(self, floor):
        data = self.event_database[self.floor_index["index"][floor]]
        return data

    def get_event_flow(self, x, y, floor):
        coordinate = str(x) + "," + str(y)
        data = self.MAP_DATABASE[self.floor_index["index"][floor]]["events"][coordinate]
        return data

    def get_floor_id(self, floor):
        floor_id = self.floor_index["index"][floor]
        return floor_id

    def clear_map(self):
        # self.group.clear()
        self.group.empty()

    def flush(self, screen=None):
        if self.temp_srufcae is not None: # 地图刷新时先直接绘上静态部分
            self.surface.blit(self.temp_srufcae, self.temp_srufcae.get_rect())
        super().flush(screen=screen)

    
    # draw_map 绘制地图，之后刷新不再重绘，除非更新地图状态
    def draw_map(self, map_data=None):
        if self.show_damage_update:
            self.damage_layer_cache = {}
        WriteLog.debug(__name__, "绘制地图")
        self.clear_map() # 清空精灵
        if map_data is None:
            map_data = self.map_data
        temp_x = 0
        temp_y = 0
        px, py = self.trans_locate(0, 0)
        rect = Rect(px, py, self.block_size, self.block_size)
        ground = get_resource('0')  # 地板 先暂时这么搞吧
        self.fill_surface(ground, mode="repeat")
        PlayerCon = global_var.get_value("PlayerCon")
        self.add_sprite(PlayerCon)
        while temp_y < self.height:
            while temp_x < self.width:
                map_element = map_data[temp_y][temp_x]
                if int(map_element) != 0:
                    # sprite的显示需要接通group
                    name = str(map_element)
                    ret = get_resource(name)
                    px, py = self.trans_locate(temp_x, temp_y, "down")
                    rect.centerx = px
                    rect.bottom = py
                    if type(ret) is tuple:  # 属于精灵 (注意：此时不能直接导入精灵，因为先有map后有精灵）
                        img = ret[0]
                        img_rect = ret[1]  # 以资源本体大小显示 用以支持超过32*32的图像
                        img_rect.topleft = rect.topleft
                        sp = list(ret[2])
                        self.add_sprite(EventSprite(name, img, sp), fill_rect=img_rect)
                    elif ret is not None:
                        self.fill_surface(ret, fill_rect=rect)
                    # 显伤怪物id和位置的缓存
                    if map_element > 200:
                        if self.show_damage_update:
                            if map_element in self.damage_layer_cache:
                                self.damage_layer_cache[map_element]["loc"].append([temp_x, temp_y])
                            else:
                                self.damage_layer_cache[map_element] = {}
                                self.damage_layer_cache[map_element]["loc"] =[]
                                self.damage_layer_cache[map_element]["loc"].append([temp_x, temp_y])  
                                check_result = self.FUNCTION.get_damage_info(map_element)
                                critical = self.FUNCTION.get_criticals(map_element, 1, damage_info=check_result)
                                if check_result == False:
                                    self.damage_layer_cache[map_element]["damage"] = "???"
                                else:
                                    self.damage_layer_cache[map_element]["damage"] = check_result["damage"]
                                if critical == []:
                                    self.damage_layer_cache[map_element]["critical"] = 0
                                else:
                                    self.damage_layer_cache[map_element]["critical"] = critical[0][0]
                temp_x += 1
            temp_y += 1
            temp_x = 0
            self.temp_srufcae = self.surface.copy()
        self.show_damage_update = False
    
    # get_block 获取指定地点的图块
    def get_block(self, x, y, floor=None):
        if floor == None:
            temp_map_data = self.map_data
        else:
            temp_map_data = self.get_map(floor)
        if temp_map_data is not None:
            if x >= 0 and x <= SIDE_BLOCK_COUNT - 1 and y >= 0 and y <= SIDE_BLOCK_COUNT - 1:
                return temp_map_data[y][x]
            else:
                WriteLog.debug(__name__, "尝试读取地图边界外数据！")
                return "onSide"
        else:
            return []
    
    # check_block 获取指定图块的地点，没有则返回空数组
    def check_block(self, target):
        if self.map_data is not None:
            temp_x = 0
            temp_y = 0
            height = int(HEIGHT / BLOCK_UNIT)
            width = int(WIDTH / BLOCK_UNIT) - 4 # -4是因为左边有状态栏
            result = []
            while temp_y < height:
                while temp_x < width:
                    if self.map_data[temp_y][temp_x] == target:
                        result.append([temp_x,temp_y])
                    temp_x += 1
                temp_y += 1
                temp_x = 0
            return result
        else:
            return []
    
    # set_block 设置指定点的图块
    def set_block(self, x, y, target):
        if self.map_data is not None:
            self.map_data[y][x] = target
            
    # remove_block 移除指定点的图块（等价于set_block(x, y, 0)）
    def remove_block(self, x, y):
        if self.map_data is not None:
            self.map_data[y][x] = 0


    # 重置地图
    def reset(self):
        self.map_data = None
        self.event_data = None
        self.event_database = {}
        self.map_database_init()
        self.event_database_init()
        self.set_map(PLAYER_FLOOR)
