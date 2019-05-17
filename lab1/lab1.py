import csv
from timeit import default_timer as timer
comparison_operations = 0
exchange_operations = 0

class Laptop(object):
    def __init__(self, cpu, ram, name_of_firm):
        self.cpu = cpu
        self.ram = ram
        self.name_of_firm = name_of_firm

    def to_string(self):
        print(str(self.name_of_firm)+", "+str(self.cpu)+", "+str(self.ram))

def insertion_sort(laptops_list):
    global comparison_operations
    global exchange_operations

    for index in range(1, len(laptops_list)):
        value = laptops_list[index]
        i = index - 1
        while i >= 0:
            if value.ram > laptops_list[i].ram:
                comparison_operations += 1
                exchange_operations += 1
                laptops_list[i+1] = laptops_list[i]
                laptops_list[i] = value
                i = i-1
            else:
                exchange_operations += 1
                break
    return laptops_list

def merge_sort(laptops_list):
   global comparison_operations
   global exchange_operations
   if len(laptops_list) > 1:
        mid = len(laptops_list) // 2
        left_half = laptops_list[:mid]
        right_half = laptops_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_iter = 0
        right_iter = 0
        temp_index = 0
        while left_iter < len(left_half) and right_iter < len(right_half):
            exchange_operations += 1
            comparison_operations += 1
            if left_half[left_iter].cpu > right_half[right_iter].cpu:
                laptops_list[temp_index] = left_half[left_iter]
                left_iter += 1
            else:
                laptops_list[temp_index] = right_half[right_iter]
                right_iter += 1
            temp_index += 1
        while left_iter < len(left_half):
           laptops_list[temp_index] = left_half[left_iter]
           left_iter += 1
           temp_index += 1
        while right_iter < len(right_half):
            laptops_list[temp_index] = right_half[right_iter]
            right_iter += 1
            temp_index += 1
        return laptops_list

def read_data_from_file():
    laptops_list = []
    try:
        with open('data.txt') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_laptop = Laptop(int(row[0]), int(row[1]), row[2])
                laptops_list.append(new_laptop)
    except FileNotFoundError:
        print("File not found!")
    return laptops_list



if __name__ == '__main__':
    laptops_list = read_data_from_file()
    print('List of laptops:')
    for i in laptops_list:
        print(i.name_of_firm, i.cpu,  i.ram)
    comparison_operations = 0
    exchange_operations = 0
    start=timer()
    sorted_laptops_by_ram = insertion_sort(laptops_list)
    end=timer()
    print('Insertion sort result:')
    for laptop in sorted_laptops_by_ram:
        laptop.to_string()
    print('The number of comparison operations : ' + str(comparison_operations))
    print('Number of exchange operations : ' + str(exchange_operations))
    print('Time: '+str(end-start))
    comparison_operations = 0
    exchange_operations = 0
    start = timer()
    sorted_laptops_by_cpu = merge_sort(laptops_list)
    end = timer()

    print("Merge sort result:")
    for laptop in sorted_laptops_by_cpu:
        laptop.to_string()
    print("Number of comparisons: " + str(comparison_operations))
    print("Number of exchange operations : " + str(exchange_operations))
    print("Time: "+str(end-start))
