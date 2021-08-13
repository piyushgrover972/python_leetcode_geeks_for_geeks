"""
    Original Problem: https://practice.geeksforgeeks.org/problems/lucky-alive-person-in-a-circle1229/1
"""


# User function Template for python3
class Solution:
    def __init__(self):
        # 10^8 is the max-limit of N. 10^8 would have around ~30 bits.
        # Hence calculating pow(2)-LUT with sufficient margin.
        self._powers_of_2 = [1 << n for n in range(35)]

    def floor_power_of_2(self, num):
        """Find the nearest lower power of 2 from LUT

           NOTE: We may use Binary Search here, however, since the LUT
           is comparatively small in size, binsearch() won't have much
           gain over linsearch()
        """
        if not num:
            return 0
        for i, pow in enumerate(self._powers_of_2):
            if num < pow:
                return self._powers_of_2[i - 1]
            elif num == pow:
                return pow

    def find(self, N=5):
        """
        :param N: Total number of persons in circle
        :return: Index of person remaining (1-based)

        :algorithm:
        Watch the pattern of solutions:
            N   find(N)
            1  =  1
            2  =  1
            3  =  3
            4  =  1
            5  =  3
            6  =  5
            7  =  7
            8  =  1
            9  =  3
            10  =  5
            11  =  7
            12  =  9
            13  =  11
            14  =  13
            15  =  15
            16  =  1
            17  =  3
            18  =  5
            19  =  7
            20  =  9
            21  =  11
            22  =  13
            23  =  15
            24  =  17
            25  =  19
            26  =  21
            27  =  23
            28  =  25
            29  =  27
            30  =  29
            31  =  31
            32  =  1
            33  =  3
            34  =  5
            35  =  7
            36  =  9
            37  =  11
            38  =  13
            39  =  15
            40  =  17
            41  =  19
            42  =  21
            43  =  23
            44  =  25
            45  =  27
            46  =  29
            47  =  31
            48  =  33
            49  =  35
            50  =  37
            51  =  39
            52  =  41
            53  =  43
            54  =  45
            55  =  47
            56  =  49
            57  =  51
            58  =  53
            59  =  55
            60  =  57
            61  =  59
            62  =  61
            63  =  63
        From the pattern, it can be seen that the answer is:
            (N - floor_power_of_2(N) ) * 2 + 1
        """
        return ((N - self.floor_power_of_2(N)) << 1) + 1


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
# } Driver Code Ends
