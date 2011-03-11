from zope.interface import implements, Interface
	
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType
	
from cenditel.ppm import ppmMessageFactory as _
from cenditel.ppm import createSubFolder
	
class Iprojectview(Interface):
    """
    project view interface
    """
    
    def test():
        """ test method """
    
class projectview(BrowserView):
    """
    project browser view
    """

    implements(Iprojectview)
	
    def __init__(self, context, request):
        self.context = context
	self.request = request
	

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')
	
    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()


    def subfol(self):
        """ 
        Run the script for the creation of sub folders
        """
        m=createSubFolder.CreatefolderActionExecutor(self.context)
        m.sub()
        return 
 
    def roles(self):
        """
        assigned the role of Owner the selected user
        """
        member=str(self.context.getManager())
        roles = self.context.get_local_roles()
        self.context.manage_setLocalRoles(member, ['Owner'])
        return "."
        
    def blog(self):
        """
        """
        try:
            holder=self.context
            catalog = getToolByName(holder, 'portal_catalog')
            List=[]
            
            for child in holder.getChildNodes():
                id=child.getId()
                if id == "Blog":
                    print "estoy en rl blog"
                    txt=child.getText()
            return txt
        except:
            pass
        



