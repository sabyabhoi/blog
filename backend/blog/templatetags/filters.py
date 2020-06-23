from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value): 
  name = value.__str__().split('-')
  firstname = name[0].capitalize()
  surname = name[1].capitalize()

  return firstname + ' ' + surname
