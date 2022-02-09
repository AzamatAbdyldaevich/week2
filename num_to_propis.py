number = int(input("Enter num:"))
propis = ["one", "two", "three", "four", "five",
          "six",
          7: "seven",
          8: "eight",
          9: "nine",
          10: "ten",
          11: "eleven",
          12: "twelve",
          13: "thirtten",
          14: "fourteen",
          15: "fifteen",
          16: "sixteen",
          17: "seventeen",
          18: "eighteen",
          19: "nineteen",
          20: "twenty",
          30: "thirtten",
          40: "fourteen",
          50: "fifteen",
          60: "sixteen",
          70: "seventeen",
          80: "eighteen",
          90: "nineteen",
          100: "hundred",
          1000: "thousand"
          }


def num_to_propis(num):
    n  = num
    p_num = ""
    while n > 0:
        for i in (propis.keys(), :-1):
            if n <= i:
                p_num += propis.get(i) + " "
                n -= i
    return p_num


print(num_to_propis(number))
