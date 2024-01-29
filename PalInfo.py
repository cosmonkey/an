import json

from enum import Enum
from PIL import ImageTk, Image
from EmptyObjectHandler import *


SkillDesc = {
        "未知": " 不存在或不在我们的数据库中",
        "空": "此帕鲁在该槽位没有技能",
        
        "一反常态": "-10%受到的无属性攻击伤害",
        "阳光开朗": "-10%受到的暗属性攻击伤害",
        "屠龙之人": "-10%受到的龙属性攻击伤害",
        "高温体质": "-10%受到的冰属性攻击伤害",
        "拥抱烈日": "-10%受到的火属性攻击伤害",
        "除草效果": "-10%受到的草属性攻击伤害",
        "抗震结构": "-10%受到的地属性攻击伤害",
        "绝缘体": "-10%受到的电属性攻击伤害",
        "防水性能": "-10%受到的水属性攻击伤害",

        "禅境": "+10%造成的无属性攻击伤害",
        "夜幕": "+10%造成的暗属性攻击伤害",
        "龙之血脉": "+10%造成的龙属性攻击伤害",
        "冷血": "+10%造成的冰属性攻击伤害",
        "喜欢玩火": "+10%造成的火属性攻击伤害",
        "草木馨香": "+10%造成的草属性攻击伤害",
        "大地之力": "+10%造成的地属性攻击伤害",
        "电容": "+10%造成的电属性攻击伤害",
        "喜欢戏水": "+10%造成的水属性攻击伤害",

        "圣天": "+20%造成的无属性攻击伤害; 圣光骑士的专属能力",
        "冥王": "+20%造成的暗属性攻击伤害; 混沌骑士的专属能力",
        "神龙": "+20%造成的龙属性攻击伤害; 空涡龙的专属能力",
        "冰帝": "+20%造成的冰属性攻击伤害; 唤冬兽的专属能力",
        "炎帝": "+20%造成的火属性攻击伤害; 焰煌的专属能力",
        "精灵王": "+20%造成的草属性攻击伤害; 百合女王的专属能力",
        "岩帝": "+20%造成的地属性攻击伤害; 阿努比斯的专属能力",
        "雷帝": "+20%造成的电属性攻击伤害; 波鲁杰克斯的专属能力",
        "海皇": "+20%造成的水属性攻击伤害; 覆海龙的专属能力",

        "勇敢": "+10%攻击力",
        "凶猛": "+20%攻击力",
        "胆小": "-10%攻击力",
        "消极主义": "-20%攻击力",
        
        "坚硬皮肤": "+10%防御力",
        "顽强肉体": "+20%防御力",
        "弱不禁风": "-10%防御力",
        "骨质疏松": "-20%防御力",

        "采伐领袖": "+25%玩家伐木效率",
        "矿山首领": "+25%玩家采矿效率",
        "突袭指挥官": "+10%玩家攻击力",
        "啦啦队": "+25%玩家工作速度",
        "铁壁军师": "+10%玩家防御力",

        "积极思维": "理智下降速度减缓10%",
        "工作狂": "理智下降速度减缓15%",
        "情绪不稳": "理智下降速度加快10%",
        "毁灭欲望": "理智下降速度加快15%",

        "小胃": "饱食下降速度减缓10%",
        "节食大师": "饱食下降速度减缓15%",
        "贪吃": "饱食下降速度加快10%",
        "无底之胃": "饱食下降速度加快15%",

        "认真": "+20%工作速度",
        "工匠精神": "+50%工作速度",
        "笨手笨脚": "-10%工作速度",
        "偷懒成瘾": "-30%工作速度",

        "灵活": "+10%移动速度",
        "运动健将": "+20%移动速度",
        "神速": "+30%移动速度",

        "社畜": "+30%工作速度, -30%攻击力",

        "粗暴": "+15%攻击力, -10%工作速度",
        "脑筋": "+30%攻击力, -50%工作速度",

        "强势": "+10%攻击力, -10%防御力",

        "自恋狂": "+10%工作速度, -10%防御力",

        "受虐狂": "+15%防御力, -15%攻击力",
        "虐待狂": "+15%攻击力, -15%防御力",

        "稀有": "+15%攻击力, +15%工作速度",
        "传说": "+20%攻击力, +20%防御力, +15%移动速度",
        
        "":""
    }
    
class PalSkills(Enum):
    UNKNOWN = "未知"
    NONE = "空"
    
    ElementResist_Normal_1_PAL = "一反常态"
    ElementResist_Dark_1_PAL = "阳光开朗"
    ElementResist_Dragon_1_PAL = "屠龙之人"
    ElementResist_Ice_1_PAL = "高温体质"
    ElementResist_Fire_1_PAL = "拥抱烈日"
    ElementResist_Leaf_1_PAL = "除草效果"
    ElementResist_Earth_1_PAL = "抗震结构"
    ElementResist_Thunder_1_PAL = "绝缘体"
    ElementResist_Aqua_1_PAL = "防水性能"

    ElementBoost_Normal_1_PAL = "禅境"
    ElementBoost_Dark_1_PAL = "夜幕"
    ElementBoost_Dragon_1_PAL = "龙之血脉"
    ElementBoost_Ice_1_PAL = "冷血"
    ElementBoost_Fire_1_PAL = "喜欢玩火"
    ElementBoost_Leaf_1_PAL = "草木馨香"
    ElementBoost_Earth_1_PAL = "大地之力"
    ElementBoost_Thunder_1_PAL = "电容"
    ElementBoost_Aqua_1_PAL = "喜欢戏水"

    ElementBoost_Normal_2_PAL = "圣天"
    ElementBoost_Dark_2_PAL = "冥王"
    ElementBoost_Dragon_2_PAL = "神龙"
    ElementBoost_Ice_2_PAL = "冰帝"
    ElementBoost_Fire_2_PAL = "炎帝"
    ElementBoost_Leaf_2_PAL = "精灵王"
    ElementBoost_Earth_2_PAL = "岩帝"
    ElementBoost_Thunder_2_PAL = "雷帝"
    ElementBoost_Aqua_2_PAL = "海皇"

    PAL_ALLAttack_up1 = "勇敢"
    PAL_ALLAttack_up2 = "凶猛"
    PAL_ALLAttack_down1 = "胆小"
    PAL_ALLAttack_down2 = "消极主义"
    
    Deffence_up1 = "坚硬皮肤"
    Deffence_up2 = "顽强肉体"
    Deffence_down1 = "弱不禁风"
    Deffence_down2 = "骨质疏松"

    TrainerMining_up1 = "矿山首领"
    TrainerLogging_up1 = "采伐领袖"
    TrainerATK_UP_1 = "突袭指挥官"
    TrainerWorkSpeed_UP_1 = "啦啦队"
    TrainerDEF_UP_1 = "铁壁军师"

    PAL_Sanity_Down_1 = "积极思维"
    PAL_Sanity_Down_2 = "工作狂"
    PAL_Sanity_Up_1 = "情绪不稳"
    PAL_Sanity_Up_2 = "毁灭欲望"

    PAL_FullStomach_Down_1 = "小胃"
    PAL_FullStomach_Down_2 = "节食大师"
    PAL_FullStomach_Up_1 = "贪吃"
    PAL_FullStomach_Up_2 = "无底之胃"
    

    CraftSpeed_up1 = "认真"
    CraftSpeed_up2 = "工匠精神"
    CraftSpeed_down1 = "笨手笨脚"
    CraftSpeed_down2 = "偷懒成瘾"

    MoveSpeed_up_1 = "灵活"
    MoveSpeed_up_2 = "运动健将"
    MoveSpeed_up_3 = "神速"

    PAL_CorporateSlave = "社畜"

    PAL_rude = "粗暴"
    Noukin = "脑筋"

    PAL_oraora = "强势"

    PAL_conceited = "自恋狂"

    PAL_masochist = "受虐狂"
    PAL_sadist = "虐待狂"
    
    Rare = "稀有"
    Legend = "传说"


class PalGender(Enum):
    MALE = "#02A3FE"
    FEMALE = "#EC49A6"
    UNKNOWN = "darkgrey"

class PalElement:
    def __init__(self, name, colour):
        self._name = name
        self._colour = colour

    def GetName(self):
        return self._name

    def GetColour(self):
        return self._colour
    
class Elements(Enum):
    NONE = PalElement("空", "lightgrey")
    NORMAL = PalElement("无", "#D8A796")
    DARK = PalElement("暗", "#AD0035")
    DRAGON = PalElement("龙", "#C22DF9")
    ICE = PalElement("冰", "#00F2FF")
    FIRE = PalElement("火", "#FF4208")
    LEAF = PalElement("草", "#83F001")
    EARTH = PalElement("地", "#BA5608")
    ELECTRICITY = PalElement("电", "#FEED01")
    WATER = PalElement("水", "#0074FF")

class PalObject:
    def __init__(self, name, primary, secondary=Elements.NONE, human=False, tower=False):
        self._name = name
        self._img = None
        self._primary = primary
        self._secondary = secondary
        self._human = human
        self._tower = tower

    def GetName(self):
        return self._name

    def IsTower(self):
        return self._tower

    def GetImage(self):
        if self._img == None:
            n = self.GetName() if not self._human else "#ERROR"
            self._img = ImageTk.PhotoImage(Image.open(f'resources/{n}.png').resize((240,240)))
        return self._img

    
    def GetPrimary(self):
        return self._primary

    def GetSecondary(self):
        return self._secondary

class PalType(Enum):
    # Thank you to @DMVoidKitten
    
    # 普通帕鲁列表
    Alpaca = PalObject("美露帕", Elements.NORMAL)#
    AmaterasuWolf = PalObject("苍焰狼", Elements.FIRE)#
    Anubis = PalObject("阿努比斯", Elements.EARTH)#
    Baphomet = PalObject("炎魔羊", Elements.FIRE, Elements.DARK)#
    Baphomet_Dark = PalObject("暗魔羊", Elements.DARK)#
    Bastet = PalObject("喵丝特", Elements.DARK)#
    Bastet_Ice = PalObject("冰丝特", Elements.ICE)#
    BerryGoat = PalObject("灌木羊", Elements.LEAF)#
    BirdDragon = PalObject("烽歌龙", Elements.FIRE, Elements.DARK)#
    BirdDragon_Ice = PalObject("霜歌龙", Elements.ICE, Elements.DARK)#
    BlackCentaur = PalObject("混沌骑士", Elements.DARK)#
    BlackGriffon = PalObject("异构格里芬", Elements.DARK)#
    BlackMetalDragon = PalObject("魔渊龙", Elements.DRAGON, Elements.DARK)#
    BlueDragon = PalObject("碧海龙", Elements.WATER, Elements.DRAGON)#
    BluePlatypus = PalObject("冲浪鸭", Elements.WATER)#
    Boar = PalObject("草莽猪", Elements.EARTH)#
    CaptainPenguin = PalObject("企丸王", Elements.WATER, Elements.ICE)#
    Carbunclo = PalObject("翠叶鼠", Elements.LEAF)#
    CatBat = PalObject("猫蝠怪", Elements.DARK)#
    CatMage = PalObject("暗巫猫", Elements.DARK)#
    CatVampire = PalObject("夜幕魔蝠", Elements.DARK)#
    ChickenPal = PalObject("皮皮鸡", Elements.NORMAL)#
    ColorfulBird = PalObject("炸弹鸟", Elements.NORMAL)#
    CowPal = PalObject("波霸牛", Elements.NORMAL)#
    CuteButterfly = PalObject("幻悦蝶", Elements.LEAF)#
    CuteFox = PalObject("玉藻狐", Elements.NORMAL)#
    CuteMole = PalObject("遁地鼠", Elements.EARTH)#
    DarkCrow = PalObject("黑鸦隐士", Elements.DARK)#
    DarkScorpion = PalObject("冥铠蝎", Elements.DARK, Elements.EARTH)#
    Deer = PalObject("紫霞鹿", Elements.NORMAL)#
    Deer_Ground = PalObject("祇岳鹿", Elements.EARTH)#
    DreamDemon = PalObject("寐魔", Elements.DARK)#
    DrillGame = PalObject("碎岩龟", Elements.EARTH)#
    Eagle = PalObject("天擒鸟", Elements.NORMAL)#
    ElecCat = PalObject("伏特喵", Elements.ELECTRICITY)#
    ElecPanda = PalObject("暴电熊", Elements.ELECTRICITY)#
    FairyDragon = PalObject("精灵龙", Elements.DRAGON)#
    FairyDragon_Water = PalObject("水灵龙", Elements.DRAGON, Elements.WATER)#
    FengyunDeeper = PalObject("云海鹿", Elements.NORMAL)#
    FireKirin = PalObject("火麒麟", Elements.FIRE)#
    FireKirin_Dark = PalObject("邪麒麟", Elements.FIRE, Elements.DARK)#
    FlameBambi = PalObject("燎火鹿", Elements.FIRE)#
    FlameBuffalo = PalObject("炽焰牛", Elements.FIRE)#
    FlowerDinosaur = PalObject("花冠龙", Elements.LEAF, Elements.DRAGON)#
    FlowerDinosaur_Electric = PalObject("雷冠龙", Elements.ELECTRICITY, Elements.DRAGON)#
    FlowerDoll = PalObject("花丽娜", Elements.LEAF)#
    FlowerRabbit = PalObject("波娜兔", Elements.LEAF)#
    FlyingManta = PalObject("鲁米儿", Elements.WATER)#
    FoxMage = PalObject("焰巫狐", Elements.FIRE)#
    Ganesha = PalObject("壶小象", Elements.WATER)#
    Garm = PalObject("猎狼", Elements.NORMAL)#
    GhostBeast = PalObject("噬魂兽", Elements.DARK)#
    Gorilla = PalObject("铁拳猿", Elements.NORMAL)#
    GrassMammoth = PalObject("森猛犸", Elements.LEAF)#
    GrassMammoth_Ice = PalObject("雪猛犸", Elements.ICE)#
    GrassPanda = PalObject("叶胖达", Elements.LEAF)#
    GrassPanda_Electric = PalObject("雷胖达", Elements.ELECTRICITY)#
    GrassRabbitMan = PalObject("踏春兔", Elements.LEAF)#
    HadesBird = PalObject("雷冥鸟", Elements.DARK)#
    HawkBird = PalObject("疾风隼", Elements.NORMAL)#
    Hedgehog = PalObject("电棘鼠", Elements.ELECTRICITY)#
    Hedgehog_Ice = PalObject("冰刺鼠", Elements.ICE)#
    HerculesBeetle = PalObject("铠格力斯", Elements.EARTH, Elements.LEAF)#
    Horus = PalObject("荷鲁斯", Elements.FIRE)#
    IceDeer = PalObject("严冬鹿", Elements.ICE)#
    IceFox = PalObject("吹雪狐", Elements.ICE)#
    IceHorse = PalObject("唤冬兽", Elements.ICE)#
    IceHorse_Dark = PalObject("唤夜兽", Elements.DARK)#
    JetDragon = PalObject("空涡龙", Elements.DRAGON)#
    Kelpie = PalObject("水灵儿", Elements.WATER)#
    Kelpie_Fire = PalObject("火灵儿", Elements.FIRE)#
    KingAlpaca = PalObject("君王美露帕", Elements.NORMAL)#
    KingAlpaca_Ice = PalObject("冰帝美露帕", Elements.ICE)#
    KingBahamut = PalObject("焰煌", Elements.FIRE)#
    Kirin = PalObject("雷角马", Elements.ELECTRICITY)#
    Kitsunebi = PalObject("火绒狐", Elements.FIRE)#
    LavaGirl = PalObject("融焰娘", Elements.FIRE)#
    LazyCatfish = PalObject("趴趴鲶", Elements.EARTH)#
    LazyDragon = PalObject("佩克龙", Elements.DRAGON, Elements.WATER)#
    LazyDragon_Electric = PalObject("派克龙", Elements.DRAGON, Elements.ELECTRICITY)#
    LilyQueen = PalObject("百合女王", Elements.LEAF)#
    LilyQueen_Dark = PalObject("黑月女王", Elements.DARK)#
    LittleBriarRose = PalObject("荆棘魔仙", Elements.LEAF)#
    LizardMan = PalObject("朋克蜥", Elements.DARK)#
    LizardMan_Fire = PalObject("热血蜥", Elements.FIRE)#
    Manticore = PalObject("狱焰王", Elements.FIRE)#
    Manticore_Dark = PalObject("狱阎王", Elements.FIRE, Elements.DARK)#
    Monkey = PalObject("新叶猿", Elements.LEAF)#
    MopBaby = PalObject("毛掸儿", Elements.ICE)#
    MopKing = PalObject("毛老爹", Elements.ICE)#
    Mutant = PalObject("秘斯媞雅", Elements.NORMAL)#
    NaughtyCat = PalObject("笑魇猫", Elements.NORMAL)#
    NegativeKoala = PalObject("瞅什魔", Elements.DARK)#
    NegativeOctopus = PalObject("勾魂鱿", Elements.DARK)#
    NightFox = PalObject("露娜蒂", Elements.DARK)#
    Penguin = PalObject("企丸丸", Elements.WATER, Elements.ICE)#
    PinkCat = PalObject("捣蛋猫", Elements.NORMAL)#
    PinkLizard = PalObject("博爱蜥", Elements.NORMAL)#
    PinkRabbit = PalObject("姬小兔", Elements.NORMAL)#
    PlantSlime = PalObject("叶泥泥", Elements.LEAF, Elements.EARTH)#
    QueenBee = PalObject("女皇蜂", Elements.LEAF)#
    RaijinDaughter = PalObject("雷鸣童子", Elements.ELECTRICITY)#
    RedArmorBird = PalObject("燧火鸟", Elements.FIRE)#
    RobinHood = PalObject("羽箭射手", Elements.LEAF)#
    RobinHood_Ground = PalObject("山岳射手", Elements.LEAF, Elements.EARTH)#
    Ronin = PalObject("浪刃武士", Elements.FIRE)#
    SaintCentaur = PalObject("圣光骑士", Elements.NORMAL)#
    SakuraSaurus = PalObject("连理龙", Elements.LEAF)#
    SakuraSaurus_Water = PalObject("海誓龙", Elements.LEAF, Elements.WATER)#
    Serpent = PalObject("滑水蛇", Elements.WATER)#
    Serpent_Ground = PalObject("流沙蛇", Elements.EARTH)#
    SharkKid = PalObject("鲨小子", Elements.WATER)#
    SharkKid_Fire = PalObject("红小鲨", Elements.FIRE)#
    Sheepball = PalObject("棉悠悠", Elements.NORMAL)#
    SkyDragon = PalObject("天羽龙", Elements.DRAGON)#
    SoldierBee = PalObject("骑士蜂", Elements.LEAF)#
    Suzaku = PalObject("朱雀", Elements.FIRE)#
    Suzaku_Water = PalObject("清雀", Elements.WATER)#
    SweetsSheep = PalObject("棉花糖", Elements.NORMAL)#
    ThunderBird = PalObject("迅雷鸟", Elements.ELECTRICITY)#
    ThunderDog = PalObject("霹雳犬", Elements.ELECTRICITY)#
    ThunderDragonMan = PalObject("波鲁杰克斯", Elements.DRAGON, Elements.ELECTRICITY)#
    Umihebi = PalObject("覆海龙", Elements.DRAGON, Elements.WATER)#
    Umihebi_Fire = PalObject("腾炎龙", Elements.DRAGON, Elements.FIRE)#
    VioletFairy = PalObject("薇莉塔", Elements.LEAF)#
    VolcanicMonster = PalObject("熔岩兽", Elements.FIRE, Elements.EARTH)#
    VolcanicMonster_Ice = PalObject("寒霜兽", Elements.ICE, Elements.EARTH)#
    WeaselDragon = PalObject("疾旋鼬", Elements.ICE, Elements.DRAGON)#
    Werewolf = PalObject("月镰魔", Elements.DARK)#
    WhiteMoth = PalObject("绸笠蛾", Elements.ICE)#
    WhiteTiger = PalObject("冰棘兽", Elements.ICE)#
    WindChimes = PalObject("吊缚灵", Elements.EARTH)#
    WindChimes_Ice = PalObject("冰缚灵", Elements.ICE)#
    WizardOwl = PalObject("啼卡尔", Elements.DARK)#
    WoolFox = PalObject("米露菲", Elements.NORMAL)#
    Yeti = PalObject("白绒雪怪", Elements.ICE)#
    Yeti_Grass = PalObject("绿苔绒怪", Elements.LEAF)#

    # 高塔BOSS
    GYM_ThunderDragonMan = PalObject("BOSS-波鲁杰克斯", Elements.DRAGON, Elements.ELECTRICITY, tower=True)#
    GYM_LilyQueen = PalObject("BOSS-百合女王", Elements.LEAF, tower=True)#
    GYM_Horus = PalObject("BOSS-荷鲁斯", Elements.FIRE, tower=True)#
    GYM_BlackGriffon = PalObject("BOSS-异构格里芬", Elements.DARK, tower=True)#
    GYM_ElecPanda = PalObject("BOSS-暴电熊", Elements.ELECTRICITY, tower=True)#

    # 人类实体 (尚未完成)
    Male_DarkTrader01 = PalObject("人类-黑市商人", Elements.NONE, human=True)#
    FireCult_FlameThrower = PalObject("人类-Brothers of the Eternal Pyre Martyr", Elements.NONE, human=True)#
    Male_Soldier01 = PalObject("人类-Burly Merc", Elements.NONE, human=True)#
    Female_Soldier01 = PalObject("人类-Expedition Survivor", Elements.NONE, human=True)#
    Believer_CrossBow = PalObject("人类-Free Pal Alliance Devout", Elements.NONE, human=True)#
    Male_Scientist01_LaserRifle = PalObject("人类-PAL Genetic Research Unit Executioner", Elements.NONE, human=True)#
    PalDealer = PalObject("人类-Pal Merchant", Elements.NONE, human=True)#
    Police_Handgun = PalObject("人类-PIDF Guard", Elements.NONE, human=True)#
    Hunter_Bat = PalObject("人类-Syndicate Thug (Bat)", Elements.NONE, human=True)#
    Hunter_FlameThrower = PalObject("人类-Syndicate Cleaner", Elements.NONE, human=True)#
    Hunter_Fat_GatlingGun = PalObject("人类-Syndicate Crusher", Elements.NONE, human=True)#
    Hunter_RocketLauncher = PalObject("人类-Syndicate Elite", Elements.NONE, human=True)#
    Hunter_Grenade = PalObject("人类-Syndicate Grenadier", Elements.NONE, human=True)#
    Hunter_Rifle = PalObject("人类-Syndicate Gunner", Elements.NONE, human=True)#
    Hunter_Shotgun = PalObject("人类-Syndicate Hunter", Elements.NONE, human=True)#
    Hunter_Handgun = PalObject("人类-Syndicate Thug (Handgun)", Elements.NONE, human=True)#
    SalesPerson = PalObject("人类-流浪商人", Elements.NONE, human=True)#

    @classmethod
    def find(self, value):
        for i in PalType:
            if i.value.GetName() == value:
                return i

class PalEntity:

    def __init__(self, data):
        self._data = data
        self._obj = data['value']['RawData']['value']['object']['SaveParameter']['value']

        if "IsPlayer" in self._obj:
            raise Exception("This is a player character")

        self.isLucky = ("IsRarePal" in self._obj)
        
        typename = self._obj['CharacterID']['value']
        # print(f"Debug: typename1 - {typename}")

        self.isBoss = False
        if typename[:5].lower() == "boss_":
            typename = typename[5:] # if first 5 characters match boss_ then cut the first 5 characters off
            # typename = typename.replace("BOSS_", "") # this causes bugs
            self.isBoss = True if not self.isLucky else False
            if typename == "LazyCatFish": # BOSS_LazyCatFish and LazyCatfish
                typename = "LazyCatfish"

        # print(f"Debug: typename2 - '{typename}'")
        if typename.lower() == "sheepball":
            typename = "Sheepball"

            # Strangely, Boss and Lucky Lamballs have camelcasing
            # Regular ones... don't
        # print(f"Debug: typename3 - '{typename}'")
        
        self._type = PalType[typename]
        print(f"Created Entity of type {typename}: {self._type.value} - Lucky: {self.isLucky} Boss: {self.isBoss}")

        if "Gender" in self._obj:
            if self._obj['Gender']['value']['value'] == "EPalGenderType::Male":
                self._gender = "雄性 ♂"
            else:
                self._gender = "雌性 ♀"
        else:
            self._gender = "未知"

        self._workspeed = self._obj['CraftSpeed']['value']

        if not "Talent_Melee" in self._obj:
            self._obj['Talent_Melee'] = EmptyMeleeObject.copy()
        self._melee = self._obj['Talent_Melee']['value']

        if not "Talent_Shot" in self._obj:
            self._obj['Talent_Shot'] = EmptyShotObject.copy()
        self._ranged = self._obj['Talent_Shot']['value']

        if not "Talent_Defense" in self._obj:
            self._obj['Talent_Defense'] = EmptyDefenceObject.copy()
        self._defence = self._obj['Talent_Defense']['value']

        if not "Rank" in self._obj:
            self._obj['Rank'] = EmptyRankObject.copy()
        self._rank = self._obj['Rank']['value']

        # Fix broken ranks
        if self.GetRank() == 0:
            self.SetRank(1)

        if not "PassiveSkillList" in self._obj:
            self._obj['PassiveSkillList'] = EmptySkillObject.copy()
        self._skills = self._obj['PassiveSkillList']['value']['values']
        self.CleanseSkills()

        self._owner = self._obj['OwnerPlayerUId']['value']

        if not "Level" in self._obj:
            self._obj['Level'] = EmptyLevelObject.copy()
        self._level = self._obj['Level']['value']

        if not "Exp" in self._obj:
            self._obj['Exp'] = EmptyExpObject.copy()
        # We don't store Exp yet

        self._nickname = ""
        if "NickName" in self._obj:
            self._nickname = self._obj['NickName']['value']

        self.isTower = self._type.value.IsTower()

    def SwapGender(self):
        if self._obj['Gender']['value']['value'] == "EPalGenderType::Male":
            self._obj['Gender']['value']['value'] = "EPalGenderType::Female"
            self._gender = "雌性 ♀"
        else:
            self._obj['Gender']['value']['value'] = "EPalGenderType::Male"
            self._gender = "雄性 ♂"
               

    def CleanseSkills(self):
        i = 0
        while i < len(self._skills):
            if self._skills[i].lower() == "none":
                self._skills.pop(i)
            else:
                i+=1
        
    def GetType(self):
        return self._type

    def SetType(self, value):
        self._obj['CharacterID']['value'] = PalType.find(value).name
        self._type = PalType.find(value)

    def GetObject(self):
        return self._type.value

    def GetGender(self):
        return self._gender

    def GetWorkSpeed(self):
        return self._workspeed

    def SetWorkSpeed(self, value):
        self._obj['CraftSpeed']['value'] = self._workspeed = value

    def SetAttack(self, mval, rval):
        self._obj['Talent_Melee']['value'] = self._melee = mval
        self._obj['Talent_Shot']['value'] = self._ranged = rval

    def GetAttackMelee(self):
        return self._melee

    def SetAttackMelee(self, value):
        self._obj['Talent_Melee']['value'] = self._melee = value

    def GetAttackRanged(self):
        return self._ranged

    def SetAttackRanged(self, value):
        self._obj['Talent_Shot']['value'] = self._ranged = value

    def GetDefence(self):
        return self._defence

    def SetDefence(self, value):
        self._obj['Talent_Defense']['value'] = self._defence = value

    def GetName(self):
        return self.GetObject().GetName()

    def GetImage(self):
        return self.GetObject().GetImage()
    
    def GetPrimary(self):
        return self.GetObject().GetPrimary().value

    def GetSecondary(self):
        return self.GetObject().GetSecondary().value

    def GetSkills(self):
        self.CleanseSkills()
        return self._skills

    def SkillCount(self):
        return len(self._skills)

    def SetSkill(self, slot, skill):
        if slot > len(self._skills)-1:
            self._skills.append(PalSkills(skill).name)
        else:
            self._skills[slot] = PalSkills(skill).name

    def GetOwner(self):
        return self._owner

    def GetLevel(self):
        return self._level

    def SetLevel(self, value):
        # We need this check until we fix adding missing nodes
        if "Level" in self._obj and "Exp" in self._obj:
            self._obj['Level']['value'] = self._level = value
            self._obj['Exp']['value'] = 0
        else:
            print(f"[ERROR:] Failed to update level for: '{self.GetName()}'")

    def GetRank(self):
        return self._rank

    def SetRank(self, value):
        if "Rank" in self._obj:
            self._obj['Rank']['value'] = self._rank = value # we dont +1 here, since we have methods to patch rank in PalEdit.py
        else:
            print(f"[ERROR:] Failed to update rank for: '{self.GetName()}'") # we probably could get rid of this line, since you add rank if missing - same with level

    def RemoveSkill(self, slot):
        if slot < len(self._skills):
            self._skills.pop(slot)

    def GetNickname(self):
        return self.GetName() if self._nickname == "" else self._nickname

    def GetFullName(self):
        return self.GetObject().GetName() + (" 💀" if self.isBoss else "") + (" ♖" if self.isTower else "" ) + (" ✨" if self.isLucky else "") + (f" - '{self._nickname}'" if not self._nickname == "" else "")

if __name__ == "__main__":
    import os

    print(len(PalType))
    
    print(PalType.GrassPanda)
    print(PalType.GrassPanda.name)
    print(PalType.GrassPanda.value)

    for i in PalType:
        if not os.path.exists(f"resources/{i.value.GetName()}.png"):
            f = open(f"resources/{i.value.GetName()}.png", "w")
            f.write("0")
            f.close()
