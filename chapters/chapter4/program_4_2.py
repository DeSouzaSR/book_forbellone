"""
Docstring for chapters.chapter4.program_4_2
"""

vet_lido = [0.0] * 10
vet_des = [0.0] * 10

for i in range(10):
    vet_lido[i] = float(input('Enter vet values: '))

media_lido = sum(vet_lido)/10

for i in range(10):
    vet_des[i] = abs(vet_lido[i] - media_lido)

media_des = sum(vet_des) /  10

print(f'Média lido: {media_lido}\n')
print(f'Média des: {media_des}\n')