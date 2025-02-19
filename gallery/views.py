import json
import math
import os.path
import os
import platform
OS_TYPE = platform.system()

from PIL import Image
from PIL.ImageFile import ImageFile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.autoreload import trigger_reload
from django.utils.safestring import mark_safe

from Global import Global

thumb_path=""

def html(request):
    global thumb_path
    info = Global.saveHistory(request, "login")
    request.session["currentPage"]="/gallery"
    if 'userAccount' not in request.session:
        return redirect("/login")
    if OS_TYPE=="Darwin":
        thumb_path="/Users/chino0207/Downloads/images/thumb"
    else:
        thumb_path = "/home/ubuntu/images/thumb"
    root = os.listdir(thumb_path)
    root.sort(reverse=True)

    tree=""
    tree=listDir(thumb_path,tree)



    print(tree)
    return render(request, "gallery/gallery.html", {"list_dir":mark_safe(tree),"info": info[1]})
def thumb(request):
    info = Global.saveHistory(request, "login")
    request.session["currentPage"] = "/gallery/thumb"
    if 'userAccount' not in request.session:
        return redirect("/login")
    return render(request,"gallery/thumb.html",{"info":info[1]})

def thumb_doing(request):
    info = Global.saveHistory(request, "login")
    print("開始製作縮中囉...")
    if OS_TYPE=="Darwin":
        primitive_path="/Users/chino0207/Downloads/images/primitive"
        thumb_path="/Users/chino0207/Downloads/images/thumb"
    else:
        primitive_path = "/home/ubuntu/images/primitive"
        thumb_path = "/home/ubuntu/images/thumb"
    if not os.path.exists(thumb_path):
        os.makedirs((thumb_path))
    primitive=dirTree(primitive_path)
    print(primitive)
    thumb=dirTree(thumb_path)

    ImageFile.LOAD_TRUNCATED_IMAGES=True
    Image.MAX_IMAGE_PIXELS=None

    for p in primitive:
        if not p.replace("primitive","thumb") in thumb:
            target=ext2lower(p)
            make_thumb(target)

    print("finished")
    tree = ""
    tree = listDir(thumb_path, tree)
    return render(request, "gallery/gallery.html", {"list_dir":mark_safe(tree),"info": info[1]})

def make_thumb(file):
    thumb_dir=os.path.dirname(file).replace("primitive","thumb")
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    pil=Image.open(file)
    pil.thumbnail((800,600))
    file=os.path.basename(file)
    pil.save(os.path.join(thumb_dir, file))

def dirTree(path):
   
    s=set([])
    for root, subdirs, files in os.walk(path):
        for file in files:
            lower=file.lower()
            if lower.endswith('.jpg') or lower.endswith('.png') or lower.endswith('.bmp') or lower.endswith('.jpeg')or lower.endswith('.webp'):
                full_path=os.path.join(root, file).replace("\\","/")
                s.add(full_path)
    return s

def ext2lower(file):
    master, slave=os.path.splitext(file)
    slave=slave.lower()
    target=f"{master}{slave}"
    os.rename(file,target)
    return target

def listDir(path,tree):
    tree += "<ul>"
    files = os.listdir(path)
    files.sort(reverse=True)
    for file in files:
        full = os.path.join(path, file).replace("\\", "/")
        if os.path.isdir(full):
            
            txt = full.replace(path, "").replace("/", "")

            
            if txt.isdigit() and len(txt) == 8:
                txt = f"{txt[4:6]}/{txt[6:8]}"  
            url = full.replace(thumb_path, "")
            tree += f"""
                   <li>
                       <a href='javascript:void(0)' onclick='loadThumb("{url}");'>
                           {txt}
                       </a>
                   </li>
               """
            tree = listDir(full, tree)
    tree += "</ul>"
    return tree


def listThumbDir(request):
    if OS_TYPE=="Darwin":
        path = "/Users/chino0207/Downloads/images/thumb"
    else:
        path="/home/ubuntu/images/thumb"
    if 'dir' in request.GET:
        dir = request.GET.get("dir", "").lstrip("/")
    else:
        dir = ''
    full = os.path.join(path, dir)
    files = os.listdir(full)
    files.sort()  
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")
    files = [
        f'{dir}/{file}' for file in files
        if file.lower().endswith(valid_extensions) and os.path.isfile(os.path.join(full, file))
    ]
    
    total = len(files)
    txt = ""
    for i in range(math.ceil(total / 5)):
        txt += "<div style='display:flex;'>"
        for j in range(5):
            if i * 5 + j < total:
                file = files[i * 5 + j]
                txt += f"""
                <div class='with_img'>
                    <a href='javascript:void(0)' onclick='showPrimitive({i * 5 + j});'>
                        <img class ='img_thumb' src='/pictures/thumb/{file}'/>
                    </a>
                </div>
                """
            else:
                txt += "<div class='without_img'></div>"
        txt += '</div>'
    return HttpResponse(
        json.dumps(
            {'url': mark_safe(txt), 'files': ','.join(files)}
        ),
        content_type='application/json'
    )

def ai_detect(request):
    pass