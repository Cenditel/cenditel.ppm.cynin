from DateTime import DateTime

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from Acquisition import aq_base, aq_inner, aq_parent

from cenditel.ppm.interfaces import Ifolderproj
from Products.Archetypes.utils import DisplayList
from DateTime import DateTime


class createtemplateview(BrowserView):

    template = ViewPageTemplateFile('templates/createtemplate.pt')
    
    def __init__(self, context, request):
         self.context=context
         self.request=request
         return
    
    def __call__(self):
        self.request.set('disable_border', True)
        return self.template()
        
        
    def create (self):
    	holder=self.context
    	if self.request.form.has_key('form.button.cancel'):
            C_url=holder.absolute_url()
            return self.request.RESPONSE.redirect(C_url) 
            
        if self.request.form.has_key('form.button.next'):
            Tit=self.request.form["subj"]
            Tit=Tit.lower()
            
            foldert=getattr(holder, "Templates")
            foldert.invokeFactory("FCKTemplate", title=Tit, id=Tit)
            propo=getattr(foldert, Tit)
            url = propo.absolute_url() + ("/edit")
            return self.request.RESPONSE.redirect(url)
