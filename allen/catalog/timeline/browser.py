from zope.publisher.browser import BrowserPage
from zope.formlib.form import Fields, PageEditForm
from interfaces import ITimeline

class Count(BrowserPage):
    """ Count timeline
    """
    def __call__(self, **kwargs):
        return '%s' % len(self.context)

class Edit(PageEditForm):
    form_fields = Fields(ITimeline)
