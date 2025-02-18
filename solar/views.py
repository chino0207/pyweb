from datetime import datetime

from django.shortcuts import render
from django.utils.safestring import mark_safe

from Global import Global


# Create your views here.
def html(request):
    info = Global.saveHistory(request, "login")
    if "year" in request.POST:
        now= int(request.POST["year"])
    else:
        now= int(datetime.now().strftime("%Y"))

    solar_dict={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5,"key6":6,"key7":7,"key8":8,"key9":9,"key10":10,"key11":11,"key12":12,
                "key13":13,"key14":13,"key15":15,"key16":16,"key17":17,"key18":18,"key19":19,"key20":20,"key21":21,"key22":22,"key23":23,"key24":24}
    terms=list(solar_dict.keys())
    html="<table>"
    for row in range(12):
        html += "<tr>"
        for col in range(2):
            index=row*2+col
            yyyy=now
            month=int(index/2)+2
            if month==13:
                month=1
                yyyy +=1
            html += f"<td>{terms[index]}</td>"
            html += f"<td>{yyyy}-{month:02d}-</td>"
        html += "</tr>"
    html +="</table"
    return render(request,"solar.html",
                  {
                    "var_now":now,
                    "var_year":list(range(1970,2051)),
                    "html":mark_safe(html),
                    "info":info[1]
                  }
                )
