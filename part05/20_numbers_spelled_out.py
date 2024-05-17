def dict_of_numbers():
    zero_ten = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    tens_list = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teen_list = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    results = {}
    for n in range(100):
        if n < 11:
            results[n] = zero_ten[n]
        elif n % 10 == 0:
            results[n] = tens_list[n//10 - 1]
        elif n < 20:
            results[n] = teen_list[n-11]
        else:
            tens = n // 10
            unit = n - (tens * 10)
            results[n] = f'{tens_list[tens-1]}-{zero_ten[unit]}'

    return results