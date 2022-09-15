"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sells = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_sum(sells_sum):
  sell_sum = 0
  for items_sold in sells_sum:
    sell_sum += items_sold
  return sell_sum

def count_avg(sells_avg):
  sell_sum = 0
  for items_sold in sells_avg:
    sell_sum += items_sold
  return round(sell_sum/len(sells_avg), 2)

all_items_sold = 0
for one_product in sells:
  product_sum = count_sum(one_product['items_sold'])
  print(f'Сумма {one_product["product"]}: {product_sum}')
for one_product in sells:
  product_avg = count_avg(one_product['items_sold'])
  print(f'Среднее количество продаж {one_product["product"]}: {product_avg}')
  all_items_sold += product_sum

all_sells_avg = round(all_items_sold/len(sells), 2)

print(f'Сумма продаж: {all_items_sold}')
print(f'Среднее количество продаж всех телефонов: {all_sells_avg}')

if __name__ == "__main__":
    count_sum('sells_sum')
    count_avg('sells_avg')