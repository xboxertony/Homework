def calculate(min,max):
    s = 0
    for i in range(min,max+1):
        s+=i
    print(s)

calculate(1,3)
calculate(4,8)

def avg(data):
    s = 0
    for p in data["employees"]:
        s+=p["salary"]
    if data["count"]!=0:
        print(s/data["count"])
    else:
        print(0)

avg({
    "count":3,
    "employees":[
        {
            "name":"John","salary":30000
        },
        {
            "name":"Bob","salary":60000
        },
        {
            "name":"Jenny","salary":50000
        }
    ]
})


def maxProduct(nums):
    m = -float("inf")
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]*nums[j]>m:
                m = nums[i]*nums[j]
    print(m)


maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])


def twoSum(nums,target):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[target-nums[i]]=i
        else:
            return [d[nums[i]],i]

result = twoSum([2,11,7,15],9)
print(result)


def maxZeros(nums):
    c = {0:0}
    m = 0
    for i in nums:
        if i==0:
            c[i]+=1
            m = max(m,c[i])
        else:
            c[0]=0
    print(m)


maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])