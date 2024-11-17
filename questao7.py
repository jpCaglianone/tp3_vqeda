def quickselect(arr, k):
    def particionar(arr, baixo, alto):
        pivo = arr[alto]
        i = baixo - 1
        for j in range(baixo, alto):
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    def quickselect_recursivo(arr, baixo, alto, k):
        if baixo <= alto:
            pi = particionar(arr, baixo, alto)
            if pi == k:
                return arr[pi]
            elif pi < k:
                return quickselect_recursivo(arr, pi + 1, alto, k)
            else:
                return quickselect_recursivo(arr, baixo, pi - 1, k)

    return quickselect_recursivo(arr, 0, len(arr) - 1, k)

arr = [10, 4, 5, 8, 6, 11, 26]
k = 3
print(f"O {k+1}-ésimo menor elemento é: {quickselect(arr, k)}")
