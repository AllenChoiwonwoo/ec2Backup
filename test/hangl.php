<?php
error_reporting(E_ALL);

ini_set("display_errors", 1);
  $result = shell_exec("python3 ../api/py_mysql.py");
  echo "뭐지?";
  echo $result."<br>";
  // if (!strcmp($result, "abcd")) {
  //   echo "true";
  // }else {
  //   echo "false";
  //   echo strlen($result);
  //   echo "<br>".strlen("abcd")."<br>";
  //   vprintf($result);
  //   vprintf("abcd");
  // }
  if (strlen($result)==5) {
    // code...
    echo "go!";
  }
 ?>
