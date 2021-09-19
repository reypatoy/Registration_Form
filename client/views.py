from django.shortcuts import render


from client.models import client_info
# Create your views here.
def homepage(request):
    context = None
    if request.method == "POST":
        data = client_info.objects.create(
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            middle_name = request.POST.get("middle_name"),
            birth_date = request.POST.get("birth_date"),
            age = request.POST.get("age"),
            weight = request.POST.get("weight"),
            height = request.POST.get("height"),
            purok_street = request.POST.get("purok_street"),
            brgy = request.POST.get("brgy"),
            municipality = request.POST.get("municipality"),
            province = request.POST.get("province"),
            ethnicity = request.POST.get("ethnicity"),
            skill = request.POST.get("skill"),
            highest_ed_attainment = request.POST.get("highest_ed_attainment"),
            year_graduated = request.POST.get("year_graduated"),
            degree_course = request.POST.get("degree_course"),
            eligibility = request.POST.get("eligibility"),
            school_graduated = request.POST.get("school_graduated"),
            mobile_num = request.POST.get("mobile_num"),
            email_add = request.POST.get("email_add"),
            afpsat_score = request.POST.get("afpsat_score"),
            date_taken = request.POST.get("date_taken"),
            occupation = request.POST.get("occupation"),
            reason_application = request.POST.get("reason_application"),
            shoes_size = request.POST.get("shoes_size"),
            tshirt_size = request.POST.get("tshirt_size"),
            short_pants = request.POST.get("short_pants"),
            mothers_name = request.POST.get("mothers_name"),
            fathers_name = request.POST.get("fathers_name"),
            present_add = request.POST.get("present_add"),
            psa_bcert = request.FILES['psa_bcert'],
            tor = request.FILES['tor'],
            form137 = request.FILES['form137'],
            body_pic = request.FILES['body_pic'],
            cenomar = request.FILES['cenomar'],
            enlistment_type = request.POST.get("enlistment_type"),
            tariff = request.POST.get("tariff")
        )
        data.save()
        context = {
            'success':"Submitted Successfully!"
        }
    return render(request,"homepage.html",context)