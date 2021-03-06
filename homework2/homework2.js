function calculate(min,max){
    let s=0
    for(let i=min;i<max+1;i++){
        s = s+i
    }
    console.log(s)
}

calculate(1,3)
calculate(4,8)


function avg(data){
    let s = 0
    for(let p=0;p<data["count"];p++){
        s+=data["employees"][p]["salary"]
    }
    if(data["count"]!==0){
        console.log(s/(data["count"]))
    }else{
        console.log(0)
    }
}

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


function maxProduct(nums){
    let first = -Infinity
    let second = -Infinity
    let first_min = Infinity
    let second_min = Infinity

    nums.forEach(e=>{
        if(e>first){
            second = first
            first=e
        }
        else if(e>second){
            second=e
        }
        if(e<first_min){
            second_min = first_min
            first_min = e
        }
        else if(e<second_min){
            second_min = e
        }
    });

    console.log(Math.max(first*second,first_min*second_min))
}

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])


function twoSum(nums,target){
    let d = {}
    for(let i=0;i<nums.length;i++){
        if(!(nums[i] in d)){
            d[target-nums[i]]=i
        }else{
            return [d[nums[i]],i]
        }
    }
}

result = twoSum([2,11,7,15],9)
console.log(result)

function maxZeros(nums){
    let c = {0:0}
    let m = 0
    nums.forEach(e=>{
        if(e===0){
            c[e]+=1
            m = Math.max(m,c[e])
        }else{
            c[0]=0
        }
    })
    console.log(m)
}

maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])