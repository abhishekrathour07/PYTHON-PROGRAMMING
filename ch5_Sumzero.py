arr = [-11,-6,-4,-2,2,4,5,7]

left =0
right = len(arr) - 1
while left<right:
    sum = arr[left]+arr[right]
    if sum==0:
        print(arr[left]," and ",arr[right])
        break
    elif sum>0:
        left+=1
    else:
        right -=1