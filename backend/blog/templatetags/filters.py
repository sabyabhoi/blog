from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value): 
  name = value.__str__().split('-')
  firstname = name[0].capitalize()
  surname = name[1].capitalize()

  return firstname + ' ' + surname

@register.filter(name='add_class')
def add_class(value, arg):
  return value.as_widget(attrs = {'class': arg})