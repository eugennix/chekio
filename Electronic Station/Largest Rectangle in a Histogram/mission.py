def largest_histogram(histogram):
    # mx - result, edge case mx = hight of row[0]
    mx =  histogram[0]
    # f[i][j] - max rectange for 'i' first elements of histogram and height 'j'
    # 0 <= j <= histogram[i]
    # I dont store all f[][], only last 2 - f_pred and f_next
    f_pred = [i+1 for i in range(histogram[0])]
    if len(histogram) > 1:
        # start from second elem
        i = 1
        while i < len(histogram):
            f_next = list()
            pred_hight = len(f_pred)
            for j in range(histogram[i]):
                f_new = f_pred[j]+j+1 if j<pred_hight else j+1
                mx = max(mx, f_new)
                f_next.append(f_new)
            f_pred = f_next
            i += 1
    return mx
