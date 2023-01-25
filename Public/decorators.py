from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_staff == True:
            return redirect('EventMgrIndex')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func