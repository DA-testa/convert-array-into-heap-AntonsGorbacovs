def sift_down(i,data,swaps):
    min_index=i
    l_child=2*i+1
    if l_child < len(data) and data[l_child] < data[min_index]:
        min_index=l_child
    r_child=2*i+2
    if r_child < len(data) and data[r_child] < data[min_index]:
        min_index=r_child
    if i != min_index:
        data[i], data[min_index]=data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(min_index, data, swaps)
        
def build_heap(data):
    swaps=[]
    for i in range(len(data)//2,-1,-1):
        sift_down(i, data, swaps)
    return swaps

def main():
    input_type=input()
    if 'I' in input_type:
        n=int(input())
        data=list(map(int,input().split()))
        assert len(data)==n
        swaps=build_heap(data)
        print(len(swaps))
        for i,j in swaps:
            print(i,j)
    elif 'F' in input_type:
        filename=input()
        with open("tests/"+filename,'r') as f:
            n=list(f.readline())
            data=list(map(int, f.readline().split()))
            assert len(data)==n
            swaps=build_heap(data)
            print(len(swaps))
            for i,j in swaps:
                print(i,j)
    else:
        print("Error")
        exit()
        
if __name__ == "__main__":
    main()
