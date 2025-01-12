def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    
    # Inisialisasi matriks untuk menyimpan item yang dipilih
    keep = [[False for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                if values[i-1] + dp[i-1][w-weights[i-1]] > dp[i-1][w]:
                    dp[i][w] = values[i-1] + dp[i-1][w-weights[i-1]]
                    keep[i][w] = True
                else:
                    dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = dp[i-1][w]

    # Fungsi untuk melakukan tracing back
    def traceback(i, w):
        if i == 0 or w == 0:
            return
        if keep[i][w]:
            traceback(i-1, w-weights[i-1])
            print(f"Pilih mata kuliah {i} dengan nilai {values[i-1]}")
        else:
            traceback(i-1, w)

    traceback(n, capacity)
    return dp[n][capacity]

# Contoh penggunaan:
values = [60, 100, 120]  # Nilai manfaat setiap mata kuliah
weights = [10, 20, 30]  # SKS setiap mata kuliah
capacity = 50  # Beban studi maksimum

result = knapsack(values, weights, capacity)
print("Nilai manfaat maksimum:", result)