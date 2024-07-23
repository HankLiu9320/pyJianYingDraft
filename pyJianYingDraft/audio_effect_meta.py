from enum import Enum
from typing import List

class Audio_effect_param:
    """音频特效参数信息"""

    sliderName: str
    """参数名称"""
    defaultValue: float
    """默认值"""
    minValue: float
    """最小值"""
    maxValue: float
    """最大值"""

    def __init__(self, sliderName: str, defaultValue: float, minValue: float, maxValue: float):
        self.sliderName = sliderName
        self.defaultValue = defaultValue
        self.minValue = minValue
        self.maxValue = maxValue

class Audio_effect_meta:
    """音频特效元数据"""

    name: str
    """效果名称"""
    is_vip: bool
    """是否为VIP特权"""

    resource_id: str
    """资源ID"""
    effect_id: str
    """效果ID"""
    md5_like_id: str
    """对应id字段, 意义不明"""

    params: List[Audio_effect_param]
    """效果的参数信息"""

    def __init__(self, name: str, is_vip: bool, resource_id: str, effect_id: str, md5_like_id: str, params: List[Audio_effect_param]):
        self.name = name
        self.is_vip = is_vip
        self.resource_id = resource_id
        self.effect_id = effect_id
        self.md5_like_id = md5_like_id
        self.params = params

class Audio_tone_effect_type(Enum):
    """剪映自带的音频“音色”效果类型"""

    # 免费
    台湾小哥    = Audio_effect_meta("台湾小哥", False, "7255565276819755576", "18149602", "8dd8889045e6c065177df791ddb3dfb8", [])
    圣诞精灵    = Audio_effect_meta("圣诞精灵", False, "7310059412062736946", "33214695", "8dd8889045e6c065177df791ddb3dfb8", [])
    圣诞老人    = Audio_effect_meta("圣诞老人", False, "7310059178133819930", "33214489", "8dd8889045e6c065177df791ddb3dfb8", [])
    广告男声    = Audio_effect_meta("广告男声", False, "7328088579811316263", "42060748", "f554735f65a98cc4da17a1c53ef6a886", [])
    港普男声    = Audio_effect_meta("港普男声", False, "7328087687548637732", "42060743", "f554735f65a98cc4da17a1c53ef6a886", [])
    老婆婆      = Audio_effect_meta("老婆婆", False, "7328089253114548799", "42060746", "f554735f65a98cc4da17a1c53ef6a886", [])
    解说小帅    = Audio_effect_meta("解说小帅", False, "7332473259369173540", "44254166", "f554735f65a98cc4da17a1c53ef6a886", [])
    大叔        = Audio_effect_meta("大叔", False, "7020344898033291790", "2672760", "2509bbd71e127b04a29f52a54e82c53c", [
                                    Audio_effect_param("音调", 0.834, 0.000, 1.000),
                                    Audio_effect_param("音色", 1.000, 0.000, 1.000)])
    """参数:
        - 音调: 默认0.83, 0.00 ~ 1.00
        - 音色: 默认1.00, 0.00 ~ 1.00
    """
    女生        = Audio_effect_meta("女生", False, "7020345715901600270", "2672757", "0ce1aade5958506c97bffea150772b6e", [
                                    Audio_effect_param("音调", 0.834, 0.000, 1.000),
                                    Audio_effect_param("音色", 0.334, 0.000, 1.000)])
    """参数:
        - 音调: 默认0.83, 0.00 ~ 1.00
        - 音色: 默认0.33, 0.00 ~ 1.00
    """
    怪物        = Audio_effect_meta("怪物", False, "7020344978794615327", "2672759", "2130ffa21e5980196e014ec0baade179", [
                                    Audio_effect_param("音调", 0.650, 0.000, 1.000),
                                    Audio_effect_param("音色", 0.780, 0.000, 1.000)])
    """参数:
        - 音调: 默认0.65, 0.00 ~ 1.00
        - 音色: 默认0.78, 0.00 ~ 1.00
    """
    机器人      = Audio_effect_meta("机器人", False, "7018011705414259213", "2672750", "4b87db25aecd2f6f71927930110c4a1e", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
    """
    男生        = Audio_effect_meta("男生", False, "7020345085233467917", "2672758", "ffd7a609207fd849efc9f63bf31697b1", [
                                    Audio_effect_param("音调", 0.375, 0.000, 1.000),
                                    Audio_effect_param("音色", 0.250, 0.000, 1.000)])
    """参数:
        - 音调: 默认0.38, 0.00 ~ 1.00
        - 音色: 默认0.25, 0.00 ~ 1.00
    """
    花栗鼠      = Audio_effect_meta("花栗鼠", False, "7018011553081332231", "2672752", "e30b1922b8300423f21f9f84eff41ced", [
                                    Audio_effect_param("音调", 0.500, 0.000, 1.000),
                                    Audio_effect_param("音色", 0.500, 0.000, 1.000)])
    """参数:
        - 音调: 默认0.50, 0.00 ~ 1.00
        - 音色: 默认0.50, 0.00 ~ 1.00
    """
    萝莉        = Audio_effect_meta("萝莉", False, "7020345789599715848", "2672756", "00b7ed2ccfe4d6076f78c8d751347a53", [
                                    Audio_effect_param("音调", 0.750, 0.000, 1.000),
                                    Audio_effect_param("音色", 0.600, 0.000, 1.000)])
    """参数:
        - 音调: 默认0.75, 0.00 ~ 1.00
        - 音色: 默认0.60, 0.00 ~ 1.00
    """


    # 付费
    TVB女声     = Audio_effect_meta("TVB女声", True, "7260024060417937978", "19186454", "8dd8889045e6c065177df791ddb3dfb8", [])
    东厂公公    = Audio_effect_meta("东厂公公", True, "7328092524612948491", "42060742", "f554735f65a98cc4da17a1c53ef6a886", [])
    云龙哥      = Audio_effect_meta("云龙哥", True, "7376558114830553612", "68856989", "f554735f65a98cc4da17a1c53ef6a886", [])
    侠客        = Audio_effect_meta("侠客", True, "7328089134331859468", "42060738", "f554735f65a98cc4da17a1c53ef6a886", [])
    做作夹子音  = Audio_effect_meta("做作夹子音", True, "7367676929496846911", "63231108", "f554735f65a98cc4da17a1c53ef6a886", [])
    八戒        = Audio_effect_meta("八戒", True, "7265891792766112314", "20427371", "8dd8889045e6c065177df791ddb3dfb8", [])
    军事解说    = Audio_effect_meta("军事解说", True, "7328092289480266252", "42060734", "f554735f65a98cc4da17a1c53ef6a886", [])
    动漫小新    = Audio_effect_meta("动漫小新", True, "7360901047662940708", "58979441", "f554735f65a98cc4da17a1c53ef6a886", [])
    动漫海绵    = Audio_effect_meta("动漫海绵", True, "7367676859883983379", "63231109", "f554735f65a98cc4da17a1c53ef6a886", [])
    咆哮哥      = Audio_effect_meta("咆哮哥", True, "7332473122605503039", "44254278", "f554735f65a98cc4da17a1c53ef6a886", [])
    商务殷语    = Audio_effect_meta("商务殷语", True, "7328085477267870249", "42060747", "f554735f65a98cc4da17a1c53ef6a886", [])
    四郎        = Audio_effect_meta("四郎", True, "7250403044414722621", "16627073", "8dd8889045e6c065177df791ddb3dfb8", [])
    太白        = Audio_effect_meta("太白", True, "7328091247308968484", "42060736", "f554735f65a98cc4da17a1c53ef6a886", [])
    如来佛祖    = Audio_effect_meta("如来佛祖", True, "7376558174049931830", "68856990", "f554735f65a98cc4da17a1c53ef6a886", [])
    姜饼人      = Audio_effect_meta("姜饼人", True, "7310059267384414747", "33214539", "8dd8889045e6c065177df791ddb3dfb8", [])
    容嬷嬷      = Audio_effect_meta("容嬷嬷", True, "7332472945366798860", "44254320", "f554735f65a98cc4da17a1c53ef6a886", [])
    小孩        = Audio_effect_meta("小孩", True, "7262648951948448315", "19716244", "8dd8889045e6c065177df791ddb3dfb8", [])
    强势妹      = Audio_effect_meta("强势妹", True, "7328091624427229759", "42060740", "f554735f65a98cc4da17a1c53ef6a886", [])
    快板        = Audio_effect_meta("快板", True, "7328088454183522827", "42060741", "f554735f65a98cc4da17a1c53ef6a886", [])
    恐怖电影    = Audio_effect_meta("恐怖电影", True, "7325710953247412787", "40932465", "f554735f65a98cc4da17a1c53ef6a886", [])
    悬疑解说    = Audio_effect_meta("悬疑解说", True, "7325711304390349362", "40932811", "f554735f65a98cc4da17a1c53ef6a886", [])
    懒小羊      = Audio_effect_meta("懒小羊", True, "7332473035116515859", "44254304", "f554735f65a98cc4da17a1c53ef6a886", [])
    搞笑解说    = Audio_effect_meta("搞笑解说", True, "7262648842238038584", "19716150", "8dd8889045e6c065177df791ddb3dfb8", [])
    文艺女声    = Audio_effect_meta("文艺女声", True, "7379565719991620132", "70562787", "f554735f65a98cc4da17a1c53ef6a886", [])
    樱桃丸子    = Audio_effect_meta("樱桃丸子", True, "7325709643332719113", "40931609", "f554735f65a98cc4da17a1c53ef6a886", [])
    樱花小哥    = Audio_effect_meta("樱花小哥", True, "7328091741678998055", "42060735", "f554735f65a98cc4da17a1c53ef6a886", [])
    武则天      = Audio_effect_meta("武则天", True, "7328088300474864167", "42060744", "f554735f65a98cc4da17a1c53ef6a886", [])
    沉稳解说    = Audio_effect_meta("沉稳解说", True, "7367676791164506636", "63231110", "f554735f65a98cc4da17a1c53ef6a886", [])
    温柔姐姐    = Audio_effect_meta("温柔姐姐", True, "7379565769190806079", "70562785", "f554735f65a98cc4da17a1c53ef6a886", [])
    熊二        = Audio_effect_meta("熊二", True, "7250403222798471740", "16627311", "8dd8889045e6c065177df791ddb3dfb8", [])
    猴哥        = Audio_effect_meta("猴哥", True, "7236944659547689531", "14477015", "4f6a1fbc0000e178c724d355efea1d9f", [])
    甜美悦悦    = Audio_effect_meta("甜美悦悦", True, "7325710673978069530", "40932253", "f554735f65a98cc4da17a1c53ef6a886", [])
    生活小妙招  = Audio_effect_meta("生活小妙招", True, "7328092409525441065", "42060737", "f554735f65a98cc4da17a1c53ef6a886", [])
    电竞解说    = Audio_effect_meta("电竞解说", True, "7325711893551649330", "40933559", "f554735f65a98cc4da17a1c53ef6a886", [])
    电视广告    = Audio_effect_meta("电视广告", True, "7360901109667336743", "58979440", "f554735f65a98cc4da17a1c53ef6a886", [])
    紫薇        = Audio_effect_meta("紫薇", True, "7281175506391667257", "23475307", "8dd8889045e6c065177df791ddb3dfb8", [])
    舌尖解说    = Audio_effect_meta("舌尖解说", True, "7328091500753982015", "42060739", "f554735f65a98cc4da17a1c53ef6a886", [])
    蜡笔小妮    = Audio_effect_meta("蜡笔小妮", True, "7379565670398169619", "70562786", "f554735f65a98cc4da17a1c53ef6a886", [])
    语音助手    = Audio_effect_meta("语音助手", True, "7325710335455793714", "40931973", "f554735f65a98cc4da17a1c53ef6a886", [])
    那姐        = Audio_effect_meta("那姐", True, "7369177370873303587", "64206631", "f554735f65a98cc4da17a1c53ef6a886", [])
    锤子哥      = Audio_effect_meta("锤子哥", True, "7328091348098093580", "42060745", "f554735f65a98cc4da17a1c53ef6a886", [])
    顾姐        = Audio_effect_meta("顾姐", True, "7250403134923608631", "16627197", "8dd8889045e6c065177df791ddb3dfb8", [])
    黛玉        = Audio_effect_meta("黛玉", True, "7255565592093004343", "18149634", "8dd8889045e6c065177df791ddb3dfb8", [])

class Audio_scene_effect_type(Enum):
    """剪映自带的音频“场景音”效果类型"""

    # 免费
    _8bit       = Audio_effect_meta("8bit", False, "7161319747584266766", "5723961", "8d24238329ea5c250e33ae241d5adae2", [
                                    Audio_effect_param("change_voice_param_pitch_shift", 0.500, 0.000, 1.000),
                                    Audio_effect_param("change_voice_param_timbre", 1.000, 0.000, 1.000),
                                    Audio_effect_param("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_pitch_shift: 默认0.50, 0.00 ~ 1.00
        - change_voice_param_timbre: 默认1.00, 0.00 ~ 1.00
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """
    低保真      = Audio_effect_meta("低保真", False, "7024390914537689614", "2672762", "7ddbd39a691a66a021f684cab756a89a", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
    """
    合成器      = Audio_effect_meta("合成器", False, "7018011500577034759", "2672753", "394efea5922637bcd8288e0fb3c2372e", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
    """
    回音        = Audio_effect_meta("回音", False, "7018011608408396325", "5723901", "5377f66109693f2d473df5ea6ec8f791", [
                                    Audio_effect_param("change_voice_param_quantity", 0.800, 0.000, 1.000),
                                    Audio_effect_param("change_voice_param_strength", 0.762, 0.000, 1.000)])
    """参数:
        - change_voice_param_quantity: 默认0.80, 0.00 ~ 1.00
        - change_voice_param_strength: 默认0.76, 0.00 ~ 1.00
    """
    扩音器      = Audio_effect_meta("扩音器", False, "7018011975514853924", "2672749", "13169f6ab9957ff005d316239bef0045", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
    """
    水下        = Audio_effect_meta("水下", False, "7106404450444513806", "2673077", "53956694a8b68b2855faa2adc043b5b1", [
                                    Audio_effect_param("深度", 0.500, 0.000, 1.000)])
    """参数:
        - 深度: 默认0.50, 0.00 ~ 1.00
    """
    没电了      = Audio_effect_meta("没电了", False, "7018012193769656845", "2672747", "87f91614bac060840ad5a57ef2b0c9ca", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
    """
    环绕音      = Audio_effect_meta("环绕音", False, "7161319847819743780", "5723960", "fa9a4cb20d3488bf79e176571d5841f5", [
                                    Audio_effect_param("change_voice_param_center_position", 0.500, 0.000, 1.000),
                                    Audio_effect_param("change_voice_param_surrounding_frequency", 0.500, 0.000, 1.000)])
    """参数:
        - change_voice_param_center_position: 默认0.50, 0.00 ~ 1.00
        - change_voice_param_surrounding_frequency: 默认0.50, 0.00 ~ 1.00
    """
    电音        = Audio_effect_meta("电音", False, "7018011438379700773", "2672754", "d893a319d5175d9f09f70ddef1f79980", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
    """
    颤音        = Audio_effect_meta("颤音", False, "7018011370289369637", "2672755", "c5e4874f83337e1cb9f8322fb843c901", [
                                    Audio_effect_param("频率", 0.714, 0.000, 1.000),
                                    Audio_effect_param("幅度", 0.905, 0.000, 1.000)])
    """参数:
        - 频率: 默认0.71, 0.00 ~ 1.00
        - 幅度: 默认0.91, 0.00 ~ 1.00
    """
    麦霸        = Audio_effect_meta("麦霸", False, "7018012141332468260", "2672748", "3eedef5ef82b32912203a1f4fb901182", [
                                    Audio_effect_param("空间大小", 0.052, 0.000, 1.000),
                                    Audio_effect_param("强弱", 0.450, 0.000, 1.000)])
    """参数:
        - 空间大小: 默认0.05, 0.00 ~ 1.00
        - 强弱: 默认0.45, 0.00 ~ 1.00
    """
    黑胶        = Audio_effect_meta("黑胶", False, "7024391411764040205", "2672761", "59e61d687a0f612bfae43bccf770f090", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000),
                                    Audio_effect_param("噪点", 0.743, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
        - 噪点: 默认0.74, 0.00 ~ 1.00
    """

    # 付费
    _3d环绕音   = Audio_effect_meta("3d环绕音", True, "7350214888242811455", "53187169", "577c3d8e5312012b1d98ba5fc0b206d0", [
                                    Audio_effect_param("强度", 0.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认0.00, 0.00 ~ 1.00
    """
    Autotune    = Audio_effect_meta("Autotune", True, "7360900806851170828", "58979352", "1477f4ca8307e2fa4ee2243d98d8b837", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    下雨        = Audio_effect_meta("下雨", True, "7375069649446113804", "68076030", "83bb223637d5368384c47e3d2b061b62", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000),
                                    Audio_effect_param("noise", 0.743, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
        - noise: 默认0.74, 0.00 ~ 1.00
    """
    乡村大喇叭  = Audio_effect_meta("乡村大喇叭", True, "7282691036197950009", "23897651", "c996243ac50d235f00e5931e5ecadc52", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    人声增强    = Audio_effect_meta("人声增强", True, "7106404399756349983", "2673078", "626f988dbd2cbd17acaa24d08451e314", [
                                    Audio_effect_param("强弱", 1.000, 0.000, 1.000)])
    """参数:
        - 强弱: 默认1.00, 0.00 ~ 1.00
    """
    低音增强    = Audio_effect_meta("低音增强", True, "7106404304247853604", "2673080", "e7c09c96d10c163269fc4e35c1f4b1ee", [
                                    Audio_effect_param("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """
    停车场      = Audio_effect_meta("停车场", True, "7372150242524795446", "66413024", "d2dd515293081a8573485159db5a71e0", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    冰川之下    = Audio_effect_meta("冰川之下", True, "7375068986829967883", "68076029", "6b9cda93f6d75b9a3b19b2e8eb6ad40f", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000),
                                    Audio_effect_param("noise", 0.743, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
        - noise: 默认0.74, 0.00 ~ 1.00
    """
    刮风        = Audio_effect_meta("刮风", True, "7375069247275274771", "68076028", "8600891882159f364d8c53e4f703cff4", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000),
                                    Audio_effect_param("noise", 0.743, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
        - noise: 默认0.74, 0.00 ~ 1.00
    """
    噪音混响    = Audio_effect_meta("噪音混响", True, "7382844688987853349", "72110975", "3b3b09b530b0a64666f1c5b6d20d4018", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    地狱        = Audio_effect_meta("地狱", True, "7375069113988682281", "68076027", "5ec03c41ada16530949daa4106c85a90", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000),
                                    Audio_effect_param("noise", 0.743, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
        - noise: 默认0.74, 0.00 ~ 1.00
    """
    复古收音机  = Audio_effect_meta("复古收音机", True, "7350215379714576907", "53187166", "301d642d131aabff7ea8c3b717b36a79", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    失真电子    = Audio_effect_meta("失真电子", True, "7350215296801575443", "53187167", "a1c00df42076ed1bd6a81f2d30b94566", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    对讲机      = Audio_effect_meta("对讲机", True, "7350214704284832275", "53187168", "016dbdb3c786896c92bb936ece11acf6", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    房间        = Audio_effect_meta("房间", True, "7282691385872880165", "23880629", "639f5c0c6b20418aaeb0e144da21151c", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    捂嘴        = Audio_effect_meta("捂嘴", True, "7372405649684042292", "66552320", "9f9a8270c0005a480547d6ddf2a9293a", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    教堂        = Audio_effect_meta("教堂", True, "7282691146759803429", "23882063", "96dc71756d0025e96a504b42d988b2ac", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    教室        = Audio_effect_meta("教室", True, "7282687783833965113", "23897703", "678c14a6f63f75e03daa062a254081f7", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    机器人2     = Audio_effect_meta("机器人2", True, "7372150541738054156", "66413023", "952f3feddf3555939adbbfd1c1869474", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    沙漠        = Audio_effect_meta("沙漠", True, "7375069515530375691", "68076025", "099c935428943c9c3662b15b35b1ee36", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000),
                                    Audio_effect_param("noise", 0.743, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
        - noise: 默认0.74, 0.00 ~ 1.00
    """
    派对        = Audio_effect_meta("派对", True, "7381685442795541042", "71718513", "723386ab87f938779a3369436234d903", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000),
                                    Audio_effect_param("noise", 0.743, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
        - noise: 默认0.74, 0.00 ~ 1.00
    """
    深海回声    = Audio_effect_meta("深海回声", True, "7350215168413929995", "53187172", "37a16a2dc77540b7d70fe301e482d4f2", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    电话        = Audio_effect_meta("电话", True, "7264894634285863483", "20255003", "5da5a98b8c926c0dcc1c3c8bc3f3012f", [
                                    Audio_effect_param("强弱", 0.700, 0.000, 1.000)])
    """参数:
        - 强弱: 默认0.70, 0.00 ~ 1.00
    """
    留声机      = Audio_effect_meta("留声机", True, "7282687663872676408", "23897797", "e692fae669650c948451b5811a04e7e6", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    百老汇      = Audio_effect_meta("百老汇", True, "7372150379150053907", "66413025", "73e3a35496b9766d0400165844be72f1", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    空灵感      = Audio_effect_meta("空灵感", True, "7350215092975178252", "53187171", "aa1887a8b3375d20df6bf9438d62083a", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    空谷回声    = Audio_effect_meta("空谷回声", True, "7350214991628210727", "53187170", "9913daa32167a17c1f41ad2f5596c411", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    老式电话    = Audio_effect_meta("老式电话", True, "7282691476843139621", "23880011", "2eb835175e1e72e9d86b09bf513077cf", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    言灵术      = Audio_effect_meta("言灵术", True, "7382844601435951653", "72110974", "7184386e75226a36942c60a5d5bb5618", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    豪宅回声    = Audio_effect_meta("豪宅回声", True, "7360900963294515775", "58979353", "7c20b5fba991f3188f14d7cdb0de1fa1", [
                                    Audio_effect_param("强度", 1.000, 0.000, 1.000)])
    """参数:
        - 强度: 默认1.00, 0.00 ~ 1.00
    """
    迷幻电子    = Audio_effect_meta("迷幻电子", True, "7375069381769826879", "68076026", "ce220d25a6f95bd31a81f6421bbf2525", [
                                    Audio_effect_param("strength", 1.000, 0.000, 1.000),
                                    Audio_effect_param("noise", 0.743, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
        - noise: 默认0.74, 0.00 ~ 1.00
    """

    @classmethod
    def from_name(cls, name: str) -> "Audio_scene_effect_type":
        name = name.lower().replace(" ", "").replace("_", "")
        for effect in cls.__members__.values():
            if effect.name.lower().replace(" ", "").replace("_", "") == name:
                return effect
        raise ValueError(f"Audio effect {name} not found.")

class Audio_style_effect_type(Enum):
    """剪映自带的音频“声音成曲”效果类型"""

    Lofi        = Audio_effect_meta("Lofi", False, "7252917861948068410", "17345060", "8dd8889045e6c065177df791ddb3dfb8", [])
    民谣        = Audio_effect_meta("民谣", False, "7251868698170888759", "17046923", "8dd8889045e6c065177df791ddb3dfb8", [])
    嘻哈        = Audio_effect_meta("嘻哈", True, "7252918249036190245", "17344948", "8dd8889045e6c065177df791ddb3dfb8", [])
    爵士        = Audio_effect_meta("爵士", True, "7264413578860433978", "20120940", "8dd8889045e6c065177df791ddb3dfb8", [])
    节奏蓝调    = Audio_effect_meta("节奏蓝调", True, "7252918101958726200", "17345046", "8dd8889045e6c065177df791ddb3dfb8", [])
    雷鬼        = Audio_effect_meta("雷鬼", True, "7264413386962637368", "20120864", "8dd8889045e6c065177df791ddb3dfb8", [])