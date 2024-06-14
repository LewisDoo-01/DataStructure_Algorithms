from student import Student
from hashtable import Hash
 
# Python3 program to implement hashing with chaining
BUCKET_SIZE = 26

def main():
	s1 = Student('Vu Thi Phuong', 20, 8.5)
	s2 = Student('Le Viet Bac', 21, 9.0)
	s3 = Student('Quang Xuan Tuyen', 22, 7.0)
	s4 = Student('Ho Nguyet Anh', 23, 6.5)
	s5 = Student('Nguyen Van Nam', 24, 5.0)
	s6 = Student('Bui Viet Hung', 19, 7.5)
	s7 = Student('Vu Viet Dung', 21, 7.5)
	s8 = Student('Nguyen Xuan Hong', 26, 4.0)
	s9 = Student('Le Thi Be', 25, 8.0)
	s10 = Student('Quang Xuan Yen', 22, 7.0)
	s11 = Student('Tran Thi Kim Xuyen', 24, 6.0)
	s12 = Student('Nguyen Thanh Trung', 23, 3.5)
	
	c = []
	c.append(s1); c.append(s2); c.append(s3); c.append(s4)
	c.append(s5); c.append(s6); c.append(s7); c.append(s8)
	c.append(s9); c.append(s10); c.append(s11); c.append(s12)
	
	# Create a empty has of BUCKET_SIZE
	h = Hash(BUCKET_SIZE)
	for s in c:
		h.insertItem(s)
		
	# Display the hash table
	h.displayHash()

# Drive Program
if __name__ == "__main__":
    main()