from astrbot.api.star import Context, Star, register, StarTools
from astrbot.api import logger, AstrBotConfig
@register(
    "url_2_knowledge_base", 
    "RC-CHN", 
    "通过 URL 提取内容，并经过处理、聚类和总结后，生成知识库文件。", 
    "v1.0.0"
)
class Url2KbPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)

    async def initialize(self):
        logger.info("该项目已废弃")

    async def terminate(self):
        """插件停用时调用的方法。"""
        logger.info("URL to Knowledge Base Plugin terminated.")