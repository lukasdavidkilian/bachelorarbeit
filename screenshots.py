number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_of_number_array(array):
    sum = 0
    for number in array:
        sum += number
    return sum

# Schreibe eine Funktion, welche den Durchschnitt von einem Array von Zahlen berechnet

def average_of_number_array(array):
    sum = sum_of_number_array(array)
    return sum / len(array)

