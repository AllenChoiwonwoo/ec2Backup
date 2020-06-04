<?php
  require "pdo_conn.php";

  $stmt = $pdo_conn->prepare("SELECT mall_id, mall_name, kor_name, mall_order FROM mall_order_list WHERE mall_order = 0 ORDER BY mall_order");
  $stmt->execute();
  $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
  $json_all = json_encode($all,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
  header('Content-Type: application/json; charset=utf8');
  echo urldecode($json_all);

  // error_log(date("Y-m-d H:i:s")
  // ."\n".$json_all"\n"
  // , 3, "/var/www/html/phplog.log");


 ?>
