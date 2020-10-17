<?php
// https://atcoder.jp/contests/abc042/tasks/abc042_a

$stdin = fopen("php://stdin", "r");
fscanf($stdin, "%[^\n]", $input);
$arr_input = explode(" ", $input);
$aux_5 = 0;
$aux_7 = 0;
foreach($arr_input as $v) {
	if($v == 5) $aux_5++;
	if($v == 7) $aux_7++;
} 
if($aux_5==2 && $aux_7==1) {
	echo "YES";
} else {
	echo "NO";
}
fclose($stdin);

