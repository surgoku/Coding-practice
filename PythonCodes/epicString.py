def epicString(s, dict):
	if s in dict:
		return s
	n = len(s)
	for i in range(1, n):
		prefix = s[:i]
		suffix = s[i:]

		if prefix in dict:
			temp_out = epicString(suffix, dict)
			if temp_out:
				return prefix + " " + temp_out

	return None


def epicStringDP(s, dict, out):
	if s in dict:
		return s
	if s in out:
		return out[s]
	n = len(s)
	for i in range(1, n):
		prefix = s[:i]
		suffix = s[i:]
		if prefix in dict:
			temp_out = epicStringDP(suffix, dict, out)
			if temp_out:
				return prefix + " " + temp_out
	out[s] = None	
	return None

s = "surchandrasvac"
dict = ["sur", "chandra", "svac"]

out = {}

print epicStringDP(s, dict, out)
