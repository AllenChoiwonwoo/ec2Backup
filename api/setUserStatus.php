<?php


// error_reporting(E_ALL);
// ini_set("display_errors", 1);

  require "pdo_conn.php";

  $userId = $_POST['id'];
  $userStatus = $_POST['userStatus'];
  // $userId = $_GET['id'];
  // $userStatus = $_GET['$userStatus'];
  // echo $userId;
  // echo $userStatus;
  error_log(date("Y-m-d H:i:s")
  ."\n"."id : ".$userId."\n"."st:".$userStatus."\n"
  , 3, "/var/www/html/phplog.log");


  $query = "UPDATE userinfo SET user_status = ? WHERE id = ? ";
  $stmt = $pdo_conn->prepare($query);
  $stmt->bindParam(1,$userStatus);
  $stmt->bindParam(2,$userId);
  $stmt->execute();



 ?>
