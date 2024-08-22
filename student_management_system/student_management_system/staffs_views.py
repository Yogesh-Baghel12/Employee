from django.shortcuts import render,redirect
from student_management_app.models import StafffLeave
from django.contrib import messages

def HOME(request):
    return render(request,'Staffs/home.html')


def STAFF_APPLY_LEAVE(request):
    return render(request,"Staffs/apply_leave.html")
        
        
def STAFF_LEAVE_HISTORY(request):
    return render(request,"Staffs/leave_history.html")

def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        names=request.POST.get('names')
        off_email=request.POST.get('off_email')
        from_date=request.POST.get("from_date")
        to_date=request.POST.get("to_date")
        reason=request.POST.get("reason")
        staff=Staff.objects.get(admin=request.user.id)
        leave=StafffLeave(
            staff_id=staff,
            from_date=from_date,
            to_date=to_date,
            messages=reason,
        )
            
        leave.save()
        messages.success(request,"Leave Successfully Sent")
    return redirect("staff_apply_leave")