<?php
// error_reporting(E_ALL);
//
// ini_set("display_errors", 1);

 $jsonArray = $_POST["jsonArray"];


  error_log($jsonArray+"\n", 3, "/var/www/html/phplog.log");


  echo "ok";
 ?>
