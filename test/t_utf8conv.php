<?php

// $string = "뭐래냐?";
//
//   $test2 = iconv("UTF-8","EUC-KR" , $string);
//   echo $test2;
$str = "\uac00\ub098\ub2e4";
// unicode_decode($var).PHP_EOL);
 echo json_decode(sprintf('"%s"', $str));
 ?>
