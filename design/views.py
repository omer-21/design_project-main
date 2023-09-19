from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *
from PIL import Image
import numpy as np
import json
from django.conf import settings

# Create your views here.
def extract_used_colors(image_file):
    with Image.open(image_file) as image:
        # Convert the image to "P" mode to get the color palette
        image = image.convert("P")
        colors = image.getcolors()

        # Get the RGB values of the colors in the palette
        color_palette = image.getpalette()
        used_colors_dict = {}
        for count, index in colors:
            r, g, b = color_palette[index * 3:index * 3 + 3]
            used_colors_dict[index] = (r, g, b)

        return used_colors_dict

def upload_design_view(request):
    if request.method == 'POST' and 'design_img' in request.FILES:
        design_img = request.FILES['design_img']
        print(design_img)
        design = Design(design_img=design_img)
        design.save()
        base_dir=settings.BASE_DIR
        #print(base_dir)
        img_url=rf"{base_dir}\uploads\images\designs\{design_img.name}"
        print(img_url)
        img=Image.open(img_url)
        img=np.array(img,dtype=np.uint8)
        design.content_list=json.dumps(img.tolist())
        # Process the image to extract the used colors
        colors = extract_used_colors(design_img)
        #colors = get_used_colors(design_img)
        design.used_colors = colors

        # Calculate the height and width of the image
        image = Image.open(design_img)
        d_width, d_height = image.size
        design.d_width = d_width
        design.d_height = d_height
        design.warp_seq=''
        design.weft_seq=''
        design.warp_rolls={}
        design.weft_rolls={}
        design.weaves_list=[]
        design.save()

        # Return a success response or redirect to a different page
        #return HttpResponse("Design uploaded successfully.")
        return HttpResponse(f'''
            <script>
                alert('Design uploaded successfully');
                setTimeout(function() {{
                    window.location.href = "{reverse('dn', args=[design.id] )}";
                }}, 0); // Redirect after 2 seconds (adjust the delay as needed)
            </script>
        ''')

    return render(request, "design/upload_design.html")

def home_page(request):
    return render(request,'design/home_page.html')

def design_list(request):
    designs = Design.objects.all()
    return render(request, 'design/design_list.html', {'designs': designs})

def dn(request,design_id):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setdn")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getdn")
        design=Design.objects.get(pk=design_id)
        # Generate HTML for color palette
        colors=design.used_colors
        color_palette_html = ''
        for key, color in colors.items():
            r=color[0] 
            g=color[1] 
            b=color[2]
            color_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
            color_palette_html += f'<div style="display: inline-block; width: 20px; height: 20px; background-color: {color_hex}; color: white; text-align: center;">{ key }</div>'
        context={'des_img':design.design_img,'color_palette_html':color_palette_html}
        return render(request,'design/design.html',context)



def WW(request,design_id):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setww")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getWW")
        return render(request,'design/warp-weft-def.html')

def sw(request,design_id):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setsw")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getWW")
        return render(request,'design/sw.html')


def cw(request,design_id):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setcw")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getcw")
        return render(request,'design/cw.html')


def ld(request,design_id):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setwld")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getld")
        return render(request,'design/ld.html')


def ex(request,design_id):
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setex")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getex")
        return render(request,'design/ex.html')






def setww(request):
    print(request.method)
    if request.method=='POST':
        #setAttribute2database
        print(request.POST)
        print("setww")
    return HttpResponse('{"POST":"POST"}')

def getValue(request):
    print(request.method)
    if request.method=='GET':
        print(request)
        return  HttpResponse ('{"get":"get"}')
    if request.method=='POST':
        return  HttpResponse('{"POST":"POST"}')    
    return HttpResponse('scdsafce')
