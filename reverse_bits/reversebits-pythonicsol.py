"""One-Line Algorithm

Time Complexity: O(n)
"""

class Solution:
    def reverse_bits(self, x):
        return int(bin(x)[2:].zfill(64)[::-1], 2)
        
def main():
    s = Solution()
    test_cases = [
        0b1110000000000001,
        0b1001111000110101,
        0b1001011100111000,
        0b1110011001100000
        ]
    for num in test_cases:
        reversed_num = s.reverse_bits(num)
        print(f'{bin(num)[2:]} -> {bin(reversed_num)[2:]}')

if __name__ == '__main__':
    main()