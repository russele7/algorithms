import sys

def main():
    # sorted_numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    # element = int(sys.stdin.readline().rstrip())

    sorted_numbers = [1, 2, 3, 5]
    element = 6


    def find_element(sorted_numbers, element):
        left = 0
        right = len(sorted_numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if sorted_numbers[mid] == element:
                return {
                    'index': mid,
                    'equality_flag': True,    
                }
            if sorted_numbers[mid] < element:
                left = mid + 1
            else:
                right = mid - 1

        if sorted_numbers[mid] < element:
            return {
                'index': mid + 1,
                'equality_flag': False,
            }
        
        return {
                'index': mid,
                'equality_flag': False,
            }

    # def find_first_dupl(sorted_numbers, mid):
    #     value = sorted_numbers[mid]
    #     # print(f'sorted_numbers = {sorted_numbers} / mid = {mid} / value = {value}')
    #     for i in range(mid-1, 0, -1):
    #         if sorted_numbers[i] != value:
    #             return i + 1
    #     return 0
    
    def find_first_dupl(sorted_numbers, mid):
        value = sorted_numbers[mid]
        # print(f'sorted_numbers = {sorted_numbers} / mid = {mid} / value = {value}')
        for i in range(mid, 0, -1):
            if sorted_numbers[i - 1] != value:
                return i
        return 0
    
    result = find_element(sorted_numbers, element)
    # print(f'result = {result}')
    if result['equality_flag']:
        answer = find_first_dupl(sorted_numbers, result['index'])
    else:
        answer = result['index']

    print(answer)


if __name__ == '__main__':
    main()