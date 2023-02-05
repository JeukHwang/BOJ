def postorder(pre_s, in_s, size):
    global preorder, inverse_inorder, answer, counter
    if size == 0:
        return
    if size == 1:
        answer[counter] = preorder[pre_s]
        counter += 1
    else:
        i = inverse_inorder[preorder[pre_s]]
        l = i - in_s
        r = size - l - 1
        postorder(pre_s + 1, in_s, i - in_s)
        postorder(pre_s + 1 + l, i + 1, r)
        answer[counter] = preorder[pre_s]
        counter += 1


for _ in range(int(input())):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    inverse_inorder = [0] * (N + 1)
    for i in range(N):
        inverse_inorder[inorder[i]] = i
    answer, counter = [0] * N, 0
    postorder(0, 0, N)
    print(*answer)
