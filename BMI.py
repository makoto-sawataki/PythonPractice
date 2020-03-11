#体重を入力する
weight = input('体重[kg]を入力してください  ')
#身長を入力する
height = input('身長[m]を入力してください   ')

#BMIを計算する
bmi = float(weight) / (float(height) ** 2)

print(bmi)

if bmi < 18.5:
    print('やせてるよ！')
elif bmi < 25:
    print('普通だよ！')
elif bmi < 35:
    print('太り気味だよ！')
else:
    print('太りすぎだよ！')

