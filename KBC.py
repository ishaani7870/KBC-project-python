def kbc():
    a= ["1=How many continents are there"]
    ["2=What is the capital of India"],
    ["3=NG mei kaun se course padhayajata hai"]
    op= [["1=Four","2=Nine","Seven","Eight"],
	["1=one","2=two","3=three","4=four"],
	["1=one","2=two","3=three","4=four"],
	["Chandigarh","Bhopal","Chennai","Delhi"],
	["Software Engineering", "Counseling","Tourism", "Agriculture"]]
    print("welcome to kbc")
    print(a[0])
    print(op[0])
    solution=[4,3,1]
    b=int(input("enter your answer"))
    i=0
    while i<=0:
        if b==1:
            print("wrong answer")
        elif b==2:
            print("wrong answer")
        elif b==3:
            print("waw! congraces rightanswer")
        elif b==4:
            print("wrong answer")
            if b==3:
                print(a[1])
                print(op[1])
                b1=int(input("enter your answer"))
                if b1==1:
                    print("wrong answer")
                elif b1==2:
                    print("wrong answer")
                elif b1==3:
                    print("wrong answer")
                elif b1==4:
                    print("waw! congrace rightanswer")
                    if b1==4:
                        print(a[2])
                        print(op[2])
                        b2=int(input("enter youranswer"))
                        if b2==1:
                            print("waw! congracerightanswer")
                        elif b2==2:
                            print("wrong answer")
                        elif b2==3:
                            print("wrong answer")
                        elif b2==4:
                            print("wrong answer")
        i=i+1
        print("congraculation youranswer right")
kbc()