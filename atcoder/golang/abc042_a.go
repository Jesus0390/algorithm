// https://atcoder.jp/contests/abc042/tasks/abc042_a
package main

import(
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scan_input := bufio.NewScanner(os.Stdin)
	scan_input.Scan()
	input := strings.Split(scan_input.Text(), " ")
	
	aux_5 := 0
	aux_7 := 0
	for i:=0; i<len(input); i++ {
		num, _ := strconv.Atoi(input[ i ])
		if num == 5 {
			aux_5++
		}
		if num == 7 {
			aux_7++
		}
	}

	if aux_5 == 2 && aux_7 == 1 {
		fmt.Println( "YES" )
	} else {
		fmt.Println( "NO" )
	}
}