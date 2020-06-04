<?php

  $array1 = array();
  array_push($array1, "추가");
  array_push($array1, "추추가");
  array_push($array1, "추추추가");

  $array2 = array();
  array_push($array2, "123");
  array_push($array2, "345");
  array_push($array2, '456');

  $array3 = array();
  array_push($array3, $array1);
  array_push($array3, $array2);

  // print_r($array3);

  // echo "";

  $a =array();
  $a["one"]="test1";
  $a["two"]="test2";
  print_r($a);


 ?>
