def flatten_json(d):
	if isinstance(d, dict):
		result = {}
		for k in d:
			r = flatten_json(d[k])
			for l in r:
				if len(l) > 0:
					result['{}.{}'.format(k, l)] = r[l]
				else:
					result[k] = r[l]
		return result
	else:
		return {
			'': d
		}
		
		
test = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}


print(flatten_json(test))

		
