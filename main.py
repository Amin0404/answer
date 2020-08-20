#-*- coding: utf-8 -*


#題目1(A):反轉字串
def string_reverse(word:str = ""):
    """
    Parameters:
        word:str = "" 想要反轉的文字
    Return:
        reverse_string
    """
    if word == "":
        return "沒有輸入文字喔~"
    reverse_word = word[::-1]

    return reverse_word

#題目1(B):反轉各個單字字串,順序不變
def string_reverse_2(words:str = ""):
    """
    Parameters:
        word:str = "" 想要反轉的文字
    Return:
        reverse_string
    """
    if words == "":
        return "沒有輸入文字喔~"
    word_list = words.split(" ")
    new_words = ""
    for word in word_list:
        new_words = f"{new_words} " + word[::-1]
    new_words = new_words.lstrip(" ")

    return new_words

#題目2
def number_count(number:int = None):
    if number == None:
        return "沒有輸入數字喔~"
    number = int(number)
    number_list = []
    for num in range(1,number+1):
        if num % 3 == 0 and num % 5 == 0:
            number_list.append(num)
        elif num % 3 != 0 and num % 5 != 0:
            number_list.append(num)
        else:
            continue

    total = len(number_list)

    return total

#題目3:
"""
我會選擇先看混和的那個袋子，原因是：
每個袋子的標示都是錯的，
混和的袋子裡面會有兩種情形:1.原子筆 2.鉛筆
鉛筆的袋子裡面有兩種情形:1.混和 2.原子筆
原子筆的袋子裡面有兩種情形:1.混和 2.鉛筆

如果混和的袋子裡面是原子筆，那麼鉛筆的袋子裡面就剩下混和，而原子筆的袋子自然就是鉛筆
如果混和的袋子裡面是鉛筆，那麼原子筆的袋子裡面就剩下混和，而鉛筆的袋子裡面自然就是原子筆
"""

#題目4:
"""
是最後的加總誤導了，原本的金額是:
300 X 3(人) = 900
因為優惠價需要退 150 元，但是員工偷走了60元，最後退了 90 元回來，所以 3 人付的總金額為 900 - 90 = 810 元，
810 / 3 = 270(每人的金額)，而員工偷走的 60 元就已經分擔到每人的 270 裡面了，
從退回90元開始，總金額就是 810 元，而不是一開始的 900 元 ,
所以 810 + 60 = 870 這個公式是錯的，總金額應該是 270 * 3 = 810
"""