"""Message templates for the discord bot."""
import typing

import jinja2
from loguru import logger


class MessageTemplates:
    """Create message templates for the discord bot."""

    def __init__(self, template_dir: str = "./templates"):
        self.env = jinja2.Environment(  # noqa: S701
            loader=jinja2.FileSystemLoader(template_dir),
            autoescape=True)

    def render(self, template_name: str, **kwargs: typing.Any):
        template = self.env.get_template(template_name)
        txt = template.render(kwargs)
        logger.debug(txt)

        return txt
