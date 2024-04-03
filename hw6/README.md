CS 601 Homework 6: CBMC

These functions recognize JSON, and a mirror-symmetric string:

```c++
// Return true if this char is a valid JSON body char
bool char_is_json(char c)
{
	if (c>='0' && c<='9') return true;
	if (c>='A' && c<='Z') return true;
	if (c>='a' && c<='z') return true;
	return false;
}


// Return true if this string is a quoted JSON string.  Updates len.
//    For example, "key" is a quoted JSON string.
bool string_is_json_string(const char *str,int &len)
{
	if (str[0]=='"') {
		for (int end=1;end<len;end++)
		{
		    char c=str[end];
			if (c=='"')
			{
				len = end+1;
				return true;
			}
			else if (!char_is_json(c))
			{
			    return false;
			}
		}
	}
	len=0;
	return false;
}


// Return true if this string is a valid JSON object
//   For example, {"key":"val","key2":"newval"} is valid.
bool string_is_json(const char *str,int len)
{
	if (str[0]=='{') { // json object
		if (str[len-1]!='}') return false;
		len--; // hide the close curly brace
		int start = 1;
		while (start < len) { // match "key":"value"
			// Match key
			int endk=len - start;
			if (!string_is_json_string(&str[start],endk))
				return false;
			//printf("Matched key from start %d to end %d\n",start,endk);
			start += endk;

			if (str[start]!=':') return false;
			start++;

			// Match value
			int endv=len - start;
			if (!string_is_json_string(&str[start],endv))
				return false;
			//printf("Matched val from start %d to end %d\n",start,endv);
			start += endv;

			if (start<len) { // need comma before next key value pair
				if (str[start]!=',') return false;
			}
		}
		return true;
	}
	return false;
}

// Return true if this char is symmetric: it reads the same forward or backward
bool symmetric_char(char c)
{
	switch (c) {
	case ' ': case '"': case '\'': case ':': case '|': case '^':
	case 'A': case 'I': case 'O': case 'o': case 'Y': case 'U':
	case 'H': case 'M': case 'T': case 'W': case 'V': case 'X':
	case 'x': case 'w': case 'v':
	case '0': case '8':
		return true;
	default:
		return false;
	}
}

// Return a mirror image of this char, or 0 if no mirror exists.
//   Call this the other way round too, it only finds one of each pair.
char mirror_char(char c)
{
	switch (c) {
	case '[': return ']';
	case '{': return '}';
	case '(': return ')';
	case 'b': return 'd';
	default:
		return 0;
	}
}

// Return true if these chars are a mirror image of each other
//   For example, '{' and '}' are mirror images.
bool mirror_image(char L,char R)
{
	if (L == R && symmetric_char(L)) return true;
	if (L == mirror_char(R)) return true;
	if (R == mirror_char(L)) return true;
	return false;
}

// Return true if the string is a "mirror palindrome":
//    it looks the same when viewed in a mirror.
//   For example, "Ib"{X}"dI" is a mirror palindrome.
bool string_is_mirror_palindrome(const char *str,int len)
{
	for (int i=0;i<=len/2;i++)
	{
		char L = str[i];
		char R = str[len-1-i];
		if (!mirror_image(L,R)) return false;
	}
	return true;
}
```

Your goal: use CBMC to automatically generate one 11-char string that satisfies both string_is_mirror_palindrome and string_is_json.

I did this by allocating an uninitialized 11-char array, and using an assert to challenge CBMC to find a string with the right combination of properties.

Hints:
If it takes more than a few seconds to run, then something has gone wrong. (Do you need a "--unwind" parameter?)
"VERIFICATION FAILED" means it broke your assert, which is usually what you want.
"VERIFICATION SUCCESSFUL" means it can't break your assert and won't give a counterexample. For example, I get this when I try to generate a 12-char string, because it's not possible to make the JSON delimiters symmetric.
