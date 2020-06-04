<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
    error_reporting(E_ALL);

    ini_set("display_errors", 1);

    function get_time() {
    list($usec, $sec) = explode(" ", microtime());
    return ((float)$usec + (float)$sec);
}

    $start = get_time();


      $command = escapeshellcmd('python3 php_python.py');
      $output = shell_exec($command);

      echo $output;
      // echo utf8_decode($output);

      echo "<br>";
      // echo "뭐지?";
  $end = get_time();

  $time = $end - $start;
  echo "<br>".$time.'sec';
     ?>

  </body>
</html>
