// Shengnan Zhou
// CSCI 305, Assigment 3 - Go Program
// Feb. 25, 2019

// This program will take the name of the input file
// from command line argument, please build the
// program first (go build firstGo.go), then run it (./firstGo input_file)





package main
import ("fmt"
	"strings"
	"io/ioutil"
	"os"
	"regexp"
)



// Function to check error
func check(e error) {
	if e != nil{
		panic(e)
	}
}



// Function to parse out numbers
func parse(c string) {
	fmt.Print(strings.Replace(c, c, "", -1))
}



// Function to open and read in from file
func readFile() string{
	// read in command line argument
	args := os.Args[1]

	// open file
	f, err := os.Open(args)
	check(err)

	// read file
	dat, err := ioutil.ReadFile(args)
	check(err)
	data := string(dat)

	// close file
	f.Close()

	// return data
	return data
}



// Function to write new result to new output file
func writeFile(c string) {

	// read in file
	data := readFile()

	// create new output file
	f, err := os.Create(c)
	check(err)
	defer f.Close()

	// regular expression for checking numbers
	re := regexp.MustCompile("[0-9]+")

	// parse numbers out of the input file
	for d:= range data {
		c := string(data[d])
		if re.MatchString(c) {		//if data matches number
			// parse number
			parse(c)
		} else {
			// write to output file
			n, err := f.WriteString(c)
			check(err)
			fmt.Print(n)
			f.Sync()
		}
	}
}



// This is the main function for the program to run
func main() {
	fmt.Println("File is read.")

	fmt.Println()

	// ask user input for the name of the output file
	fmt.Println("Enter the name of the output file: ")
	var input string
	fmt.Scanln(&input)
	fmt.Println()

	// create and write to file
	writeFile(input)
	fmt.Println()
	fmt.Println("New output file has been created.")
}
