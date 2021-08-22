# Цени на играчките:
#  Пъзел - 2.60 лв.
#  Говореща кукла - 3 лв.
#  Плюшено мече - 4.10 лв.
#  Миньон - 8.20 лв.
#  Камионче - 2 лв.
#
# От конзолата се четат 6 реда:
# 1. Цена на екскурзията - реално число;
# 2. Брой пъзели - цяло число;
# 3. Брой говорещи кукли - цяло число;
# 4. Брой плюшени мечета - цяло число;
# 5. Брой миньони - цяло число;
# 6. Брой камиончета - цяло число.

excursion_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_min = int(input())
number_lorries = int(input())

total_sum = number_puzzles*2.6+number_dolls*3+number_bears*4.10+number_min*8.2+number_lorries*2
total_number = number_puzzles + number_dolls + number_bears + number_min + number_lorries

if total_number >= 50:
    total_sum = total_sum*0.75

final_sum = 0.9*total_sum

if final_sum >= excursion_price:
    print(f"Yes! {(final_sum-excursion_price):.2f} lv left.")
else:
    print(f"Not enough money! {(excursion_price-final_sum):.2f} lv needed.")


