# -*- coding: utf-8 -*-

from django.template import Library, Node

from django.template.loader import get_template
from jchat.models import Room

register = Library()
#@register.simple_tag
#@register.assignment_tag
#@register.filter

###################" help fonction ##################

def next_bit_for(bits, key, if_none=None):
    try:
        res = bits[bits.index(key)+1]
        if res in ('as','for','with','into') or "=" in res:
            return if_none
        return res
    except:
        return if_none

def resolve(var, context):
    """Resolves a variable out of context if it's not in quotes"""
    if var[0] in ('"', "'") and var[-1] == var[0]:
        return var[1:-1]
    else:
        try:
            return Variable(var).resolve(context)
        except:
            return var

########## tags #####################

class GetChatNode(Node):

    def __init__(self,link_obj):
        self.link_obj = link_obj

    def render(self,context):
        t = get_template("jchat/chat.html")
        if self.link_obj:
            self.link_obj = resolve(self.link_obj,context)
            room = Room.get_or_create(self.link_obj)
        else:
            room = Room.objects.get(id=1)
        context["jchat_room"] = room
        res = t.render(context)
        return res

def get_chat(parser,token):
    bits = token.contents.split()
    link = next_bit_for(bits,'for',None)
    return GetChatNode(link)
register.tag('get_chat',get_chat)

