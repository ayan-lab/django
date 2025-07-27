from rest_framework.permissions import SAFE_METHODS,BasePermission,DjangoModelPermissions

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view): 
        if request.method in SAFE_METHODS:
        # or if request.method == 'GET: # but isme head aur options bhi secure ho jyenge (i.e need authentication)
            return True
        return bool(request.user.is_staff and request.user)
    
class FullDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        
        
        
class ViewCustomerHistoryPermission(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.has_perm('store.view_history')
    
    

