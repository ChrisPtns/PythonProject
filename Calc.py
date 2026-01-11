import math

# Συναρτήσεις για τις βασικές πράξεις
def prosthesi(a, b):
    return a + b

def afairesi(a, b):
    return a - b

def pollaplasiasmos(a, b):
    return a * b

def diairesi(a, b):
    # Έλεγχος δεδομένων: διαίρεση με το μηδέν
    if b == 0:
        return "Σφάλμα: Διαίρεση με το μηδέν!"
    return a / b

# Συναρτήσεις για προχωρημένες πράξεις
def dynami(base, exp):
    return math.pow(base, exp)

def tetragoniki_riza(n):
    # Έλεγχος δεδομένων: αρνητικός αριθμός στη ρίζα
    if n < 0:
        return "Σφάλμα: Δεν ορίζεται ρίζα αρνητικού αριθμού!"
    return math.sqrt(n)

def trigonometria(moires, typos):
    # Μετατροπή μοιρών σε ακτίνια (radians) γιατί η math δουλεύει με radians
    rad = math.radians(moires)
    if typos == "sin":
        return math.sin(rad)
    elif typos == "cos":
        return math.cos(rad)

# Κύριο Μενού
def menu():
    print("\n--- Έξυπνη Αριθμομηχανή ---")
    print("1. Πρόσθεση (+)")
    print("2. Αφαίρεση (-)")
    print("3. Πολλαπλασιασμός (*)")
    print("4. Διαίρεση (/)")
    print("5. Ύψωση σε Δύναμη (x^y)")
    print("6. Τετραγωνική Ρίζα (√)")
    print("7. Ημίτονο (sin)")
    print("8. Συνημίτονο (cos)")
    print("9. Έξοδος")
    return input("Επιλέξτε μια πράξη (1-9): ")

# Κύριο Πρόγραμμα
while True:
    epilogi = menu()

    if epilogi == '9':
        print("Τερματισμός προγράμματος...")
        break

    if epilogi in ['1', '2', '3', '4', '5']:
        # Ζητάμε δύο αριθμούς για αυτές τις πράξεις
        try:
            num1 = float(input("Δώστε τον πρώτο αριθμό: "))
            num2 = float(input("Δώστε τον δεύτερο αριθμό: "))
            
            if epilogi == '1':
                print(f"--------\nΑποτέλεσμα: {num1} + {num2} = {prosthesi(num1, num2)}")
            elif epilogi == '2':
                print(f"--------\nΑποτέλεσμα: {num1} - {num2} = {afairesi(num1, num2)}")
            elif epilogi == '3':
                print(f"--------\nΑποτέλεσμα: {num1} * {num2} = {pollaplasiasmos(num1, num2)}")
            elif epilogi == '4':
                print(f"--------\nΑποτέλεσμα: {num1} / {num2} = {diairesi(num1, num2)}")
            elif epilogi == '5':
                print(f"--------\nΑποτέλεσμα: {num1}^{num2} = {dynami(num1, num2)}")
        except ValueError:
            print("Σφάλμα: Παρακαλώ εισάγετε έγκυρους αριθμούς.")

    elif epilogi in ['6', '7', '8']:
        # Ζητάμε έναν αριθμό για αυτές τις πράξεις
        try:
            num = float(input("Δώστε τον αριθμό: "))
            
            if epilogi == '6':
                print(f"--------\nΑποτέλεσμα: √{num} = {tetragoniki_riza(num)}")
            elif epilogi == '7':
                print(f"--------\nΑποτέλεσμα: sin({num}°) = {trigonometria(num, 'sin'):.4f}")
            elif epilogi == '8':
                print(f"--------\nΑποτέλεσμα: cos({num}°) = {trigonometria(num, 'cos'):.4f}")
        except ValueError:
            print("Σφάλμα: Παρακαλώ εισάγετε έγκυρο αριθμό.")
    else:
        print("Μη έγκυρη επιλογή, προσπαθήστε ξανά.")