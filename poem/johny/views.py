from django.http import HttpResponse

# Create your views here.
def one(request, x):
    poem = (
        f"Father: <b>{x}, {x}!</b><br>"
        f"{x}: <b>Yes, Papa?</b><br>"
        f"Father: <b>Eating sugar?</b><br>"
        f"{x}: <b>No, Papa!</b><br>"
        f"Father: <b>Telling lies?</b><br>"
        f"{x}: <b>No, Papa!</b><br>"
        f"Father: <b>Open your mouth.</b><br>"
        f"{x}: <b>Ha, ha, ha!</b><br>"
    )
    return HttpResponse(poem)
