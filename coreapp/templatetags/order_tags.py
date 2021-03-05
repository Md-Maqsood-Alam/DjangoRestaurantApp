from django import template
register=template.Library()

@register.filter
def order_dishes_quantity(order):
    dishesMap=eval(order.dishes_ordered)
    return [(dishesMap[dishId][0],dishesMap[dishId][1])  for dishId in dishesMap]