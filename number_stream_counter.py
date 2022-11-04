"""
    For this challenge you will determine if a stream of digits occurs in a string.
    Reference: https://stackoverflow.com/questions/59036027/the-number-stream-detection
    https://pythontutor.com/render.html#code=def%20number_stream_counter%28number_stream%29%3A%0A%20%20%20%20%22%22%22%0A%20%20%20%20Take%20the%20number_stream%20to%20be%20passed%20that%20includes%20numbers%202%20through%209%0A%20%20%20%20Determine%20if%20there%20is%20a%20consecutive%20stream%20of%20digits%20on%20N%20in%20length%20where%20N%20is%20the%20number%20of%20repeats%0A%20%20%20%20N%20repeats%20must%20at%20least%20%3D%20N%20the%20value%0A%20%20%20%20So%20if%205%20is%20N%20then%20there%20must%20be%20at%20least%20five%20repeats%20or%20more%0A%20%20%20%20%20%20%20%20of%20the%20number%20in%20the%20stream%20like%20%3A%205,5,5,5,5%0A%0A%0A%20%20%20%20%3Aparam%20number_stream%3A%20str%0A%20%20%20%20%3Areturn%3A%20true%20if%20N%20occurs%20N%20times%20in%20number_stream%20-%20otherwise%20return%20false%0A%0A%20%20%20%20input%20%3D%20%225556293383563665%22%20%23%20Not%20enough%20of%20the%20numbers%20repeat%20to%20number%20value%0A%20%20%20%20output%20False%0A%0A%20%20%20%20input%20%3D%20%225788888888882339999%22%20%23%2010%20number%20eights%20are%20True%0A%20%20%20%20output%20True%0A%20%20%20%20%22%22%22%0A%20%20%20%20k%20%3D%20len%28number_stream%29%0A%20%20%20%20count%20%3D%201%0A%20%20%20%20number_list%20%3D%20%5B%5D%0A%20%20%20%20for%20i%20in%20number_stream%3A%0A%20%20%20%20%20%20%20%20i%20%3D%20int%28i%29%0A%20%20%20%20%20%20%20%20number_list.append%28i%29%0A%20%20%20%20for%20index,%20i%20in%20enumerate%28number_list%29%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%23%20Only%20run%20while%20the%20list%20has%20a%20future%20position%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20number_list%5Bindex%5D%20%3D%3D%20number_list%5Bindex%20%2B%201%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20count%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20count%20%3D%3D%20number_list%5Bindex%20%2B%201%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20count%20%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20number_list%5Bindex%5D%20!%3D%20number_list%5Bindex%20%2B%201%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20count%20%3D%201%20%20%23%20reset%20the%20count%20back%20to%201%20-%20start%20over%0A%20%20%20%20%20%20%20%20except%20IndexError%3A%20%20%23%20if%20statement%20would%20not%20have%20a%20range%20and%20would%20fail%0A%20%20%20%20%20%20%20%20%20%20%20%20pass%0A%20%20%20%20return%20False%0A%0A%23%20number_stream%20%3D%20%225723399999999%22%20%23%20False%208%20nines%20instead%20of%20nine,%202%20threes%20instead%20of%20three%0A%23%20number_stream%20%3D%20%225556293383563665%22%20%23%20False%20--%20similar%0A%23%20number_stream%20%3D%20%225788888888882339999%22%20%23%20True%20--%2010%208's%0Anumber_stream%20%3D%20%2257233999999999%22%20%23%20True%20-%209%20nines%20%0Aprint%28number_stream_counter%28number_stream%29%29&cumulative=false&curInstr=126&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"""
import doctest


def number_stream_counter(number_stream):
    """
    Take the number_stream to be passed that includes numbers 2 through 9
    Determine if there is a consecutive stream of digits on N in length
    where N is the number of repeats
    N repeats must at least = N the value
    So if 5 is N then there must be at least five repeats or more
        of the number in the stream like : 5,5,5,5,5


    :param number_stream: str
    :return: true if N occurs N times in number_stream - otherwise return false

    input = "5556293383563665" # Not enough of the numbers repeat to number value
    output False

    input = "5788888888882339999" # 10 number eights are True
    output True

    >>> number_stream_counter("5556293383563665")
    """
    count = 1
    number_list = []
    for i in number_stream:
        i = int(i)
        number_list.append(i)
    for index, i in enumerate(number_list):
        try:
            # Only run while the list has a future position
            if number_list[index] == number_list[index + 1]:
                count += 1
                if count == number_list[index + 1]:
                    count = 1
                    return True
            if number_list[index] != number_list[index + 1]:
                count = 1  # reset the count back to 1 - start over
        except IndexError:  # if statement would not have a range and would fail
            pass
    return False


number_stream = (
    "5723399999999"  # False 8 nines instead of nine, 2 threes instead of three
)
# number_stream = "5556293383563665"  # False -- similar
# number_stream = "5788888888882339999"  # True -- 10 8's

print(number_stream_counter(number_stream))

doctest.run_docstring_examples(
    number_stream_counter, globals(), verbose=True, name="number_stream_counter"
)
