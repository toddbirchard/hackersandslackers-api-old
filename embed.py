class LinkPreview:

    """Build preview object embed."""

    def __init__(self, rawhtml):
        self.html = str(rawhtml)
        self.cleanhtml = self.cleanhtml()
        self.links = self.getlinks

    def cleanhtml():
        if self.html is not None:
            html = self.html.replace('<p>', '')
            html = self.html.replace('</p>', '')
            return html

    def getLinks():
        self.cleanhtml.splice('')

    def make_preview():
        pieces = {
            'opentag': '<div class="link-preview">',
            'image': '<div class="preview-image" style="background-image:url(' + x + ');"></div>
            'info': '<div class="link-info">',
            'title': '<h4>' + v + '</h4>',
            'description': '<p>' + t + '</p>',
            'url': '<span class="url-info"><i class="far fa-link"></i>' + url + '</span>'
            'end': '</div></div>''
        }
