<?php
  require "pdo_conn.php";

  $filter = $_POST['filter'];

  if (empty($filter)) {// 비어있다면
    $stmt = $pdo_conn->prepare("SELECT orderNumb, orderDate, orderState, finalBill,numb, deliveryNumb, deliveryState FROM all_orders");
    $stmt->execute();
    $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $json_all = json_encode($all, JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
    header('Content-Type: application/json; charset=utf8');
    echo urldecode($json_all);

    error_log(date("Y-m-d H:i:s")
    ."\n"."주문내역-전체"."\n".$json_all."\n"
    , 3, "/var/www/html/phplog.log");
  }else {
    if($filter == 1){
      $filter = '입금전';
      $stmt = $pdo_conn->prepare("SELECT orderNumb, orderDate, orderState, finalBill,numb, deliveryNumb, deliveryState FROM all_orders WHERE orderState = '$filter'");
      $stmt->execute();
      $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
      $json_all = json_encode($all, JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
      header('Content-Type: application/json; charset=utf8');
      echo urldecode($json_all);

      error_log(date("Y-m-d H:i:s")
      ."\n"."주문내역-입금전"."\n".$json_all."\n"
      , 3, "/var/www/html/phplog.log");
    }elseif ($filter ==2) {
      $filter = '결제완료';
      $stmt = $pdo_conn->prepare("SELECT orderNumb, orderDate, orderState, finalBill,numb, deliveryNumb, deliveryState FROM all_orders WHERE orderState = '$filter'");
      $stmt->execute();
      $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
      $json_all = json_encode($all, JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
      header('Content-Type: application/json; charset=utf8');
      echo urldecode($json_all);

      error_log(date("Y-m-d H:i:s")
      ."\n"."주문내역-결제완료"."\n".$json_all."\n"
      , 3, "/var/www/html/phplog.log");
    }

  }




 ?>
