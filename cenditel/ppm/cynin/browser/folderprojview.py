from zope.interface import implements, Interface
	
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
#from Products.CMFPlone.utils import _createObjectByType
from Products.ATContentTypes.lib import constraintypes
	
from cenditel.ppm import ppmMessageFactory as _
from cenditel.ppm import search
	
class Ifolderprojview(Interface):
    """
    proj view interface
    """
    
    def test():
        """ test method """
    
class folderprojview(BrowserView, object):
    """
    proj browser view
    """

    implements(Ifolderprojview)
	
    def __init__(self, context, request):
        self.context = context
	self.request = request
	
    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')
	
    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()
    

    def searching(self):
        z=search.searching()
        self.result=z.searching(self.context)
        return self.result
    
	
    def GetTags(self):
        """
        the tag list that are within the portfolio of projects
        """
        tagsList=[]
    	for element in self.result:
    	    tagsList.extend(element.getTags())
        return tagsList
        
    def proposals(self):
        """
        """
        holder=self.context
        listid=[]
        catalog = getToolByName(holder, 'portal_catalog')
        for child in holder.getChildNodes():
            listid.append(child.getId())
            
        result=catalog.searchResults(portal_type='proposals', review_state='approved_by_organization_council', getId = listid)
        listobj=[]
        dic=[]
    	for brain in result:
    		dic=brain
    		obj=dic.getObject()
    		listobj.append(obj)
    	return listobj       

    def createfol(self):
        """
        Create the containing folder of the proposals
        and a template 
        """
        holder = self.context
        txt = """Subject: $Subject

Group: $Group

Email: 

Telephone:

Fax:

Date Request Submitted (YYYY/MM/DD): $Date

Note: The newProposal script will substiute $Subject, $Group, and $Date
with appropriate values from the form regardless of where they are in the template.

To create a new proposal type, you can copy and paste this or any other template
and its associated Dashboard wiki page, rename it appropriately, and modify its
contents with the information you want collected.

"""
        try:
            '''
            self.context.invokeFactory("Folder", title="Proposal Templates", id="Templates")
            # Enable contstraining
            self.context.setConstrainTypesMode(constraintypes.ENABLED)
            # Types for which we perform Unauthorized check
            self.context.setLocallyAllowedTypes(['FCKTemplate'])
            # Add new... menu  listing
            folder.setImmediatelyAddableTypes(['FCKTemplate'])
            # Object reindex for enabled to search
            self.context.reindexObject()
            
            foldert = getattr(holder, "Templates")
            foldert.invokeFactory("FCKTemplate", title="Example", id="example")
            
            example = getattr(foldert, "example")
            example.setText(txt)
            '''
            self.context.invokeFactory("Folder", title="Proposal Templates", id="Templates")
            
            foldert=getattr(holder, "Templates")
            
            foldert.invokeFactory("FCKTemplate", title="Example", id="example")
            
            example=getattr(foldert, "example")

            example.setText(txt)
        except:
            pass
        return 

