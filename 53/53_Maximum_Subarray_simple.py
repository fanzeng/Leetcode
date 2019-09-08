

list_test = [
([-2,1,-3,4,-1,2,1,-5,4],6),
([1,-1,-1,2],2),
([1,0,1,2],4),
([-2,1],1),
([-2,-1],-1),
([-1,-2],-1),
([-2,-3,-1],-1),
([1,2],3),
([2,1],3),
([1],1),
([-1],-1),
([8,-19,5,-4,20],21),
([2,-1,1,1],3),
([1,0,0,0],1),
([3,-4,2,-3],3),
([-3,3,3,3,2,3],14)
]
def do_test(list_test):
	for t in list_test:
		test_in, ans = t
		test(test_in, ans)

def test(test_in, ans):
	test = Solution()
	res = test.maxSubArray(test_in)

	if res != ans:
		print test_in, res, '!=', ans

do_test(list_test)