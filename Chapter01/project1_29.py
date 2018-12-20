#Write a Python program that outputs all possible strings formed by using the
#characters c , a , t , d , o ,and g exactlyonce.

data = list('catdog')

#function to return list 
def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l =[]
        for i in range (len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                l.append([x] + p)
        return l

#printing the string
if __name__ == "__main__":
    for k in perm1(data):
        fullstr = ''.join(k)
        print(fullstr)
    
