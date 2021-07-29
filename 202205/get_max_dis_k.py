def get_max_len_dis_k(s, k):
	cur_k = 0
	d = {}
	l = 0
	r = 0
	max_len_far = 0
	for i, v in enumerate(s):
		if i == 0:
			l = r = i
			d[v] = 1
			cur_k += 1
		else:
			if v in d:
				d[v] += 1
			else:
				d[v] = 1
				cur_k += 1
		
				if cur_k > k:
					len_now = r - l + 1
					if len_now > max_len_far:
						print(s[l:r+1])
						max_len_far = len_now
					while cur_k > k:
						d[s[l]] -= 1
						if d[s[l]] == 0:
							del d[s[l]]
							cur_k -= 1
						l += 1
			r += 1
	len_now = r - l + 1
	if len_now > max_len_far:
		print(s[l:r+1])
		max_len_far = len_now
	return max_len_far
	



m = get_max_len_dis_k('abcba', 2)
print(m)
m = get_max_len_dis_k('abba', 1)
print(m)
