# Python 魔塔样板

## 简介

使用Python的Pygame模块制作的魔塔样板，理论上支持全平台游戏！

## 运行说明

电脑需要安装：

* Python3.6或以上版本
* Pygame（从pip安装即可）

运行test.py即可进行游戏～

## 操作说明

运行test.py即可进行游戏～

目前的demo魔塔全部层数都开放了，内容基本完整，但是还没有做事件流，因此通关画面是没有的，仅作演示用途。不过背包内的道具都是可用的，各位可以随便用～

Demo的游戏内容取自《中秋2019：桂魄》的咸鱼难度，应该挺容易的。现在跟原版的差距就在事件了。

当前可用的快捷键：

* X = 怪物手册
* G = 楼层传送器
* T = 玩家背包（带分类二级菜单）
* S = 存档界面
* D = 读档界面
* Z = 勇士转身（顺时针）
* H = 帮助界面
* ESC = 一般情况用来在各种菜单中进行返回操作
* Enter = 一般情况用来在各种菜单中进行确认操作

在例如怪物手册，存档界面等菜单中，可以通过左右方向键快速跨页面移动高亮光标。

/tools文件夹下有一个使用Tkinter写的地图数据编辑器。这个编辑器非常简陋，但是能用，而且编辑完数值后会自动保存。

/tools文件夹下还有一个”一键H5魔塔地图转Python魔塔地图“工具，目前没有写GUI。这个转换器需要使用到json5这个包，因为H5魔塔中的地图文件并不是符合规范的JSON文件（关于这个问题可以搜索”trailing comma json“来了解更多）。常规的json包无法解析这样的JSON文件，所以只能使用json5。

## 更新说明

### 2019.09.15 V0.8.0

* [x] 实现了楼层传送器
* [x] 实现了游戏内帮助页面
* [x] 修复了使用背包内的constants道具会扣除的问题
* [x] 实现了大部分常见的怪物属性
* [x] 实现了商店
* [x] 新增npc.py，用来处理NPC的图片
* [x] 修改change_floor方法，增加其功能

已实现的怪物属性：0:无,1:先攻,2:魔攻,3:坚固,4:2连击,5:3连击,6:n连击,7:破甲,8:反击,9:净化,10:模仿,11:吸血,19:自爆,20:无敌,21:退化,22:固伤

未实现的怪物属性：12:中毒,13:衰弱,14:诅咒,15:领域,16:夹击,17:仇恨,18:阻击,23:重生,24:激光,25:光环

### 2019.09.15 V0.7.1

* [x] 在utools.py中增加get_time方法，用于获取当前时间
* [x] 存档增加当前时间和玩家角色的朝向
* [x] 存读档界面现在能够显示详细信息，并由每页4条变成每页6条（充分利用空间）

### 2019.09.14 V0.7.0

* [x] 增加4种不可通行的障碍（两种墙，星空，岩浆）
* [x] 修复了玩家可以直接穿过花门的问题
* [x] 增加Z键转向（转向有冷却时间设定，避免操作响应太过灵敏）
* [x] 玩家现在可以在sysconf.py里头调节勇士行走速度，目前默认速度是125
* [x] 新增音乐包装类（music.py中的MusicWrapper类），操作音乐音效更容易
* [x] 将sound文件夹拆分成BGM和SE两个文件夹，所有BGM和SE无需任何注册即可直接使用。
* [x] 实现进行特定操作时音效的播放
* [x] 实现一些获取怪物特殊能力相关内容的接口
* [x] 实现了部分的怪物特殊能力（例如：魔攻，连击，先攻）
* [x] 怪物手册现在能够显示对应怪物的动图和特殊能力（有些能力还没实现，比如“模仿”）
* [x] 实现了怪物手册中怪物伤害从小到大排列
* [x] 更换了自带demo，游戏内容取自《中秋2019：桂魄》
* [x] 新增一键H5魔塔地图转Python魔塔地图的工具

### 2019.09.13 V0.6.0

在摸鱼很久之后，我又回来啦～

* [x] 怪物显伤
* [x] 增加全局变量模块
* [x] 简陋的开始界面
* [x] 简陋的怪物手册
* [x] 重构ui.py，增加action.py，引入新的注册机制
* [x] 简陋的背包UI
* [x] 简陋的图形化地图编辑器
* [x] 具体存读档实现
* [x] 读档会把背包数组中str道具id转成int
* [x] 解决UI互相冲突问题
* [x] 解决勇士行走到边缘时，地图数组越界问题
* [x] 基本道具已经全部实现并测试通过
* [x] 实现背景音乐

### 2019.04.26 V0.5.1

* [x] 初步完成重构

当前待处理工作：
* 道具 - 背包UI，具体道具效果代码核查
* 怪物手册UI
* 怪物显伤
* 音效
* 存读档 - 界面UI，具体存读档实现
* 开始界面UI


### 2019.02.05 V0.5.0

* [x] 重构大部分显示代码实现以及工程目录分布
* [x] 实现画布系统，树形结构，统一管理，画布内使用相对坐标
* [x] 基于画布的地图显示模块，提供逻辑坐标和地图信息的访问接口，不再直接访问地图数据库
* [x] 素材分类管理，通过get_resource以标识符访问，素材改用带透明通道的png
* [x] 增加事件精灵EventSprite，实现怪物动画
* [x] 实现简单的控制台实时调试 

当前待处理工作：把旧有内容移植到新框架下（旧有部分除了素材目前仍然兼容）


### 2019.02.04 V0.4.0

* [x] 修复若干bugs
* [x] 简单怪物手册实现
* [x] 简单怪物显伤实现
* [x] 完成大部分道具效果

### 2019.02.01 V0.3.1

* [x] 废除get_item函数并改用pick_item函数
* [x] 增加use_item函数
* [x] 引入HTML5魔塔样板的item数据并存放到items.py
* [x] 完成部分道具的实现
* [x] 将地图数据分离到tower_map.py
* [x] 将怪物数据分离到monster.py
* [x] 将地图数据映射表分离到id_map.py
* [x] 废除tower_database.py

### 2019.01.31 V0.3.0

* [x] 添加ActorSprite
* [x] 实现勇士动态行走图
* [x] 补全get_item函数
* [x] 完成不同函数间坐标的对接
* [x] 移动所有常数到sysconf.py
* [x] 修复crop_image函数切图错误
* [x] 修复get_damage_info函数破防判断错误
* [x] 本次自带demo取自《生命之林》魔塔的一部分

### 2019.01.29 V0.2.0

* [x] 实现上下楼以及开门的处理
* [x] 增加change_floor函数
* [x] 增加open_door函数
* [x] 增加check_map函数

### 2019.01.29 V0.1.0

* [x] 增加crop_image函数

### 2019.01.28 V0.0.1

* [x] 发布初版Python魔塔样板的雏形

---------------------------

# MagicTower-Python
## Intro
Magic Tower written in Python
