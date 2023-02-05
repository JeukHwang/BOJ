def postorder(pre_s, pre_f, in_s, in_f):
    global preorder, inverse_inorder, answer, counter
    if pre_f - pre_s == 0:
        return
    if pre_f - pre_s == 1:
        answer[counter] = preorder[pre_s]
        counter += 1
    else:
        i = inverse_inorder[preorder[pre_s]]
        l, r = i - in_s, in_f - i - 1
        postorder(
            pre_s + 1,
            pre_s + 1 + l,
            in_s,
            i,
        )
        postorder(
            pre_f - r,
            pre_f,
            i + 1,
            in_f,
        )
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
    postorder(0, N, 0, N)
    print(*answer)
