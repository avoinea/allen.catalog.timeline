from zope.publisher.browser import BrowserPage

class Count(BrowserPage):
    """ Count timeline
    """
    def __call__(self, **kwargs):
        return '%s' % len(self.context)
