"""定义视频片段及其相关类

包含图像调节设置、动画效果、特效、转场等相关类
"""

import uuid
import warnings

from typing import Optional, Literal, Union
from typing import Dict, List, Tuple, Any

from .time_util import tim, Timerange
from .segment import Media_segment
from .local_materials import Video_material
from .keyframe import Keyframe_property, Keyframe_list

from .metadata import *

class Clip_settings:
    """素材片段的图像调节设置"""

    alpha: float
    """图像不透明度, 0-1"""
    flip_horizontal: bool
    """是否水平翻转"""
    flip_vertical: bool
    """是否垂直翻转"""
    rotation: float
    """顺时针旋转的**角度**, 可正可负"""
    scale_x: float
    """水平缩放比例"""
    scale_y: float
    """垂直缩放比例"""
    transform_x: float
    """水平位移, 单位为整个画布上的半个像素?"""
    transform_y: float
    """垂直位移, 单位为整个画布上的半个像素?"""

    def __init__(self, *, alpha: float = 1.0,
                 flip_horizontal: bool = False, flip_vertical: bool = False,
                 rotation: float = 0.0,
                 scale_x: float = 1.0, scale_y: float = 1.0,
                 transform_x: float = 0.0, transform_y: float = 0.0):
        """初始化图像调节设置, 默认参数表示不作任何图像变换

        Args:
            alpha (float, optional): 图像不透明度, 0-1. 默认为1.0.
            flip_horizontal (bool, optional): 是否水平翻转. 默认为False.
            flip_vertical (bool, optional): 是否垂直翻转. 默认为False.
            rotation (float, optional): 顺时针旋转的**角度**, 可正可负. 默认为0.0.
            scale_x (float, optional): 水平缩放比例. 默认为1.0.
            scale_y (float, optional): 垂直缩放比例. 默认为1.0.
            transform_x (float, optional): 水平位移, 单位为像素. 默认为0.0.
            transform_y (float, optional): 垂直位移, 单位为像素. 默认为0.0.
        """
        self.alpha = alpha
        self.flip_horizontal, self.flip_vertical = flip_horizontal, flip_vertical
        self.rotation = rotation
        self.scale_x, self.scale_y = scale_x, scale_y
        self.transform_x, self.transform_y = transform_x, transform_y

    def export_json(self) -> Dict[str, Any]:
        clip_settings_json = {
            "alpha": self.alpha,
            "flip": {"horizontal": self.flip_horizontal, "vertical": self.flip_vertical},
            "rotation": self.rotation,
            "scale": {"x": self.scale_x, "y": self.scale_y},
            "transform": {"x": self.transform_x, "y": self.transform_y}
        }
        return clip_settings_json

class Animation:
    """一个动画效果"""

    name: str
    """动画名称, 默认取为动画效果的名称"""
    effect_id: str
    """另一种动画id, 由剪映本身提供"""
    animation_type: Literal["in", "out", "group"]
    resource_id: str
    """资源id, 由剪映本身提供"""

    start: int
    """动画相对此片段开头的偏移, 单位为微秒"""
    duration: int
    """动画持续时间, 单位为微秒, 各动画有其默认值"""

    category_id: Literal["ruchang", "chuchang", "group"]
    category_name: Literal["入场", "出场", "组合"]
    """动画类型, 入场/出场/组合"""

    is_video_animation: bool

    def __init__(self, animation_type: Union[Intro_type, Outro_type, Group_animation_type],
                 start: int, duration: int):
        type_meta = animation_type.value
        self.name = type_meta.title
        self.effect_id = type_meta.effect_id
        self.resource_id = type_meta.resource_id

        if isinstance(animation_type, Intro_type):
            self.animation_type = "in"
            self.category_id = "ruchang"
            self.category_name = "入场"

            self.is_video_animation = True
        elif isinstance(animation_type, Outro_type):
            self.animation_type = "out"
            self.category_id = "chuchang"
            self.category_name = "出场"

            self.is_video_animation = True
        elif isinstance(animation_type, Group_animation_type):
            self.animation_type = "group"
            self.category_id = "group"
            self.category_name = "组合"

            self.is_video_animation = True

        self.start = start
        self.duration = duration

    def export_json(self) -> Dict[str, Any]:
        return {
            "anim_adjust_params": None,
            "platform": "all",
            "panel": "video" if self.is_video_animation else "",
            "material_type": "video" if self.is_video_animation else "sticker",

            "name": self.name,
            "id": self.effect_id,
            "type": self.animation_type,
            "resource_id": self.resource_id,
            "category_id": self.category_id,
            "category_name": self.category_name,

            "start": self.start,
            "duration": self.duration,
            # 不导出path和request_id字段
        }

class Segment_animations:
    """附加于某素材上的一系列动画（一般是入场/出场/组合动画）"""

    animation_id: str
    """动画系列全局id, 自动生成"""
    animation_type: str
    """animation_type字段, 似乎总是'sticker_animation'"""

    animations: List[Animation]
    """动画列表"""

    def __init__(self, animation_type: str = "sticker_animation"):
        self.animation_id = uuid.uuid4().hex
        self.animation_type = animation_type
        self.animations = []

    def add_animation(self, animation: Animation) -> None:
        # 不允许添加超过一个同类型的动画（如两个入场动画）
        if animation.animation_type in [ani.animation_type for ani in self.animations]:
            raise ValueError(f"Duplicate animation type '{animation.animation_type}'")
        # 不允许组合动画与出入场动画同时出现
        if any(ani.animation_type == "group" for ani in self.animations):
            raise ValueError("Group animation contradicts with any other animation")
        if animation.animation_type == "group" and len(self.animations) > 0:
            raise ValueError("Cannot add group animation when there are animations exist")

        self.animations.append(animation)

    def export_json(self) -> Dict[str, Any]:
        return {
            "id": self.animation_id,
            "type": self.animation_type,
            "multi_language_current": "none",
            "animations": [animation.export_json() for animation in self.animations]
        }

class Mask:
    """蒙版对象"""

    mask_meta: Mask_meta
    """蒙版元数据"""
    global_id: str
    """蒙版全局id, 由程序自动生成"""

    center_x: float
    center_y: float
    width: float
    height: float
    aspect_ratio: float

    rotation: float
    invert: bool
    feather: float
    """羽化程度, 0-1"""
    round_corner: float
    """矩形蒙版的圆角, 0-1"""

    def __init__(self, mask_meta: Mask_meta,
                 cx: float, cy: float, w: float, h: float,
                 ratio: float, rot: float, inv: bool, feather: float, round_corner: float):
        self.mask_meta = mask_meta
        self.global_id = uuid.uuid4().hex

        self.center_x, self.center_y = cx, cy
        self.width, self.height = w, h
        self.aspect_ratio = ratio

        self.rotation = rot
        self.invert = inv
        self.feather = feather
        self.round_corner = round_corner

    def export_json(self) -> Dict[str, Any]:
        return {
            "config": {
                "aspectRatio": self.aspect_ratio,
                "centerX": self.center_x,
                "centerY": self.center_y,
                "feather": self.feather,
                "height": self.height,
                "invert": self.invert,
                "rotation": self.rotation,
                "roundCorner": self.round_corner,
                "width": self.width
            },
            "id": self.global_id,
            "name": self.mask_meta.name,
            "platform": "all",
            "position_info": "",
            "resource_type": self.mask_meta.resource_type,
            "resource_id": self.mask_meta.resource_id,
            "type": "mask"
            # 不导出path字段
        }

class Video_effect:
    """视频特效素材"""

    name: str
    """特效名称"""
    global_id: str
    """特效全局id, 由程序自动生成"""
    effect_id: str
    """某种特效id, 由剪映本身提供"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    effect_type: Literal["video_effect", "face_effect"]
    apply_target_type: Literal[0, 2]
    """应用目标类型, 0: 片段, 2: 全局"""

    adjust_params: List[Effect_param_instance]

    def __init__(self, effect_meta: Union[Video_scene_effect_type, Video_character_effect_type],
                 params: Optional[List[Optional[float]]] = None, *,
                 apply_target_type: Literal[0, 2] = 0):
        """根据给定的特效元数据及参数列表构造一个视频特效对象, params的范围是0~100"""

        self.name = effect_meta.value.name
        self.global_id = uuid.uuid4().hex
        self.effect_id = effect_meta.value.effect_id
        self.resource_id = effect_meta.value.resource_id
        self.adjust_params = []

        if isinstance(effect_meta, Video_scene_effect_type):
            self.effect_type = "video_effect"
        elif isinstance(effect_meta, Video_character_effect_type):
            self.effect_type = "face_effect"
        else:
            raise TypeError("Invalid effect meta type %s" % type(effect_meta))
        self.apply_target_type = apply_target_type

        self.adjust_params = effect_meta.value.parse_params(params)

    def export_json(self) -> Dict[str, Any]:
        return {
            "adjust_params": [param.export_json() for param in self.adjust_params],
            "apply_target_type": self.apply_target_type,
            "apply_time_range": None,
            "category_id": "", # 一律设为空
            "category_name": "", # 一律设为空
            "common_keyframes": [],
            "disable_effect_faces": [],
            "effect_id": self.effect_id,
            "formula_id": "",
            "id": self.global_id,
            "name": self.name,
            "platform": "all",
            "render_index": 11000,
            "resource_id": self.resource_id,
            "source_platform": 0,
            "time_range": None,
            "track_render_index": 0,
            "type": self.effect_type,
            "value": 1.0,
            "version": ""
            # 不导出path、request_id和algorithm_artifact_path字段
        }

class Filter:
    """滤镜素材"""

    global_id: str
    """滤镜全局id, 由程序自动生成"""

    effect_meta: Effect_meta
    """滤镜的元数据"""
    intensity: float
    """滤镜强度(滤镜的唯一参数)"""

    apply_target_type: Literal[0, 2]
    """应用目标类型, 0: 片段, 2: 全局"""

    def __init__(self, meta: Effect_meta, intensity: float, *,
                 apply_target_type: Literal[0, 2] = 0):
        """根据给定的滤镜元数据及强度构造滤镜素材对象"""
        if len(meta.params) == 0 and intensity != 1.0:
            warnings.warn("Filter '%s' cannot set intensity, input intensity '%f' is ignored" % (meta.name, intensity))
            intensity = 1.0

        self.global_id = uuid.uuid4().hex
        self.effect_meta = meta
        self.intensity = intensity
        self.apply_target_type = apply_target_type

    def export_json(self) -> Dict[str, Any]:
        return {
            "adjust_params": [],
            "algorithm_artifact_path": "",
            "apply_target_type": self.apply_target_type,
            "bloom_params": None,
            "category_id": "", # 一律设为空
            "category_name": "", # 一律设为空
            "color_match_info": {
                "source_feature_path": "",
                "target_feature_path": "",
                "target_image_path": ""
            },
            "effect_id": self.effect_meta.effect_id,
            "enable_skin_tone_correction": False,
            "exclusion_group": [],
            "face_adjust_params": [],
            "formula_id": "",
            "id": self.global_id,
            "intensity_key": "",
            "multi_language_current": "",
            "name": self.effect_meta.name,
            "panel_id": "",
            "platform": "all",
            "resource_id": self.effect_meta.resource_id,
            "source_platform": 1,
            "sub_type": "none",
            "time_range": None,
            "type": "filter",
            "value": self.intensity,
            "version": ""
            # 不导出path和request_id
        }

class Transition:
    """转场对象"""

    name: str
    """转场名称"""
    global_id: str
    """转场全局id, 由程序自动生成"""
    effect_id: str
    """转场效果id, 由剪映本身提供"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    duration: int
    """转场持续时间, 单位为微秒"""
    is_overlap: bool
    """是否与上一个片段重叠(?)"""

    def __init__(self, effect_meta: Transition_type, duration: Optional[int] = None):
        """根据给定的转场元数据及持续时间构造一个转场对象"""
        self.name = effect_meta.value.name
        self.global_id = uuid.uuid4().hex
        self.effect_id = effect_meta.value.effect_id
        self.resource_id = effect_meta.value.resource_id

        self.duration = duration if duration is not None else effect_meta.value.default_duration
        self.is_overlap = effect_meta.value.is_overlap

    def export_json(self) -> Dict[str, Any]:
        return {
            "category_id": "", # 一律设为空
            "category_name": "", # 一律设为空
            "duration": self.duration,
            "effect_id": self.effect_id,
            "id": self.global_id,
            "is_overlap": self.is_overlap,
            "name": self.name,
            "platform": "all",
            "resource_id": self.resource_id,
            "type": "transition"
            # 不导出path和request_id字段
        }

class Video_segment(Media_segment):
    """安放在轨道上的一个视频/图片片段"""

    material_size: Tuple[int, int]
    """素材尺寸"""

    clip_settings: Clip_settings
    """图像调节设置, 其效果可被关键帧覆盖"""

    uniform_scale: bool
    """是否锁定XY轴缩放比例"""

    effects: List[Video_effect]
    """特效列表

    在放入轨道时自动添加到素材列表中
    """
    filters: List[Filter]
    """滤镜列表

    在放入轨道时自动添加到素材列表中
    """
    animations_instance: Optional[Segment_animations]
    """动画实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """
    mask: Optional[Mask]
    """蒙版实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """
    transition: Optional[Transition]
    """转场实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, material: Video_material, target_timerange: Timerange, *,
                 source_timerange: Optional[Timerange] = None, speed: Optional[float] = None, volume: float = 1.0,
                 clip_settings: Optional[Clip_settings] = None):
        """利用给定的视频/图片素材构建一个轨道片段, 并指定其时间信息及图像调节设置

        片段创建完成后, 可通过`Script_file.add_segment`方法将其添加到轨道中

        Args:
            material (`Video_material`): 素材实例, 注意你仍然需要为其调用`Script_file.add_material`来将其添加到素材列表中
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围
            source_timerange (`Timerange`, optional): 截取的素材片段的时间范围, 默认从开头根据`speed`截取与`target_timerange`等长的一部分
            speed (`float`, optional): 播放速度, 默认为1.0. 此项与`source_timerange`同时指定时, 将覆盖`target_timerange`中的时长
            volume (`float`, optional): 音量, 默认为1.0
            clip_settings (`Clip_settings`, optional): 图像调节设置, 默认不作任何变换

        Raises:
            `ValueError`: 指定的或计算出的`source_timerange`超出了素材的时长范围
        """
        if source_timerange is not None and speed is not None:
            target_timerange = Timerange(target_timerange.start, round(source_timerange.duration / speed))
        elif source_timerange is not None and speed is None:
            speed = source_timerange.duration / target_timerange.duration
        else: # source_timerange is None
            speed = speed if speed is not None else 1.0
            source_timerange = Timerange(0, round(target_timerange.duration * speed))

        if source_timerange.end > material.duration:
            raise ValueError(f"Source timerange {source_timerange} exceeds material duration {material.duration}")

        super().__init__(material.material_id, source_timerange, target_timerange, speed, volume)

        self.material_size = (material.width, material.height)

        self.clip_settings = clip_settings if clip_settings is not None else Clip_settings()
        self.uniform_scale = True
        self.effects = []
        self.filters = []
        self.animations_instance = None
        self.transition = None
        self.mask = None

    def add_animation(self, animation_type: Union[Intro_type, Outro_type, Group_animation_type]) -> "Video_segment":
        """将给定的入场/出场/组合动画添加到此片段的动画列表中, 动画的起止时间自动确定"""
        if isinstance(animation_type, Intro_type):
            start = 0
            duration = animation_type.value.duration
        elif isinstance(animation_type, Outro_type):
            start = self.target_timerange.duration - animation_type.value.duration
            duration = animation_type.value.duration
        elif isinstance(animation_type, Group_animation_type):
            start = 0
            duration = self.target_timerange.duration
        else:
            raise TypeError("Invalid animation type %s" % type(animation_type))

        if self.animations_instance is None:
            self.animations_instance = Segment_animations()
            self.extra_material_refs.append(self.animations_instance.animation_id)

        self.animations_instance.add_animation(Animation(animation_type, start, duration))

        return self

    def add_effect(self, effect_type: Union[Video_scene_effect_type, Video_character_effect_type], params: Optional[List[Optional[float]]] = None) -> "Video_segment":
        """为视频片段添加一个作用于整个片段的特效

        Args:
            effect_type (`Video_scene_effect_type` or `Video_character_effect_type`): 特效类型
            params (`List[Optional[float]]`, optional): 特效参数列表, 参数列表中未提供或为None的项使用默认值.
                参数取值范围(0~100)与剪映中一致. 某个特效类型有何参数以及具体参数顺序以枚举类成员的annotation为准.

        Raises:
            `ValueError`: 提供的参数数量超过了该特效类型的参数数量, 或参数值超出范围.
        """
        if params is not None and len(params) > len(effect_type.value.params):
            raise ValueError("Too many parameters for effect %s" % effect_type.value.name)

        effect_inst = Video_effect(effect_type, params)
        self.effects.append(effect_inst)
        self.extra_material_refs.append(effect_inst.global_id)

        return self

    def add_filter(self, filter_type: Filter_type, intensity: Optional[float] = None) -> "Video_segment":
        """为视频片段添加一个滤镜

        Args:
            filter_type (`Filter_type`): 滤镜类型
            intensity (`float`, optional): 滤镜强度, 取值范围0~100, 仅当滤镜能够自定义强度时允许指定, 默认100.
        """
        if intensity is not None: intensity /= 100 # 转化为0~1范围

        filter_inst = Filter(filter_type.value, intensity if intensity is not None else 1.0)
        self.filters.append(filter_inst)
        self.extra_material_refs.append(filter_inst.global_id)

        return self

    def add_keyframe(self, _property: Keyframe_property, time_offset: Union[int, str], value: float) -> "Video_segment":
        """为给定属性创建一个关键帧, 并自动加入到关键帧列表中

        Args:
            _property (`Keyframe_property`): 要控制的属性
            time_offset (`int` or `str`): 关键帧的时间偏移量, 单位为微秒. 若传入字符串则会调用`tim()`函数进行解析.
            value (`float`): 属性在`time_offset`处的值

        Raises:
            `ValueError`: 试图同时设置`uniform_scale`以及`scale_x`或`scale_y`其中一者
        """

        if (_property == Keyframe_property.scale_x or _property == Keyframe_property.scale_y) and self.uniform_scale:
            self.uniform_scale = False
        elif _property == Keyframe_property.uniform_scale:
            if not self.uniform_scale: raise ValueError("Cannot set uniform_scale when scale_x or scale_y already exist")
            _property = Keyframe_property.scale_x

        if isinstance(time_offset, str): time_offset = tim(time_offset)

        for kf_list in self.common_keyframes:
            if kf_list.keyframe_property == _property:
                kf_list.add_keyframe(time_offset, value)
                return self
        kf_list = Keyframe_list(_property)
        kf_list.add_keyframe(time_offset, value)
        self.common_keyframes.append(kf_list)
        return self

    def add_mask(self, mask_type: Mask_type, *, center_x: float = 0.0, center_y: float = 0.0, size: float = 0.5,
                 rotation: float = 0.0, feather: float = 0.0, invert: bool = False,
                 rect_width: Optional[float] = None, round_corner: Optional[float] = None) -> "Video_segment":
        """为视频片段添加蒙版

        Args:
            mask_type (`Mask_type`): 蒙版类型
            center_x (`float`, optional): 蒙版中心点X坐标(以素材的像素为单位), 默认设置在素材中心
            center_y (`float`, optional): 蒙版中心点Y坐标(以素材的像素为单位), 默认设置在素材中心
            size (`float`, optional): 蒙版的“主要尺寸”(镜面的可视部分高度/圆形直径/爱心高度等), 以占素材高度的比例表示, 默认为0.5
            rotation (`float`, optional): 蒙版顺时针旋转的**角度**, 默认不旋转
            feather (`float`, optional): 蒙版的羽化参数, 取值范围0~100, 默认无羽化
            invert (`bool`, optional): 是否反转蒙版, 默认不反转
            rect_width (`float`, optional): 矩形蒙版的宽度, 仅在蒙版类型为矩形时允许设置, 以占素材宽度的比例表示, 默认与`size`相同
            round_corner (`float`, optional): 矩形蒙版的圆角参数, 仅在蒙版类型为矩形时允许设置, 取值范围0~100, 默认为0

        Raises:
            `ValueError`: 试图添加多个蒙版或不正确地设置了`rect_width`及`round_corner`
        """

        if self.mask is not None:
            raise ValueError("Cannot add multiple masks")
        if (rect_width is not None or round_corner is not None) and mask_type != Mask_type.矩形:
            raise ValueError("`rect_width` and `round_corner` can only be set for rectangle mask")
        if rect_width is None and mask_type == Mask_type.矩形:
            rect_width = size
        if round_corner is None:
            round_corner = 0

        self.mask = Mask(mask_type.value, center_x, center_y,
                         w=rect_width if rect_width else size * self.material_size[1] * mask_type.value.default_aspect_ratio / self.material_size[0],
                         h=size, ratio=mask_type.value.default_aspect_ratio,
                         rot=rotation, inv=invert, feather=feather/100, round_corner=round_corner/100)
        self.extra_material_refs.append(self.mask.global_id)
        return self

    def add_transition(self, transition_type: Transition_type, *, duration: Optional[Union[int, str]] = None) -> "Video_segment":
        """为视频片段添加转场, 注意转场应当添加在**前面的**片段上

        Args:
            transition_type (`Transition_type`): 转场类型
            duration (`int` or `str`, optional): 转场持续时间, 单位为微秒. 若传入字符串则会调用`tim()`函数进行解析. 若不指定则使用转场类型定义的默认值.

        Raises:
            `ValueError`: 试图添加多个转场.
        """
        if self.transition is not None:
            raise ValueError("Cannot add multiple transitions")
        if isinstance(duration, str): duration = tim(duration)

        self.transition = Transition(transition_type, duration)
        self.extra_material_refs.append(self.transition.global_id)
        return self

    def export_json(self) -> Dict[str, Any]:
        json_dict = super().export_json()
        json_dict.update({
            "clip": self.clip_settings.export_json(),
            "hdr_settings": {"intensity": 1.0, "mode": 1, "nits": 1000},
            "uniform_scale": {"on": self.uniform_scale, "value": 1.0},
        })
        return json_dict
