from django import template

register = template.Library()

def cut(value): 
  name = value.__str__().split('-')
  firstname = name[0].capitalize()
  surname = name[1].capitalize()

  return firstname + ' ' + surname

register.filter('cut', cut)