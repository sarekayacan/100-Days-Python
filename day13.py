#Student Grade Manager
scores_input = input("Öğrenci notlarını virgülle ayırarak girin: ")
scores = [int(score) for score in scores_input.split(",")]

grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in scores
]

passing_scores = [score for score in scores if score >= 60]
failing_scores = [score for score in scores if score < 60]

average_score = sum(scores) / len(scores)

ascending = sorted(scores) #artan
descending = sorted(scores, reverse=True) #azalan

max_score = max(scores)
min_score = min(scores)

max_index = scores.index(max_score) #max_score değerinin scores listesindeki yerini bulur.
min_index = scores.index(min_score) #min_score değerinin scores listesindeki yerini bulur.

print("\n--- Öğrenci Notları ---")
for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Öğrenci {i}: Not = {score}, Harf = {grade}")

print("\n--- Özet ---")
print(f"Ortalama Not: {average_score:.2f}")
print(f"Geçenler: {passing_scores}")
print(f"Kalanlar: {failing_scores}")

print("\n--- Sıralama ---")
print(f"Artan: {ascending}")
print(f"Azalan: {descending}")

print("\n--- En Yüksek / En Düşük ---")
print(f"En Yüksek Not: Öğrenci {max_index + 1} → {max_score}")
print(f"En Düşük Not: Öğrenci {min_index + 1} → {min_score}")

