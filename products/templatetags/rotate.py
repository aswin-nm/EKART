from django import template

register=template.Library()

@register.filter(name='rotate')
def rotate(list,rotate_size):
    rotate=[]
    i=0
    for item in list:
        rotate.append(item)
        i=i+1
        if i==rotate_size:
            yield rotate
            i=0
            rotate=[]
    if rotate:
        yield rotate        