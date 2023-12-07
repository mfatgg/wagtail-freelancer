from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class PortfolioBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title")
    image = ImageChooserBlock()
    intro = blocks.RichTextBlock()

    class Meta:
        template = 'freelancer/blocks/portfolio.html'
